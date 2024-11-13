# Detector de Cartas

## Sistema de Detecção de Cartas de Baralho com OpenCV

Este projeto utiliza **técnicas de processamento de imagens** para detectar a cor e o número de uma carta de baralho padrão (52 cartas) capturada em tempo real por uma webcam. Ele identifica se a carta é vermelha ou preta e estima o número com base na contagem de símbolos visíveis. 

A detecção, entretanto, é limitada às cartas de Ás a 10. **Não identifica**:

- Naipes;
- Ás de Espadas (♠);
- Valetes (J);
- Damas (Q);
- Reis (K)

## Demonstração
![Demonstração usando 9 de paus e Ás de ouros](https://github.com/FilhoDeEd/Cards-Detector/blob/main/assets/demo.gif)

## Instalação

### Pré-requisitos

- **Python 3**
- **OpenCV (cv2)**
- **Baralho ou imagem de uma carta**

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

1. **Clone o Repositório**

```bash
   git clone https://github.com/FilhoDeEd/Cards-Detector.git
```

2. **Execute o código**
- Na pasta do repositório, execute o comando para iniciar a identificação de cartas:
```bash
   python main.py
```

3. **Aproxime a carta desejada no local indicado**

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
   - Exibe o resultado com a cor e numeração da carta.

5. **Encerramento**
   - Pressione a tecla 'q' para encerrar a captura e fechar a janela.

## Autores
- André Lisboa Augusto; 
- Edson Rodrigues da Cruz Filho;
- Marcos Henrique Maimoni Campanella;
- Rodolfo Henrique Raymundo Engelmann;

### Engenharia da Computação - IFSP Piracicaba. Novembro, 2024
