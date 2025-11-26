from django import forms

class CreateTask(forms.Form):
    name_task = forms.CharField()
    discription = forms.CharField()
    date = forms.DateField()
    time = forms.TimeField()