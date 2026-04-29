from django.db import models


class Student(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Enrolled', 'Enrolled'),
        ('Rejected', 'Rejected'),
    ]

    name            = models.CharField(max_length=200)
    email           = models.EmailField(unique=True)
    course_interest = models.CharField(max_length=200)
    status          = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.status})"
