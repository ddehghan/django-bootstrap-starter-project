from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.http import HttpResponse

from coffin.views.generic.simple import direct_to_template
from coffin.shortcuts import get_object_or_404


def home(request):
    return direct_to_template(request, 'index.html', {
        'a': 'a',
    })


@login_required
def private(request):
    return direct_to_template(request, 'private.html', {
        'a': 'a',
    })

