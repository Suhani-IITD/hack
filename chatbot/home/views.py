from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
#from back_func import chatbot_io
from home.models import account

# Create your views here.

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
                    return redirect('interface')
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
            return redirect('interface')
            # return render(request,'home.html',context)
    return render(request,'SignUp.html',context)