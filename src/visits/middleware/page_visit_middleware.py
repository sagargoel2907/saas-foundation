import time
from visits.models import PageVisit

class PageVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        PageVisit.objects.create(path=request.path)
        response = self.get_response(request)
        duration = time.time()-start_time
        print(f'Request processed in {duration:.4f} seconds')
        return response
