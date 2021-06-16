from django import forms


class TextForm(forms.Form):

    name = forms.CharField(label='name', max_length=100),
    surname = forms.CharField(label='surname', max_length=100)