from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.http import HttpResponse
from django.template import RequestContext

from coffin.views.generic.simple import direct_to_template
from coffin.shortcuts import get_object_or_404


def home(request):
    return direct_to_template(request, 'home.html', {
        'a': 'a',
    }, context_instance=RequestContext(request))


def index(request):
    return direct_to_template(request, 'index.html', {
        'a': 'a',
    }, context_instance=RequestContext(request))


@login_required
def private(request):
    return direct_to_template(request, 'private.html', {
        'a': 'a',
    }, context_instance=RequestContext(request))
