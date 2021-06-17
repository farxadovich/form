from django import forms


class TextForm(forms.Form):
    ismi = forms.CharField(label="Your first name ", max_length=80)
    familiyasi = forms.CharField(label="Your second name", max_length=90)