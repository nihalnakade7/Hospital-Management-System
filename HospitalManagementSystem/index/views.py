from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Invoice,Prescription,Appointments
from accounts.models import MyUsers
# Create your views here.


def index(request):
    if('user_id' in request.session):
        role = request.session.get('role')
        context = {'role':role}
        return render(request,'index/index.html',context)
    else:
        return render(request,'index/index.html')

def about(request):
    if('user_id' in request.session):
        role = request.session.get('role')
        context = {'role':role}
        return render(request,'index/about.html',context)
    else:
        return render(request,'index/about.html')

def contact(request):
    if('user_id' in request.session):
        role = request.session.get('role')
        context = {'role':role}
        return render(request,'index/contact.html',context)
    else:
        return render(request,'index/contact.html')



def appointments(request):
    if('user_id' in request.session):
        user_id = request.session.get('user_id')
        print(user_id)
        role = request.session.get('role')
        if (role == 'Doctor'):
            apt = Appointments.objects.filter(doctor_id = user_id)
            user = User.objects.get(id = apt[0].patients_id)
            
        else:
            apt = Appointments.objects.filter(patients_id = user_id)
            user = User.objects.get(id = apt[0].doctor_id)
       
        context = {'role':role,'apt':apt,'user':user}
        return render(request,'index/appointments.html',context)
    else:
        return render(request,'index/appointments.html')

def invoice(request):
    if('user_id' in request.session):
        user_id = request.session.get('user_id')
        print(user_id)
        role = request.session.get('role')
        invoice = Invoice.objects.filter(patient_id = user_id)

        context = {'role':role,'invoice':invoice}
        return render(request,'index/invoice.html',context)
    else:
        return render(request,'index/invoice.html')

def profile(request):
    if('user_id' in request.session):
        user_id = request.session.get('user_id')
        print(user_id)
        role = request.session.get('role')
        user = User.objects.get(id = user_id)

        context = {'role':role,'user':user}
        return render(request,'index/profile.html',context)
    else:
        return render(request,'index/profile.html')

def med_history(request):
    if('user_id' in request.session):
        user_id = request.session.get('user_id')
        print(user_id)
        role = request.session.get('role')
        if(role == "Doctor"):
            history = Prescription.objects.filter(doctor = user_id)
        else:
            history = Prescription.objects.filter(patient_id = user_id)
        
        user = User.objects.get(id = history[0].patient_id)
        context = {'role':role,'history':history,'user':user}
        return render(request,'index/med_history.html',context)
    else:
        return render(request,'index/med_history.html')


def res_dashboard(request):
    
    if('user_id' in request.session):
        user_id = request.session.get('user_id')
        print(user_id)
        role = request.session.get('role')
        history = Appointments.objects.all()
        ta = len(history)
        patients = MyUsers.objects.filter(role = 'Patient')
        completed = Appointments.objects.filter(status = 'completed')
        pending = Appointments.objects.filter(status = 'pending')
        ca = len(completed)
        pa = len(pending)
        context = {'role':role,'history':history,'patients':patients,'ta':ta,'ca':ca,'pa':pa}
        return render(request,'index/res_dashboard.html',context)
    else:
        return render(request,'index/res_dashboard.html')

def create_app(request):
    if (request.method == 'POST'):
        date = request.POST['date']
        time = request.POST['time']
        status = request.POST['status']
        doc_id = request.POST['doc_id']
        pat_id = request.POST['pat_id']

        print('values',date,time,status,doc_id,pat_id)

        appointment = Appointments()
        appointment.time = time
        appointment.date = date
        appointment.status = status
        appointment.doctor_id = doc_id
        appointment.patients_id = pat_id
        appointment.save()
        return redirect('res_dashboard')
    else:
        user = User.objects.all()
        context = {'user':user}
        return render(request,'index/create_app.html',context)

def update_user(request):
    if (request.method == 'POST'):
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        uid = request.POST['uid']
        user = User.objects.get(id = uid)
        user.first_name = fname
        user.last_name = lname
        user.email = email
        user.username = uname
        user.save()
        return redirect('res_dashboard')
    else:
        uid = request.GET['uid']
        user = User.objects.get(id = uid)
        context = {'user':user}
        return render(request,'index/update_user.html',context)


def del_user(request):
    uid = request.GET['uid']
    user = User.objects.get(id = uid)
    user.delete()
    return redirect('res_dashboard')

def del_confirm(request):
    id = request.GET['uid']
    context = {'id':id}
    return render(request,'index/del_confirm.html',context)


def hr_dashboard(request):
    if('user_id' in request.session):
        user_id = request.session.get('user_id')
        print(user_id)
        role = request.session.get('role')
        doctors = MyUsers.objects.filter(role = 'Doctor')
        patients = MyUsers.objects.filter(role = 'Patient')
        onduty = MyUsers.objects.filter(status = 'Active')
        dc = len(doctors)
        pc = len(patients)
        oc = len(onduty)
        context = {'role':role,'doctors':doctors,'dc':dc,'pc':pc,'oc':oc}
        return render(request,'index/hr_dashboard.html',context)
    else:
        return render(request,'index/hr_dashboard.html')

