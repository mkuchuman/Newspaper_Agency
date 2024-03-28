from django.urls import path

from agency.views import index, TopicListView, RedactorListView, NewspaperListView

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("news/", NewspaperListView.as_view(), name="news-list"),
]


app_name = 'agency'
