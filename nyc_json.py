import xmltojson
import json
import requests
  
  
#fetch the html page
url = "https://data.cityofnewyork.us/resource/8wbx-tsch.json"
  
#Headers to mimic the browser
headers = {}
  
#Get the page through get() method
html_response = requests.get(url=url, headers = headers)
  
#Save the page content as fhv_nyc.html
with open("fhv_nyc.html", "w") as html_file:
    html_file.write(html_response.text)
      
with open("fvh_nyc.html", "r") as html_file:
    html = html_file.read()
    json_ = xmltojson.parse(html)
      
with open("data.json", "w") as file:
    json.dump(json_, file)
      
print(json_)