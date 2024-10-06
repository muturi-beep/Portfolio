from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def experiences(request):

    experiences=[
        {"company":"ABC",
         "position":"python developer"},
        {"company":"ABC2",
         "position":"python developer2"},
        {"company":"ABC3",
         "position":"python developer3"}
    ]

    return render (request,'experiences.html',{'experiences':experiences})

def projects(request):

    projects_show=[
        {
            'title': 'Rasoi Connect',
            'path': 'images/rasoi_connect.PNG',
        },
        {
            'title': 'Ecommerce',
            'path': 'images/ecommerce.PNG',
        },

        {
            'title': 'Timetable Scheduler',
            'path': 'images/timtable.PNG',
        },
        {
            'title': 'CRUD',
            'path': 'images/CRUD.PNG',
        },

         {
            'title': 'Photo Uploader',
            'path': 'images/photo_uploader.PNG',
        },
          {
            'title': 'To do list',
            'path': 'images/todolist.PNG',
        },
         {
            'title': 'Portfolio',
            'path': 'images/portfolio.PNG',
        },
                  {
            'title': 'Labour Hiring',
            'path': 'images\labour_hiring.PNG',
        },

    ]


# Passing data in form of a dictonary
    return render(request,'projects.html',{'projects_show': projects_show})

def certificates(request):
    return render(request, 'certificates.html')

def contact(request):
    return render(request, 'contact.html')

def resume(request):
    resume_path="mycv/SM.docx"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="SM.docx"
            return response
    else:
        return HttpResponse("resume not found", status=404)


