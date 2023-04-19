from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import TopicForm, EntryForm
from .models import Topic, Entry


# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request):
    topic_list = Topic.objects.order_by('date_added')
    context = {'topics': topic_list}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    find_topic = Topic.objects.get(id=topic_id)
    entries = find_topic.entry_set.order_by('date_added')
    context = {'topic': find_topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("learning_logs:topics"))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    exist_topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            add_entry = form.save(commit=False)
            add_entry.topic = exist_topic
            add_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': exist_topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
