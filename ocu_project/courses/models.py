from django.db import models
from groups.models import Group

# Create your models here.
class CourseDetails(models.Model):
    course_code = models.CharField(max_length=10, null=False, blank=False)
    course_name = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        ordering = ["course_code"]


class Course(models.Model):
    teacher = models.CharField(max_length=200, null=True, blank=True)
    details = models.ForeignKey(CourseDetails, on_delete=models.CASCADE)
    class_link = models.URLField(max_length=256, null=True, blank=True)
    class_id = models.CharField(max_length=50, null=True, blank=True)
    class_password = models.CharField(max_length=50, null=True, blank=True)
    extra_links = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    group = models.ManyToOneRel(Group, on_delete=models.CASCADE)
