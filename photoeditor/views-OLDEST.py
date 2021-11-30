from django.shortcuts import render, get_object_or_404, redirect
from photoeditor.models import PhotoImage, PhotoOriginal
from photoeditor.forms import PhotoImageForm, PhotoDataForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from PIL import Image, ImageFilter, ImageEnhance
import PyPDF2
from pathlib import Path


from django.core.files.storage import FileSystemStorage

from django.conf import settings        # import settings.py into views.py
import random


# Create your views here.


# WORKING WITH SESSIONS
# --------------------------------------------------------------------------------    
def decrease_brightness(request):
# --------------------------------------------------------------------------------
    # # CREATE/GET IMAGE SESSION NUMBER
    # # ----------------------------------------------------------------------
    # Get the current images session number
    request.session.get('current_image_session_number')

    if request.session.get('current_image_session_number'):
        request.session['current_image_session_number'] = request.session.get('current_image_session_number') + 1.25
        print(request.session.get('current_image_session_number'))
        return redirect('photoeditor_complete')

    else:
        request.session['current_image_session_number'] = 2.5
        print(request.session.get('current_image_session_number'))
        return redirect('photoeditor_complete')