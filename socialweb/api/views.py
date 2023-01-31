
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView,ListView,DetailView,View
from api.forms import RegistrationForm,LoginForm,PostForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin

from api.models import Posts, MyUser,Comments

# Create your views here.



class SignupView(CreateView):
    model=MyUser
    form_class= RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("register")

class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"
    def post (self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr= authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render(request,self.template_name,{"form":form})







class IndexView(FormView,ListView):
    template_name="home.html"
    model=Posts
    context_object_name="posts"
    success_url=reverse_lazy("index")
    form_class=CommentForm
    pk_url_kwarg: str="id"

    # def form_valid(self, form):
    #     form.instance.user=self.request.user
    #     return super().form_valid(form)
    

    def get_queryset(self):
        return Posts.objects.all().exclude(user=self.request.user)


def add_comment(request,*args,**kwargs):
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.cleaned_data.get("comment")
            pid=kwargs.get("id")
            pos=Posts.objects.get(id=pid)
            Comments.objects.create(user=request.user,post=pos,comment=comment)
            return redirect("index")
        else:
            return redirect("index")

def remove_comment(request,*args,**kwargs):
    ans_id=kwargs.get("id")
    Comments.objects.get(id=ans_id).delete()
    return redirect("index")

class PostAddView(CreateView):
    model=Posts
    template_name="addpost.html"
    success_url=reverse_lazy("index")
    form_class=PostForm

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        return Posts.objects.all().filter(user=self.request.user)





class MypostView(ListView,FormView):
    model=Posts
    form_class=PostForm
    template_name="profile.html"
    pk_url_kwargs="id"
    context_object_name="myposts"

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Posts.objects.all().filter(user=self.request.user)


def remove_post(request,*args,**kwargs):
    p_id=kwargs.get("id")
    Posts.objects.get(id=p_id).delete()
    return redirect("profile")



def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("login")



# def like_view(request,*args,**kwargs):
#     l_id=kwargs.get("id")
#     like=Posts.objects.get(id=l_id)
#     like.likes.add(request.user)
#     like.save()
#     return redirect("index")


# class AddLike(LoginRequiredMixin,View):
#     def post(request,*args,**kwargs):
#         l_id=kwargs.get("id")
#         post=Posts.objects.get(id=l_id)
#         is_like=False

#         for like in post.like.all():
#             if like == request.user:
#                 is_like=True
#                 break
#             if not is_like:
#                 post.like.add(request.user)

#             if is_like:
#                 post.like.remove(request.user)