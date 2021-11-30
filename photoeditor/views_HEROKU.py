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



# ---------------------------------------------------------------------------------
# Photo Editor
# ---------------------------------------------------------------------------------

def photoeditor(request):
    # CREATE/GET USER_SESSION_ID
    # ----------------------------------------------------------------------
    # get the user_session_id
    current_user_session_id = request.session.get('user_session_id', None)

    if current_user_session_id is None:
        # create a new user_session_id
        generated_Number = random.randrange(0, 1000000)
        request.session['user_session_id'] = generated_Number
    else:
        # print the user_session_id
        print(request.session.get('user_session_id', None))
    # ----------------------------------------------------------------------

    try:
        # POST method -------------------------------
        if request.method == 'POST':

            existing_photo, created = PhotoImage.objects.get_or_create(user_session_id=current_user_session_id)

            existing_original_photo, created = PhotoOriginal.objects.get_or_create(user_session_id=current_user_session_id)


            form = PhotoImageForm(request.POST, request.FILES)

            if form.is_valid():
                photo = form.cleaned_data['photo']

                if existing_photo:
                    existing_photo.photo = photo
                    existing_photo.save()
                else:
                    newform = form.save(commit=False)
                    newform.user_session_id = current_user_session_id
                    newform.save()


                if existing_original_photo:
                    existing_original_photo.photo = photo
                    existing_original_photo.save()
                else:
                    pass
        
                return redirect('photoeditor_complete')
            
            else:
                return redirect('photoeditor')

        # GET method -------------------------------
        else:
            # directory of uploaded images to be edited
            image_edit_dir = settings.MEDIA_EDIT_URL
        
            for pix in image_edit_dir.glob('*.*'):
                pix.unlink()


            # directory of uploaded images original copy
            image_original_dir = settings.MEDIA_ORIGINAL_URL
        
            for pix in image_original_dir.glob('*.*'):
                pix.unlink()


            form = PhotoImageForm()
            context = {'form': form}
            return render(request, 'photoeditor/photoeditor.html', context)
    
    except:
        return redirect('photoeditor')
        






# ---------------------------------------------------------------------------------
# Photo Editor Complete
# ---------------------------------------------------------------------------------

