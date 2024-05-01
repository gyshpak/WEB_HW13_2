from django_mongoengine import Document, fields

class Author(Document):
    fullname = fields.StringField(max_length=50)
    born_date = fields.DateField()
    born_location = fields.StringField(max_length=50)
    description = fields.StringField()


class Quote(Document):
    tags = fields.ListField(fields.StringField(max_length=10))
    authors =fields.ReferenceField(Author)
    quotes = fields.StringField()
