from django.db import models
from datetime import timedelta, datetime
from django.utils import timezone

class Task(models.Model):
    URGENCY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_recurring = models.BooleanField(default=False)
    recurring_frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, blank=True, null=True)
    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES, default='low')

    def next_due_date(self):
        if not self.is_recurring or not self.recurring_frequency:
            return None
        base = self.created_at
        now = timezone.now()
        delta = {
            'daily': timedelta(days=1),
            'weekly': timedelta(weeks=1),
            'monthly': timedelta(days=30),
        }.get(self.recurring_frequency, timedelta(days=0))
        while base <= now:
            base += delta
        return base

    def __str__(self):
        return self.title
