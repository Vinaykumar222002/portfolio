from django.shortcuts import render

# Create your views here.
def certifications(request):
    return render(request, 'certifications.html')