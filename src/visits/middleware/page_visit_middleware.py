import time
from visits.models import PageVisit


class PageVisitMiddleware:
    """
    Refernce # https://medium.com/@techWithAditya/middleware-magic-how-to-use-django-middleware-for-advanced-error-handling-and-exception-management-78573a27204e
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time()-start_time
        print(f'Request processed in {duration:.4f} seconds')
        PageVisit.objects.create(path=request.path)
        return response
