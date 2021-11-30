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

super_photo = ''



# ---------------------------------------------------------------------------------
# Photo Editor
# ---------------------------------------------------------------------------------

def photoeditor(request):
    # create/get current user session number
    # ----------------------------------------------------------------------
    # Get the current user session number
    request.session.get('current_user_session_number')

    if request.session.get('current_user_session_number'):
        print(request.session.get('current_user_session_number'))

    else:
        # create a new current user session number
        generated_Number = random.randrange(0, 1000000)
        request.session['current_user_session_number'] = generated_Number
        print(request.session.get('current_user_session_number'))

    # ----------------------------------------------------------------------

    # POST method -------------------------------
    if request.method == 'POST':

        form = PhotoImageForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.cleaned_data['photo']
            newform = form.save(commit=False)
            newform.user_session_id = request.session.get('current_user_session_number')
            newform.save()


            existing_original_photo = PhotoOriginal.objects.create(user_session_id=request.session.get('current_user_session_number'), photo=photo)
            existing_original_photo.save()

            global super_photo
            super_photo = photo

            print('nawa = ', super_photo)

            return redirect('photoeditor_complete')
        
        else:
            return redirect('photoeditor')



    # GET method -------------------------------
    else:

        existing_photo, created = PhotoImage.objects.get_or_create(user_session_id=request.session.get('current_user_session_number'))

        existing_original_photo, created = PhotoOriginal.objects.get_or_create(user_session_id=request.session.get('current_user_session_number'))


        if existing_photo:
            existing_photo.delete()
        else:
            pass


        if existing_original_photo:
            existing_original_photo.delete()
        else:
            pass


        form = PhotoImageForm()
        context = {'form': form}
        return render(request, 'photoeditor/photoeditor.html', context)
    







# ---------------------------------------------------------------------------------
# Photo Editor Complete
# ---------------------------------------------------------------------------------

def photoeditor_complete(request):
    # create/get current user session number
    # ----------------------------------------------------------------------
    # Get the current user session number
    request.session.get('current_user_session_number')

    if request.session.get('current_user_session_number'):
        print(request.session.get('current_user_session_number'))

    else:
        # create a new current user session number
        generated_Number = random.randrange(0, 1000000)
        request.session['current_user_session_number'] = generated_Number
        print(request.session.get('current_user_session_number'))

    # ----------------------------------------------------------------------

    # POST method ----------------------------------------
    if request.method == 'POST':

        existing_photo = PhotoImage.objects.get(user_session_id=request.session.get('current_user_session_number'))

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
            

            
            myPHOTO = existing_photo.photo.path


            if brightness:
                with Image.open(myPHOTO) as file:
                    file_brightness = ImageEnhance.Brightness(file).enhance(1.1)
                    file_brightness.save(myPHOTO, 'png')
                    file_brightness.close()
            else:
                pass


            if darken:
                with Image.open(myPHOTO) as file:
                    file_darken = ImageEnhance.Brightness(file).enhance(0.85)
                    file_darken.save(myPHOTO, 'png')
                    file_darken.close()
            else:
                pass


            if contrast:
                with Image.open(myPHOTO) as file:
                    file_contrast = ImageEnhance.Contrast(file).enhance(1.05)
                    file_contrast.save(myPHOTO, 'png')
                    file_contrast.close()
            else:
                pass

            
            if sharpness:
                with Image.open(myPHOTO) as file:
                    file_sharpness = ImageEnhance.Sharpness(file).enhance(2.0)
                    file_sharpness.save(myPHOTO, 'png')
                    file_sharpness.close()
            else:
                pass


            if blur:
                with Image.open(myPHOTO) as file:
                    file_blur = file.filter(ImageFilter.BoxBlur(radius=0.15))
                    file_blur.save(myPHOTO, 'png')
                    file_blur.close()
            else:
                pass

            
            if flip_left_right:
                with Image.open(myPHOTO) as file:
                    file_left_right = file.transpose(Image.FLIP_LEFT_RIGHT)
                    file_left_right.save(myPHOTO, 'png')
                    file_left_right.close()
            else:
                pass


            if flip_top_bottom:
                with Image.open(myPHOTO) as file:
                    file_top_bottom = file.transpose(Image.FLIP_TOP_BOTTOM)
                    file_top_bottom.save(myPHOTO, 'png')
                    file_top_bottom.close()
            else:
                pass

            
            if smoothness:
                with Image.open(myPHOTO) as file:
                    file_smooth = file.filter(ImageFilter.SMOOTH)
                    file_smooth.save(myPHOTO, 'png')
                    file_smooth.close()
            else:
                pass


            if more_color:
                with Image.open(myPHOTO) as file:
                    file_more_color = ImageEnhance.Color(file).enhance(1.3)
                    file_more_color.save(myPHOTO, 'png')
                    file_more_color.close()
            else:
                pass


            if less_color:
                with Image.open(myPHOTO) as file:
                    file_less_color = ImageEnhance.Color(file).enhance(0.7)
                    file_less_color.save(myPHOTO, 'png')
                    file_less_color.close()
            else:
                pass


            if grayscale:
                with Image.open(myPHOTO) as file:
                    file_black = file.convert('L')
                    file_black.save(myPHOTO, 'png')
                    file_black.close()
            else:
                pass


            return redirect('photoeditor_complete')
        else:
            print('not valid')
            return redirect('photoeditor_complete')


    # GET method -----------------------------------------------
    else:
        existing_photo = PhotoImage.objects.get(user_session_id=request.session.get('current_user_session_number'))

        form = PhotoDataForm()
    
        context = {
            'existing_photo': existing_photo.photo,
            'form': form
        }

        return render(request, 'photoeditor/photoeditor_complete.html', context)











