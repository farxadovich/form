from django.shortcuts import render
from django.http import HttpResponse
from .forms import TextForm





def index(request):
    if request.method == 'GET':
        form = TextForm()
        return render(request, 'form/index.html', {'form': form})



def post_method(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            ismi = form.cleaned_data['ismi']
            familiyasi = form.cleaned_data['familiyasi']
            return HttpResponse(f"salom {ismi}  {familiyasi}")
        return render(request, 'form/index.html', {'form': form})

