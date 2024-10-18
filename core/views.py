from django.shortcuts import render
from django.urls import reverse_lazy

def main(request):
    return render(request, 'core/main.html', {})