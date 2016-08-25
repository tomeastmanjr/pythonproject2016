from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User

class Loan(models.Model):
    loan_name = models.CharField(max_length = 50)
    descrption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # creator = models.ForeignKey("loginreg.User", related_name = "creator")
    # travelers = models.ManyToManyField("loginreg.User", related_name = "travelers") # User.objects.get(id=request.session['id']).travelers.all is what the related name "travelers" allows you to do. That would give you all of the trips of the User.id referenced is traveling on
    # def __repr__(self):
    #     return self.destination + " " + self.creator.name + " " + str(self.travelers.all())
class Lender(models.Model):
    loan = models.ForeignKey('Loan')
    user = models.ForeignKey('loginreg.User')
    lend_amount = models.DecimalField(max_digits=19, decimal_places=2)
    min_payment_date = models.DateField()
    payment_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Borrower(models.Model):
    loan = models.ForeignKey('Loan')
    user = models.ForeignKey('loginreg.User')
    minimum = models.DecimalField(max_digits=19, decimal_places=2)
    total_amount = models.DecimalField(max_digits=19, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Card(models.Model):
    card_name = models.CharField(max_length = 50)
    card_type = models.CharField(max_length=50)
    card_number= models.BigIntegerField()
    exp_date = models.DateField()
    card_code = models.CharField(max_length=20)
    user = models.ForeignKey('loginreg.User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Bank(models.Model):
    bank_name = models.CharField(max_length=100)
    routing_number = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Bank_Account(models.Model):
    bank = models.ForeignKey('Bank')
    user = models.ForeignKey('loginreg.User')
    account_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
