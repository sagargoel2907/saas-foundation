from .models import PageVisit


def calculate_page_visit_metrics(path):
    total_visits = PageVisit.objects.all().count()
    page_visits = PageVisit.objects.filter(path=path).count()
    try:
        percentage_visits = round(page_visits*100.0/total_visits, 2)
    except:
        percentage_visits = 0
    metric_data = {
        'total_visits': total_visits,
        'page_visits': page_visits,
        'percentage_visits': percentage_visits,
    }

    return metric_data
