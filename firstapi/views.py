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

def visit(request):
    visitor_name = request.GET.get('visitor_name', '')
    client_ip = get_client_ip(request)
    
    # Fetch location and weather using a free API (like OpenWeatherMap)
    weather_api_key = 'b8f58ffa031a3ba694ea099e9ea25576'
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q=Lagos,nigeria&appid={weather_api_key}&units=metric'
    response = requests.get(weather_url)
    weather_data = response.json()
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



