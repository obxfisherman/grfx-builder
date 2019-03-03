import sys
from PIL import Image
from os import listdir

def build_image(input_dir, ouput_file):
    new_im = Image.new('RGBA', (512,512)) 
    temp=listdir(input_dir)
    temp.sort()
    h=0
    v=0
    for imagename in temp:
        print('{}/{}'.format(input_dir, imagename))
        im = Image.open('{}\\{}'.format(input_dir, imagename))
        new_im.paste(im,(h,v))
        h+=32
        if h>255:
            h=0
            v+=32
    new_im.save(ouput_file)


build_image('wall', 'grfx_wall.png')
build_image('actors', 'grfx_actors.png')
build_image('floor','grfx_floor.png')
build_image('objects','grfx_obj.png')