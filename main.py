import face_recognition
import os
import cv2
from PIL import Image,ImageDraw,ImageFont

image_elon_musk = face_recognition.load_image_file('images face/elon musk.jpg')
elon_musk_encode = face_recognition.face_encodings(image_elon_musk)[0]
image_sundar_pichai = face_recognition.load_image_file('images face/sundar pichai.jpg')
sundar_pichai_encode = face_recognition.face_encodings(image_sundar_pichai)[0]
padma_img = face_recognition.load_image_file('images face/naveen.jpg')
padma_encode = face_recognition.face_encodings(padma_img)[0]

#array of encodings
known_face_encoding = [
    elon_musk_encode,
    sundar_pichai_encode,
    padma_encode
]

known_face_names = [
    'Elon musk',
    'Sundar Pichai',
    'Naveen'
]

#test images
test_image = face_recognition.load_image_file('unknown faces/IMG_20200114_135325.jpg')
#Find face in images
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image,face_locations)

#convert pil image
pil_image = Image.fromarray(test_image)


#create image draw instances
draw = ImageDraw.Draw(pil_image)

#loop through faces
for (top,right,bottom,left), face_encodings in zip(face_locations,face_encodings):
    matches = face_recognition.compare_faces(known_face_encoding,face_encodings)

    name = 'Unknown Person'
    #if match
    if True in matches:
        face_match_index = matches.index(True) 
        name = known_face_names[face_match_index]

    #draw box
    draw.rectangle(((left,top),(right,bottom)),outline=('red'))
    #draw label
    text_width,text_height = draw.textsize(name)
    # draw.rectangle(((left,bottom - text_height -10),(right,bottom)),fill=(0,0,0),outline=(0,0,0))
    font = ImageFont.truetype('arial.ttf',size=60)
    draw.text((left + 6 , bottom - text_height - 5),name,fill=('white'),font=font)

del draw

#image show
pil_image.show()
