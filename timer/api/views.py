from django.shortcuts import render
import pytz
from datetime import datetime

def get_current_time():
    # Get the current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist)
    return current_time.strftime('%I:%M:%S %p')

def home(request):
    context = {
        'current_time': get_current_time(),
    }
    return render(request, 'current_time.html', context)
