import json
from base64 import b64encode as enc64
from base64 import b64decode as denc64


def binary_pict(pict):
    with open(pict, 'rb') as f:
        binary = enc64(f.read())
    print(binary)


    with open('data.text', 'w') as outfile:
        outfile.write(str(binary))


# def binary_image(binary):
#     image = denc64(binary)
pict = '45.jpg'
binary_pict(pict)
