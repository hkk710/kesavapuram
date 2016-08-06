from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from mail_templated import send_mail


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, email and password.
        """
        if not email:raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    Extends the default User profiles of Django. The fields of this model can be obtained by the
    user.get_profile method and it's extended by the django-profile application.
    """
    user_id = models.AutoField(primary_key=True)
    aums_id = models.CharField(_('Aums ID'),  max_length=32, blank=False, unique=True)
    first_name = models.CharField(_('First Name'), max_length=32, blank=True, null=True,
                                  validators=[RegexValidator(regex='^[A-Za-z]*$')])
    last_name = models.CharField(_('Last Name'), max_length=32, blank=True, null=True,
                                    validators=[RegexValidator(regex='^[A-Za-z]*$')])
    email = models.EmailField(_('Email'), db_index=True, unique=True)
    username = models.CharField(_('username'), max_length=32, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_cir_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        return self.email


class StudentManager(models.Manager):

    def create_student_fromfile(self, aums_id, name, curr_course, branch, tenth_mark, twelth_mark,
                                s1, s2, s3, s4, s5, s6, cgpa, curr_arrears, hist_arrears):
        student = self.create(aums_id=aums_id, name=name, curr_course=curr_course ,branch=branch,
                              tenth_mark=tenth_mark, twelth_mark=twelth_mark, s1=s1, s2=s2, s3=s3, s4=s4,
                              s5=s5, s6=s6, cgpa=cgpa, curr_arrears=curr_arrears, hist_arrears=hist_arrears)

        # do something with the book
        return student

Prathishtta  = (('SreekrishnaSwamy', _('SreekrishnaSwamy')), ('Ganapathi', _('Ganapathi')), ('Devi', _('Devi')),
         ('Nagar', _('Nagar')),
         )

Vazhipad_cattegory = (('Archana', _('Archana')), ('Homam', _('Homam')), ('Pooja', _('Pooja')),
                  ('Samarppanam', _('Samarppanam')),
                  )
Archana = (('Ashttothara', _('Ashttothara')), ('Vishnusahasranama', _('Vishnusahasranama')), ('Bhagyasuktha', _('Bhagyasuktha')),
            ('Swayawara', _('Swayawara')),
           )

price = ((20.0, _(20.0)), )

class Student(models.Model):
    aums_id = models.CharField(_('Prathishtta'),  max_length=32, choices=Prathishtta, blank=False, unique=True,primary_key=True)
    name = models.CharField(_('Vazhipad cattegory'), max_length=32, choices=Vazhipad_cattegory,blank=True, null=True)
    curr_course = models.CharField(_('Vazhipad'), max_length=32,choices= Archana ,blank=True, null=True,
                                  validators=[RegexValidator(regex='^[A-Za-z]*$')])
    branch = models.CharField(_('Your Name'), max_length=32, blank=True, null=True)
    tenth_mark = models.DateField(_('Vazhipad Date'), null=True)
    twelth_mark = models.FloatField( _('Price'), blank=True, null=True)

    Objects = StudentManager()

class Chocolate(models.Model):
    id           = models.AutoField(primary_key=True)
    name         = models.CharField(_('Your Name'), max_length=100, blank=True, null=True)
    description  = models.CharField(_('Your Star'), max_length=100, blank=True, null=True)
    manufacturer = models.CharField(_('Vazhipad Date'), max_length=100, blank=True, null=True)
    price        = models.IntegerField(_('Price'),
                                 validators=[MaxValueValidator(1000), MinValueValidator(0)],
                                 help_text=_('4 digits maximum'), blank=True, null=True)