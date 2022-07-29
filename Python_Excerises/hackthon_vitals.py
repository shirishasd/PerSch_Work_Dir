from base64 import decode
import json
import requests
import math
import sys
import re
import random
import os

response= requests.get("https://jsonmock.hackerrank.com/api/medical_records")
pages_response=json.loads(response.text)
no_pages=pages_response["total_pages"]+1

def bodyTemperature(doctorName, diagnosisId):
    # Write your code here
    page = 1
    user_vitals = []
    while page <= no_pages:
        response_data = requests.get(f'https://jsonmock.hackerrank.com/api/medical_records?page={page}')
        page_response = json.loads(response_data.text)
        page = page + 1
        for k in page_response["data"]:
            if k["doctor"]["name"].upper() == doctorName.upper():
                if k["diagnosis"]['id'] == diagnosisId:
                    user_vitals.append(k["vitals"]["bodyTemperature"])
    print(int(min(user_vitals)), int(max(user_vitals)))
    return (int(min(user_vitals)),int(max(user_vitals)))


bodyTemperature('Dr Arnold Bullock',2)



