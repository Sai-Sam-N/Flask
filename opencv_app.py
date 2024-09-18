from flask import Flask, render_template, Response
import cv2

app=Flask(__name__)
camera=cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index_cv2.html')

@app.route('/video')
def video():
    # Provide the frames we get from the webcam and give it back to the index_cv2.html
    pass