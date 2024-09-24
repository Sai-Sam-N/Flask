from flask import Flask, render_template, Response
import cv2

app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    #Frames should be read continuously
    while True:
        #Read the frame
        success, frame = camera.read() #success-boolean variable
        if not success:
            break
        else:
            detector = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
            eye_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
            faces = detector.detectMultiScale(frame, 1.1, 7)
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Converts the colored image into greyscale

            # draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
            
            # if we are getting the frame, we will encode it
            ret, buffer = cv2.imencode('.jpg',frame) #encodes an image into a memory buffer
            # this buffer can be parsed into an image source
            # usually when we are parsing from backend to frontend in the form of buffer it will be able to capture and display it in a proper way

            # (2) Convert this buffer back to bytes
            frame = buffer.tobytes()

            # (3) Return the entire frame - if explicitly done, it captures one or two frames and returns it here
        # return frame # will just return one frame. But we need other frames, as in the frame has to be returned and keep continuing returning without ending function execution
        yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') # usually used with a generator; after returning a frame, it would come back, fetch the next frame and return the frame again
        # whenever images are in the form of bytes, we gotta set it up with Content-Type as specified above
             

@app.route('/')
def index():
    return render_template('index_cv2.html')

@app.route('/video')
def video():
    # Provide the frames we get from the webcam and give it back to the index_cv2.html
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame') 
    #func() takes frames from webcam and pass the entire response to index_cv2.html

if __name__ == '__main__':
    app.run(debug=True)