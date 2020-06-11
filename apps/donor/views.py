from django.shortcuts import render
from .models import Donor
# Create your views here.

def home(request):
    total_donor = Donor.objects.filter(status='p').count()
    donor_list = Donor.objects.order_by('name').filter(status='p',blood_donor_status=True)
    context = {
        'total_donor' : total_donor,
        'donor_list' : donor_list,
        'nbar':'home'
    }
    return render(request,'index.html',context)

def organisation(request):
    return render(request,'donor/organisation.html')

# def home1(request):
    
#     total_org_list = Organisation.objects.filter(status=True).count()
#     divisions = City.objects.all().order_by('name')
#     districts = District.objects.all().order_by('name')
#     thanas = Thana.objects.all().order_by('name')
#     all_org_page_obj = None
#     context = {}
#     if total_org_list > 0:
#         all_org = Organisation.objects.filter(status=True).order_by('name')
#         paginator = Paginator(all_org, 10) # Show 25 contacts per page.
#         page_number = request.GET.get('page')
#         all_org_page_obj = paginator.get_page(page_number)
#     else:
#         all_org = False
    
#     total_org_project_list = OrgProject.objects.filter(status=True,end_date__gte=datetime.date.today()).count()
#     all_running_projects = None
#     if total_org_project_list > 0:
#         all_running_projects = OrgProject.objects.filter(status=True,end_date__gte=datetime.date.today()).order_by('end_date')
    
#     context = {
#         'organisation_list': all_org_page_obj,
#         'all_running_projects': all_running_projects,
#         'divisions': divisions,
#         'districts': districts,
#         'thanas': thanas,
#         'nbar': 'home',
#     }
#     return render(request, 'index_main.html', context)