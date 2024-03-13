from django import forms
from django.forms import ModelForm
from . import models

# class ParticipantForm(forms.ModelForm):
#     class Meta:
#         model = models.Participant
#         fields = "__all__"
#         labels = {
#             "name": "Your name",
#             "age": "your age",
#             "favorite_book": "your favorite book"
#         }

class FormDataForm(forms.ModelForm):
    class Meta:
        model = models.FormData
        fields = "__all__"
