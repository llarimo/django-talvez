from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Courses
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



