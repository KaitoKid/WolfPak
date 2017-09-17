from django.conf.urls import url

from api.views.quest import QuestDetail
from api.views.receive import ReceiveDetail
from api.views.allquests import AllQuestsDetail
from api.views.deletedwight import DDwightDetail

urlpatterns = [
    url(r'^quests/(?P<quest_id>\d+)', QuestDetail.as_view()),
    url(r'^receive/', ReceiveDetail.as_view()),
    url(r'^allquests/', AllQuestsDetail.as_view()),
    url(r'^ddwight/', DDwightDetail.as_view()),
]
