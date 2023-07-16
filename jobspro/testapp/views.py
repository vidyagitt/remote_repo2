from django.shortcuts import render
from testapp.models import HydJobs,BangaluruJobs,ChennaiJobs

def home_view(x):
    return render(x,"testapp/home.html")
def hyd_view(x):
    hyd=HydJobs.objects.all()
    return render(x,"testapp/hyd.html",{"hyd":hyd})
def bangalore_view(x):
    ban=BangaluruJobs.objects.all()
    return render(x,"testapp/bang.html",{"ban":ban})
def chennai_view(x):
    che=ChennaiJobs.objects.all()
    return render(x,"testapp/chen.html",{"che":che})

