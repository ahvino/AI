#/Users/seliksamai/repos/AI/AI/FacialRecognition


from deepface import DeepFace


face_analysis = DeepFace.analyze(img_path="FacialRecognition/happy_face.jpeg")
print(face_analysis[0]["emotion"])

