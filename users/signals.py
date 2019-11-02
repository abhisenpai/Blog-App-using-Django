from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile 
#import profile model to create a profile for every user

@receiver(post_save,sender=User) #post_save is the signal, sender is User, when the user is saved then send this signal and this signal is received by this receiver(@receive())
def create_profile(sender,instance,created,**kwargs): #this receiver is theis create_profile funcion which has 4 args
    if created:  #if user created then create a profile object with the profile equal to instance of the user that was created
        Profile.objects.create(user = instance)
    

@receiver(post_save,sender=User) 
def save_profile(sender,instance,**kwargs): 
    instance.profile.save()    
    
