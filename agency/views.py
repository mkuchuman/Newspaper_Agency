from django.shortcuts import render

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
