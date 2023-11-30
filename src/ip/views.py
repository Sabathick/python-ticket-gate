from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import requests
import json

from src.ip.models import RejectList


@csrf_exempt
def http_header_reader(request):
    if request.method == 'POST' or 'GET':
        client_ip = request.META.get('REMOTE_ADDR')

        user_agent = request.META.get('HTTP_USER_AGENT')

        referer = request.META.get('HTTP_REFERER')

        return JsonResponse(client_ip, user_agent, referer)
    else:
        return JsonResponse({"message": "No permission for this method"})


def address_ip_checker(ip_address):
    api_url = 'http://ip-api.com/json/'

    try:
        response = requests.get(api_url + ip_address)

        if response.status_code == 200:
            data = response.json()
            relevant_data = {
                "Status": data["status"],
                "IP": data["query"],
                "Country": data["country"],
                "Region": data["regionName"],
                "District": data["district"],
                "Mobile": data["mobile"],
                "Proxy": data["proxy"],
                "Hosting": data["hosting"],
                "Timezone": data["timezone"],
                "City": data["city"],
                "Zip Code": data["zip"],
                "Latitude": data["lat"],
                "Longitude": data["lon"],
                "ISP": data["isp"],
            }
            return relevant_data
        else:
            return {"error": "API integration error"}
    except Exception as e:
        return {"error": str(e)}


@csrf_exempt
@require_POST
def save_zip_code(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        ip_address = data.get('ip_address')

        if ip_address:
            ip_data = address_ip_checker(ip_address)
            zip_code = ip_data.get('zip_code')

            if zip_code:
                ip_suspect, created = RejectList.objects.update_or_create(
                    ip_address=ip_address,
                    defaults={'zip_code': zip_code}
                )

                return JsonResponse({'success': True, 'message': 'Zip code saved successfully.'})
            else:
                return JsonResponse({'success': False, 'message': 'Zip code not found in IP data.'}, status=400)
        else:
            return JsonResponse({'success': False, 'message': 'ip_address is required.'}, status=400)

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)