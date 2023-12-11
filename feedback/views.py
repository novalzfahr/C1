from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Feedback
from django.db.utils import OperationalError
from userauth.models import UserDataModel
import json
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Feedback
from .forms import FeedbackForm
from django.shortcuts import get_object_or_404

@login_required(login_url='/userauth/')
def read_feedback(request):
    current_user = UserDataModel.objects.get(id=request.user.id)
    if current_user.role == 'admin':
        feedbacks = Feedback.objects.all()
        if feedbacks.count() == 0:
            exist = False
        else:
            exist = True
        admin = True
        context = {'feedbacks': feedbacks,
                   'exist': exist,
                   'admin': admin}
        return render(request, 'read_feedback.html', context)
    if current_user.role == 'pelanggan':
        try:
            feedbacks = Feedback.objects.filter(user=request.user)
            if feedbacks.count() == 0:
                exist = False
            else:
                exist = True
        except:
            exist = False
        admin = False
        context = {'feedbacks': feedbacks,
                   'exist': exist,
                   'admin': admin}
        return render(request, 'read_feedback.html', context)

@csrf_exempt
@login_required(login_url='/userauth/')
def create_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('/feedback/')
    else:
        form = FeedbackForm()
    return render(request, 'create_feedback.html', {'form': form})

@login_required(login_url='/userauth/')
def delete_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id, user=request.user)
    
    if request.method == 'POST':
        feedback.delete()
        return redirect('feedback:read_feedback')

    # Handle the case where the user accesses the delete page directly
    return HttpResponseBadRequest("Bad Request")