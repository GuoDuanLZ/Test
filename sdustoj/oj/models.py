from django.db import models


class Jumachine(models.Model):
    jid = models.IntegerField(unique=True)
    jname = models.CharField(max_length=30)
    jstate = models.CharField(max_length=20)


class Process(models.Model):
    machine = models.ForeignKey(to=Jumachine,to_field='jid',related_name='process')
    ptype = models.CharField(max_length=30)
    pid = models.IntegerField()
    pstate = models.IntegerField()