from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import JournalBookForm
from django.db import transaction
# Create your views here.
def index(request):
    n = range(1,12)
    journals = request.user.user_journalbooks.all()
    context = { 
        "n" : n,
        "journals" : journals 
    }
    return render(request, "journal/index.html", context=context)

class JournalBookList(LoginRequiredMixin, ListView):

    model = JournalBook
    context_object_name = 'journals'
    template_name = "journal/index.html"

    def get_queryset(self):
        return self.request.user.user_journalbooks.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class JournalDetailView(LoginRequiredMixin, DetailView):
    model = JournalBook
    context_object_name = 'journal'




class JournalEntryDetailView(LoginRequiredMixin, DetailView):
    model = JournalEntry
    context_object_name = 'entry'


"""
Function-based Views
We will convert them to class-based views soon.
"""
@login_required()
@transaction.atomic()
def create_journal_book(request):
    form = JournalBookForm()

    if request.method == 'GET':
        return render(request, "journal/journalbook_create.html", { "form" : form })
    elif request.method == 'POST':
        form = JournalBookForm(request.POST)
        if form.is_valid():
            journalbook = form.save(commit=False)
            journalbook.user = request.user
            journalbook.save()
        return redirect(reverse("journal:detail", args=(journalbook.id,)))

@login_required()
@transaction.atomic()
def update_journal_book(request, pk):
    journal = request.user.user_journalbooks.get(pk=pk)
    form = JournalBookForm(instance=journal)

    if request.method == 'GET':
        return render(request, "journal/journalbook_update.html", { "form" : form })
    elif request.method == 'POST':
        form = JournalBookForm(request.POST, instance=journal)

        if form.is_valid():
            journalbook = form.save()
        return redirect(reverse("journal:detail", args=(journalbook.id,)))

@login_required()
def delete_journal_book(request, pk):
    journal = request.user.user_journalbooks.get(pk=pk)
    journal.delete()
    return redirect(reverse("journal:index"))

@login_required()
@transaction.atomic()
def create_entry(request, pk):
    journal = request.user.user_journalbooks.get(pk=pk)
    if request.method == 'GET':
        context = {
            "journal" : journal,
        }
        return render(request, "journal/journalentry_create.html", context)
    elif request.method == "POST":
        entry = JournalEntry(
            title=request.POST['title'],
            body=request.POST['text_body'],
            journalbook=journal,
            user=request.user
        )
        entry.save()
        return redirect(reverse("journal:entry_detail", args=(entry.id,)))


@login_required()
def update_journal_entry(request, pk):
    entry = request.user.user_journalentries.get(pk=pk)

    if request.method == 'POST':
        entry.title = request.POST['title']
        entry.body = request.POST.get('text_body')
        entry.save()
        
    return redirect(reverse("journal:entry_detail", args=(entry.id,)))

@login_required()
def delete_journal_entry(request, pk):
    entry = request.user.user_journalentries.get(pk=pk)
    journal = request.user.user_journalbooks.get(pk=entry.journalbook.id)
    entry.delete()
    return redirect(reverse("journal:detail", args=(journal.id,)))


