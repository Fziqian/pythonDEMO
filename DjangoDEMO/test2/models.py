# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 对应test2_user表
class User(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(default=0)