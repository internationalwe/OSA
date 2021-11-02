from django.shortcuts import render,HttpResponse
from .models import CompanyList, CompanyESG

# Create your views here.
def cmplist(request):
    company_list = CompanyList.objects.order_by('id')
    context = {
        'company_list' : company_list
    }
    return render(request, 'cmpapp/cmplist.html', context)

def cmp(request, company_id):
    company = CompanyList.objects.get(pk=company_id)
    company_esg = CompanyESG.objects.get(pk=company_id)
    return render(request, 'cmpapp/cmp.html', {'company' : company, 'company_esg' : company_esg})