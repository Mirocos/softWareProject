from PIL import Image
import os

list = os.listdir("./face_catimage")
print(list)

for image in list:
    id_tag = image.find(".")
    name=image[0:id_tag]
    print(name)

    im=Image.open("./face_catimage/"+image)
    out = im.resize((128, 128))
    #out.show()
    out.save("./resize_catimage/"+name+".jpg")

