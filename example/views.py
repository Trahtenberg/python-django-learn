from django.http import HttpResponse

def hello(request):
    print(request)
    print()
    print(dir(request))
    print()
    pass
    #return HttpResponse('<h1>Hello Roman, you top developer</h1>')