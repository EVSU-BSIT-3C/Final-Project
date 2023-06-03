from django.db import models
import datetime


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    todo_count = models.IntegerField(default=0)

    def __str__(self):
        return self.category_name


class NotificationTime(models.Model):
    notification_time = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.notification_time


class Todo(models.Model):
    todo_text = models.CharField(max_length=1000)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    due_date = models.DateTimeField('due_date', null=True)
    email_notification = models.EmailField(max_length=500, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    notification_time = models.CharField(max_length=400, null=True)
    sent_reminder = models.CharField(max_length=10, default="False")

    def __str__(self):
        return self.todo_text