from django.db import models
from django.core.exceptions import ValidationError
import datetime

'''
entity: Category
attributes:
    category_name - the name of the category
    todo_count - number of tasks under the category
'''
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    todo_count = models.IntegerField(default=0)

    def __str__(self):
        return self.category_name


'''
attribute of Todo: notification_time
'''
class NotificationTime(models.Model):
    notification_time = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.notification_time

'''
entity: Todo
attributes:
    todo_text - text in task
    date_created - date the task was created
    due_date - date the task is due
    email_notification - contains the email address to send notification to
    category - the category the task belongs to (this is a foreign key, [ todos M>------1 category ] )
    notification_time - time when to notify user
    send_reminder - whether to send reminder or not
'''
class Todo(models.Model):
    todo_text = models.CharField(max_length=1000)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    due_date = models.DateTimeField('due_date', null=True)
    email_notification = models.EmailField(max_length=500, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    notification_time = models.CharField(max_length=400, null=True)
    sent_reminder = models.CharField(max_length=10, default="False")

    def clean(self):
        if self.due_date is not None and self.date_created is not None:
            if self.due_date < self.date_created:
                raise ValidationError("Due date cannot be before the date created.")
