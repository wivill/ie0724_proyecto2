from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import usuario

# Create your views here.
def new(request):    
    return HttpResponse('Showing \'new\' view page')

def show(request, pk=None):
    if pk is not None:
        try:
            user = usuario.objects.get(pk=pk)
        except usuario.DoesNotExist:
            raise Http404('Usuario con pk {} no existe'.format(pk))
        return render(
            request,
            'show.html',
            {
                'object_pk': user.pk,
                'object_name': user.name,
                'object_age': user.age,
            }
        )

    else:
        users_dict = {}
        for user in usuario.objects.all():
            users_dict[user.name] = {
                'pk': user.pk,
                'age': user.age
            }

        return render(
            request,
            'show.html',
            {
                'users_dict': users_dict
            }
        )