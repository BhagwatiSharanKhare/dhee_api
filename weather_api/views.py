from rest_framework.views import APIView
from rest_framework.response import Response
import requests


def OpenWeather(cityname):
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cityname+'&appid=')
    api_data = response.json()
    return api_data['weather'][0]['main']

class WeatherApiView(APIView):
    def post(self,request):
        data = request.data
        city_name = data['city']
        conditions = OpenWeather(city_name)
        return Response({
    success:true,
    result: {
        condition : conditions,
    },
    resetList : [],
    errorMessageKey : Error_Response
})
