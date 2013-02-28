from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

# from coffin.views.generic.simple import direct_to_template
from coffin.shortcuts import get_object_or_404, render_to_response

from website.models import LandingForm


# def home(request):
#     return direct_to_template(request, 'home.html', {
#         'a': 'a',
#     }, context_instance=RequestContext(request))


def index(request):
    return render_to_response('index.html', {
        'a': 'a',
    }, context_instance=RequestContext(request))


@login_required
def private(request):
    return render_to_response('private.html', {
        'a': 'a',
    }, context_instance=RequestContext(request))


def home(request):
    # Show the sign page and collect emails

    show_invite = True
    if request.method == "POST":
        myform = LandingForm(request.POST)
        landing_instance = myform.save(commit=False)
        if myform.is_valid():
            landing_instance.ip_address = request.META['REMOTE_ADDR']
            landing_instance.save()
            show_invite = False

            # send_email("PIKFOOD: Landing page ","email=" + request.POST["email"])

        else:
            return HttpResponse("error")

    myform = LandingForm()
    return render_to_response('home.html', {
        "myform": myform,
        "show_invite": show_invite
    }, context_instance=RequestContext(request))
