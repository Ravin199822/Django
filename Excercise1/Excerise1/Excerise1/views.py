# I have created this file

from django.http import HttpResponse

def index(request):
    s="<h1>Navigator</h1><a href='https://www.facebook.com/'>Facebook</a1><br><a href='https://www.google.com/'>Google</a><br><a href='https://www.codewithharry.com/'>Code With Harry</a><br><a href='https://www.instagram.com/'>Instagram</a><br><a href='https://www.youtube.com/'>youtube</a>"
    return HttpResponse(s)