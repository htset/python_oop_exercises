import requests
import jsonpickle

api_url = "https://api.open-meteo.com/v1/forecast?latitude=51.5128&longitude=-0.0918&current_weather=true"
response = requests.get(api_url)

j = jsonpickle.decode(response.content)
print(j)


