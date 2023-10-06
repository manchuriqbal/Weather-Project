from django.shortcuts import render
import requests
import datetime

def home(request):

    try:
        if request.method == 'POST':
            city = request.POST['city']
        else:
            city = 'dhaka'
    except Exception as e:
        print(e)


    appid = 'bad55fd05f6fdec19b7084dc8f426beb'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS ={ 'q': city, 'appid': appid, 'units': 'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today()

    return render(request, 'weatherapp/index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city})