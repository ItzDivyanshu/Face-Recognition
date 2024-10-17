import face_recognition

picture_of_me = face_recognition.load_image_file(r"C:\Users\Dell\Downloads\project\obama1.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]



unknown_picture = face_recognition.load_image_file(r"C:\Users\Dell\Downloads\project\robert2.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

#unknown_picture = face_recognition.load_image_file(r"C:\Users\Dell\Downloads\project\obama1.jpg")
#unknown_face_encoding = face_recognition.face_encodings(picture_of_me)[0]



results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("The faces match")
else:
    print("The faces does not match")