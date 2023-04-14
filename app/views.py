from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


# Create your views here.
def hello(request):

    if request.method == 'GET':
        # รับค่าตำแหน่งปัจจุบันของผู้ใช้
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
        location = "13.7293834,100.7754963"
        radius = "1500"
        types = "restaurant"
        keyword = "food"
        api_key = "AIzaSyD0jw7NhIQb_NZj86Ku4JtLhbtqJqEwLgs"

        # สร้าง URL พร้อมใส่ API key และ parameter อื่น ๆ
        request_url = f"{url}location={location}&radius={radius}&types={types}&keyword={keyword}&key={api_key}"

        # เรียกใช้งาน API ด้วย HTTP GET request
        response = requests.get(request_url)

        # แสดงผลลัพธ์
        print(response.json())
        return HttpResponse('hi')
    
@csrf_exempt
def webhook(request):
    if request.method == "POST":
        # อ่านข้อมูลจาก request body
        data = json.loads(request.body)
        # ทำการเพิ่มข้อมูลลงใน Database
        #webhook = Webhook.objects.create(payload=data)
        # ส่งข้อมูลกลับไปยัง Dialogflow โดยใช้ JSON
        response_data = {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "Webhook received!"
                        ]
                    }
                }
            ]
        }
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({}, safe=False)