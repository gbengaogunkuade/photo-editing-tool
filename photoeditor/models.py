from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


from django.conf import settings        # import settings.py into views.py
from pathlib import Path









# Create your models here.


class PhotoImage(models.Model):
    user_session_id = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='Uploaded_Images/', default='default.jpg')
    


    # THE MODEL ADMIN "VERBOSE NAME PLURAL"
    class Meta:
        verbose_name_plural = "PhotoImage"


    # Display the Title in the ADMIN page instead of the modelName
    # def __str__(self):
    #     return self.user_session_id




    
    # # ADD A TITLE TO THE MODEL FOR EACH PHOTO SAVED
    # def save(self, *args, **kwargs):

    #     self.user_session_id = str(self.user_session_id)

    #     self.title = self.user_session_id + '-' + Path(self.photo.path).stem

    #     # self.photo = self.user_session_id + '-' + Path(self.photo.path).stem

    #     super().save(*args, **kwargs)

    






# class PhotoOriginal(models.Model):
#     user_session_id = models.TextField(null=True, blank=True)
#     photo = models.ImageField(upload_to='Original_Images/', default='default.jpg')


#     # THE MODEL ADMIN "VERBOSE NAME PLURAL"
#     class Meta:
#         verbose_name_plural = "PhotoOriginal"


    # Display the Title in the ADMIN page instead of the modelName
    # def __str__(self):
    #     return self.user_session_id



    # # ADD A TITLE TO THE MODEL FOR EACH PHOTO SAVED
    # def save(self, *args, **kwargs):

    #     self.user_session_id = str(self.user_session_id)

    #     self.title = self.user_session_id + '-' + Path(self.photo.path).stem

    #     super().save(*args, **kwargs)




    # # COMPRESS THE IMAGES UPLOADED TO THE MODEL ABOVE BEFORE SAVING INTO THE MODEL
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     photo = Image.open(self.photo.path)

    #     if (photo.width > 800) or (photo.height > 800):
    #         photo.thumbnail((800, 800))
    #         photo.save(self.photo.path)












