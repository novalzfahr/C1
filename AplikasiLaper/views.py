# ---- Django Imports ----
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def main_page(request):
    context = {
        'logged_in' : request.user
    }
    return render(request, 'main_page.html', context)