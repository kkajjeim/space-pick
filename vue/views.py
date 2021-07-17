from django.shortcuts import render


# Create your views here.
def hello_space_pick(request):
    return render(request, 'vue/index.html');
