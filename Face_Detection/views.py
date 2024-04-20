from django.shortcuts import render,redirect
from Face_Detection.detection import FaceRecognition
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

faceRecognition = FaceRecognition()

def home(request):
    return render(request,'faceDetection/home.html')

def about(request):
    return render(request,'faceDetection/about.html')

def team(request):
    return render(request,'faceDetection/team.html')

@login_required(login_url = 'login')
def searchAttendence(request):
    attendences = Attendence.objects.all()
    myFilter = AttendenceFilter(request.GET, queryset=attendences)
    attendences = myFilter.qs
    context = {'myFilter':myFilter, 'attendences': attendences, 'ta':False}
    return render(request, 'faceDetection/attendence.html', context)

def register(request):
    if request.method == "POST":
        form = ResgistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            print("IN HERE")
            messages.success(request,"SuceessFully registered")
            addFace(request.POST['face_id'])
            redirect('home')
        else:
            messages.error(request,"Account registered failed")
    else:
        form = ResgistrationForm()

    return render(request, 'faceDetection/register.html', {'form':form})

def addFace(face_id):
    face_id = face_id
    faceRecognition.faceDetect(face_id)
    faceRecognition.trainFace()
    return redirect('/')

def login(request):
     face_id = faceRecognition.recognizeFace()
     print(face_id)
     return redirect('staff' )

def Greeting(request,face_id):
    face_id = int(face_id)
    context ={
        'user' : UserProfile.objects.get(face_id = face_id)
    }
    return render(request,'faceDetection/greeting.html',context=context)

#from django.shortcuts import render, redirect
#from django.contrib.auth import authenticate, login  # For user authentication (optional)
#from .models import Attendance, UserProfile
#import json

# def login(request):
#    if request.method == 'POST':
#        data = json.loads(request.body)
#       recognized_id = data.get("id")
#
        # Assuming your logic (replace with your actual implementation)
        # This logic should retrieve the student object based on the recognized_id
        # (e.g., face recognition, unique identifier mapping, etc.)
#        student = None
        # ... your logic here

#        if student:
            # Mark attendance
#            Attendance.objects.create(student=student)
#            return JsonResponse({"message": "Attendance marked successfully!"})

#        else:
#            return JsonResponse({"message": "ID not found or invalid!"})

    # Authentication logic (optional)
#    if request.user.is_authenticated:
#        return redirect('home')  # Redirect to homepage after successful login

    # Render login template (optional)
#    return render(request, 'faceDetection/login.html')
