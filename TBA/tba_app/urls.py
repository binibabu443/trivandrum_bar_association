from django.views.generic import TemplateView
from django.urls import path
from tba_app import views

urlpatterns=[
    path('registration/',TemplateView.as_view(template_name='registration.html'),name='registration'),
    path('login/',TemplateView.as_view(template_name='login.html'),name='login'),
    path('member/',TemplateView.as_view(template_name='member.html'),name='member'),
    path('memberhome/',TemplateView.as_view(template_name='memberhome.html'),name='memberhome'),
    path('viewregistration/',views.view_pending_reg,name='viewregistration'),
    path('profileview/',views.viewprofile,name='profileview'),
    path('editprofile/',views.editprofileview,name='editprofile'),
    path('contacts/',views.viewmsg,name='contacts'),
    path('adminhome',views.authenticate,name='auth'),
    path('registration',views.register,name='reg'),
    path('read',views.readmsg,name='readmessage'),
    path('adminhome/',views.viewreg,name='adminhome'),
    path('',views.view_approved_reg,name='index'),
    path('approval',views.approval,name='apprv'),
    path('message',views.submitmsg,name='submsg'),
    path('edit',views.editprofile,name='edit'),
]