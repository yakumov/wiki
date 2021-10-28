from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def oarticle(request, title):
    content = util.get_entry(title)
    result = markdown2.Markdown(content)
    return render(request, "encyclopedia/oarticle.html", {
        "title": title,
        "content": result
    })