from django.urls import path
from agency.views import index, TopicListView, RedactorListView, NewspaperListView, NewspaperDetailView, \
    TopicDetailView, TopicCreateView, TopicUpdateView, TopicDeleteView, NewspaperCreateView, NewspaperUpdateView, \
    NewspaperDeleteView, RedactorDetailView, RedactorUpdateView, RedactorDeleteView, register_user

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("news/", NewspaperListView.as_view(), name="news-list"),
    path("news/<int:pk>/", NewspaperDetailView.as_view(), name="news-detail"),
    path("topics/<int:pk>/", TopicDetailView.as_view(), name="topic-detail"),
    path('topics/create/', TopicCreateView.as_view(), name='topic-create'),
    path('topics/<int:pk>/update/', TopicUpdateView.as_view(), name='topic-update'),
    path('topics/<int:pk>/delete/', TopicDeleteView.as_view(), name='topic-delete'),
    path('news/create/', NewspaperCreateView.as_view(), name='newspaper-create'),
    path('news/<int:pk>/update/', NewspaperUpdateView.as_view(), name='newspaper-update'),
    path('news/<int:pk>/delete/', NewspaperDeleteView.as_view(), name='newspaper-delete'),
    path('profile/<int:pk>/', RedactorDetailView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', RedactorUpdateView.as_view(), name='profile-update'),
    path('profile/<int:pk>/delete/', RedactorDeleteView.as_view(), name='profile-delete'),
    path('registration/', register_user, name='registration'),
]

app_name = 'agency'
