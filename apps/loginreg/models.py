from __future__ import unicode_literals
from django.db import models

import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def register(self, reg_data):
        errors = []
        first_name = reg_data['first_name']
        last_name = reg_data['last_name']
        email = reg_data['email']
        username = reg_data['username']
        password = reg_data['password']
        confirm_password = reg_data['confirm_password']
        ssn = reg_data['ssn']
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        try:
            user = self.get(email=email)
        except:
            user = False
        if not first_name:
            errors.append("Please enter a valid first name")
        if not last_name:
            errors.append("Please enter a valid last name")
        if not EMAIL_REGEX.match(email):
            errors.append("Please enter a valid email")
        if user:
            errors.append("Email already exists. Please enter a different email")
        if not len(username)>3:
            errors.append("Please enter a valid username")
        if not len(password)>5:
            errors.append("Please enter a valid password")
        if not password == confirm_password:
            errors.append("Make sure password and confirm password are matching")
        if not len(ssn)==9:
            errors.append("Enter your 9 digit Social Security Number")
        if errors:
            return (False, errors)
        else:
            u = self.create(first_name=first_name, last_name=last_name, email=email, username=username, ssn=ssn, password=hashed)
            return (True, u)

    def login(self, log_data):
        email = log_data['email']
        user = self.filter(email=email)
        password = log_data['password']
        if len(user) and bcrypt.hashpw(password.encode(), user[0].password.encode()) == user[0].password:
            return (True, user[0])
        return (False, 'Password or username are incorrect')



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=150)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=100)
    ssn = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
