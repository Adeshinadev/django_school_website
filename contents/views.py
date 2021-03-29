from django.shortcuts import render
from contents.models import event,latest_news
# import pandas as pd
from  django.http import HttpResponse
# Create your views here.
def home(request):
    all_contents=event.objects.all()
    latest_newss=latest_news.objects.all()


    # df = {'name': ['aina', 'adeshina', 'daniel'], 'total_score': [120, 100, 200]}
    # df_test = [['aina', 200], ['adeshina', 100], ['daniel', 150, ]]
    # index = [1,2,3]
    # df1 = pd.DataFrame(df,)
    #
    # b=df1.sort_values(by='total_score',ascending=False)
    # a=b.to_html(classes='table table-striped')


    return render(request,'index.html',{'all_contents':all_contents,'latest_newss':latest_newss})
    # return HttpResponse('<h1 style="color:red">position Table {}</h1>'.format(a))


def documentation(request):
    return render(request,'documentation.html')