# # ---------------------------------------------------------------------------------
# def photoeditor_reset(request):
# # ---------------------------------------------------------------------------------
#     # create/get current user session number
#     # ----------------------------------------------------------------------
#     # Get the current user session number
#     request.session.get('current_user_session_number')

#     if request.session.get('current_user_session_number'):
#         print(request.session.get('current_user_session_number'))

#     else:
#         # create a new current user session number
#         generated_Number = random.randrange(0, 1000000)
#         request.session['current_user_session_number'] = generated_Number
#         print(request.session.get('current_user_session_number'))

#     # ----------------------------------------------------------------------

#     existing_photo = PhotoImage.objects.get(user_session_id=request.session.get('current_user_session_number'))

#     if existing_photo:
#         existing_photo.delete()
#     else:
#         pass

#     existing_original_photo = PhotoOriginal.objects.get(user_session_id=request.session.get('current_user_session_number'))

#     existing_photo = PhotoImage.objects.create(user_session_id=request.session.get('current_user_session_number'), photo=existing_original_photo.photo)
#     # existing_photo.save()

#     existing_original_photo.delete()


#     existing_original_photo = PhotoOriginal.objects.create(user_session_id=request.session.get('current_user_session_number'), photo=existing_photo.photo)
#     existing_original_photo.save()



#     # ==============================================
#     # SHUTIL
#     # ==============================================
#     # Syntax: shutil.copy(source, dstination)

#     # Parameter: 
#     # src : source directory
#     # dst : destination director
#     # copy_function (optional): Default – copy2(). copy() method may also be used.
#     # Returns :The newly created destination directory name

#     # import shutil

#     # for pix in original_path.glob('*.*'):
#     #     shutil.copy(pix, upload_path)

#     # ==============================================

#     return redirect('photoeditor_complete')




    




# ---------------------------------------------------------------------------------
def photoeditor_reset(request):
# ---------------------------------------------------------------------------------
    # create/get current user session number
    # ----------------------------------------------------------------------
    # Get the current user session number
    request.session.get('current_user_session_number')

    if request.session.get('current_user_session_number'):
        print(request.session.get('current_user_session_number'))

    else:
        # create a new current user session number
        generated_Number = random.randrange(0, 1000000)
        request.session['current_user_session_number'] = generated_Number
        print(request.session.get('current_user_session_number'))

    # ----------------------------------------------------------------------

    existing_photo = PhotoImage.objects.get(user_session_id=request.session.get('current_user_session_number'))

    if existing_photo:
        existing_photo.delete()
    else:
        pass

    existing_original_photo = PhotoOriginal.objects.get(user_session_id=request.session.get('current_user_session_number'))

    existing_photo = PhotoImage.objects.create(user_session_id=request.session.get('current_user_session_number'), photo=existing_original_photo.photo)
    existing_photo.save()

    return redirect('photoeditor_complete')











