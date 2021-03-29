from django.db import models

# Create your models here.
class Admission_Info(models.Model):
    firstname = models.CharField(max_length=255)
    othername = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    Date_of_Birth = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    local_government_area = models.CharField(max_length=255)
    state_of_origin = models.CharField(max_length=255)
    Religion = models.CharField(max_length=255)
    Present_school = models.CharField(max_length=255)
    class_for_admission = models.CharField(max_length=255)
    reason_for_leaving_current_or_last_school = models.CharField(max_length=500)
    Testimonial_exam_results_from_last_school = models.CharField(max_length=255)
    health_conditions = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname


class Admission_info_More(models.Model):

    preferred_way_to_be_contacted=models.CharField(max_length=255)
    enter_prefered_way=models.CharField(max_length=255)
    how_did_you_hear=models.CharField(max_length=255)
    preferred_examination_center=models.CharField(max_length=255)
    signature=models.CharField(max_length=255)

    def __str__(self):
        return self.signature