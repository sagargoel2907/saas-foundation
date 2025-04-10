from .models import PageVisit
from django.db.models import Max


def calculate_page_visit_metrics(path):
    """
    A function that takes page path string and returns the page visit metrics data
    """
    total_visits = PageVisit.objects.all().count()
    page_visits = PageVisit.objects.filter(path=path).count()
    last_visit_time = PageVisit.objects.aggregate(Max('timestamp'))['timestamp__max']
    try:
        percentage_visits = round(page_visits*100.0/total_visits, 2)
    except:
        percentage_visits = 0
    metric_data = {
        'total_visits': total_visits,
        'page_visits': page_visits,
        'percentage_visits': percentage_visits,
        'last_visit_time': last_visit_time,
    }

    return metric_data
