from django_mongoengine import Document, fields, EmbeddedDocument

# class Author(Document):
#     fullname = fields.StringField(max_length=50)#, required=True)
#     born_date = fields.DateField() #verbose_name=('date of birth'))
#     born_location = fields.StringField(max_length=50)
#     description = fields.StringField()


# class Author(EmbeddedDocument):
class Author(Document):
    fullname = fields.StringField(max_length=50)  # , required=True)
    born_date = fields.DateField()  # verbose_name=('date of birth'))
    born_location = fields.StringField(max_length=50)
    description = fields.StringField()


class Quote(Document):
    tags = fields.ListField(fields.StringField(max_length=10))
    # tags = fields.ListField()
    # tags = fields.StringField(max_length=220)
    # authors = fields.EmbeddedDocumentField(Author)
    authors =fields.ReferenceField(Author)
    quotes = fields.StringField()
