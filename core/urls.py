from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from transactions.views import MonthlySummaryView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth endpoints
    path('api/auth/register/', include('users.urls')),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='refresh'),

    # Transaction endpoints
    path('api/transactions/', include('transactions.urls')),

    # Summary endpoint
    path('api/summary/monthly/', MonthlySummaryView.as_view(), name='monthly-summary'),

    # Budget endpoints
    path('api/budgets/', include('budgets.urls')),
]