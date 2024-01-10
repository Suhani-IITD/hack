from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
#from back_func import chatbot_io
from home.models import account,appointment,sleephrs,lastemail
import datetime

# Create your views here.

def appoint(request):
    context = {"success1":True,"name":'yup'}
    return render(request,"appoint.html",context)

def new(request):
    c = {'name':'try'}
    return render(request,"home.html",c)


@csrf_exempt  # Only for demonstration, handle CSRF properly in a production environment
def interface(request):
    context = {'m': "hi",'a':'hello'}
    if request.method == 'POST':
        your_variable = request.POST.get('textinput')
        context['m'] = your_variable
        context['a'] = "training on hold"
        #context['a'] = chatbot_io.working(your_variable)
        # Your Python function logic here to process your_variable
        processed_result = f"Processed: {context['a']}"
        return JsonResponse({'result': processed_result})

    return render(request, "bot_interface.html", context)


def dash(request):
    # if request.method == 'POST':
    #     data = json.loads(request.body)
    #     print('done')
    #     day = data.get('day', '')
    #     sleep_hours = data.get('sleepHours', '')

    #     # Now you can use 'day' and 'sleep_hours' in your Django views logic

    #     # For example, you can send a response back to the client
    #     response_data = {'message': 'Data received successfully'}
    #     return JsonResponse(response_data)

    # # Handle other HTTP methods if needed
    # return JsonResponse({'error': 'Invalid request method'})

    for i in lastemail.objects.all():
        e=i.email
        print(e)
    # hr = request.POST.get('sleep')
    # day = request.POST.get('day')
    # time=datetime.datetime.now()
    # ins =sleephrs(email=e,sleephr=hr,d=time,day=day)
    # ins.save()
    # l=[["Day", "Sleep"],]
    # l={}
    # l2=["Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"]
    # for j in l2:
    #     for i in sleephrs.objects.filter(email=e,day=j):
    #         pass
    #     # l1=[]
    #     l[j] = i
    #     # l1.append(i.day)
    #     # l1.append(i.sleephr)
    #     # l.append(l1)
    # context={"sleep":l}
    if request.method=='POST':
        print('in')
        d = request.POST.get('day')
        s = request.POST.get('sleep')
        # processed_result = f"Processed: {context['a']}"
        # return JsonResponse({'result': processed_result})
    return render(request,"dashboard.html")
    # for i in sleephrs.objects.filter(email=e,day="tuesday"):
    #     l1=[]
    #     l1.append(i.day)
    #     l1.append(i.sleephr)
    #     l.append(l1)
    # for i in sleephrs.objects.filter(email=e,day="wednesday"):
    #     l1=[]
    #     l1.append(i.day)
    #     l1.append(i.sleephr)
    #     l.append(l1)
    # for i in sleephrs.objects.filter(email=e,day="thrusday"):
    #     l1=[]
    #     l1.append(i.day)
    #     l1.append(i.sleephr)
    #     l.append(l1)
    # for i in sleephrs.objects.filter(email=e,day="friday"):
    #     l1=[]
    #     l1.append(i.day)
    #     l1.append(i.sleephr)
    #     l.append(l1)
    # for i in sleephrs.objects.filter(email=e,day="saturday"):
    #     l1=[]
    #     l1.append(i.day)
    #     l1.append(i.sleephr)
    #     l.append(l1)
    # for i in sleephrs.objects.filter(email=e,day="sunday"):
    #     l1=[]
    #     l1.append(i.day)
    #     l1.append(i.sleephr)
    #     l.append(l1)
    
    
    
    #return render(request,"sleep.html",context)
    # return render(request,"dashboard.html")


def login(request):
    context={'success1':False}
    if request.method=="POST":
        #allacc = account.objects.all()
        e=request.POST['Email']
        pas=request.POST['userpassword']
        if (e,) in account.objects.values_list('email') :
            for i in account.objects.filter(email=e):
                if i.password==pas:
                    context={'success1':True,'name':i.name}
                    lastemail.objects.all().delete()
                    ins=lastemail(email=e)
                    ins.save()
                    return redirect('dashboard')
                else:
                   context={'success1':True}
                   return render(request,'LoginPage.html',context) 
        else:
            context={'success1':True}
            return render(request,'LoginPage.html',context)
    return render(request,'LoginPage.html',context)

def create(request):
    context={'success':False}
    #accounts=account.objects.all()
    #print(account.objects.values_list('email'))
    if request.method=="POST":
        n=request.POST['Full Name']
        e=request.POST['Email']
        pas=request.POST['Password']
        ph=request.POST['phoneNumber']
        d = request.POST['DOB']
        g = request.POST['gender']
        if (e,) in account.objects.values_list('email'):
            context={'success':True}
            return render(request,'SignUp.html',context)
        else:
            ins =account(name=n,email=e, password=pas,phone=ph, dob = d, gender = g)
            ins.save()
            lastemail.objects.all().delete()
            ins=lastemail(email=e)
            ins.save()
            return redirect('dashboard')
            # return render(request,'home.html',context)
    return render(request,'SignUp.html',context)