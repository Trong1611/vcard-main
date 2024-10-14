import socket


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def template_and_logo(qr_generator, data):
    if 'template' in data.keys():
        template = data['template']
        print("abcd ", template)
        qr_generator.create_img(module_number=int(template))
            
    if 'logo_path' in data.keys():
        logo_path = data['logo_path']
        qr_generator.add_logo(qr_generator.read_logo(logo_path))


