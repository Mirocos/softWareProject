from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datetime_safe import time


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # username = request.POST['username']
        # password = request.POST['pwd']
        # phone = request.POST['phone']
        # e_mail = request.POST['e_mail']
        file_obj = request.FILES.get('photo')
        # print(username,password,phone,e_mail)
        file_name = './static/img/'+str(int(time.time()))+'.'+file_obj.name.split('.')[-1]#构造文件名以及文件路径
        if file_obj.name.split('.')[-1] not in ['jpeg','jpg','png']:
            return HttpResponse('输入文件有误')
        try:
            # user = UserInfo()
            # user.username = username
            # user.phone = phone
            # user.password = password
            # user.e_mail = e_mail
            # Image = file_name[1:]
            # user.save()
            with open(file_name,'wb+') as f:
                f.write(file_obj.read())
        except Exception as e:
            print(e)
        return HttpResponse('OK')
