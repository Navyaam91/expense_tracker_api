from django.urls import path
from .views import TransactionListCreateView, MonthlySummaryView

urlpatterns = [
    path('', TransactionListCreateView.as_view(), name='transactions'),
]