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
    md2 = markdown2.Markdown()
    result = md2.convert(content)
    return render(request, "encyclopedia/oarticle.html", {
        "title": entry,
        "content": result
    })

def search(request):
    if request.method == "POST":
        get_form = request.POST
        print(f"get_form = {get_form}")
        all_list = util.list_entries()
        print(f"all_list = {all_list}")
        list_search = []
        for text in all_list:
            list = get_form.lover()
            print(f"list = {list}")
            print(f"text = {text}")
            print(f"get_form.lover() = {get_form.lover()}")
            if get_form.lover() != '' and get_form.lover() in text.lover():
                list_search.append(text)
            else:
                return render(request, "encyclopedia/oarticle.html")



    else:
        return render(request, "encyclopedia/oarticle.html")