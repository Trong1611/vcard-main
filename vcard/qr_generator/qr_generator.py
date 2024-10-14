from PIL import Image
import io
import base64

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer, RoundedModuleDrawer, \
    GappedSquareModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer



class QrGenerator:
    def __init__(self) -> None:
        self.basewidth = 150
        self.fill_color = 'black'
        self.back_color = 'white'
        self.qr_code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,
                                     version=1,
                                     box_size=10)
        self.qr_code.clear()
        self.qr_img = None
        self.style_dict = {
            1: CircleModuleDrawer(),
            2: RoundedModuleDrawer(),
            3: GappedSquareModuleDrawer(),
            4: VerticalBarsDrawer(),
            5: HorizontalBarsDrawer()
        }

    def add_data(self, text):
        self.qr_code.clear()
        self.qr_code.add_data(text)
        self.qr_code.make(fit=True)
        self.create_img()

    def create_img(self, fill_color=None, back_color=None, module_number=0):
        if fill_color is None:
            fill_color = self.fill_color
        if back_color is None:
            back_color = self.back_color
        if module_number not in self.style_dict.keys():
            self.qr_img = self.qr_code.make_image(
                fill_color=fill_color,
                back_color=back_color,
                image_factory=StyledPilImage, 
            ).convert('RGB')
        else:
            self.qr_img = self.qr_code.make_image(
            fill_color=fill_color,
            back_color=back_color,
            image_factory=StyledPilImage, 
            module_drawer=self.style_dict[module_number]
        ).convert('RGB')
    
    def read_logo(self, logo_path):
        logo = Image.open(logo_path)
        wpercent = (self.basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((self.basewidth, hsize), Image.LANCZOS)
        return logo
    
    def add_logo(self, logo):
        if self.qr_img is not None:
            pos = (
                (self.qr_img.size[0] - logo.size[0]) // 2, 
                (self.qr_img.size[1] - logo.size[1]) // 2
                )
            self.qr_img.paste(logo, pos)
            # self.qr_img.save(format='PNG')
        else:
            pass

    def generate_image(self, file_name='qr_image.png'):
        self.qr_img.save(file_name)

    def after_image_processing(self, format='b64'):
        img_byte_arr = io.BytesIO()
        self.qr_img.save(img_byte_arr, format='PNG')
        if format == 'b64':
            img_byte_arr = base64.b64encode(img_byte_arr.getvalue()).decode()
        return img_byte_arr


    

    