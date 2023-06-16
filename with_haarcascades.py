import cv2 as cv
import time

# Carregando o haarcascades do OpenCV
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Função de detecção de faces advinda da documentação do OpenCV
def detectFace(frame):
    # Tranformamos a imagem em tons de cinza
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        # Desenhamos um ellipse no local indicado pelo algoritmo do haarcascades
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
    return frame


# Carrengo o vídeo requisitado no enunciado
input_video = cv.VideoCapture('./videos/arsene.mp4')

# Pegando as dimensões do vídeo para estabelecer a mesma para o vídeo de resultado
WIDTH  = int(input_video.get(cv.CAP_PROP_FRAME_WIDTH))
HEIGHT = int(input_video.get(cv.CAP_PROP_FRAME_HEIGHT))

# Agora criamos um objeto responsável por armazenar o vídeo de saída, para isso, precisamos passar as informações necessárias, como dimensão, codec, path onde o arquivo deve ser salvo e o fps.

# Estamos pegando o timestamp em unix para evitar conflitos
timestamp = int(time.time() * 1000)

output_video = cv.VideoWriter( f'./videos/result/haarcascades/arsene_resul_{timestamp}.mp4',cv.VideoWriter_fourcc(*'mp4v'), 24, (WIDTH, HEIGHT))

# Utilizamos um while loop para pegar cada frame e utilizamos o modelo padrão do Yolov8 para realizar as detecções na imagem
while True:
   res, frame = input_video.read()

   # Checamos se ainda existe frame a ser "pego"
   if not res:
      break
   
   # Realizamos a detecção da face utilizando o haarcascade
   result = detectFace(frame=frame)
   # Escrevemos o resultado no objeto vídeo
   output_video.write(result)

# Concluímos a "construção do vídeo de resultado"
output_video.release()