from django.forms import ModelForm
from .models import Student


class StudentFrom(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'age', 'emeil']

