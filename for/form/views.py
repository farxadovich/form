from django.shortcuts import render
from django.http import HttpResponse
from .forms import TextForm





def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']

            return HttpResponse(f'salom ,{name} ,{surname}')
    else:
        form = TextForm()
    return render(request, 'form/index.html', {'form': form})
