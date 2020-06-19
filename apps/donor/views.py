from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.http import JsonResponse

from django.views import generic

from .models import Donor, Member, OrgMemorie
from .forms import DonorRegForm
from apps.information.models import OrgContact

# Create your views here.




def home(request):
    contact = OrgContact.objects.order_by('-created_date')[:1]
    contact_obj = ''
    if contact:
        contact_obj = contact[0]
    global donor_form
    total_donor = Donor.objects.filter(status='p').count()
    donor_list = Donor.objects.order_by('name').filter(status='p', blood_donor_status=True)

    if request.method == 'POST':
        form = DonorRegForm(request.POST)

        if form.is_valid():
            form.save()
            message = 'ব্লাড ডোনার হিসেবে যোগদান করার জন্যে আপনাকে ধন্যবাদ !'
            messages.success(request, message)
            print('success')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        donor_form = DonorRegForm()

    context = {
        'total_donor': total_donor,
        'donor_list': donor_list,
        'nbar': 'home',
        'contacts': contact_obj,
        'form': donor_form,
    }
    return render(request, 'index.html', context)


class OrganisationView(generic.ListView):
    model = Member
    context_object_name = 'member_list'  # your own name for the list as a template
    template_name = 'donor/organisation.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(OrganisationView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        contact = OrgContact.objects.order_by('-created_date')[:1]
        contact_obj = ''
        if contact:
            contact_obj = contact[0]
        context['nbar'] = 'org'
        context['contacts'] = contact_obj
        context['org_activities'] = OrgMemorie.objects.filter()[0:10]
        return context

    # def get_queryset(self):
    #     return Member.objects.filter(title__icontains='war')[:5] 
# def organisation(request):
#     return render(request,'donor/organisation.html')

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
