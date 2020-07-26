from django.forms import ModelForm
from .models import JournalBook

class JournalBookForm(ModelForm):
    class Meta:
        model = JournalBook
        fields = ['title','description',]