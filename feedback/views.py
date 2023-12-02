from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Feedback
from .forms import FeedbackForm
from django.db.utils import OperationalError


def feedback_view(request):
	feedbacks = feedback.objects.all()
	feedabacks_data = list(map(serialize_feedbacks, medicines))
	return JsonResponse(medicines_data, safe=False)
	
def serialize_feedbacks(feedaback):
	obj = {}
	obj['pk'] = feedaback.pk
	obj['fields'] = {}
	obj['fields']['name'] = medicine.name
	obj['fields']['stock'] = medicine.stock
	return obj

@csrf_exempt
# @login_required
def feedback_create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.pelanggan = request.user
            feedback.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = FeedbackForm()

    context = {
        'form': form
    }
    return JsonResponse(context)

