from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class JournalBook(models.Model):
    user = models.ForeignKey(User, related_name="user_journalbooks", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Journal Books"

    def __str__(self):
        return self.title

class JournalEntry(models.Model):
    user = models.ForeignKey(User, related_name="user_journalentries", on_delete=models.CASCADE)
    journalbook = models.ForeignKey(JournalBook, related_name="journalbook_entries", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Journal Entries"

    def __str__(self):
        return self.title


