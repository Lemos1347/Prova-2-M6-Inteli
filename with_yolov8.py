from ultralytics import YOLO
import cv2 as cv
import time

# Carrengado o modelo padrão do YOLO
model = YOLO('yolov8n.pt')

# Carregando o vídeo em uma variável
input_video = cv.VideoCapture('./videos/arsene.mp4')

# Pegando as dimensões do vídeo para estabelecer a mesma para o vídeo de resultado
WIDTH  = int(input_video.get(cv.CAP_PROP_FRAME_WIDTH))
HEIGHT = int(input_video.get(cv.CAP_PROP_FRAME_HEIGHT))

# Agora criamos um objeto responsável por armazenar o vídeo de saída, para isso, precisamos passar as informações necessárias, como dimensão, codec, path onde o arquivo deve ser salvo e o fps.

# Estamos pegando o timestamp em unix para evitar conflitos
timestamp = int(time.time() * 1000)

output_video = cv.VideoWriter( f'./videos/result/yolov8/arsene_resul_{timestamp}.mp4',cv.VideoWriter_fourcc(*'mp4v'), 24, (WIDTH, HEIGHT))

# Utilizamos um while loop para pegar cada frame e utilizamos o modelo padrão do Yolov8 para realizar as detecções na imagem
while True:
   res, frame = input_video.read()

   # Checamos se ainda existe frame a ser "pego"
   if not res:
      break
   
   # Realizamos a predição do frame com uma confiança mínima de 0.3
   result = model.predict(frame, conf=0.3)
   # Escrevemos o resultado no objeto vídeo
   output_video.write(result[0].plot())

# Concluímos a "construção do vídeo de resultado"
output_video.release()

print("----------AGORA VAMOS REPRODUZIR O RESULTADO----------")
time.sleep(1)
print("Começamos em...")
print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
time.sleep(0.5)

# Carregamos o vídeo resultado salvo
video_resul = cv.VideoCapture(f'./videos/result/yolov8/arsene_resul_{timestamp}.mp4')

# Checa se foi possivel abrir o arquivo
if not video_resul.isOpened():
    print("Error opening video file")
    exit(1)

# Loop para lermos frame por frame
while True:
    # Leitura de um frame
    ret, frame = video_resul.read()

    # Interrompemos o programa caso não haja mais frames
    if not ret:
        break

    # Exibe o frame
    cv.imshow('Video Playback', frame)

    # Se o usuario apertar q, encerra o playback
    # Definimos o fps da reprodução no valor informado no "waitKey"
    if cv.waitKey(24) == ord('q'):
      break
    
# Fechamos a reprodução e encerramos o programa
video_resul.release()
cv.destroyAllWindows()