from django.contrib import admin
from .models import Site, Host, Link

# Register your models here.
admin.site.register(Site)
admin.site.register(Host)

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
	list_display = ('video_url', 'site', 'host', 'time_requested')
	list_filter = ('site', 'host', 'time_requested')

