# Prova-2-M6-Inteli

Desenvolva um código em Python capaz de utilizar o openCV para a leitura de um vídeo (frame a frame) e, para cada frame, o seu código deve identificar e marcar na imagem os retângulos correspondentes a cada uma das faces encontradas. Ao final do código, um novo vídeo deve ser salvo com as faces identificadas.

Um repositório com exemplos relevantes e o arquivo de vídeo que deve ser utilizado pode ser encontrado em: [https://github.com/rmnicola/p2-pratica](https://github.com/rmnicola/p2-pratica)

O programa deve ser entregue em um repositório do github contendo uma explicação da implementação no arquivo README.md, além do script Python utilizado e o vídeo gravado com as faces identificadas.

## Demonstração do resultado

https://github.com/Lemos1347/Prova-2-M6-Inteli/assets/99190347/c19d409a-2be7-4aa4-a102-39c437606a32

## Explicação

Foi desenvolvido duas versões para essa atividade. Uma delas foi com o algoritmo do OpenCV chamado haarcascades e outra com o Yolov8. Isso aconteceu pois o Yolov8 detecta uma pessoa/face melhor que o haarcascades, porém o haarcascades detecta efetivamente uma face, então por via das dúvidas, ambos estão disponíveis nesse repositório:

- [Com o Yolov8](/with_yolov8.py)
- [Com o haarcascades](/with_haarcascades.py)

### Yolov8

Para a criação dessa resolução, primeiro realizo a instalação do modelo do [Yolov8](https://github.com/ultralytics/ultralytics). Com isso, agora temos o modelo padrão na raíz do projeto: [yolov8n.pt](/yolov8n.pt).

No arquivo [main.py](/main.py), realizo a importação das bibliotecas necessárias, especialmente a classe Yolo. Com essa classe, consigo agora criar um objeto que tenha como base o modelo padrão de predição do Yolov8.

O vídeo requisitado no enunciado para utilizarmos pode ser encontrado em: [/videos/arsene.mp4](/videos/arsene.mp4)

Agora então, utilizamos o OpenCV para carregar o vídeo em uma variável. Em seguida, utilizamos o OpenCV também para criar um objeto de vídeo responsável por criar um novo vídeo com os frames resultantes da predição do Yolov8.

Com tudo configurado, é criado um "while loop" responsável por armazenar cada frame do vídeo em uma variável (esse frame é capturado utilizando o OpenCV) e "alimentar" o modelo com esse frame. E então, o resultado é a predição do frame, o qual é armazenado na variável responsável por criar o novo vídeo. Esse loop acontece até que não é possível mais "extrair" um frame do vídeo. Ao final, finalizamos a criação do novo vídeo e a salvamos nessa [pasta](/videos/result/yolov8/)

### Haarcascades

Com esse algoritmo, ao invés de baixarmos um modelo externo, apenas o importamos da própria biblioteca do OpenCV. Foi necessário também a criação de uma função que realiza a transformação dos frames para tons de cinza e o desenho de um elipse no local que o algoritmo identificou como sendo uma face. Esse função que é utilizada a cada frame no `while loop`. O processo de carregar e salvar os vídeos aconteceu da mesma maneira que explicado na versão com o Yolov8, apenas em uma pasta diferente, nessa [aqui](/videos/result/haarcascades/).

### Observações

- As dimensões do vídeo de resultado é mantido a mesma do vídeo original
- O fps do vídeo resultado é de 24.
- Caso deseja rodar o projeto, basta baixar as bibliotecas em `requirements.txt`:

```shell
pip install -r requirements.txt
```
