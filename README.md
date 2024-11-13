# projeto1-PDIC8


Sistema de Detecção de Cartas de Baralho com OpenCV

Este projeto utiliza OpenCV para detectar a cor e o número de uma carta de baralho padrão (52 cartas) capturada em tempo real através de uma webcam. Ele identifica se a carta é vermelha ou preta e estima o número da carta com base na contagem de símbolos visíveis (2-10, J, Q, K, A).
Instalação
Pré-requisitos

    Python 3.7+
    OpenCV (cv2)

Passos para Instalar

    Instalar o Python no Windows
        Baixe o Python no site oficial: https://www.python.org/downloads/
        Ao instalar, marque a opção "Add Python to PATH".
        Após a instalação, abra o terminal (Prompt de Comando) e digite python --version para verificar.

    Instalar o OpenCV
        No terminal, execute:
            pip install opencv-python

Como Usar

Clone este repositório e execute o script de detecção com uma webcam conectada.

Estrutura do Código

    1. Definição do Filtro e Máscara
        Configura um filtro HSV para detectar a cor vermelha.
        Cria uma máscara retangular para delimitar a área de interesse da carta.

    2. Configuração da Webcam
        A webcam é inicializada e configurada para capturar imagens em uma resolução de 1280x720.
        Se não for possível abrir a câmera, o script exibe um erro e encerra.

    3. Processamento de Imagem
        O código captura a imagem da câmera e processa cada frame para identificar a cor e o número da carta:
            Detectar Cor: Verifica se a carta é vermelha ou preta.
            Contar Símbolos: Utiliza SimpleBlobDetector para contar os símbolos (números e figuras) e identificar o número da carta.

    4. Exibição da Imagem Processada
        Exibe a imagem com os resultados sobrepostos (cor e número da carta) em uma janela de visualização.

    5. Encerramento
        Pressione a tecla 'q' para encerrar a captura e fechar a janela.

