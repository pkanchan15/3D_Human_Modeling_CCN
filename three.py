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
file = "C://Users//kanch//Pictures//Camera Roll//WIN_20230407_13_06_46_Pro.mp4"
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    cap = cv2.VideoCapture(file)
    if cap.isOpened() == False:
        print("Error opening video stream or file")
        raise TypeError
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    data = np.empty((3, len(poselandmarks_list), length))    
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
anim.save('result.mp4', fps=30, extra_args=['-vcodec', 'libx264'], dpi=300)