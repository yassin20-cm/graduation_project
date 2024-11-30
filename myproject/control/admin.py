from django.contrib import admin
from .models import User
from .models import Request

# Register your models here.
admin.site.site_header='ينتفع به'
admin.site.site_title='ينتفع به'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'academic_year', 'email', 'join_date')
    search_fields = ('user_name', 'email', 'academic_year')
    list_filter = ('academic_year', 'join_date')
    readonly_fields = ('join_date',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('user_name', 'email', 'profile_image', 'academic_year')
        }),
        ('Other Details', {
            'fields': ('join_date',)
            }),

    )



@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'user', 'request_state', 'request_date', 'related_file')
    search_fields = ('request_description', 'user__user_name', 'request_state')
    list_filter = ('request_state', 'request_date') 
    readonly_fields = ('request_date',)
    fieldsets = (
        ('Request Information', {
            'fields': ('user', 'request_state', 'request_description', 'related_file')
        }),
        ('Date Information', {
            'fields': ('request_date',)
        }),
    )
    list_per_page = 20




