from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.db.models.fields import BigAutoField
from courses.models import Course
from users.models import Student
from groups.models import Group

# Create your models here.
class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=100, null=False, blank=False)
    deadline = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(Student, on_delete=models.SET_NULL)
    group = models.ManyToOneRel(Group, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-updated_at"]
