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
        all_list = util.list_entries()
        set_list = []
        list_search_low.clear()
        for text in all_list:
            list_search_low.append(text.lower())
        if get_form['q'].lower() != '' and get_form['q'].lower() in list_search_low:
                return HttpResponseRedirect(f"/wiki/{get_form['q']}")
        else:
            for text in all_list:
                if text.lower().find(get_form['q']) != -1:
                    set_list.append(text)
            context = {
                "non": set_list
            }
            return render(request, "encyclopedia/search.html", context = context)

    else:
        return render(request, "encyclopedia/oarticle.html")