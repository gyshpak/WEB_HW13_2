from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


from .connect import connect

#### for test ####
# from connect import connect
# from models_mongo import Author, Quote
#### for test ####

from .forms import AuthorForm, QuoteForm
from .models import Quote, Author

def main(request, page=1):

    quotes = Quote.objects.aggregate(
        [
            {
                "$lookup": {
                    "from": "author",
                    "localField": "authors",
                    "foreignField": "_id",
                    "as": "author",
                    "pipeline": [{"$project": {"fullname": 1, "_id": 0}}],
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "tags": 1,
                    "quotes": 1,
                    "authors": 1,
                    "author": {"$arrayElemAt": ["$author.fullname", 0]},
                }
            },
        ]
    )

    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


def author(request, authors):
    author = Author.objects("_id" == authors).first()
    return render(request, "quotes/author.html", context={"author": author})


def tag(request, tag):
    quotes = Quote.objects(tags = tag)
    return render(
        request, "quotes/tag.html", context={"quotes": quotes, "viev_tag": tag}
    )


@login_required


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(to="quotes:root")
            except Exception:
                # form.is_valid(): не працює (((
                print("Помилка при збереженні даних:")
                return render(request, "quotes/add_author.html", {"form": form})
        else:
            return render(request, "quotes/add_author.html", {"form": form})
    else:
        return render(request, "quotes/add_author.html", {"form": AuthorForm()})


# def add_author(request):
#     if request.method == "POST":
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to="quotes:root")
#         else:
#             return render(request, "quotes/add_author.html", {"form": form})
#     else:
#         return render(request, "quotes/add_author.html", {"form": AuthorForm()})


@login_required
def add_quote(request):
    authors = Author.objects()
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            # print(f" author = {form.authors}")
            form.save()
            return redirect(to="quotes:root")
        else:
            # print(f" author = {form.quotes}")
            return render(request, "quotes/add_quote.html", {"form": form})
    else:
        return render(request, "quotes/add_quote.html", {"authors": authors, "form": QuoteForm()})

    # return render(request, "quotes/add_quote.html", context={"quote": "add_quote"})


###########################   TEST   #################################
# def author2(authors = None):
#     quotes = []
#     # author = Author.objects()
#     # print(f"author = {author.fullname}")
#     quotes_ = Quote.objects()
#     # for quote in quotes_:
#     #     quotes.append(quote.quotes)
#     print (quotes_)


# def tag2(tag):

#     quotes = Quote.objects(tags = tag)
#     for quote in quotes:
#         print(quote)


# if __name__ == "__main__":
#     # author2()
#     # author2("65fa02258b6d7cf555553c6d")
#     tag2("thinking")
