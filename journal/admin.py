from django.contrib import admin
from .models import JournalBook, JournalEntry
# Register your models here.
admin.site.register(JournalBook)
admin.site.register(JournalEntry)