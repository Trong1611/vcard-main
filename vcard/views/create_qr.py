import json

from django.shortcuts import render, redirect

from vcard.qr_generator.generate import generate_qr
from vcard.models import VcardInformation


def create_qr_view(request):
    if request.method == "POST":
        crsf_token, DisplayName, Company, Position, \
            PhoneNumber, Address, Email, Website, step, submit_type = (request.POST.get(key) for key in request.POST.keys())
        fileName = DisplayName.replace(" ", "-")
        fileName = fileName + '-' + PhoneNumber + '.vcf'
        data = {"name": DisplayName,
                "company": Company,
                "position": Position,
                "phone": PhoneNumber,
                "address": Address,
                "email": Email,
                "website": Website,
                "vcf_file_name": fileName}
        qr_b64 = generate_qr(data)
        request.session['data'] = json.dumps(data)
        if submit_type == "view_qr":
            return render(request, 'vcard/vcard.html', {"qrimg": qr_b64, "name": DisplayName,
                                                    "company": Company,
                                                    "position": Position,
                                                    "phone": PhoneNumber,
                                                    "address": Address,
                                                    "email": Email,
                                                    "website": Website,
                                                    "vcf_file_name": fileName})
        else:
            return redirect('/vcard/create/format')
    return render(request, 'vcard/vcard.html', {})