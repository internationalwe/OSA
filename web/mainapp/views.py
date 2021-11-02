from django.shortcuts import render
from cmpapp.models import CompanyList

# Create your views here.
def main(request):
    company_name_list = CompanyList.objects.order_by('id')
    context = {
        'company_name_list' : company_name_list
    }
    return render(request, 'mainapp/mainview.html', context)