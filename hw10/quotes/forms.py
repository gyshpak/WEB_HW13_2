from django_mongoengine.forms import DocumentForm, fields
from django.forms import DateInput, TextInput
from .models import Author, Quote


class AuthorForm(DocumentForm):
    class Meta:
        document = Author
        fields = '__all__'
        widgets = {
            "fullname": TextInput(attrs={"class": "form-control"}),
            "born_date": DateInput(attrs={"class": "form-control"}),
            "born_location": TextInput(attrs={"class": "form-control"}),
            "description": TextInput(attrs={"class": "form-control"}),
        }


class QuoteForm(DocumentForm):
    # authors = fields.EmbeddedDocumentField(AuthorForm)
    class Meta:
        document = Quote
        fields = ["tags", "authors", "quotes"]




# class AuthorForm(DocumentForm):
#     class Meta:
#         document = Author
#         fields = "__all__"
#         widgets = {
#             "fullname": TextInput(attrs={"class": "form-control"}),
#             "born_date": DateInput(attrs={"class": "form-control"}),
#             "born_location": TextInput(attrs={"class": "form-control"}),
#             "description": TextInput(attrs={"class": "form-control"}),
#         }


# fullname = fields.StringField(max_length=50, required=True)
#     born_date = fields.DateField(verbose_name=('date of birth'))
#     born_location = fields.StringField(max_length=50)
#     description = fields.StringField()

# def clean_born_date(self):
#     born_date = self.cleaned_data.get("born_date")
#     if not born_date:
#         raise ValidationError("Born date is required")
#     # try:
#     #     # Перевірка, чи можна конвертувати введену дату в формат datetime
#     #     datetime.strptime(born_date, "%Y-%m-%d")
#     # except ValueError:
#     #     raise ValidationError("Incorrect date format, should be YYYY-MM-DD")
#     return born_date


# # class TagForm(ModelForm):
# #     name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

# #     class Meta:
# #         model = Tag
# #         fields = ["name"]
