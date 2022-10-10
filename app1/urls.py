from django.urls import path
#allows us to configure each url
#allows us to have multiple urls in our list named urlpatterns
from . import views #importing views to use them

#Calling the view via an url

urlpatterns=[
    path('',views.index,name='index'),
    path('counter',views.counter,name='counter'),
    path('register',views.register,name='register')
]

'''
the '' is the root url....when the user comes to this url,it sees that it needs to go to views 
and look for a function called index.And then whatever is done in the index is going to be rendered
back to the user.
the name...is some kind of id.
'''
#now, we have configured the url files, but what happens when the user comes to one?
#=>That is going to be done in views.index......we may render an html file,or,set a restful http response or a JSON response
#index is a function created in views.py 