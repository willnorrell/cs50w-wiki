from django.shortcuts import render
from markdown2 import Markdown
from . import util
from django import forms


def converter(name):
    file = util.get_entry(name)
    markdowner = Markdown()
    html_file = markdowner.convert(file)
    if file != None:
        return html_file
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
    elif html_file == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/error.html" )


def search(request):
    entries = util.list_entries()
    matches = []

    if request.method == "POST":
        answer = request.POST["q"]
        html_file = converter(answer)
        for i in entries:
            if answer in entries:
                matches.append(i)
        if html_file != None:
            return render(request, "encyclopedia/entry.html", {
                "file": html_file,
                "title": answer
            })
        elif len(matches) != 0:
            render(request, "search.html")
        else:
            render(request, "encyclopedia/search.html")


'''
    for string in string_list:
        if target_string in string:
            matches.append(string)
    return matches
'''