# Generated by Django 3.2.6 on 2021-09-01 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['course_code'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(blank=True, max_length=200, null=True)),
                ('class_link', models.URLField(blank=True, max_length=256, null=True)),
                ('class_id', models.CharField(blank=True, max_length=50, null=True)),
                ('class_password', models.CharField(blank=True, max_length=50, null=True)),
                ('extra_links', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.coursedetails')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group')),
            ],
        ),
    ]
