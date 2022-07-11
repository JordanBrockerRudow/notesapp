from django.core.management.base import BaseCommand
from PIL import Image

class ConvertImage():
    icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (255, 255)]
    
    def __init__(self, filename):
        self.filename = filename
        self.ico_name = filename.split('.')[0] + '.ico'
        self.img = Image.open(filename)

    def create_favicon(self):
        self.img.save('favicon.ico', sizes=[(16, 16)])
        return 'Success! Favicon created.'

    def create_icon(self):
        #img = Image.open(self.filename)
        self.img.save(self.ico_name, sizes=self.icon_sizes)
        return 'Success! Icon created.'



class Command(BaseCommand):
    help = 'Converts PNG to ICO'

    def add_arguments(self, parser):
        parser.add_argument('name', action='store', help='Name of PNG file to convert')
        parser.add_argument('-f', '--favicon', type=bool, help='Save as favicon')

  
    def handle(self, *args, **kwargs):
        f = kwargs['favicon']
        if not f:
            f = False


