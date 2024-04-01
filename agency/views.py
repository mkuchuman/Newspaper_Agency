from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from agency.forms import TopicForm, NewspaperForm
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
    paginate_by = 6


class RedactorListView(ListView):
    model = Redactor
    template_name = "agency/redactors.html"
    paginate_by = 3


class NewspaperListView(ListView):
    model = Newspaper
    template_name = "agency/news.html"
    paginate_by = 3


class TopicDetailView(DetailView):
    model = Topic
    template_name = "agency/topic-detail.html"


class NewspaperDetailView(DetailView):
    model = Newspaper
    template_name = "agency/new-detail.html"


class TopicCreateView(CreateView):
    model = Topic
    form_class = TopicForm
    template_name = 'agency/form.html'
    success_url = reverse_lazy('agency:topic-list')


class TopicUpdateView(UpdateView):
    model = Topic
    form_class = TopicForm
    template_name = 'agency/form.html'
    success_url = reverse_lazy('agency:topic-list')


class TopicDeleteView(DeleteView):
    model = Topic
    template_name = "agency/confirmation.html"
    success_url = reverse_lazy('agency:topic-list')


class NewspaperCreateView(CreateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = 'agency/form.html'
    success_url = reverse_lazy("agency:news-list")


class NewspaperUpdateView(UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = 'agency/form.html'
    success_url = reverse_lazy("agency:news-list")


class NewspaperDeleteView(DeleteView):
    model = Newspaper
    template_name = "agency/confirmation.html"
    success_url = reverse_lazy("agency:news-list")
