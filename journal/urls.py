from django.urls import path
from . import views

app_name = "journal"

urlpatterns = [
    path("", views.JournalBookList.as_view(), name="index"),
    path("<int:pk>", views.JournalDetailView.as_view(), name="detail"),
    path("<int:pk>/update", views.update_journal_book, name="update"),
    path("<int:pk>/delete", views.delete_journal_book, name="delete"),
    path("create", views.create_journal_book, name="create"),
    path("entries/<int:pk>", views.JournalEntryDetailView.as_view(), name='entry_detail'),
    path("entries/create/<int:pk>", views.create_entry, name='entry_create'),
    path("entries/<int:pk>/update", views.update_journal_entry, name='entry_update'),
    path("entries/<int:pk>/delete", views.delete_journal_entry, name='entry_delete'),
]