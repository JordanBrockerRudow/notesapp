from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as main_logout

# Logged-in User View
@login_required
def profile(request):
    return render(request, "notesapp_auth/profile.html")


def logout(*args, **kwargs):
    resp = main_logout(*args, **kwargs)
    # redirect to home page after 2 seconds
    resp['Refresh'] = '2;URL=/'
    return resp