from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def IndexView(request):
    #return HttpResponse("Newsfeed Page")

def newsfeedView(request, username):
	return render(request, 'newsfeed/newsfeed.html', {'current_user': request.user})
