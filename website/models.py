from __future__ import unicode_literals
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Hits(models.Model):
    name = models.CharField(max_length = 200)
    hits = models.IntegerField(default = 0)
    created = models.DateTimeField(auto_now_add = True, blank = True)
    #^^^auto_now_add makes the row have a timestamp for when it was first added^^^
