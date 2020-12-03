from django.shortcuts import render,redirect, render_to_response
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from newsapi import NewsApiClient
from .models import Account, Blog
from django.views import generic
import hashlib



# Create your views here.

def signup_view(request):
    form1 = UserCreationForm()
    return render(request,'signup2.html',{'form':form1})

def save_user(request):
    if request.method =='POST':
        #form1 = UserCreationForm(request.POST)
        #if form1.is_valid():
        #user = form1.save()
        email = request.POST["email"]
        password = request.POST["password1"]
        account = Account(email=email,password=password)
        account.save()
        request.session["accountid"] = account.accountid
        request.session["email"]=email
        #login(request,user)
        return redirect("/BlogNewsApp/homepage")
    form1 = UserCreationForm()
    return render(request,'signup2.html',{'form':form1})

def login_view(request):
    if request.method == 'POST':
        #form1 = AuthenticationForm(data=request.POST)
        #if form1.is_valid():
         #   user = form1.get_user()
            email=request.POST["email"]
            password=request.POST["pass"]
            if authenticate(email, password, request):
                #login(request,user)
                return redirect("homepage/")

    form1 = AuthenticationForm()
    return render(request,'index.html',{'form':form1, 'authentication_failed':True})

def authenticate(email, password, request):
    try:
        account = Account.objects.get(email=email, password=password)
    except:
        return False
    if account is None:
        return False

    request.session["accountid"] = account.accountid
    request.session["email"]=email
    return True


def logout_view(request):
    #logout(request)
    del request.session["accountid"]
    del request.session["email"]
    return redirect("/BlogNewsApp/")

def homepage(request):
   # return HttpResponse("homepag)
   # email=request.POST["email"]
    #password=request.POST["pass"]
    #account=Account(email=email,password=password)
    #account.save()
    newsapi = NewsApiClient(api_key='4194374ba17d44c5aa601934cf2f47ed')
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")
    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img, url)

    return render(request,'homepage.html', context={"mylist":mylist})

def index(request):
    return render(request,'index.html')

class Bloglist(generic.ListView):
    def get_queryset(self):
        accountid = self.request.session['accountid']
        return Blog.objects.filter(author=accountid).order_by('posted')
    template_name = 'Myblogs.html'

def create_view(request):
    return render(request, "CreateBlog.html")

def create_blog_view(request):
    if request.method == 'POST':
        author = request.session["accountid"]
        title = request.POST['title']
        body = request.POST['body']
        account = Account.objects.filter(accountid=author)[0]
        blog = Blog(title=title, body=body, author=account)
        blog.save()
    return redirect("/BlogNewsApp/homepage/Myblogs")

def delete_view(request):
    if request.method == 'GET':
        blogid = request.GET['blogid']
        blog = Blog.objects.filter(blogid=blogid)[0]
        blog.delete()
    return redirect("/BlogNewsApp/homepage/Myblogs")
    #return render(request, "delete.html")

#def update_view(request):
