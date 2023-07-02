from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home') # Редирект на домашнюю страницу после успешной регистрации
	else:
		form = UserRegistrationForm()
	return render(request, 'registration/register.html', {'form': form})


def index(request):
	return HttpResponse("<h1>Hello Nahui</h1>")