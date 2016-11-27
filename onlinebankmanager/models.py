from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

#userdata base for setting data base

class UserDataBase(models.Model):
    user=models.OneToOneField(User)
    question=models.CharField(max_length=50)
    ans=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    phonumber=PhoneNumberField(blank=True)


    def __unicode__(self):
        return self.user.username

# delatil of account type
class accDetail(models.Model):
    account_choise=(('Student','Student'),('Saving','Saving'))
    uname=models.OneToOneField(UserDataBase)
    account_number=models.AutoField(primary_key=True,editable=False)
    acc_type=models.CharField(max_length=30,choices=account_choise)
    amount=models.FloatField(unique=True)


    def __unicode__(self):
        return str(self.account_number)
# detail of all trainsation delail
class traDetail(models.Model):
    tar_option=(('Withdraw','Withdraw'),('Deposite','Deposite'))
    tra_id=models.AutoField(primary_key=True,editable=False)
    ac_id=models.ForeignKey(accDetail)
    tra_type=models.CharField(max_length=30,choices=tar_option)
    tra_amt=models.FloatField()

    def __unicode__(self):
        return str(self.tra_id)





