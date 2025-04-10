from django.shortcuts import render
from visits.utils import calculate_page_visit_metrics


def home_view(request):
    page_visit_metrics = calculate_page_visit_metrics(request.path)
    context = {
        **page_visit_metrics
    }
    return render(request, 'home.html', context)


def about_view(request):
    page_visit_metrics = calculate_page_visit_metrics(request.path)
    context = {
        **page_visit_metrics
    }
    return render(request, 'about.html', context)
