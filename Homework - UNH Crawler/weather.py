import urllib.request
import json
from pprint import pprint

page = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=west%20haven,%20ct")
content=page.read()
content_string = content.decode("utf-8")

json_data = json.loads(content_string)

print("The current weather in West Haven is",json_data["weather"][0]["main"])

