from django.db import models


# class Participant(models.Model):
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()
#     favorite_book = models.CharField(max_length=80)
#


class FormModel(models.Model):
    name = models.CharField(max_length=50)


class FormField(models.Model):
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=50)
    form = models.ForeignKey(FormModel, on_delete=models.CASCADE)


class FormRecord(models.Model):
    date = models.DateTimeField(auto_now_add=True)


class FormData(models.Model):
    form = models.ForeignKey(FormModel, on_delete=models.CASCADE)
    field = models.ForeignKey(FormField, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)
    record = models.ForeignKey(FormRecord, on_delete=models.CASCADE)


