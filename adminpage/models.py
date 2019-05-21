# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.timezone import now
from django.db import models

# Create your models here.

class Faq(models.Model):
    faq_id = models.CharField(max_length=16, default='0000000000000001')
    faq_type = models.CharField(max_length=10, default='999')
    faq_question = models.TextField(default='질문')
    faq_answer = models.TextField(default='답변')

    def __str__(self):
        return self.faq_question


class Log(models.Model):
    log_date = models.DateField(default=now)
    log_time = models.TimeField(default=now)
    log_userid = models.CharField(max_length=60)
    log_question = models.TextField(default='질문')
    log_answer = models.TextField(default='답변')
