from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentFrom





def index(request):
    if request.method == 'GET':
        form = StudentFrom()
        return render(request, 'form/index.html', {'form': form})

def qabul(request):
    if request.method == 'POST':
        form = StudentFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Bajarildi')




