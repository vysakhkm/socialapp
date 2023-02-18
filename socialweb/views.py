from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,ListView
from socialweb.forms import RegistrationForm,LoginForm,UserprofileForm,PostForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from api.models import Userprofile,Post
from django.urls import reverse_lazy
from api.models import Post,Comments

# Create your views here.


class SignUpView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("signin")
    # def get(self,request,*args,**kwargs):
    #     form=RegistrationForm()
    #     return render(request,"register.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=RegistrationForm(request.POST)
    #     if form.is_valid():
    #         return redirect("signin")
    #     else:
    #         return render(request,"register.html",{"form":form})
            

class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                 return render(request,"login.html",{"form":form})

class HomeView(View):
    def get(self,request,*args,**kwargs):
        Post.objects.all()
        return render(request,"base.html")

class ProfileCreateView(View):
    def get(self,request,*args,**kwargs):
        form=UserprofileForm()
        return render(request,"userprofile.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=UserprofileForm(request.POST,files=request.FILES)
        if form.is_valid():
            usr=User.objects.get(username=request.user.username)
            form.instance.user=usr
            form.save()
            return redirect("profile_detail")
        else:
            return render(request,"userprofile.html",{"form":form})

class UserprofileView(CreateView,ListView):
    model=Post
    form_class=PostForm
    template_name="profile_detail.html"
    success_url=reverse_lazy("profile_detail")
    context_object_name="posts"

    def form_valid(self, form):
        form.instance.user=self.request.user 
        return super().form_valid(form)

    # def get(self,request,*args,**kwargs):
    #     qs=Userprofile.objects.filter(user=request.user)
    #     return render(request,"profile_detail.html",{"profile":qs})

class AddCommentView(View):
    def post(self,request,*args,**kwargs):
        pid=kwargs.get("id")
        po=Comments.objects.get(id=pid)
        com=request.POST.get("comments")
        Comments.objects.create(post=po,comment=com)
        return redirect("profile_detail")
        