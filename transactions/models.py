from django.db import models
from django.conf import settings

class Transaction(models.Model):
    TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

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
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.type} - {self.amount} - {self.date}"