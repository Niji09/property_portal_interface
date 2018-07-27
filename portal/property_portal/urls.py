from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from .import views
from django.contrib.auth.views import(password_reset, password_reset_done, password_reset_confirm, password_reset_complete)
from django.contrib.auth.decorators import login_required
#namespace
app_name = "property_portal"
urlpatterns = [
    # homepage
    url(r'^$',views.home, name = 'home'),
    # /property_portal/rent/
    url(r'^rent/$', views.RentView.as_view(), name = 'rent'),
    # /property_portal/buy/
    url(r'^buy/$', views.BuyView.as_view(), name = 'buy'),
    #/property_portal/buy_details/id/
    url(r'^buy_details/(?P<pk>[0-9]+)/$', views.BuyDetailView.as_view(), name = 'buy_details'),
    #/property_portal/rent_details/id/
    url(r'^rent_detail/(?P<pk>[0-9]+)/$', views.RentDetailView.as_view(), name = 'rent_detail'),
    # /property_portal/register/
    url(r'^register/$', views.register, name = 'register'),
    # /property_portal/login/
    url(r'^login/$', views.LoginFormView.as_view(), name = 'login'),
    # /property_portal/logout
    url(r'^logout/$', views.logout_view, name = 'logout'),
    #/poroperty_portal/sell_property/
    url(r'^sell_property/$', login_required( views.SellPropertyView.as_view()), name = "sell_property"),
    #/poroperty_portal/rent_property/
    url(r'^rent_property/$', login_required( views.RentPropertyView.as_view()), name = "rent_property"),
    # /property_portal/userprofile/
    url(r'^profile/$', views.profile, name = "profile"),
    # /property_portal/profile/edit/
    url(r'^profile/edit/$', views.edit_profile, name = 'editprofile'),
    # /property_portal/change_password/
    url(r'^change_password/$', views.change_password, name = 'change_password'),

    # /property_portal/reset_password/
    #url(r'^password-reset/', password_reset, name = 'password_reset'),
    # /property_portal/reset_password/done/
    #url(r'^password-reset/done/$', password_reset_done, name = 'password_reset_done'),

]
