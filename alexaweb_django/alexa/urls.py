from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url
from views import(StartAuthView,
                  CodeAuthView)

urlpatterns = [
                url(r'^start/$',
                    csrf_exempt(StartAuthView.as_view())),
                url(r'^code/$',
                    csrf_exempt(CodeAuthView.as_view())),        
        ]