from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'auto_dnup/post_list.html', {})