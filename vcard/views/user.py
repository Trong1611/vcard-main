from django.shortcuts import render, redirect

from vcard.models import VcardInformation


def get_vcard_list(request):
    vcards = VcardInformation.objects.filter(UserID=request.user, active=True)
    return vcards


def list_vcard(request):
    render_object = dict()
    vcards = get_vcard_list(request)
    render_object['vcards'] = vcards
    return render(request, "vcard/listCard.html", render_object)


def delete_vcard(request, vcard_id):
    vcard = VcardInformation.objects.get(id=vcard_id)
    vcard.active = False
    vcard.save()
    return redirect('/vcard/list')