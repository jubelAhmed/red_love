from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.http import JsonResponse

from .models import BloodInformation, Message, OrgContact


# Create your views here.

def blood_news(request):
    information = BloodInformation.objects.filter(status=True)
    contact = OrgContact.objects.order_by('-created_date')[:1]
    global contact_obj
    if contact:
        contact_obj = contact[0]
    # print(contact_obj)
    context = {
        'information': information,
        'nbar': 'news',
        # 'contacts':contact_obj,

    }
    return render(request, 'information/news.html', context)


def message(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    print(name, phone, message)
    if name and phone and message:
        try:
            msg = Message(
                name=name, phone=phone, message=message
            )
            msg.save()
            message = 'জিজ্ঞাসা করার জন্যে আপনাকে ধন্যবাদ !'
            messages.success(request, message)
            print('success')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            message = 'Message sending fail!!'
            messages.warning(request, message)
            print('fail')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        message = 'Please provide all value field'
        messages.warning(request, message)
        print('null fail')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#     registered = False

#     if request.method == 'POST':
#         user_form = UserProfileForm(data=request.POST)

#         if user_form.is_valid() :

#             user = user_form.save(commit = True)
#             registered = True
#             return redirect('login')

#     else:
#         user_form = UserProfileForm()
#     dic = {'title':'registration','registered':registered,'form':user_form,
#             }
#     return render(request,'userApp/signup.html',dic)
