from django.shortcuts import render
from django.views import  View
from .models import *
from .forms import *
from django.http import *
from django.contrib import auth
# Create your views here.
class Home(View):
    def get(self,request):

        return render(request,"main.html",{'fullname':'Guest'})


class LoginHome(View):


    def get(self,request):
        if request.user.is_authenticated():
            return render(request,'main.html',{'fullname':request.user.username})
        else:
            return HttpResponseRedirect('/login/')

class LogoutOption(View):
    def get(self,request):
        auth.logout(request)
        return HttpResponseRedirect('/')



class Athe(View):
    def post(self,request):
        username = request.POST.get('username', '')
        print 'x'
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        print 'x'

        if user is not  None:
            auth.login(request,user)
            return HttpResponseRedirect('/accounts/home/')
        else:
            return HttpResponseRedirect('/accounts/invalid/')

class invalidClass(View):
    def get(self, request):
        return render(request, 'doLogin.html',{'error':'username or password is invalid'})



class CreateAccount(View):
    formreg=AccRegistration

    def get(self,request):
        form=self.formreg()
        return render(request,'register.html',{'form':form})


    #validation
    def post(self,request):
        form=self.formreg(request.POST)
        if form.is_valid():
            user=User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )
            userdata=UserDataBase(
                user=user,
                question=form.cleaned_data['que'],
                ans=form.cleaned_data['ans'],
                address=form.cleaned_data['address'],
                phonumber=form.cleaned_data['phno']
            )
            userdata.save()
            account=accDetail(
                uname=userdata,
                acc_type=form.cleaned_data['acc_type'],
                amount=0
            )
            account.save()
        #return  HttpResponse('sucess')
        return  HttpResponseRedirect('/')

class Login(View):

    def get(self,request):
        return  render(request,'doLogin.html')

class DepositeMoney(View):
    formdep=DepoAmount
    def get(self,request):
        if request.user.is_authenticated():
            form = self.formdep()
            u=User.objects.get(username=request.user)
            udata = UserDataBase.objects.get(user=u)
            uaccount = accDetail.objects.get(uname=udata)
            return render(request, 'deposite.html', {'form': form,
                                                     'accountnumber':uaccount.account_number,
                                                     'balance':uaccount.amount,
                                                     'name':request.user})
        else:
            return HttpResponseRedirect('/login/')


    def post(self,request):
        form=self.formdep(request.POST)
        try:
            if form.is_valid():
                u = User.objects.get(username=request.user)
                udata = UserDataBase.objects.get(user=u)
                uaccount = accDetail.objects.get(uname=udata)

                uaccount.amount += form.cleaned_data['amount']
                k = 'Deposite'
                tra = traDetail(
                    ac_id=uaccount,
                    tra_amt=form.cleaned_data['amount'],
                    tra_type=k
                )
                tra.save()
                uaccount.save()
                # return HttpResponse('sucess')
                return render(request, 'doDeposite.html', {'money': uaccount.amount,
                                                           'name': request.user})  # after putting money
        except:
            return render(request, 'deposite.html', {'form': form,
                                                     'accountnumber': uaccount.account_number,
                                                     'balance': uaccount.amount,
                                                     'name': request.user,
                                                     'error':'something went wrong please reenter the amount'})



class WithDrawMoney(View):
    formdep = WithDraw

    def get(self, request):
        if request.user.is_authenticated():
            form = self.formdep()
            u = User.objects.get(username=request.user)
            udata = UserDataBase.objects.get(user=u)
            uaccount = accDetail.objects.get(uname=udata)
            return render(request, 'withdraw.html',{'form': form,
                                                     'accountnumber':uaccount.account_number,
                                                     'balance':uaccount.amount,
                                                     'name':request.user})
        else:
            return HttpResponseRedirect('/login/')

    def post(self, request):
        form = self.formdep(request.POST)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            udata = UserDataBase.objects.get(user=u)
            uaccount = accDetail.objects.get(uname=udata)
            k=form.cleaned_data['amount']
            if(uaccount.amount<k):
                return render(request, 'withdraw.html', {'form': form,
                                                         'accountnumber': uaccount.account_number,
                                                         'balance': uaccount.amount,
                                                         'error':'low balance',
                                                         'name': request.user})



            uaccount.amount -= form.cleaned_data['amount']


            tra = traDetail(
                ac_id=uaccount,
                tra_amt=form.cleaned_data['amount'],
                tra_type='Withdraw'
            )
            tra.save()
            uaccount.save()
            #return HttpResponse('sucess')
            return render(request,'doWithdraw.html',{'money':uaccount.amount,
                                                     'name':request.user} )  # after withdraw money



class allTransation(View):

    def get(self,request):
        if request.user.is_authenticated():
            u = User.objects.get(username=request.user)
            udata = UserDataBase.objects.get(user=u)
            uaccount = accDetail.objects.get(uname=udata)
            tobj=traDetail.objects.all().filter(ac_id=uaccount)
            return render(request,'view-reports.html',{'trantion':tobj,
                                                       'name':request.user,
                                                       'accountnumber':uaccount.account_number})
        else:
            return HttpResponseRedirect('/login/')

class getBalance(View):

    def get(self,request):
        if request.user.is_authenticated():
            u = User.objects.get(username=request.user)
            udata = UserDataBase.objects.get(user=u)
            uaccount = accDetail.objects.get(uname=udata)

            return render(request,'get-balance-fanal.html',{'money':uaccount.amount,
                                                            'name':request.user,
                                                            'accountnumber':uaccount.account_number})
        else:
            return HttpResponseRedirect('/login/')




class userDetail(View):

    def get(self,request):
        if request.user.is_authenticated():
            u = User.objects.get(username=request.user)
            udata = UserDataBase.objects.get(user=u)
            uaccount = accDetail.objects.get(uname=udata)

            return render(request, 'userdetail.html', {'accdetail': uaccount,
                                                              'user':udata })
        else:
            return HttpResponseRedirect('/login/')



