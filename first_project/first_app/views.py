from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Webpage, Topic
# Create your views here.

def index(request):
    from_db = AccessRecord.objects.order_by('date')
    db_dict =  {'insert_me':from_db}
    return render (request,'first_app/index.html',context=db_dict) 