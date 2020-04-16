import face_recognition
import os
from PIL import Image,ImageDraw,ImageFont

path = 'path/unknown faces'
save_images = 'path/detected faces'

#faces
elon_musk = face_recognition.load_image_file('images face/elon musk.jpg')
elon_musk_encode = face_recognition.face_encodings(elon_musk)[0]
jeff_bezos = face_recognition.load_image_file("images face/jeff bezos.jpg")
jeff_bezos_encode = face_recognition.face_encodings(jeff_bezos)[0]

known_face_encoding = [
    elon_musk_encode,
    jeff_bezos_encode,
]

known_face_names = [
    'Elon Musk',
    'Jeff Bezos',
]

images_save = []
for img in os.listdir(path):
    images_save.append(path + "/" + img)
num = 1
images_count = 0
for i in range(len(images_save)):
    print("Processing image")
    test_image = face_recognition.load_image_file(images_save[i])
    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image,face_locations)
    pil_image = Image.fromarray(test_image)
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
        font = ImageFont.truetype('arial.ttf',size=50)
        draw.text((left + 6 , bottom - text_height - 5),name,fill=('white'),font=font)
    del draw

    #image show
    # pil_image.show()
    rename = 'image'
    pil_image.save(os.path.join(save_images,rename + str(num)) + '.JPG', 'JPEG')
    num += 1
    images_count += 1
    print("Completed!")
    print("No of images processed and finished %d"%(images_count))
    
