from django.shortcuts import render
from markdown2 import Markdown
from . import util
from django import forms


def converter(name):
    file = util.get_entry(name)
    markdowner = Markdown()
    if file != None:
        return markdowner.convert(file)
    else:
        return None


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    html_file = converter(title)
    if html_file:
        return render(request, f"encyclopedia/entry.html", {
            "file": html_file,
            "title": title
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": title
        } )


def search(request):
    entries = util.list_entries()
    matches = []

    if request.method == "POST":
        answer = request.POST["q"]
        html_file = converter(answer)

        if html_file != None:
            return render(request, "encyclopedia/entry.html", {
                "file": html_file,
                "title": answer
            })

        else:
            for i in entries:
                if answer.lower() in i.lower():
                    matches.append(i)

            return render(request, "encyclopedia/search.html", {
                            "entries": matches   
                         })


def new(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST['content']
        util.save_entry(title, content)
    else:
        return render(request, "encyclopedia/new.html")