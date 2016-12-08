from django.utils import timezone
from .models import UserProfile


class UpdateLastActivityMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    # def process_view(self, request):
    #     assert hasattr(request, 'user')
    #     print("AZAZAZA\n")
    #     if request.user.is_authenticated():
    #         UserProfile.objects.filter(user__id=request.user.id) \
    #                             .update(last_activity=timezone.now())

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        assert hasattr(request, 'user')
        if request.user.is_authenticated():
            UserProfile.objects.filter(user__id=request.user.id) \
                .update(last_activity=timezone.now())

        return response