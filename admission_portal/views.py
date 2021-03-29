from django.shortcuts import render
from .models import Admission_Info,Admission_info_More
# Create your views here.
def enter_admission_details(request):
    if request.method == "POST":
        firstname=request.POST['firstname']
        othername=request.POST['othername']
        fullname=request.POST['fullname']
        surname=request.POST['surname']
        Date_of_Birth=request.POST['Date_of_Birth']
        gender=request.POST['gender']
        local_government_area=request.POST['local_government_area']
        state_of_origin=request.POST['state_of_origin']
        Religion=request.POST['Religion']
        Present_school=request.POST['Present_school']
        class_for_admission=request.POST['class_for_admission']
        reason_for_leaving_current_or_last_school=request.POST['reason_for_leaving_current_or_last_school']
        Testimonial_exam_results_from_last_school=request.POST['Testimonial_exam_results_from_last_school']
        health_conditions=request.POST['health_conditions']
        saved_details=Admission_Info(surname=surname,othername=othername,firstname=firstname,fullname=fullname,Date_of_Birth=Date_of_Birth,gender=gender,local_government_area=local_government_area
                                     ,state_of_origin=state_of_origin,Religion=Religion,Present_school=Present_school,class_for_admission=class_for_admission,
                                     reason_for_leaving_current_or_last_school=reason_for_leaving_current_or_last_school,Testimonial_exam_results_from_last_school=
                                     Testimonial_exam_results_from_last_school,health_conditions=health_conditions,)
        saved_details.save()
        return render(request,'afterapplicant.html')
    else:
        return render(request,'applicant.html')




def afteradd(request):
    if request.method == "POST":
        preferred_way_to_be_contacted=request.POST['preferred_way_to_be_contacted']
        enter_prefered_way=request.POST['enter_prefered_way']
        how_did_you_hear=request.POST['how_did_you_hear']
        preferred_examination_center=request.POST['preferred_examination_center']
        signature=request.POST['signature']

        save_afteradd=Admission_info_More(preferred_way_to_be_contacted=preferred_way_to_be_contacted,enter_prefered_way=enter_prefered_way
                                          ,how_did_you_hear=how_did_you_hear,preferred_examination_center=preferred_examination_center,signature=signature)
        save_afteradd.save()
        return render(request,'homepage.html')
    else:
        return render(request,'afterapplicant.html')
