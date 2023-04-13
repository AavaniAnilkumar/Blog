from django.shortcuts import render,redirect
from . models import logindb,post,Comment
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


from .forms import EditForm

from django.views.generic import DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    data = post.objects.all()
    print(data)
    
    return render(request,"index.html",{'data':data})

def loginpg(request):
    return render(request,"login.html")

def adminlog(request):
    if request.method == "POST":
        username_r = request.POST.get('user')
        password_r = request.POST.get('pass')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)

            if user is not None:
                login(request, user)
                request.session['user'] = username_r
                request.session['pass'] = password_r
                return redirect(index)

            else:
                return redirect(loginpg)

        else:
            return redirect(loginpg)

def addpost(request):
    return render(request,"add_post.html")



def addpostsave(request):
    if request.method == "POST":
        t = request.POST.get('title')
        desc = request.POST.get('description')
        i = request.FILES['image']
        d = request.POST.get('date')
        obj = post(title =t, description=desc, image=i,date=d)
        obj.save()
        return redirect(index)
    

class PostDetailView(DetailView):
    model = post
    
    template_name = "post_detail.html"
   
    

# class PostUpdateView(UpdateView):
#     model = post
#     form_class = EditForm
#     template_name = 'post_update.html'

# class PostDeleteView(DeleteView):
#     model = post
#     template_name = 'post_delete.html'
#     success_url = reverse_lazy('index')
def adminlogout(request):
    del request.session['user']
    del request.session['pass']
    return redirect(loginpg)