from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *

def insert_topic(request):
    TFO=Topic_Form()
    d={'TFO': TFO}

    if request.method=='POST':
        TFD=Topic_Form(request.POST)

        if TFD.is_valid():
            S_No=TFD.cleaned_data['S_No']
            Topic_Name=TFD.cleaned_data['Topic_Name']

            TO=Topic.objects.get_or_create(S_No=S_No, Topic_Name=Topic_Name)[0]
            TO.save()

            TQS=Topic.objects.all()
            d1={'TQS': TQS}
            return render(request, 'display_topic.html', d1)

    return render(request, 'Topic_Form.html', d)

