import csv, io
from django.shortcuts import render
from .models import Student_Result,Year,Class_of_student,Term,Subject_name,Student_data,Result_extra
from django.db.models import Avg,Sum
from django.db.models import Q
from django.contrib import messages
from account.models import User
# Create your views here.
import math

def search(request):
    return render(request, 'search.html')





def search_r(request):
    template='search_result.html'

    query=request.GET.get('q')
    querys = request.GET.get('currentuser')
    queryss = request.GET.get('qs')
    querysss=request.GET.get('qss')
    results=Student_Result.objects.filter(Q(studentclass=query) & Q(users=querys) & Q(term=queryss) & Q(year=querysss))

    resultse = Result_extra.objects.filter(Q(studentclass=query) & Q(term=queryss) & Q(year=querysss))
    if results:
        No_of_result=results.count()
        ty=results.aggregate(averagescore=Avg('score'))
        Marks_obtainable=100*No_of_result
        Marks_obtained = results.aggregate(Markobtained=Sum('score'))
        ip=math.floor(ty['averagescore'])
        Display_Marks_obtained=Marks_obtained['Markobtained']
        principal_remark_below_50="Below average result,put more effort next term."
        principal_remark_on_50="An Average result,put more effort next term."
        principal_remark_below_60to70="Good result,but there's still room for improvement."
        Principal_remark_above_70="Very good result, keep it up."

        return render(request, template,{'results':results,'No_of_result':No_of_result,'ip':ip,'resultse':resultse,
                                         'Marks_obtainable':Marks_obtainable,'Display_Marks_obtained':Display_Marks_obtained,
                                         'principal_remark_below_50':principal_remark_below_50,'principal_remark_on_50':principal_remark_on_50,
                                         'principal_remark_below_60to70':principal_remark_below_60to70,'Principal_remark_above_70':Principal_remark_above_70})
    else:
        messages.info(request,'invalid/unregistered input(s)')
        return render(request, 'student_dashboard.html')





def Enter_result(request):
    prompt = {
        'order': 'Order of the csv should be users,studentclass,year,term,subject_name,first_test,second_test,exam_score,score,Grade '
    }
    if request.method=='GET':
        return render(request, 'teacher.html')
    csv_file=request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'this is  not a csv file')
    data_set=csv_file.read().decode('UTF-8')
    io_string=io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string,delimiter=',',quotechar="|"):
        __,created=Student_Result.objects.update_or_create(
            users=User.objects.get(email=column[0]),
            studentclass=Class_of_student.objects.get(class_of_student=column[1]),
            year=Year.objects.get(year=column[2]),
            term=Term.objects.get(term=column[3]),
            subject_name=Subject_name.objects.get(Subject_name=column[4]),
            first_test=column[5],
            second_test=column[6],
            exam_score=column[7],
            score=column[8],
            grade=column[9],
        )
    context={}
    return render(request, 'index.html',context,prompt)



def student_profile(request):
    info=Student_data.objects.all()
    return render(request,'profile.html',{'info':info})





def test(request):
    template='test.html'

    query=request.GET.get('q')
    querys = request.GET.get('currentuser')
    queryss = request.GET.get('qs')
    querysss=request.GET.get('qss')
    results=Student_Result.objects.filter(Q(studentclass=query) & Q(users=querys) & Q(term=queryss) & Q(year=querysss))
    resultse = Result_extra.objects.filter(Q(studentclass=query) & Q(term=queryss) & Q(year=querysss))

    No_of_result=results.count()
    ty=results.aggregate(averagescore=Avg('score'))
    print(results.objects.all())
    Marks_obtainable=100*No_of_result
    Marks_obtained = results.aggregate(Markobtained=Sum('score'))
    ip=math.floor(ty['averagescore'])
    Display_Marks_obtained=Marks_obtained['Markobtained']
    principal_remark_below_50="Below average result,put more effort next term."
    principal_remark_on_50="An Average result,put more effort next term."
    principal_remark_below_60to70="Good result,but there's still room for improvement."
    Principal_remark_above_70="Very good result, keep it up."

    return render(request, template,{'results':results,'resultse':resultse,'No_of_result':No_of_result,'ip':ip,
                                     'Marks_obtainable':Marks_obtainable,'Display_Marks_obtained':Display_Marks_obtained,
                                     'principal_remark_below_50':principal_remark_below_50,'principal_remark_on_50':principal_remark_on_50,
                                     'principal_remark_below_60to70':principal_remark_below_60to70,'Principal_remark_above_70':Principal_remark_above_70})



def check_result(request):
    return render(request,'student_dashboard.html')


def Idcard(request):
    return render(request,'idcard.html')