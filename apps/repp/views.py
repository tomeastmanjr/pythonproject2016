from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Loan
from ..loginreg.models import User
from django.contrib import messages
from datetime import datetime

def index(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))

    user = User.objects.get(id=request.session["id"])
    context = {
     "users":User.objects.all()[:100],
    #     "me": (Trip.objects.filter(creator=user) | Trip.objects.filter(travelers__id=user.id)).distinct(),
    #     "notme": Trip.objects.all().exclude(creator=user).exclude(travelers__id=user.id),
    #     "name": user.name
    }
    return render(request, 'repp/index.html', context)

def show(request):
# def show(request, trip_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))

    context = {
        # "trip": Trip.objects.get(id=trip_id),
        # "users": User.objects.all()
    }
    return render(request, 'repp/show.html', context)

def add(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))

    return render(request, 'repp/add.html')

def ryan_test(request):
    return render(request, 'repp/ryan_test.html')
def create(request, id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    
    #     user = User.objects.get(id=request.session['id'])
    #     description = request.POST["description"]
    #     trip_begin = datetime.strptime(request.POST["trip_begin"], '%Y-%m-%d')
    #     trip_end = datetime.strptime(request.POST["trip_end"], '%Y-%m-%d')
    #     destination=request.POST["destination"]
    #

    return redirect(reverse('repp:ryan_test'))
    # kwargs={"trip_id":trip.id}))
    pass

def update(request):
# def update(request, trip_id):
#     if 'id' not in request.session:
#         return redirect(reverse('loginreg:index'))
#
#     userid = User.objects.get(id=request.session['id'])
#     selected_trip = Trip.objects.get(id=trip_id)
#     selected_trip.travelers.add(userid)

    # return redirect(reverse('repp:show', kwargs={"trip_id":selected_trip.id}))
    return redirect(reverse('repp:index'))

def test(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    return render(request, 'repp/bootstrap_test.html')

def about(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    return render(request, 'repp/about.html')

def logout(request):
    request.session.clear()
    return redirect('loginreg:index')
