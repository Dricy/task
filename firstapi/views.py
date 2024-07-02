from django.http import JsonResponse
from django.views.decorators.http import require_GET
import requests

@require_GET
def hello_view(request):
    visitor_name = request.GET.get('visitor_name', '')
    client_ip = request.META.get('REMOTE_ADDR', '')
    location = "New York"  # You can use an IP geolocation service to get the actual location based on client_ip
    temperature = 11  # Replace with actual temperature query logic
    
    response_data = {
        'client_ip': client_ip,
        'location': location,
        'greeting': f'Hello, {visitor_name}! The temperature is {temperature} degrees Celsius in {location}'
    }
    
    return JsonResponse(response_data)


def intro_view(request):
    visitor_name = request.GET.get('visitor_name', '')
    client_ip = request.META.get('REMOTE_ADDR', '')
    location = get_location(client_ip)
    temperature = get_temperature(location)
    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"
    response_data = {
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    }
    return JsonResponse(response_data)

def get_location(ip):
    # You can use a free IP Geolocation API like ipstack.com or ipinfo.io
    # Example using ipinfo.io:
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()
    return data.get('city', 'Unknown')

def get_temperature(location):
    # You would typically use a weather API to get the temperature for a location
    # For simplicity, let's assume a static temperature
    return 11  # Assuming 11 degrees Celsius

def hello(request):
    visitor_name = request.GET.get('visitor_name', '')
    client_ip = request.META.get('REMOTE_ADDR', '')
    
    # Fetch location and weather using a free API (like OpenWeatherMap)
    weather_api_key = 'your_weather_api_key_here'
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q=New York&appid={weather_api_key}&units=metric'
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



