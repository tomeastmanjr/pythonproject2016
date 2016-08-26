from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Loan, Lender, Borrower
from ..loginreg.models import User
from django.contrib import messages
from datetime import datetime

def index(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))

    user = User.objects.get(id=request.session["id"])
    context = {
        "lender": Lender.objects.filter(user__id=request.session["id"]),
        "borrower": Borrower.objects.filter(user__id=request.session["id"])
    }
    return render(request, 'repp/index.html', context)

def show_loan(request, loan_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))

    context = {
        "loan": Loan.objects.get(id=loan_id)
    }
    return render(request, 'repp/show_loan.html', context)
    # return render(request, 'repp/show_loan.html')

def add_loan(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))

    return render(request, 'repp/add_loan.html')

def ryan_test(request):
    return render(request, 'repp/ryan_test.html')

def create(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    if request.POST["payment_deadline"] and request.POST["min_payment_date"]:
       user = User.objects.get(id=request.session['id'])
       descrption = request.POST["descrption"]
       payment_deadline = datetime.strptime(request.POST["payment_deadline"], '%Y-%m-%d')
       min_payment_date = datetime.strptime(request.POST["min_payment_date"], '%Y-%m-%d')
       borrower_email=request.POST["borrower_email"]
       loan_name=request.POST["loan_name"]
       lend_amount=request.POST["lend_amount"]
       borrow= User.objects.get(email=borrower_email)


       if len(descrption) >1:
           loan = Loan.objects.create(loan_name=loan_name, descrption=descrption)
           lender = Lender.objects.create(loan=loan, user=user,  lend_amount=lend_amount, min_payment_date=min_payment_date, payment_deadline=payment_deadline)
           borrower = Borrower.objects.create(loan=loan, user=borrow, minimum=lend_amount, total_amount=lend_amount)
        #    loan.save()
        #    lender.save()
        #    borrower.save()
           return redirect(reverse('repp:show_loan', kwargs={"loan_id":loan.id}))
        #    return redirect(reverse('repp:show_loan'))
    else:
        messages.add_message(request, messages.SUCCESS, 'Try again')
        return redirect(reverse('repp:add_loan'))
    # kwargs={"loan_id":loan.id}))

def update(request, loan_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    if request.POST["payment_deadline"] and request.POST["min_payment_date"] and request.POST["descrption"] and request.POST["loan_name"]:
        a = Loan.objects.get(id=loan_id)
        a.descrption = request.POST["descrption"]
        a.loan_name = request.POST["loan_name"]
        a.payment_deadline = datetime.strptime(request.POST["payment_deadline"], '%Y-%m-%d')
        a.min_payment_date = datetime.strptime(request.POST["min_payment_date"], '%Y-%m-%d')
        # today = datetime(year=now.year, month=now.month, day=now.day)
        # if a.payment_deadline >= today:
        a.save()
        # else:
        #     print a.min_payment_date
        #     messages.add_message(request, messages.SUCCESS, 'Try again')
        #     a = Loan.objects.get(id=loan_id)
        #     return redirect(reverse('repp:update', kwargs={"loan_id":a.id}))
    else:
        messages.add_message(request, messages.SUCCESS, 'Try again')
        a = Loan.objects.get(id=loan_id)
        return redirect(reverse('repp:update', kwargs={"loan_id":a.id}))
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
