import os
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse

from vcard.forms import UploadIconForm
from vcard.qr_generator.helpers import image_to_b64, handle_uploaded_file
from vcard.qr_generator.generate import generate_qr
from vcard.helpers.constants import MEDIA_PATH, TEMP_PATH
from vcard.models import VcardInformation


def save_vcard_information(request, data):
    template = "" if 'template' not in data.keys() else data['template']
    logo = "" if 'logo' not in data.keys() else data['logo']
    vcard_info = VcardInformation(UserID=request.user,
                                  DisplayName=data['name'],
                                  Company=data['company'],
                                  Position=data['position'],
                                  PhoneNumber=data["phone"],
                                  Address=data["address"],
                                  Email=data["email"],
                                  Website=data["website"],
                                  fileName=data['vcf_file_name'],
                                  template=template,
                                  logo=logo)
    vcard_info.save()
    return vcard_info.pk


def load_qr_from_request(request):
    if 'data' in request.session and request.session['data'] is not None:
        data = json.loads(request.session['data'])
        return data
    else:
        return {}


def style_qr_view(request):
    data = load_qr_from_request(request)
    if len(data) <= 0:
        return redirect('/vcard/create')
    image_form = UploadIconForm()

    if request.method == "POST":
        step = request.POST.get('step')
        csrf_token = request.POST.get('csrfmiddlewaretoken')
        if step == 'download':
            if request.user.is_authenticated:
                vcard_id = save_vcard_information(request, data)
                save_path = os.path.join(TEMP_PATH, '{}.jpg'.format(csrf_token))
                qr_b64 = generate_qr(data=data, save_img_path=save_path)
                download_img = open(save_path, 'rb').read()
                os.remove(os.path.join(TEMP_PATH, '{}.jpg'.format(csrf_token)))
                response = HttpResponse(
                    download_img,
                    headers={
                        'Content-Type': 'image/jpeg',
                        'Content-Disposition': 'attachment; filename="qr.jpg"'})
                return response
            else:
                # return render(request, 'vcard/login.html', {'saveInfor': 'save'})
                return redirect("/vcard/login")
        else:
            image_form = UploadIconForm(request.POST, request.FILES)
            qr_b64 = generate_qr(data)
            if image_form.is_valid():
                logo_path = os.path.join(TEMP_PATH, '{}.png'.format(csrf_token))
                handle_uploaded_file(request.FILES['file'], logo_path)
                data['logo_path'] = logo_path
                qr_b64 = generate_qr(data)
            request.session['data'] = json.dumps(data)
            return render(request,
                          'vcard/vcard_style.html',
                          {
                              'data': data,
                              'qrimg': qr_b64,
                              'form': image_form
                          })

    elif request.method == "GET":
        if 'template' in request.GET:
            template = request.GET.get('template')
        elif 'template' in data.keys():
            template = data['template']
        else:
            template = '0'
        data['template'] = template
        request.session['data'] = json.dumps(data)
        qr_b64 = generate_qr(data)

        return render(request,
                      'vcard/vcard_style.html',
                      {
                          "data": data,
                          "qrimg": qr_b64,
                          "form": image_form
                      })
