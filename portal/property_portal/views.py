from django.views import generic
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, FormView
from property_portal.models import Rent, Buy,UserProfile
from property_portal.forms import(
 LoginForm, RentPropertyForm, SellPropertyForm,
 RegistrationForm, EditProfileForm
 )
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django import forms


#homepage view
def home(request):
    return render(request, 'property_portal/homepage.html')

# Rent view
class RentView(generic.ListView):
    template_name = 'property_portal/rent.html'
    context_object_name = "rent_object"
    def get_queryset(self):
        return Rent.objects.all()
# Buy view
class BuyView(generic.ListView):
    template_name = 'property_portal/buy.html'
    context_object_name = "buy_object"
    def get_queryset(self):
        return Buy.objects.all()

# Buy Details
class BuyDetailView(generic.DetailView):
    model = Buy
    template_name = 'property_portal/buy_details.html'
    context_object_name = 'b_item'

# Rent Details
class RentDetailView(generic.DetailView):
    model = Rent
    template_name = 'property_portal/rent_details.html'
    context_object_name = 'ritem'

# User register view
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_portal:login')
    else:
        form =RegistrationForm()
        args = {'form': form}
        return render(request, 'property_portal/register.html', args)


# Login form view
class LoginFormView(View):
    form_class = LoginForm
    template_name = 'property_portal/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(username = username, password = password)
        args = {
        'form':form
        }
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('property_portal:home')
        else:
            return render(request, 'property_portal/login.html', args)
        #return render(request, 'property_portal/login.html')

# Logout the user
@login_required
def logout_view(request):
    logout(request)
    form = RegistrationForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect('property_portal:home')

# Rent Property views
class RentPropertyView(View):
    form_class = RentPropertyForm
    template_name = 'property_portal/rent_property.html'
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            return redirect('property_portal:rent')
        return render(request, self.template_name, {'form': form})


# Rent Property views
class SellPropertyView(View):
    form_class = SellPropertyForm
    template_name = 'property_portal/sell_property.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            return redirect('property_portal:buy')
        return render(request, self.template_name, {'form': form})

# Profile View
@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'property_portal/profile.html', args)


# edit profile view
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(data = request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('property_portal:profile')
    else:
        form=EditProfileForm(instance = request.user)
        args = {'form':form}
        return render(request, 'property_portal/editprofile.html', args)


# change password view
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('property_portal:profile')
        else:
            return redirect('property_portal:change_password')
    else:
        form=PasswordChangeForm(user = request.user)
        args = {
        'form':form,
        }
        return render(request, 'property_portal/change_password.html', args)
