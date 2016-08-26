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

def show_loan(request):
# def show_loan(request, loan_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))

    # context = {
    #     "loan": Loan.objects.get(id=loan_id),
    #     "users": User.objects.all()
    # }
    # return render(request, 'repp/show_loan.html', context)
    return render(request, 'repp/show_loan.html')

def add_loan(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))

    return render(request, 'repp/add_loan.html')

def ryan_test(request):
    return render(request, 'repp/ryan_test.html')

def create(request):
    errors = []
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    if request.POST["payment_deadline"] and request.POST["min_payment_date"]:
       user = User.objects.get(id=request.session['id'])
       description = request.POST["description"]
       payment_deadline = datetime.strptime(request.POST["payment_deadline"], '%Y-%m-%d')
       min_payment_date = datetime.strptime(request.POST["min_payment_date"], '%Y-%m-%d')
       destination=request.POST["destination"]

       if len(description) >1 and len(description) >1 and trip_begin > datetime.now() and trip_end > trip_begin:
           trip = Trip.objects.create(description=description, trip_begin=trip_begin, trip_end=trip_end, destination=destination, creator=user)
           return redirect(reverse('repp:show_loan', kwargs={"loan_id":loan.id}))
    else:
        messages.add_message(request, messages.SUCCESS, 'Try again')
        return redirect(reverse('repp:add_loan', kwargs={"loan_id":loan.id}))
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
