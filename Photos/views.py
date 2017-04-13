# coding: utf-8

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from Photos.models import Photo
from Photos.forms import PhotoEditForm


def single_photo(request, pk):
    #photo = get_object_or_404(Photo, pk=photo_id)
    photo = get_object_or_404(Photo, pk=pk)
    #print(Photo.id)
    Photo1 = Photo.objects.all
    # return render(
    #     request,
    #     'photo.html',
    #     {
    #         'photo': photo,
    #         'Photo': Photo1,
    #     }
    # )

    messages = (
        '<p>{pk}번 사진 보여줄게요</p>'.format(pk=photo.pk),
        '<p>주소는 {url}</p>'.format(url=photo.image_file.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image_file.url),
    )

    return HttpResponse('\n'.join(messages))

@login_required
def new_photo(request):
    # if not request.user.is_authenticated():
    #     return redirect(settings.LOGIN_URL)
    if request.method == "GET":
        edit_form = PhotoEditForm()
    elif request.method == "POST":
        edit_form = PhotoEditForm(request.POST, request.FILES)

        if edit_form.is_valid():
            new_photo = edit_form.save(commit=False)
            new_photo.user = request.user
            new_photo.save()

            return redirect(new_photo.get_absolute_url())

    return render(
        request,
        'new_photo.html',
        {
            'form': edit_form,
        }
    )