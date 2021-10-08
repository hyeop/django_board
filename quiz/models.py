from django.db import models
from acc.models import User

# Create your models here.
class Quiz(models.Model):
    question = models.TextField()
    answer = models.TextField()
    solver = models.ManyToManyField(User, blank=True)
    point = models.IntegerField()
#  - question (TextField)
#  - answer (TextField)
#  - solver (ManyToMany)
#  - point (Integer)
