from django.db import models
from django.contrib.auth.models import User

class WeeklySummary(models.Model):
    WEEK_CHOICES = [
        ('wk01', 'Week 1'),
        ('wk02', 'Week 2'),
        ('wk03', 'Week 3'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    week = models.CharField(max_length=5, choices=WEEK_CHOICES)  # 🔄 removed unique=True
    revenue = models.FloatField()
    expense = models.FloatField()
    profit = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'week')  # ✅ enforce unique combo