def photoeditor_complete(request):
    # CREATE/GET USER_SESSION_ID
    # ----------------------------------------------------------------------
    # get the user_session_id
    current_user_session_id = request.session.get('user_session_id', None)

    if current_user_session_id is None:
        # create a new user_session_id
        generated_Number = random.randrange(0, 1000000)
        request.session['user_session_id'] = generated_Number
    else:
        # print the user_session_id
        print(request.session.get('user_session_id', None))
    # ----------------------------------------------------------------------

    # POST method ----------------------------------------
    if request.method == 'POST':

        existing_photo, created = PhotoImage.objects.get_or_create(user_session_id=current_user_session_id)

        form = PhotoDataForm(request.POST)

        if form.is_valid():
            brightness = form.cleaned_data['brightness']
            darken = form.cleaned_data['darken']
            contrast = form.cleaned_data['contrast']
            sharpness = form.cleaned_data['sharpness']
            blur = form.cleaned_data['blur']
            flip_left_right = form.cleaned_data['flip_left_right']
            flip_top_bottom = form.cleaned_data['flip_top_bottom']
            smoothness = form.cleaned_data['smoothness']
            more_color = form.cleaned_data['more_color']
            less_color = form.cleaned_data['less_color']
            grayscale = form.cleaned_data['grayscale']
            

            # directory of uploaded pdf files
            image_edit_dir = settings.MEDIA_EDIT_URL
            

            if brightness:
                for pix in image_edit_dir.glob('*.*'):
                    with Image.open(pix) as file:
                        file_brightness = ImageEnhance.Brightness(file).enhance(1.1)
                        file_brightness.save(pix, 'png')
                        file_brightness.close()
            else:
                pass


            if darken:
                for pix in image_edit_dir.glob('*.*'):
                    with Image.open(pix) as file:
                        file_darken = ImageEnhance.Brightness(file).enhance(0.85)
                        file_darken.save(pix, 'png')
                        file_darken.close()
            else:
                pass


            if contrast:
                for pix in image_edit_dir.glob('*.*'):
                    with Image.open(pix) as file:
                        file_contrast = ImageEnhance.Contrast(file).enhance(1.05)
                        file_contrast.save(pix, 'png')
                        file_contrast.close()
            else:
                pass

            
            if sharpness:
                for pix in image_edit_dir.glob('*.*'):
                    with Image.open(pix) as file:
                        file_sharpness = ImageEnhance.Sharpness(file).enhance(2.0)
                        file_sharpness.save(pix, 'png')
                        file_sharpness.close()
            else:
                pass


            if blur:
                for pix in image_edit_dir.glob('*.*'):
                    with Image.open(pix) as file:
                        file_blur = file.filter(ImageFilter.BoxBlur(radius=0.15))
                        file_blur.save(pix, 'png')
                        file_blur.close()
            else:
                pass

            
            if flip_left_right:
                for pix in image_edit_dir.glob('*.*'):
                    with Image.open(pix) as file:
                        file_left_right = file.transpose(Image.FLIP_LEFT_RIGHT)
                        file_left_right.save(pix, 'png')
                        file_left_right.close()
            else:
                pass


            if flip_top_bottom:
                for pix in image_edit_dir.glob('*.*'):
                    with Image.open(pix) as file:
                        file_top_bottom = file.transpose(Image.FLIP_TOP_BOTTOM)
                        file_top_bottom.save(pix, 'png')
                        file_top_bottom.close()
            else:
                pass

            
            if smoothness:
                for pix in image_edit_dir.glob('*.*'):
                    with Image.open(pix) as file:
                        file_smooth = file.filter(ImageFilter.SMOOTH)
                        file_smooth.save(pix, 'png')
                        file_smooth.close()
            else:
                pass


            if more_color:
                for pix in image_edit_dir.glob('*.*'):
                    with Image.open(pix) as file:
                        file_more_color = ImageEnhance.Color(file).enhance(1.3)
                        file_more_color.save(pix, 'png')
                        file_more_color.close()
            else:
                pass


            if less_color:
                for pix in image_edit_dir.glob('*.*'):
                    with Image.open(pix) as file:
                        file_less_color = ImageEnhance.Color(file).enhance(0.7)
                        file_less_color.save(pix, 'png')
                        file_less_color.close()
            else:
                pass


            if grayscale:
                for pix in image_edit_dir.glob('*.*'):
                    with Image.open(pix) as file:
                        file_black = file.convert('L')
                        file_black.save(pix, 'png')
                        file_black.close()
            else:
                pass


            return redirect('photoeditor_complete')
        else:
            print('not valid')
            return redirect('photoeditor_complete')


    # GET method -----------------------------------------------
    else:
        existing_photo, created = PhotoImage.objects.get_or_create(user_session_id=current_user_session_id)

        existing_original_photo, created = PhotoOriginal.objects.get_or_create(user_session_id=current_user_session_id)

        form = PhotoDataForm()
    
        context = {
            'existing_photo': existing_photo,
            'form': form,
        }

        return render(request, 'photoeditor/photoeditor_complete.html', context)









# ---------------------------------------------------------------------------------
def photoeditor_reset(request):
# ---------------------------------------------------------------------------------

    # CREATE/GET USER_SESSION_ID
    # ----------------------------------------------------------------------
    # get the user_session_id
    current_user_session_id = request.session.get('user_session_id', None)

    if current_user_session_id is None:
        # create a new user_session_id
        generated_Number = random.randrange(0, 1000000)
        request.session['user_session_id'] = generated_Number
    else:
        # print the user_session_id
        print(request.session.get('user_session_id', None))
    # ----------------------------------------------------------------------

    existing_photo, created = PhotoImage.objects.get_or_create(user_session_id=current_user_session_id)

    existing_original_photo, created = PhotoOriginal.objects.get_or_create(user_session_id=current_user_session_id)


    # directory of uploaded images to be edited
    image_edit_dir = settings.MEDIA_EDIT_URL

    for pix in image_edit_dir.glob('*.*'):
        pix.unlink()


    # directory of uploaded images original copy
    image_original_dir = settings.MEDIA_ORIGINAL_URL


    # ==============================================
    # SHUTIL
    # ==============================================
    # Syntax: shutil.copy(source, dstination)

    # Parameter: 
    # src : source directory
    # dst : destination director
    # copy_function (optional): Default – copy2(). copy() method may also be used.
    # Returns :The newly created destination directory name

    import shutil

    for pix_original in image_original_dir.glob('*.*'):
        file = pix_original
        shutil.copy(file, image_edit_dir)

    # ==============================================

    return redirect('photoeditor_complete')




    
