from django.db import models
import time
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create Accaunt meneger
class AccauntManager(BaseUserManager):

    def _create_user(self, username, email, first_name, last_name, password=None, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault("is_admin", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password, **extra_fields)

    def create_superuser(self, username, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password, **extra_fields)


# Create own accaunt permissions
class PermissionsAccaunt(models.Model):
    is_superuser = models.BooleanField(
        "superuser status",
        default=False,
        help_text="if user is a superuser,it returns True"
    )
    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True
    
    def has_module_perms(self, app_label):
        return True



# create my own abstract user
class Accaunt(AbstractBaseUser, PermissionsAccaunt):

    username_validator = UnicodeUsernameValidator()

    username            = models.CharField(
        'username', 
        max_length = 255, 
        unique=True, 
        validators=[username_validator],
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages={
            "unique" : "A user with that username already exists."
        }
    )
    first_name          = models.CharField("first name", max_length = 150)
    last_name           = models.CharField("lastname", max_length = 150)
    email               = models.EmailField("email", max_length = 60)
    borth_day           = models.DateField("borth_day",auto_now=False, auto_now_add=False, null=True, blank=True)
    is_staff            = models.BooleanField(
        "is staffman", 
        default=True, 
        help_text="If user is a staff member, it returns True"
        )
    is_active           = models.BooleanField(
        "is active", 
        default=True,
        help_text="If user is active, it returns True"
    ) 
    is_admin            = models.BooleanField(
        "is admin", 
        default=False,
        help_text="If user is admin, it returns True"
    ) 

    data_joined         = models.DateTimeField(auto_now_add=True)
    last_login          = models.DateTimeField(auto_now=True)

    objects             = AccauntManager()

    USERNAME_FIELD      = "username"
    REQUIRED_FIELDS     = ["first_name", "last_name", "email"]

    
    "get a full name"
    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    @property
    def Professions(self):
        return self.profession_set.all()  

def card_image_location(instance, filename):
    extension   = filename.split('.')[-1]
    name        = time.strftime('%Y_%m_%d%H%M%S')
    send        = 'images/card/%s.%s' % (name, extension) 
    return send

class Profession(models.Model):
    user        =models.ForeignKey(Accaunt,on_delete=models.CASCADE)
    picture     = models.ImageField(upload_to=card_image_location, max_length=100)
    title       =models.CharField(max_length=150)
    exprience   =models.CharField(max_length=100)
    amount_work =models.IntegerField()
    degree      =models.IntegerField()
    text_title  = models.CharField(max_length=255)

    @property
    def SubProfessions(self):
        return self.subprofession_set.all()

    def __str__(self):
        return self.title

class SubProfession(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    definition = models.CharField(max_length=255)

    def __str__(self):
        return self.definition 

def contact_icon(instance, filename):
    format_icon = filename.split('.')[-1]
    times       = time.strftime('%Y-%m-%d %H:%M:%S')
    milles      = round(time.time() * 1000)
    return 'images/contacts/%s_%s.%s' % (times, milles, format_icon)
class Contact(models.Model):
    user        = models.ForeignKey(Accaunt, on_delete=models.CASCADE)
    title       = models.CharField(max_length = 150)
    link        = models.URLField()
    icon        = models.ImageField(upload_to=contact_icon, max_length=100)

    def __str__(self):
        return self.title
    
      
        
    
