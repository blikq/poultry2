from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import render, HttpResponse
# from .forms import NewsForm
from .models import NewsModel, BlogModel
from .serializers import NewsSerializer, BlogSerializer, NewsNoImageSerializer
import random

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect

# Create your views here.
def index_render(request):
    return render(request, "master/index.html")

def about_render(request):
    return render(request, "master/about.html")
    
def news_render(request):
    news = NewsModel.objects.all()
    data = []
    for new in news:
        new.timestamp = f"{new.timestamp.replace(microsecond=0).date()} {new.timestamp.replace(microsecond=0).time()}"
        # new.timestamp = new.timestamp.today().replace(microsecond=0).strftime('%Y-%m-%d ')
        new.article = f"<p style='text-overflow:ellipsis;'>{new.article}</p>"
        data.append(new)
    real = {
        "newss": data
    }
    return render(request, "master/blog.html", real)

def news_sin_render(request, id):
    news = NewsModel.objects.get(id=id)
    if not news:
        return HttpResponse("Not Found")
    news.timestamp = f"{news.timestamp.replace(microsecond=0).date()} {news.timestamp.replace(microsecond=0).time()}"

    return render(request, "master/blog-single.html", {"news":news})

def blogs_render(request):
    blogs = BlogModel.objects.all()
    data = []
    for blog in blogs:
        blog.timestamp = f"{blog.timestamp.replace(microsecond=0).date()} {blog.timestamp.replace(microsecond=0).time()}"
        # new.timestamp = new.timestamp.today().replace(microsecond=0).strftime('%Y-%m-%d ')
        blog.description = f"<p style='text-overflow:ellipsis;'>{blog.description}</p>"
        data.append(blog)
    real = {
        "blogs": data
    }
    return render(request, "master/vid-blog.html", real)



def blogs_sin_render(request, id):
    blog = BlogModel.objects.get(id=id)
    if not blog:
        return HttpResponse("Not Found")
    blog.timestamp = f"{blog.timestamp.replace(microsecond=0).date()} {blog.timestamp.replace(microsecond=0).time()}"

    return render(request, "master/vid-blog-single.html", {"blog": blog})

def contact_render(request):
    return render(request, "master/contact.html")


@login_required(login_url="/master/login")
@api_view(["POST", "GET"])
def dashboard_render(request):
    data = {
        "newss": NewsModel.objects.all().reverse(),
        "blogs": BlogModel.objects.all().reverse()
    }
    if request.method == "POST":
        if request.POST.get("news-submit") == "Save Article":
            serializer = NewsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

        if request.POST.get("blog-submit") == "Save Video":
            serializer = BlogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
    return render(request, "master/dashboard.html", data)

    

@login_required(login_url="/master/login")
def edit_news_render(request, id):
    news = NewsModel.objects.get(id=id)
    if not news:
        return HttpResponse("Not Found")

    if request.method == "POST":
        if request.POST.get("news-submit") == "Edit Article":
            if len(request.FILES.getlist('images')) == 0: 
                news.author = request.POST.get("author")
                news.title = request.POST.get("title")
                news.article = request.POST.get("article")
            elif len(request.FILES.getlist('images')) > 0:
                news.author = request.POST.get("author")
                news.title = request.POST.get("title")
                news.article = request.POST.get("article")
                news.images = request.FILES.getlist('images')[0]
            news.save()    

    return render(request, "master/edit-news.html", {"news": news})


@login_required(login_url="/master/login")
def edit_blog_render(request, id):
    blog = BlogModel.objects.get(id=id)
    if not blog:
        return HttpResponse("Not Found")

    if request.method == "POST":
        if request.POST.get("blog-submit") == "Edit Vlog":
        
            if len(request.FILES.getlist('video')) == 0:
                blog.title = request.POST.get("title")
                blog.description = request.POST.get("description")
            elif len(request.FILES.getlist('video')) > 0:
                blog.title = request.POST.get("title")
                blog.description = request.POST.get("description")
                blog.video = request.FILES.getlist('video')[0]
            else:
                print("if not reached")
            blog.save()

    return render(request, "master/edit-blog.html", {"blog": blog})

@api_view(["POST"])
def delete_api(request):

    id_ = request.headers.get("ido")
    if id_:
        if request.headers["model"] == "news":
            news = NewsModel.objects.get(id=id_)
            if news:
                news.delete()
                return HttpResponse(200)
            if not news:
                return HttpResponse(404)

        if request.headers["model"] == "blog":
            blog = BlogModel.objects.get(id=id_)
            if blog:
                blog.delete()
                return HttpResponse(200)
            if not blog:
                return HttpResponse(404)
    else:
        return HttpResponse(401)

    
    # NewsModel.objects.delete(id=)

    return HttpResponse(200)

def login_render(request):
    # request.user.
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect("/master/dashboard")
        else:
            return HttpResponse("unsuccessful login")

    return render(request, "master/sign-in.html")

def logout_(request):
    logout(request)
    return redirect("/master/dashboard")
