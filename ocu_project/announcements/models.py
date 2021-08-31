from ocu_project.users.models import Student
from django.db import models
from users.models import Student
from groups.models import Group

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(Student, on_delete=models.SET_NULL)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-updated_at"]
