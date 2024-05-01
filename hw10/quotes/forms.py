from django_mongoengine.forms import DocumentForm, fields
from django.forms import DateInput, TextInput
from .models import Author, Quote


class AuthorForm(DocumentForm):
    class Meta:
        document = Author
        fields = "__all__"
        widgets = {
            "fullname": TextInput(attrs={"class": "form-control"}),
            "born_date": DateInput(attrs={"class": "form-control"}),
            "born_location": TextInput(attrs={"class": "form-control"}),
            "description": TextInput(attrs={"class": "form-control"}),
        }


class QuoteForm(DocumentForm):
    class Meta:
        document = Quote
        fields = ["tags", "authors", "quotes"]
