from django.shortcuts import render
from django.http import HttpResponse
from wx.face.cat_test import get_pred
import os
import base64
from  softproject import settings
# Create your views here.
import cv2



def index(request):
    #return HttpResponse("Hello,world.")
    list = get_pred()
    return HttpResponse(list)

def register(request):
    print(request.POST)#测试接收post传过来的数据
    print(request.FILES)#测试接收上传文件
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        file_obj = request.FILES.get('photo')
        # file_name = settings.MEDIA_ROOT.replace('\\','/') + ' / ' + file_obj.name
        #os.path.join('./face/uploadImage/')
        file_name = file_obj.name
        print(file_name)
        path = os.path.abspath('.').replace('\\', '/') + '/wx/face/uploadImage/'
        print(path)
        try:
            with open(path + file_name, 'wb+') as f:
                f.write(file_obj.read())
        except Exception as e:
            print(e)
        return HttpResponse('OK')

def changoToBase64(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        file_obj = request.FILES.get('photo')
        # file_name = file_obj.name
        # print(file_name)
        #path = os.path.abspath('.').replace('\\', '/') + '/wx/face/uploadImage/'
        #print(path)
        # try:
        #     with open(path + file_name, 'wb+') as f:
        #         f.write(file_obj.read())
        # except Exception as e:
        #     print(e)
        base64_data = base64.b64encode(file_obj.read())
        imgb64 = base64.b64decode(base64_data)
        try:
            with open('temp.jpg', 'wb') as f:
                f.write(imgb64)
        except Exception as e:
            print(e)
    return HttpResponse(imgb64, content_type="image/jpg")
