import os

from .vcard import VCard
from .qr_generator import QrGenerator
from vcard.helpers.constants import VCF_PATH, HOST
from vcard.helpers.view_functions import get_ip


def template_and_logo(qr_generator: QrGenerator,
                      data: dict):
    if 'template' in data.keys():
        template = data['template']
        print("abcd ", template)
        qr_generator.create_img(module_number=int(template))
            
    if 'logo_path' in data.keys():
        logo_path = data['logo_path']
        qr_generator.add_logo(qr_generator.read_logo(logo_path))


def generate_qr(data, save_img_path=None):
    vcf_file_name = data['vcf_file_name'] if 'vcf_file_name' in data.keys() else None
    
    qr_generator = QrGenerator()
    v_card = VCard()
    vcf = v_card.generate_vcard(**data)
    if vcf_file_name is not None:
        vcf_file_path = os.path.join(VCF_PATH, vcf_file_name)
        with open(vcf_file_path, 'w', encoding="utf-8") as f:
            f.write(vcf)
    else:
        return b""
    # current_ip = get_ip()
    current_ip = '175.41.173.117'
    hosted_file_location = HOST.format(current_ip) + '/media/vcf/' + vcf_file_name
    qr_generator.add_data(hosted_file_location)

    template_and_logo(qr_generator=qr_generator, 
                      data=data)
    qr_b64 = qr_generator.after_image_processing()
    if save_img_path is not None:
        qr_generator.generate_image(file_name=save_img_path)
    return qr_b64
