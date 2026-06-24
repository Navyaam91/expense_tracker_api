from django.db import models
from django.conf import settings

class Budget(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('salary', 'Salary'),
        ('entertainment', 'Entertainment'),
        ('utilities', 'Utilities'),
        ('healthcare', 'Healthcare'),
        ('shopping', 'Shopping'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'category', 'month', 'year']

    def __str__(self):
        return f"{self.user} - {self.category} - {self.limit}"