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