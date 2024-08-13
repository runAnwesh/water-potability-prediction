import json
import requests

url = "https://water-test-mrgh.onrender.com/predict"

x_new = dict(   
  ph = 120.0,
  Hardness = 10.2,
  Solids = 0.4,
  Chloramines = 0.5,
  Sulfate = 0.7,
  Conductivity = 30.12,
  Organic_carbon = 2.7,
  Trihalomethanes = 61.7,
  Turbidity = 4.5

)

x_new_json = json.dumps(x_new)

response = requests.post(url, data = x_new_json)   

print("Response Text: ",response.text)
print("Status code: ",response.status_code)