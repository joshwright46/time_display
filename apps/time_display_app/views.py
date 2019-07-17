from django.shortcuts import render
from time import gmtime, strftime, strptime, localtime, clock, timezone, tzname
import os, time
from datetime import datetime
import pytz

# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    chicago = pytz.timezone('US/Central')
    datetime_chi = datetime.now(chicago)
    context = {
        "time": datetime_chi.strftime("%-I:%M:%S %p %Z"),
        "date": datetime_chi.strftime("%A %B %d, %Y")
    }
    return render(request,'time_display_app/time_display.html', context)