from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

from . import util
import markdown2
from random import *


class NewArticleForms( forms.Form) :
    article = forms.CharField(label="Найменування статті",widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label= "", widget=forms.Textarea(attrs={'class': 'form-control', 'style' :"height:100%; margin:5px 2px;"}))

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
        list_search_low = []
        for text in all_list:
            list_search_low.append(text.lower())
        if get_form['q'].lower() in list_search_low:
            return HttpResponseRedirect(f"/wiki/{get_form['q']}")
        else:
            for text in all_list:
                if text.lower().find(get_form['q']) != -1:
                    set_list.append(text)
#            if not set_list:
#                    return render(request, "encyclopedia/search.html", {
#                    "non": str("Відсутні")
#                    })
#            else:
                    return render(request, "encyclopedia/search.html", {
                    "entries": set_list
                    })
#                elif not set_list:
#                    return render(request, "encyclopedia/search.html", {
#                    "non": str("Відсутні")
#                    })

def add(request):
    if request.method == "POST":
        form = NewArticleForms(request.POST)
        if form.is_valid() :
            article = form.cleaned_data["article"]
            content = form.cleaned_data["content"]
            old_content=util.get_entry(article)
            if old_content==None:
                util.save_entry(article, content)
                return HttpResponseRedirect(f"/wiki/{oarticle}")
            else:
                return render(request, "./encyclopedia/add.html", {
                        "form": form,
                        "error": f"Стаття з назвою '{article}' вже існує. Змініть назву."
                        })
        else:
            return render(request, "./encyclopedia/add.html", {
            "form": form
            })
    else:
        return render(request, "encyclopedia/add.html", {
            "form": NewArticleForms()
            })

def edit(request, name):
    content = util.get_entry(name)
    return render(request, "encyclopedia/edit.html", {
            "form": NewArticleForms({'article':name,'content':content}),
            "title_page":name
                })


def saveedit(request):
    if request.method == "POST":
        form = NewArticleForms(request.POST)
        if form.is_valid() :
            article = form.cleaned_data["article"]
            content = form.cleaned_data["content"]
            util.save_entry(article, content)
            return HttpResponseRedirect(f"/wiki/{oarticle}")


def random(request):
    seq =  util.list_entries()
    rand = random.choice(seq)
    return HttpResponseRedirect(f"/wiki/{rand}")
