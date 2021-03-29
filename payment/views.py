from django.shortcuts import render
from .models import Paymentinfo,finalpayment
from django.db.models import Avg,Sum
from django.db.models import Q
import math
# Create your views here.
def paymentpage(request):
    return render(request,'payment.html')

def paymentsearch(request):
    template = 'payment2.html'
    query = request.GET.get('q')
    querys = request.GET.get('qs')
    queryss=request.GET.get('qss')
    resul=Paymentinfo.objects.filter(Q(paymentclass__icontains=query) & Q(paymentterm__icontains=querys) & Q(section__icontains=queryss))

    return render(request, template, {'resul': resul})

def finalpayments(request):
    if request.method == "POST":
        reference_id = request.POST['reference_id']
        email = request.POST['email']
        date = request.POST['date']
        paymentclass = request.POST['paymentclass']
        paymentterm=request.POST['paymentterm']
        paymentamount=request.POST['paymentamount']
        section=request.POST['section']
        savefinalpaymentss=finalpayment(section=section,paymentamount=paymentamount,date=date,email=email,reference_id=reference_id,paymentclass=paymentclass,paymentterm=paymentterm)
        savefinalpaymentss.save()
        return render(request,'payment-success.html')
    else:
        return render(request,'payment2.html')

def paymentreceipt(request):
    template = 'receipt.html'
    query = request.GET.get('q')
    resul=finalpayment.objects.filter(Q(reference_id__icontains=query))

    return render(request, template, {'resul': resul})

def calculations(request):
    return render(request,'account2.html')



def paymenteval(request):
    template = 'account3.html'
    query = request.GET.get('q1')
    querys= request.GET.get('qs2')
    queryss = request.GET.get('qss3')
    accounts=finalpayment.objects.filter(Q(paymentclass__icontains=query) & Q(section__icontains=querys) & Q(paymentterm__icontains=queryss))
    real=Paymentinfo.objects.filter(Q(paymentclass__icontains=query) & Q(section__icontains=querys) & Q(paymentterm__icontains=queryss))
    ty = accounts.aggregate(sum_of_fee=Sum('paymentamount'))
    ip = math.floor(ty['sum_of_fee'])
    ti = real.aggregate(sum_of=Sum('paymentamount'))
    il = math.floor(ti['sum_of'])
    ki=accounts.count()
    ji=il*ki
    op=ji-ip
    return render(request, template, {'accounts': accounts,'ip':ip,'real':real,'ji':ji,'op':op})
