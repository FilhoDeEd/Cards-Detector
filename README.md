# Detector de Cartas

## Sistema de Detecção de Cartas de Baralho com OpenCV

Este projeto utiliza **OpenCV** para detectar a cor e o número de uma carta de baralho padrão (52 cartas) capturada em tempo real por uma webcam. Ele identifica se a carta é vermelha ou preta e estima o número com base na contagem de símbolos visíveis. A detecção, entretanto, é limitada às cartas de Ás a 10; cartas com figuras como valete, dama e rei não são identificadas, já que o método se baseia na contagem dos símbolos na carta. O Ás de espadas, por exemplo, comumente possui uma imagem decorativa que também dificulta uma identificação precisa.

## Instalação

### Pré-requisitos

- **Python 3.7+**
- **OpenCV (cv2)**

### Passos para Instalar

1. **Instalar o Python no Windows**
   - Baixe o Python no site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Durante a instalação, marque a opção "Add Python to PATH".
   - Após a instalação, abra o terminal (Prompt de Comando) e verifique a instalação digitando:
     ```bash
     python --version
     ```

2. **Instalar o OpenCV**
   - No terminal, execute o seguinte comando:
     ```bash
     pip install opencv-python
     ```

## Como Usar

Clone este repositório e execute o script de detecção com uma webcam conectada para iniciar o processo de reconhecimento de cartas.

## Estrutura do Código

1. **Definição do Filtro e Máscara**
   - Configura um filtro HSV para detectar a cor vermelha.
   - Cria uma máscara retangular para delimitar a área de interesse da carta.

2. **Configuração da Webcam**
   - A webcam é inicializada e configurada para capturar imagens em uma resolução de 1280x720.
   - Se não for possível abrir a câmera, o script exibe uma mensagem de erro e encerra o programa.

3. **Processamento de Imagem**
   - O código captura a imagem da câmera e processa cada frame para identificar a cor e o número da carta:
     - **Detectar Cor**: Verifica se a carta é vermelha ou preta.
     - **Contar Símbolos**: Utiliza SimpleBlobDetector para contar o número de símbolos do naipe presentes na carta, permitindo identificar seu valor.

4. **Exibição da Imagem Processada**
   - Exibe a imagem com os resultados sobrepostos (número e cor da carta) em uma janela de visualização.

5. **Encerramento**
   - Pressione a tecla 'q' para encerrar a captura e fechar a janela.
