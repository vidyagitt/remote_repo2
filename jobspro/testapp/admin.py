from django.contrib import admin
from testapp.models import HydJobs,BangaluruJobs,ChennaiJobs

class HydJobsModel(admin.ModelAdmin):
    list_display=["date","title","eligibility","email","phonenumber"]
admin.site.register(HydJobs,HydJobsModel)

class BangaluruJobsModel(admin.ModelAdmin):
    list_display=["date","title","eligibility","email","phonenumber"]
admin.site.register(BangaluruJobs,BangaluruJobsModel)

class ChennaiJobsModel(admin.ModelAdmin):
    list_display=["date","title","eligibility","email","phonenumber"]
admin.site.register(ChennaiJobs,ChennaiJobsModel)