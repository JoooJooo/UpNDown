from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Upload
from django.template import loader
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import datetime

def simple_upload(request):
    print("Bakwaaaaaaaas")
    postCalled1=1
    return render(request, 'upload/index.html', {'postCalled1': postCalled1})

def index(request):
    all_uploads = Upload.objects.all()
    template=loader.get_template('upload/index.html')
    postCalled = 1
    context = {
        'all_uploads': all_uploads,
        'postCalled': postCalled
    }
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        upload = Upload(user=request.POST['user'],
                        name=filename,
                        dateOfUpload=datetime.datetime.today(),
                        extension=filename.rsplit('.', 1)[1].lower(),
                        link=uploaded_file_url)
        upload.save()
        postCalled1 = 1
        return render(request, 'upload/index.html', {
            'uploaded_file_url': uploaded_file_url,
            'postCalled1': postCalled1
        })
    print("Hello It called here ")
    print(all_uploads)
    html = ''
    for upload in all_uploads :
        url = '/upload/' + str(upload.id) + '/'
        html += '<a href = "' + url + '"> ' + upload.name + '</a><br>'
    return render(request, 'upload/index.html', context)


def detail(request, upload_id):
    try:
        upload = Upload.objects.get(pk=upload_id)
    except Upload.DoesNotExist:
        raise Http404("upload does not exist")
    return render(request, 'upload/detail.html', {'upload': upload})




