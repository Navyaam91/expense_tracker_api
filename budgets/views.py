from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from .models import Budget
from .serializers import BudgetSerializer
from transactions.models import Transaction

class BudgetListCreateView(generics.ListCreateAPIView):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save the budget
        budget = serializer.save(user=self.request.user)

        # Check how much user already spent this month
        spent = Transaction.objects.filter(
            user=request.user,
            type='expense',
            category=budget.category,
            date__month=budget.month,
            date__year=budget.year,
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        # Build response
        response_data = serializer.data
        response_data['spent_so_far'] = spent
        response_data['remaining'] = float(budget.limit) - float(spent)

        # 🚨 Check if budget already exceeded
        if spent > budget.limit:
            response_data['alert'] = (
                f"🚨 WARNING! You have already exceeded your "
                f"{budget.category} budget for "
                f"{budget.month}/{budget.year}! "
                f"Spent: {spent}, Limit: {budget.limit}"
            )
        elif float(spent) >= float(budget.limit) * 0.8:
            response_data['alert'] = (
                f"⚠️ CAUTION! You have used 80% or more of your "
                f"{budget.category} budget for "
                f"{budget.month}/{budget.year}! "
                f"Spent: {spent}, Limit: {budget.limit}"
            )
        else:
            response_data['alert'] = None

        return Response(response_data, status=status.HTTP_201_CREATED)