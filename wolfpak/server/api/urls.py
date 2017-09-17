from django.conf.urls import url, include

from api.views.pak import PakDetail

urlpatterns = [
    url(r'^pak/(?P<pak_id>\d+)', PakDetail.as_view()),
]
