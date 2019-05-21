from django.db import models
from datetime import datetime

class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        shows = Shows.objects.filter(title = postData['title'])
        current_time = datetime.now()
        if postData['release_date'] > str(current_time):
            errors['release_date'] = "Date cannot be in the future"
        print("*" *50)
        print(postData['release_date'])
        print(current_time)
        if len(shows) > 0:
            errors['title'] = "Title already exists"
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters"
        if len(postData['desc']) > 0:
            if len(postData['desc']) < 10:
                errors['desc'] = "Description should be at least 10 characters"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length = 45)
    network = models.CharField(max_length = 45)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowsManager()