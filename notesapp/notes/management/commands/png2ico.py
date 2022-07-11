from distutils.log import error
from django.core.management.base import BaseCommand
from PIL import Image
import os
from notesapp.settings import BASE_DIR

class ConvertImage():
    icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (255, 255)]
    
    def __init__(self, filename):
        self.ico_name = os.path.normpath((filename.split('.')[0] + '.ico'))
        self.img = Image.open(os.path.normpath(filename))

    def create_favicon(self):
        self.img.save(self.ico_name, sizes=[(16, 16)])

    def create_icon(self):
        #img = Image.open(self.filename)
        self.img.save(self.ico_name, sizes=self.icon_sizes)



class Command(BaseCommand):
    help = 'Converts PNG to ICO'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str, help='Name of PNG file to convert')
        parser.add_argument('--favicon', action='store_true', help='Convert to favicon. Only saves size (16x16).')

  
    def handle(self, *args, **options):
        for name in options['filename']:
            try:
                name = str(BASE_DIR) + '/' + name
                filepath = os.path.normpath(name)
                convert = ConvertImage(filename=name)
                if options['favicon']:
                    convert.create_favicon()
                    self.stdout.write(self.style.SUCCESS('Success! Favicon created.'))
                else:
                    convert.create_icon()
                    self.stdout.write(self.style.SUCCESS('Success! Icon created.'))

            except Exception as e:
                print('ERROR!')
                print('Current Directory: ', os.getcwd())
                print('Base Directory: ', BASE_DIR)
                print(e)
        

