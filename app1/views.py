from django.shortcuts import render
from django.http import HttpResponse
#suppose we want to return an HttpResponse..so we need to import it first
from .models import Feature

# Create your views here.
def index(request):
    
    '''
    feature1=Feature()
    feature1.id=0
    feature1.name='you'
    feature1.details='series'
    
    feature2=Feature()
    feature2.id=1
    feature2.name='you'
    feature2.details='series'
    
    feature3=Feature()
    feature3.id=2
    feature3.name='you'
    feature3.details='series'
    features=[feature1,feature2,feature3]
    '''
    # return HttpResponse('<h1>Hey there!</h1>')
    #the HttpResponse above is gonna be like an html tag only.
    features=Feature.objects.all()
    return render(request,'index.html',)
    #the function index which has a request,returns,i.e,renders index.html
    
def register(request):
    if request.method==POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        
        if password==password1:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already used')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                #creating a new username with the credentials
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Passwords do not match.')
            return redirect('register')
    else:
        return render(request,'register.html')
    
        
def counter(request):
    words=request.POST['words']
    #'words' is the name of the textarea
    #sending a request to whatever is being passed to the particular view and then we want 
    #to get it
    data={'words':words,'l':count(words)}
    return render(request,'counter.html',data)

def count(words): 
    return len(words.split())
#Django views are Python functions that takes http requests and returns http response, like HTML documents.
# This is a simple example on how to send a response back to the browser.
