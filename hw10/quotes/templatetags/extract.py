from django import template

# from bson.objectid import ObjectId

from ..connect import connect
from ..models import Author


register = template.Library()


def get_authors(id_):

    author = Author.objects("_id" == id_).first()
    return author.fullname


register.filter("author", get_authors)
