from base64 import decode
import json
import pip._vendor.requests


response= pip._vendor.requests.get("https://private-anon-b4db8b107a-carsapi1.apiary-mock.com/manufacturers")

manufacturers=json.loads(response.text)
print(manufacturers)

brand_data={}

for brand in manufacturers:
    brand_data[brand["name"]]=brand["num_models"]
print(brand_data)

def model_qty(num):
  brand_name=[]
  for name in brand_data:
      if brand_data[name]>= num:
       brand_name.append(name)
  return(brand_name)

print(model_qty(5))


def value_count(num):
    return [item.get('name','num_models') for item in manufacturers if item.get('num_models') >= num]
print(value_count(5))



