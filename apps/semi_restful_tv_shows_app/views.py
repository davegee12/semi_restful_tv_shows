from django.shortcuts import render, HttpResponse, redirect
from .models import Shows

def index(request):
    context = {
        "all_shows": Shows.objects.all()
    }
    return render(request, 'semi_restful_tv_shows_app/index.html', context)

def add_show(request):
    return render(request, 'semi_restful_tv_shows_app/add_show.html')

def view_show(request, id):
    id = int(id)
    request.session['show_id'] = id
    context = {
        "this_show": Shows.objects.get(id = id)
    }
    return render(request, 'semi_restful_tv_shows_app/view_show.html', context)

def edit_show(request, id):
    id = int(id)
    request.session['show_id'] = id
    context = {
        "this_show": Shows.objects.get(id = id)
    }
    return render(request, 'semi_restful_tv_shows_app/edit.html', context)

def create_show(request):
    if request.method == "POST":
        show = Shows.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['release_date'], desc = request.POST['desc'])
        request.session['show_id'] = show.id
    return redirect(f"/shows/{show.id}", show)

def update_show(request):
    if request.method =="POST":
        show = Shows.objects.get(id = request.session['show_id'])
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.desc = request.POST['desc']
        show.save()
    return redirect(f"/shows/{show.id}", show)


def destroy_show(request, id):
    id = int(id)
    show = Shows.objects.get(id = id)
    show.delete()
    return redirect("/shows", show)
