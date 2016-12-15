from django.shortcuts import render

# Create your views here.
#views.py
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from login import forms
from login import models
from models import UploadForm, Upload
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = forms.RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render(request,
    'registration/register.html',{'form': form})
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    #context = dict()
    #context['user'] = request.user
    context = create(request)
    # return render_to_response(
    # 'home.html',
    # context,
    # )

    return render(request, 'home.html', context)

def create(request):
    if request.method=="POST":
        img = UploadForm(request.POST, request.FILES)
        if img.is_valid():
            img.save()
            return HttpResponseRedirect(reverse('imageupload'))
    else:
        img=UploadForm()
    images=Upload.objects.all()
    # return render(request,'templates/home.html', RequestContext({'form':img,'images':images})))
    # return render_to_response('templates/home.html', {'form':img, 'images':images}, context_instance=RequestContext(request))
    context = {'form':img, 'images':images}
    return context
    # return render(request,'templates/home.html',context)

def load_items(request):
    item_list = ['Pink Shirt', 'Red Pants', 'Striped Socks', 'Blue Scarf']

    n = 0
    for item in item_list:
        #create an item object
        new_item = Upload(name=item, created_date='2016-12-08')
        new_item.save()
        n += 1

    return HttpResponse('loaded %d' % n)


def detail(request, upload_id):
    try:
        upload = Upload.objects.get(pk=upload_id)
    except Upload.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'upload/detail.html', {'upload': upload, 'id': upload_id})
