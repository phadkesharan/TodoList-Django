from datetime import datetime
from django.db import models
import datetime

# Create your models here.

class TodoItem(models.Model):

    content = models.TextField()
