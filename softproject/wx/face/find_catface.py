from PIL import Image
import cv2
import os
#print("h")

face_model = cv2.CascadeClassifier('C:/Users/Administrator/Desktop/cat/haarcascade_frontalcatface.xml')


def find_and_save_face(web_file, face_file):
    # Load the jpg file into a numpy array

    image = cv2.imread(web_file)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    face_locations = face_model.detectMultiScale(gray)
    print(image.dtype)
    # Find all the faces in the image
    #face_locations = face_recognition.face_locations(image)

    print("I found {} face(s) in this photograph.".format(len(face_locations)))

    for (x, y, w, h) in face_locations:

        # Print the location of each face in this image
        # top, right, bottom, left = face_location
        # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # You can access the actual face itself like this:
        face_image = image[y: y + h, x: x + w]
        #cv2.imshow(face_image)
        pil_image = Image.fromarray(cv2.cvtColor(face_image, cv2.COLOR_BGRA2RGB))
        pil_image.save(face_file)
list = os.listdir("web_catimage/")
print(list)

for image in list:
    id_tag = image.find(".")
    name=image[0:id_tag]
    print(name)

    web_file = "./web_catimage/" +image
    face_file="./face_catimage/"+name+".jpg"

    im=Image.open("./web_catimage/"+image)
    try:
        result = find_and_save_face(web_file,face_file)
    except:
        print("fail")