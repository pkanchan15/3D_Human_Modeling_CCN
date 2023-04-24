import streamlit as st
from PIL import Image
import os
import base64
import cv2
import mediapipe as mp
import urllib.request
import numpy as np
import pickle
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation
import PyQt5
from PIL import Image
from IPython.display import Video
import nb_helpers
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
mp_pose = mp.solutions.pose
mp_face_mesh = mp.solutions.face_mesh
poselandmarks_list =mp_holistic.PoseLandmark
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)


def get_in_3d(uploadedfile):
    file="c://users//kanch//desktop//ccn//uploads//"+uploadedfile.name
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        cap = cv2.VideoCapture(file)
        if cap.isOpened() == False:
            print("Error opening video stream or file")
            raise TypeError
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        data = np.empty((3, len(poselandmarks_list), length))   
        lan=[] 
        frame_num = 0
        while cap.isOpened():
            ret, image = cap.read()
            if not ret:
                break
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            results = pose.process(image)
            
            landmarks = results.pose_world_landmarks.landmark
            for i in range(len(mp_pose.PoseLandmark)):
                data[:, i, frame_num] = (landmarks[i].x, landmarks[i].y, landmarks[i].z)  
            
            frame_num += 1
        cap.release()
        
        fig = plt.figure()
        fig.set_size_inches(5, 5, True)
        ax = fig.add_subplot(projection='3d')
    anim = nb_helpers.time_animate(data, fig, ax)
    f = r"c://Users//kanch//Desktop//ccn//result.gif" 
    writergif = animation.PillowWriter(fps=30) 
    anim.save(f,writer=writergif)
    #anim.save('result.mp4', fps=30, extra_args=['-vcodec', 'libx264'], dpi=300)
    read_video(uploadedfile)
    

def save_uploaded_file(uploadedfile):
    with open(os.path.join("uploads", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
        
def read_video(uploadedfile):
    uploaded='c://users//kanch//desktop//ccn//result.gif'
    file_ = open(uploaded, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    video_bytes = uploadedfile.read()
    
    video_layout=f"""
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
       f' <video src="{video_bytes}" style="width: 50%; height: auto; object-fit: contain;" controls></video>"""
    st.components.v1.html(video_layout, width=800, height=600)

# Create uploads folder if it doesn't exist
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Display instructions
if __name__=='__main__':
    st.write("## Upload a video")
    st.write("Supported formats: mp4, mov, avi, mkv")
    st.write("Maximum file size: 500MB")

    # Allow user to upload a file
    uploaded_file = st.file_uploader("", type=["mp4", "mov", "avi", "mkv"])

    if uploaded_file is not None:
        # Save uploaded file
        save_uploaded_file(uploaded_file)
        
        # Display the uploaded video
        
        get_in_3d(uploaded_file)
        
        
