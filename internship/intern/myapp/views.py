from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# def home(request):
#     return render(request, 'myapp/home.html')
#
# def home(request):
#     if request.method == 'POST' and request.FILES['myfile'] and request.FILES['myfile_second']:
#         myfile = request.FILES['myfile']
#         myfile_second = request.FILES['myfile_second']
#
#         print("file runing")
#         return render(request, 'myapp/home.html',{
#         myfile:myfile,
#         myfile_second:myfile_second
#         })
#     return render(request, 'myapp/home.html')

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')
