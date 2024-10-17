from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import face_recognition
import cv2
import numpy as np
from detect.models import face_data, face_detect, face_contact


# Create your views here.

def main(request):
    return render(request,'main.html')
def service(request):
    return render(request,'service.html')
def about(request):
    return render(request,'about.html')
def detection(img):


    video_capture = cv2.imread(img, cv2.IMREAD_COLOR)

    # Load a sample picture and learn how to recognize it.
    aryan_image = face_recognition.load_image_file(r"C:\Users\Dell\Downloads\project\aryan.jpg")
    aryan_face_encoding = face_recognition.face_encodings(aryan_image)[0]

    obama_image = face_recognition.load_image_file(r"C:\Users\Dell\Downloads\project\obama1.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

    # # Load a second sample picture and learn how to recognize it.
    virat_image = face_recognition.load_image_file(r"C:\Users\Dell\Downloads\project\virat1_27zBdLP.jpg")
    virat_face_encoding = face_recognition.face_encodings(virat_image)[0]

    swift_image = face_recognition.load_image_file(r"C:\Users\Dell\Downloads\project\swift1.jpg")
    swift_face_encoding = face_recognition.face_encodings(swift_image)[0]

    robert_image = face_recognition.load_image_file(r"C:\Users\Dell\Downloads\project\robert2.jpg")
    robert_face_encoding = face_recognition.face_encodings(robert_image)[0]

    shahrukh_image = face_recognition.load_image_file(r"C:\Users\Dell\Downloads\project\shahrukh2.jpg")
    shahrukh_face_encoding = face_recognition.face_encodings(shahrukh_image)[0]

    # Create arrays of known face encodings and their names
    # rahul_face_encoding
    known_face_encodings = [
        aryan_face_encoding,
        obama_face_encoding,
        virat_face_encoding,
        swift_face_encoding,
        robert_face_encoding,
        shahrukh_face_encoding,
    ]
    known_face_names = [
        "Divyanshu",
        "Obama",
        "Virat",
        "Taylor Swift",
        "Robert Downey jr",
        "Shahrukh Khan"
    ]

    # Initialize some variables
    # Initialize some variables
    # Initialize some variables
    # Initialize some variables
    # Initialize some variables
    # Initialize some variables
    scale_factor = 2  # Increase the frame size by a factor of 2
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        frame = video_capture
        # roi_top = 100
        # roi_bottom = 300
        # roi_left = 100
        # roi_right = 300
        # roi_frame = frame[roi_top:roi_bottom, roi_left:roi_right]
        # resized_frame = cv2.resize(roi_frame, (0, 0), fx=0.5, fy=0.5)
        # cv2.rectangle(frame, (roi_left, roi_top), (roi_right, roi_bottom), (0, 0, 255), 3)

        # Resize the frame for faster processing and larger face detection

        # d_w=1280
        # d_h=720

        # cv2.namedWindow('video',cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('video',d_w,d_h)
        resized_frame = cv2.resize(frame, (0, 0), fx=1 / scale_factor, fy=1 / scale_factor)

        # Only process every other frame of video to save time
        if process_this_frame:
            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_resized_frame)
            face_encodings = face_recognition.face_encodings(rgb_resized_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale up the face locations to the original frame size
            top *= scale_factor
            right *= scale_factor
            bottom *= scale_factor
            left *= scale_factor

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1):
            break

    # Release handle to the webcam

    cv2.destroyAllWindows()
    if len(face_names) != 0:
        name = face_names[0]
        er = ""
    else:
        name = "We could not detect face or the image quality was low"
    return name
#

#     return render(request,'detect.html')
# def mainl(request):
#     return render(request, 'login.html')
@csrf_exempt
def login(request):
    # pic=face_data.objects.all()
    # context={'pic':pic}
    if request.method=='POST':
        user=request.POST.get('uname')
        if len(request.FILES) !=0:
            image=request.FILES['image']
            print(image)
        data=face_data(username=user,image=image)
        data.save()
        #value=models.check.objects.all().values()
    return render(request,'login.html')

@csrf_exempt
def detect(request):
    # pic=face_data.objects.all()
    # context={'pic':pic}
    d={}
    if request.method=='POST':
        if len(request.FILES) !=0:
            img=request.FILES['pic']
            print(img)
            #d={'img':img}
        data=face_detect(pic=img)
        data.save()
        x=detection(f'static/image/{img}')
        d = {'img': img,'name':x}
        #value=models.check.objects.all().values()
        return render(request, 'detect.html',context=d)

    return render(request,'detect.html')

@csrf_exempt
def contact(request):
    # pic=face_data.objects.all()
    # context={'pic':pic}
    if request.method == 'POST':
        cname = request.POST.get('name')
        mail = request.POST.get('mail')
        msg = request.POST.get('msg')
        data = face_contact(name=cname, mail=mail , msg=msg)
        data.save()
        #value=models.check.objects.all().values()
    return render(request,'contact.html')

