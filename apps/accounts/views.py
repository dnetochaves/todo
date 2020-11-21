from django.shortcuts import render

# Create your views here.
def begin(request):
    return render(request, 'accounts/begin.html', {})
