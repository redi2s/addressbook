# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    fullname = models.CharField(max_length=100, verbose_name=u'ФИО')
    birthdate = models.DateField(blank=True, null=True, verbose_name=u'Дата рождения', help_text=u'дд.мм.гггг')
    address = models.CharField(max_length=150, verbose_name=u'Адрес')
    phone = models.CharField(blank=True, null=True, max_length=15, verbose_name=u'Телефон')
    email = models.EmailField(blank=True, null=True, verbose_name=u'Эл. почта')
    comment = models.CharField(blank=True, null=True, max_length=255, verbose_name=u'Комментарий')
    user = models.ForeignKey(User)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = u'Записи'
        verbose_name = u'Запись'
