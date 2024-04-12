from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)

from agency.forms import TopicForm, NewspaperForm, RedactorForm, SignUpForm
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
    paginate_by = 3


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


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    form_class = TopicForm
    template_name = "agency/form.html"
    success_url = reverse_lazy("agency:topic-list")


class TopicUpdateView(LoginRequiredMixin, UpdateView):
    model = Topic
    form_class = TopicForm
    template_name = "agency/form.html"
    success_url = reverse_lazy("agency:topic-list")


class TopicDeleteView(LoginRequiredMixin, DeleteView):
    model = Topic
    template_name = "agency/confirmation.html"
    success_url = reverse_lazy("agency:topic-list")


class NewspaperCreateView(LoginRequiredMixin, CreateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "agency/form.html"
    success_url = reverse_lazy("agency:news-list")


class NewspaperUpdateView(LoginRequiredMixin, UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "agency/form.html"
    success_url = reverse_lazy("agency:news-list")


class NewspaperDeleteView(LoginRequiredMixin, DeleteView):
    model = Newspaper
    template_name = "agency/confirmation.html"
    success_url = reverse_lazy("agency:news-list")


class RedactorDetailView(LoginRequiredMixin, DetailView):
    model = Redactor
    template_name = "agency/profile.html"


class RedactorUpdateView(LoginRequiredMixin, UpdateView):
    model = Redactor
    template_name = "agency/form.html"
    form_class = RedactorForm
    success_url = reverse_lazy("agency:profile")


class RedactorDeleteView(LoginRequiredMixin, DeleteView):
    model = Redactor
    template_name = "agency/confirmation.html"


class RegisterUserView(FormView):
    template_name = "registration/register.html"
    form_class = SignUpForm
    success_url = reverse_lazy("agency:index")

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=raw_password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return super().form_invalid(form)
