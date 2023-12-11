from django.http import JsonResponse
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

@login_required(login_url='/userauth/')
def read_feedback(request):
    current_user = UserDataModel.objects.get(id=request.user.id)
    if current_user.role == 'admin':
        feedbacks = Feedback.objects.all()
        if feedbacks.count() == 0:
            exist = False
        else:
            exist = True
        context = {'feedbacks': feedbacks,
                   'exist': exist}
        return render(request, 'read_feedback.html', context)
    if current_user.role == 'pelanggan':
        feedbacks = Feedback.objects.filter(user=request.user)
        if feedbacks.count() == 0:
            exist = False
        else:
            exist = True
        context = {'feedbacks': feedbacks,
                   'exist': exist}
        return render(request, 'read_feedback.html', context)

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

# class create_feedback(LoginRequiredMixin, CreateView):
#     model = Feedback
#     form_class = FeedbackForm
#     template_name = 'create_feedback.html'
#     success_url = '/feedback/'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)