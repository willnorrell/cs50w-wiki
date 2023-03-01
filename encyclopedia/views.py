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
            "title": title,
            "already_exists": False
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
        entries = util.list_entries()
        lower_list = []
        title = request.POST["title"]
        for string in entries:
            lower_list.append(string.lower())
        if title.lower() in lower_list:
            return render(request, "encyclopedia/error.html", {
                    "title": False,
                    "already_exists": title
                    })
        else:
            content = request.POST['content']
            util.save_entry(title, content)
            html_file = converter(title)
            return render(request, "encyclopedia/entry.html", {
                "file": html_file,
                "title": title
            })
    else:
        return render(request, "encyclopedia/new.html")
    

def edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })


def save(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        html_file = converter(title)
        return render(request, f"encyclopedia/entry.html", {
            "file": html_file,
            "title": title
        })


def random(request):
    pass