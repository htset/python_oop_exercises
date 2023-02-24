import requests, json

class Location:
    def __init__(self, latitude, longitude, current_weather) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.current_weather = current_weather

    @staticmethod
    def from_json(json_dict):
        if 'temperature' in json_dict:
            return CurrentWeather.from_json(json_dict)
        elif 'latitude' in json_dict:
            return Location(json_dict['latitude'], \
                json_dict['longitude'], \
                json_dict['current_weather'])
        else:
            return json_dict

    def to_json(self):
        return {"latitude" : self.latitude, \
            "longitude" : self.longitude, \
            "current_weather": self.current_weather.to_json() }

class CurrentWeather:
    def __init__(self, temperature, wind_speed) -> None:
        self.temperature = temperature
        self.wind_speed = wind_speed

    @staticmethod
    def from_json(json_dict):
        return CurrentWeather(json_dict['temperature'], \
            json_dict['windspeed'])

    def to_json(self):
        return {"temperature" : self.temperature, \
            "wind_speed" : self.wind_speed }


api_url = "https://api.open-meteo.com/v1/forecast?latitude=51.5128&longitude=-0.0918&current_weather=true"
response = requests.get(api_url)

j = json.loads(response.content, object_hook=Location.from_json)
print(json.dumps(j.to_json()))
