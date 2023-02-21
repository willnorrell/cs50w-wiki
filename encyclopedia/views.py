from django.shortcuts import render
from markdown2 import Markdown
from . import util

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
    entries = util.list_entries()
    if title in entries:
        return  