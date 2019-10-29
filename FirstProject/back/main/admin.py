from django.contrib import admin

from main.models import Reviewer, Review, Company


@admin.register(Reviewer)
class ReviewerAdmin(admin.ModelAdmin):
    list_display = ['id',  'first_name', 'last_name', 'email']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'address', 'about_info', 'email']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'rating', 'summary', 'ip_address', 'date']