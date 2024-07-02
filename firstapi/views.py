from django.http import JsonResponse
from django.views.decorators.http import require_GET
import requests

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_geolocation(ip):
    api_key = '7591ec4f-66ec-43b6-966b-0ff9fb935edd'# Replace with your IPXplorer API key
    url = f'https://ipxplorer.com/api/ip?ip={ip}&key={api_key}'
    response = requests.get(url)
    geolocation_data = response.json()
    print(geolocation_data)
    location = geolocation_data.get('location', {})
    latitude = location.get('latitude')
    longitude = location.get('longitude')
    return latitude, longitude

def visit(request):
    visitor_name = request.GET.get('visitor_name', '')
    client_ip = get_client_ip(request)
    #client_ip = '102.89.33.147'
    
    # Fetch location and weather using a free API (like OpenWeatherMap)
    weather_api_key = 'b8f58ffa031a3ba694ea099e9ea25576'
    latitude, longitude = get_geolocation(client_ip)
    if latitude is not None and longitude is not None:
        
        print(longitude, latitude)
        weather_url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={weather_api_key}&units=metric'
        response = requests.get(weather_url)
        weather_data = response.json()
        print(weather_data)
        if weather_data['cod'] == '400':
            return JsonResponse({'error': weather_data['message']})
            
        temperature = weather_data['main']['temp']
        city = weather_data['name']
        
        greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
        
        # Respond with JSON
        data = {
            'client_ip': client_ip,
            'location': city,
            'greeting': greeting
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'Unable to retrieve geolocation data.'}, status=400)


