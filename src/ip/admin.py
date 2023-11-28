from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from .models import AllowList


def add_allowlist_ip(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')

        if ip_address:
            AllowList.objects.get_or_create(ip_address=ip_address)
            return JsonResponse({'success': True, 'message': 'IP added to AllowList successfully.'})

    return JsonResponse({'success': False, 'message': 'Invalid request.'}, status=400)


@admin.register(AllowList)
class AllowListAdmin(admin.ModelAdmin):
    change_list_template = 'admin/ip_allowlist_change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('add-allowlist-ip/', self.admin_site.admin_view(add_allowlist_ip)),
        ]
        return custom_urls + urls

