from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Sum
from datetime import date
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['type', 'category', 'date']
    ordering_fields = ['date', 'amount']

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class MonthlySummaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get year and month from URL params
        # If not provided, use current year and month
        year = int(request.query_params.get('year', date.today().year))
        month = int(request.query_params.get('month', date.today().month))

        # Filter transactions for this user, year and month
        qs = Transaction.objects.filter(
            user=request.user,
            date__year=year,
            date__month=month
        )

        # Calculate totals
        total_income = qs.filter(
            type='income'
        ).aggregate(
            Sum('amount')
        )['amount__sum'] or 0

        total_expenses = qs.filter(
            type='expense'
        ).aggregate(
            Sum('amount')
        )['amount__sum'] or 0

        # Breakdown expenses by category
        by_category = list(
            qs.filter(type='expense')
            .values('category')
            .annotate(total=Sum('amount'))
            .order_by('-total')
        )

        return Response({
            'year': year,
            'month': month,
            'total_income': total_income,
            'total_expenses': total_expenses,
            'net_savings': total_income - total_expenses,
            'expenses_by_category': by_category,
        })