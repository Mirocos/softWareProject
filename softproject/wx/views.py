from django.shortcuts import render
from django.http import HttpResponse
from wx.face.cat_test import get_pred
import os
import base64
from qiniu import Auth, put_file, etag
from . import models
from django.forms.models import model_to_dict
import json
from django.core import serializers
import qiniu.config
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


#将图片上传至七牛云
def uploadToQiuniuCloud(file_obj, name):
    access_key = 'Mgvh_rm8w7nrnhPc2ZYzp0oI8bURQL4Z1h6YcESh'
    secret_key = 'ZwCPtSA80kZuneZvSxXaZ6bIaFGwukrnn-UIsNg5'
    q = Auth(access_key, secret_key)
    bucket_name = 'petwiki'
    key = name #上传后保存的文件名
    token = q.upload_token(bucket_name, key, 3600)
    try:
        with open(name, 'wb') as f:
            f.write(file_obj.read())
    except Exception as e:
        print(e)

    localfile = name  #要上传的文件
    ret, info = put_file(token, key, localfile)
    os.remove(localfile)
    return HttpResponse(info)


def savePetWiki(request):
    if request.method == 'POST':
        PetKind = request.POST.get("PetKind")
        intro = request.POST.get("intro")
        maxOld = request.POST.get("maxOld")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        price = request.POST.get("price")
        Morphological_characteristic = request.POST.get("Morphological_characteristic")
        Personality_characteristics = request.POST.get("Personality_characteristics")
        Breeding_method = request.POST.get("Breeding_method")
        comb = request.POST.get("comb")
        imgName = PetKind + '.jpg'
        file_obj = request.FILES.get("photo")
        info = uploadToQiuniuCloud(file_obj, imgName)

        pw = models.Pet(PetKind=PetKind, intro=intro, maxOld=maxOld, height=height, weight=weight,
                       price=price, Morphological_characteristic=Morphological_characteristic,
                       Personality_characteristics=Personality_characteristics, Breeding_method=Breeding_method,
                       comb=comb, imgName=imgName)
        pw.save()

        return HttpResponse(pw.id) #f返回该宠物种类的id值（独一无二）


def queryPetById(id):
    obj = models.Pet.objects.filter(id=id)
    # obj = json.dumps(obj)
    # print(type(obj))
    # label = ["maxOld", "height", "weight", "price"]
    # TagIDs = []
    # for i in label:
    #     TagIDs.append(obj[i])
    #     obj.pop(i)
    #
    # obj["TagIDs"] = TagIDs
    # return json.dumps(obj)
    obj = serializers.serialize("json", obj)
    data = json.loads(obj)
    print(type(data[0]))
    label = ["maxOld", "height", "weight", "price"]
    TagIDs = []
    for i in label:
        TagIDs.append(data[0]['fields'][i])
        data[0]['fields'].pop(i)
    # for key in data[0]['fields']:
    #     print(data[0]['fields'][key])
    #     data[0]['fields'][key] = data[0]['fields'][key].replace('\\\\', '\\')
    data[0]['fields']['TagIDs'] = TagIDs
    return data





def getPetWiki(request):
    if request.method == "POST":
        # try:
        id = request.POST.get("id")
        print(id)
        return HttpResponse(queryPetById(id))
        # except Exception as e:
        #     return HttpResponse("Record not found")
    else:
        return HttpResponse("Method expected to be POST but found with GET")


