import base64


def image_to_b64(img_path):
    binary_str = open(img_path, 'rb').read()
    base64_utf8_str = base64.b64encode(binary_str).decode('utf-8')
    return base64_utf8_str


def handle_uploaded_file(f, file_out):
    with open(file_out, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)