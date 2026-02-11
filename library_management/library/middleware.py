import datetime


class LoggingMiddleware:

    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        print(f"[{datetime.datetime.now()}] {request.method} {request.path}")
        response = self.get_response(request)
        print(f"[{datetime.datetime.now()}] Response status: {response.status_code}")
        return response
