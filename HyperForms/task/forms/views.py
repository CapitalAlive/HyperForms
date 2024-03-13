from django.shortcuts import render, redirect
from . import forms
from django.forms import templates
from django.views.generic import FormView
from . import models
from datetime import datetime


def index(request):
    fields = models.FormField.objects.all()
    lines = models.FormRecord.objects.all()
    print("lines:", lines)
    table = []
    table_2 = []
    for line in lines:
        line_objects = models.FormData.objects.filter(record_id=line)
        table.append(line_objects)
    print("table:", table)
    print()
    for x in table:
        elem = []
        for d in x:
            print("x", d.value, end=", ")
            elem.append(d.value)
        print("")
        table_2.append(elem)

    context = {"fields": fields, "table": table, "table_2": table_2}
    print("this is render", render(request, template_name="index.html", context=context).content.decode('utf-8'))
    return render(request, template_name="index.html", context=context)

class Register(FormView):
    form_name = "participants"
    form_class = forms.FormDataForm
    success_url = "/"
    def get(self, request):
        form_fields_objects = models.FormField.objects.filter(form__name=self.form_name)
        return render(request, template_name="register.html", context={"field_list": form_fields_objects})

    def post(self, request):
        print(request.POST)
        form_fields_objects = models.FormField.objects.filter(form__name=self.form_name)
        record_instance = models.FormRecord.objects.create()
        for field in form_fields_objects:
            form_model_id = models.FormModel.objects.filter(name=self.form_name).first()
            form_field_id = models.FormField.objects.filter(form_id=form_model_id, name=field.name).first()
            value = request.POST[field.name]
            models.FormData.objects.create(form=form_model_id, field=form_field_id, value=value, record=record_instance)

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect(self.success_url)