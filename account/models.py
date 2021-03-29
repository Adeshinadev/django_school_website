from django.db import models
from django.contrib.auth.models import (
AbstractBaseUser, BaseUserManager

)

class UserManager(BaseUserManager):
    def create_user(self,email,
                    password=None, *args, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        if not password:
            raise ValueError("Users must have a password")
        user_obj=self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)

        user_obj.staff=True
        user_obj.admin=True
        user_obj.active=True
        user_obj.applicant=False
        user_obj.accountant=False

        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self,email,
                     password=None, *args, **kwargs):
        user = self.create_user(
            email,
            password=password,
            *args, **kwargs
        )
        return user

    def create_staffuser(self,email,D_O_B,disability,genotype,blood_group,parent_office,home_address,phone,contact_address,admission_no,maiden_no,domination,
                    home_town,place_of_birth,profile_image,Religion,state_of_origin,local_government,gender,marital_status,Age,country,entry_class,othername,first_name,surname,
                    password=None):
        user=self.create_user(
            email,
            D_O_B,email,D_O_B,disability,genotype,blood_group,parent_office,home_address,phone,contact_address,admission_no,maiden_no,domination,
            home_town,place_of_birth,Religion,profile_image,state_of_origin,local_government,gender,marital_status,Age,country,entry_class,othername,first_name,surname,
            password=password,
            is_staff=True
        )
        return user



class User(AbstractBaseUser):
    objects =UserManager()

    email=models.EmailField(max_length=255,unique=True,primary_key=True)
    D_O_B = models.CharField(max_length=100,blank=True, null=True)
    surname = models.CharField(max_length=255,blank=True, null=True)
    first_name = models.CharField(max_length=255,blank=True, null=True)
    profile_image=models.ImageField(blank=True, null=True)
    othername = models.CharField(max_length=255,blank=True, null=True)
    entry_class = models.CharField(max_length=255,blank=True, null=True)
    country = models.CharField(max_length=255,blank=True, null=True)
    Age = models.CharField(max_length=5,blank=True, null=True)
    marital_status = models.CharField(max_length=255,blank=True, null=True)
    gender = models.CharField(max_length=255,blank=True, null=True)
    local_government= models.CharField(max_length=255,blank=True, null=True)
    state_of_origin = models.CharField(max_length=255,blank=True, null=True)
    Religion = models.CharField(max_length=255,blank=True, null=True)
    place_of_birth = models.CharField(max_length=255,blank=True, null=True)
    home_town = models.CharField(max_length=255,blank=True, null=True)
    domination = models.CharField(max_length=255,blank=True, null=True)
    maiden_no = models.CharField(max_length=255,blank=True, null=True)
    admission_no = models.CharField(max_length=4,blank=True, null=True, default='1506')
    contact_address = models.CharField(max_length=255,blank=True, null=True)
    phone = models.CharField(max_length=255,blank=True, null=True)
    home_address= models.CharField(max_length=255,blank=True, null=True)
    parent_office= models.CharField(max_length=255,blank=True, null=True)
    blood_group = models.CharField(max_length=255,blank=True, null=True)
    genotype=models.CharField(max_length=255,blank=True, null=True)
    disability = models.CharField(max_length=255,blank=True, null=True)
    active= models.BooleanField(default=False)
    staff= models.BooleanField(default=False)
    admin= models.BooleanField(default=False)
    applicant=models.BooleanField(default=False)
    accountant=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['D_O_B','disability','genotype','blood_group','parent_office','home_address','phone','contact_address','admission_no','maiden_no','domination',
                    'home_town','place_of_birth','Religion','profile_image','state_of_origin','local_government','gender','marital_status','Age','country','entry_class','othername','first_name','surname', 'password', 'active', 'admin', 'staff','applicant','accountant']

    def __str__(self):
        return self.email


    def get_first_name(self):
        return self.first_name

    def get_disability(self):
        return self.disability
    def get_genotype(self):
        return self.genotype
    def get_blood_group(self):
        return self.D_O_B

    def get_parent_office(self):
        return self.parent_office
    def get_s(self):
        return self.email

    def get_home_address(self):
        return self.home_address

    def get_home_town(self):
        return self.home_town

    def get_phone(self):
        return self.phone

    def get_contact_address(self):
        return self.contact_address

    def get_admission_no(self):
        return self.admission_no

    def get_maiden_no(self):
        return self.maiden_no

    def get_domination(self):
        return self.domination

    def get_place_of_birth(self):
        return self.place_of_birth

    def get_religion(self):
        return self.Religion

    def get_state_of_origin(self):
        return self.state_of_origin

    def get_local_government(self):
        return self.local_government

    def get_gender(self):
        return self.gender

    def get_marital_status(self):
        return self.marital_status

    def get_entry_class(self):
        return self.entry_class

    def get_othername(self):
        return self.othername

    def get_first_name(self):
        return self.first_name

    def get_surname(self):
        return self.surname

    def get_D_O_B(self):
        return self.D_O_B

    def get_Age(self):
        return self.Age

    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    def get_short_name(self):
        return self.email
    def get_profile_image(self):
        return self.profile_image

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_applicant(self):
        return self.applicant

    @property
    def is_accountant(self):
        return self.accountant

