from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from json import dumps
from back_func import chatbot_io
from home.models import account,appointment,sleephrs,lastemail
import datetime

# Create your views here.

def help(request):
    return render(request,"help.html",)


def sleep_default(e):
    l2=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    for i in l2:
        ins =sleephrs(email=e,sleephr=0,day=i)
        ins.save()



def appoint(request):
    context = {"success1":True,"name":'yup'}
    return render(request,"appointments.html",context)

def new(request):
    c = {'name':'try'}
    return render(request,"homepage.html",c)

# def handle_voice_input(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         voice_input = data.get('voiceInput', '')
#         print(voice_input)
#         text_from_backend = "Hello from Django!"
#         print('returning')
#         return JsonResponse({'text': text_from_backend})
        
#         # Process the voice input as needed (e.g., perform some action, save to database)
#         # ...

#         # Return a response, you can customize this based on your requirements
#         #return JsonResponse({'status': 'success', 'message': 'Voice input processed successfully'})
#     return render(request,'voice.html')


@csrf_exempt  # Only for demonstration, handle CSRF properly in a production environment
def interface(request):
    context = {'m': "hi",'a':'hello'}
    if request.method == 'POST':
        your_variable = request.POST.get('textinput')
        context['m'] = your_variable
        #context['a'] = "training on hold"
        context['a'] = chatbot_io.working(your_variable)
        # Your Python function logic here to process your_variable
        processed_result = f"Processed: {context['a']}"
        return JsonResponse({'result': processed_result})

    return render(request, "bot_interface.html", context)


def dash(request):
    # if request.method == 'POST':
    #     your_variable = request.POST.get('sleepHour')
    #     #context['a'] = chatbot_io.working(your_variable)
    #     # Your Python function logic here to process your_variable
    #     print(your_variable)
    #     processed_result = "8"
    #     return JsonResponse({'result': processed_result})
    return render(request,"dashboard.html")
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

    # for i in lastemail.objects.all():
    #     e=i.email
    #     print(e)
    # hr = request.POST.get('sleep')
    # day = request.POST.get('day')
    # time=datetime.datetime.now()
    # ins =sleephrs(email=e,sleephr=hr,d=time,day=day)
    # ins.save()
    # l=[["Day", "Sleep"],]
    # l={}
    # 
    # for j in l2:
    #     for i in sleephrs.objects.filter(email=e,day=j):
    #         pass
    #     # l1=[]
    #     l[j] = i
    #     # l1.append(i.day)
    #     # l1.append(i.sleephr)
    #     # l.append(l1)
    # context={"sleep":l}
    
        # print('in')
        # da = request.POST.get('day')
        # s = request.POST.get('sleep')
        # sleep_record = sleephrs.objects.get(email=e,day=da)
        # sleep_record.sleephr = s
        # sleep_record.save()
        # l1=[["Day","Sleep"]]
        #l2=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        # for i in l2:
        #     data = sleephrs.objects.get(email=e, day = i)
        #     l1.append([i,data.sleephr])
        # context = {"sleep":l1}
        # print(context)
        # return render(request, 'dashboard.html',context)
        # processed_result = f"Processed: {context['a']}"
        # return JsonResponse({'result': processed_result})
    # return render(request,"dashboard.html")
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
            sleep_default(e)
            return redirect('dashboard')
            # return render(request,'home.html',context)
    return render(request,'SignUp.html',context)