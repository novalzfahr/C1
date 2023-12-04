from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Feedback
from django.db.utils import OperationalError
from userauth.models import UserDataModel
import json
from django.core import serializers
from django.shortcuts import render
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

# @csrf_exempt
# @login_required(login_url='/userauth/')
# def create_feedback(request):
#     if request.method == 'GET':
#         return render(request, 'create_feedback.html')
#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         feedback = Feedback.objects.create(
#             user=request.user,
#             message=data['message'],
#             date_created=datetime.now()
#         )
#         return render(request, 'create_feedback.html', {'feedback': feedback})


class create_feedback(LoginRequiredMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'create_feedback.html'
    success_url = '/feedback/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)