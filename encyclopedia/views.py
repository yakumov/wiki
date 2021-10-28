from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def oarticle(request, entry):
    content = util.get_entry(entry)
    print(f"request={content}")
    print(f"title={title}")
    result = markdown2.Markdown(content)
    return render(request, "encyclopedia/oarticle.html", {
        "title": entry,
        "content": result
    })