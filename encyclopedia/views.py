from django.shortcuts import render
from markdown2 import Markdown
from . import util
from django import forms

class NewSearchForm(forms.Form):
    task = forms.CharField(label="search")

def converter(name):
    file = util.get_entry(name)
    markdowner = Markdown()
    html_file = markdowner.convert(file)
    return html_file



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
    return render(request, "entry.html", {
        "form": NewSearchForm()
    })

