from django.shortcuts import render

from django.http import HttpResponse

from .models import Company

def index(request):
    latest_question_list = Company.objects.order_by('-created_At')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'portfolio/index.html', context)