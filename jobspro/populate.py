import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","jobspro.settings")
import django
django.setup()

import random
from faker import Faker
from testapp.models import HydJobs,BangaluruJobs,ChennaiJobs
f=Faker()
def phone():
    r=random.randint(6,9)
    num=str(r)
    for i in range(9):
        num=num+str(random.randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        edate=f.date()
        etitle=f.random_element(elements=("Mtech","Inter","B.tech","Degree"))
        eeligibility=f.random_element(elements=("software Engg","HR","Manager","Teamlead"))
        eaddress=f.address()
        eemail=f.email()
        ephone=phone()
        hyd_jobs_rec=HydJobs.objects.get_or_create(
            date=edate,
            title=etitle,
            eligibility=eeligibility,
            adderess=eaddress,
            email=eemail,
            phonenumber=ephone
        )
# n=int(input("enter no. of records: "))
# populate(n)
# print(n,"no. of records inserted successfully for Hyd")

def populate(n):
    for i in range(n):
        edate=f.date()
        etitle=f.random_element(elements=("Mtech","Inter","B.tech","Degree"))
        eeligibility=f.random_element(elements=("software Engg","HR","Manager","Teamlead"))
        eaddress=f.address()
        eemail=f.email()
        ephone=phone()
        hyd_jobs_rec=BangaluruJobs.objects.get_or_create(
            date=edate,
            title=etitle,
            eligibility=eeligibility,
            adderess=eaddress,
            email=eemail,
            phonenumber=ephone
        )
n=int(input("enter no. of records: "))
populate(n)
print(n,"no. of records inserted successfully for Bangalore")

def populate(n):
    for i in range(n):
        edate=f.date()
        etitle=f.random_element(elements=("Mtech","Inter","B.tech","Degree"))
        eeligibility=f.random_element(elements=("software Engg","HR","Manager","Teamlead"))
        eaddress=f.address()
        eemail=f.email()
        ephone=phone()
        hyd_jobs_rec=ChennaiJobs.objects.get_or_create(
            date=edate,
            title=etitle,
            eligibility=eeligibility,
            adderess=eaddress,
            email=eemail,
            phonenumber=ephone
        )
# n=int(input("enter no. of records: "))
# populate(n)
# print(n,"no. of records inserted successfully for Chennai")


  