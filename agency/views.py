from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import ListView

from agency.models import Redactor, Topic, Newspaper


def index(request):
    num_of_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()
    num_newspaper = Newspaper.objects.count()
    context = {
        "num_of_redactors": num_of_redactors,
        "num_topics": num_topics,
        "num_newspaper": num_newspaper,

     }
    return render(request, "index.html", context=context)


class TopicListView(ListView):
    model = Topic
    context_object_name = "topics"
    template_name = "agency/topics.html"


class RedactorListView(ListView):
    model = Redactor
    template_name = "agency/redactors.html"


class NewspaperListView(ListView):
    model = Newspaper
    template_name = "agency/news.html"

