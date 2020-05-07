from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

posts = [
    {'author': 'Lyncorn',
     'title': 'Blog post 1',
     'content': 'First post content',
     'date_posted': 'May 7 2020'
     },
     {'author': 'Test',
      'title': 'Blog post 2',
      }
]

def business(request):
    return render(request, 'blog/business.html')