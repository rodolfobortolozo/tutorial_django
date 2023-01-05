from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/1
    path('<int:questionId>/', views.detail, name='detail'),
    # /polls/1/results
    path('<int:questionId>/results', views.results, name='results'),
    # /polls/1/vote
    path('<int:questionId>/vote', views.vote, name='vote'),
    
]