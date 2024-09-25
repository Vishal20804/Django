from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_delete,pre_save,post_delete,post_init,post_save
from django.core.signals import request_started,request_finished,got_request_exception

#1st method
@receiver(user_logged_in,sender=User)
#receiver function

def login_success(sender,request,user,**kwargs):
    print("______________________")
    print("loggged-in signal .....Run Intro")
    print("sender:",sender)
    print("Request:",request)
    print("User:",user)
    print(f'kwargs:{kwargs}')
#2nd method
# user_logged_in.connect(login_success,sender=User)
#@receiver(user_logged_out,sender=User)
#loggedout
def log_out(sender,request,user,**kwargs):
    print("______________________")
    print("log_out signal .....Run outro")
    print("sender:",sender)
    print("Request:",request)
    print("User:",user)
    print(f'kwargs:{kwargs}')
    
user_logged_out.connect(log_out,sender=User)

#log in failed
@receiver(user_login_failed)

def login_failed(sender,credentials,request,**kwargs):
    print("______________________")
    print("login failed signal .....Run outro")
    print("sender:",sender)
    print("Request:",request)
    print(f'kwargs:{kwargs}')
    print("creadentials",credentials)



@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("______________________")
    print("Pre Save signal .....")
    print("sender:",sender)
    print(f'kwargs:{kwargs}')
    print("instance",instance)   
#pre_save.connect(at_beginning_save,sender=User)

@receiver(post_save,sender=User)
def at_end_save(sender,instance,created,**kwargs):
    if created:
        print("______________________")
        print("Post Save signal .....")
        print("New Record .....")        
        print("sender:",sender)
        print(f'kwargs:{kwargs}')
        print("created",created)
        print("instance",instance)  
    else:
        print("______________________")
        print("updated.....")
        print("New Record .....")        
        print("sender:",sender)
        print(f'kwargs:{kwargs}')
        print("created",created)
        print("instance",instance)  
#post_save.connect(at_end_save,sender=User)


@receiver(pre_delete,sender=User)
def at_beginning_del(sender,instance,**kwargs):
    print("______________________")
    print("Pre deleted signal .....")
    print("sender:",sender)
    print(f'kwargs:{kwargs}')
    print("instance",instance)   
#pre_delete.connect(at_beginning_del,sender=User)

@receiver(post_delete,sender=User)
def at_end_del(sender,instance,**kwargs):
    print("______________________")
    print("Post delete signal .....")
    
    print("sender:",sender)
    print(f'kwargs:{kwargs}')

    print("instance",instance)  

#post_save.connect(at_end_save,sender=User)



@receiver(request_started)
def at_beginning_req(sender,environ,**kwargs):
    print("______________________")
    print("At beginning Request .....")
    print("sender:",sender)
    print("environment:",environ)
    print(f'kwargs:{kwargs}')

   
@receiver(request_finished)
def at_end_req(sender,**kwargs):
    print("______________________")
    print("At ending Request .....")
    print("sender:",sender)

    print(f'kwargs:{kwargs}')

   
@receiver(got_request_exception)
def at_req_exception(sender,**kwargs):
    print("______________________")
    print("Request exceptions.....")
    print("sender:",sender)
    print(f'kwargs:{kwargs}')

   