# ⌨️ AutoTyper — Digitação Automatizada

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)
![Library](https://img.shields.io/badge/Biblioteca-pynput-green)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

Automação desenvolvida em Python para simular a digitação humana caractere por caractere em qualquer campo de texto do sistema operacional ou navegador. Diferente de automações baseadas em área de transferência (`Ctrl + V`), este projeto emite eventos reais de teclado, garantindo compatibilidade total com acentuação em português e aplicações que bloqueiam a colagem de texto.

---

## ✨ Funcionalidades

- **Emulação Nativa de Teclado:** Utiliza a biblioteca `pynput` para enviar sinais diretos de pressionamento de teclas ao sistema operacional.
- **Cadência Humana:** Aplica intervalos de tempo aleatórios entre cada caractere digitado, reproduzindo o ritmo natural de uma pessoa.
- **Suporte Completo a UTF-8:** Digita acentos, cedilhas e pontuações sem falhas de codificação.
- **Temporizador de Segurança:** Contagem regressiva de 5 segundos antes do início da execução para posicionamento seguro do cursor.

---

## 📁 Estrutura do Projeto

```text
├── main.py              # Script principal de automação
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação
```

---

## ⚙️ Pré-requisitos

- **Python 3.7** ou superior instalado na máquina.
- Gerenciador de pacotes **pip**.

---

## 🚀 Instalação

1. Acesse a pasta do projeto pelo terminal:
   ```bash
   cd caminho/para/seu-projeto
   ```

2. Instale as dependências listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
   *(Caso o comando `pip` não seja reconhecido no Windows, utilize `python -m pip install -r requirements.txt`)*

---

## 💻 Como Usar

1. Abra o arquivo `main.py` e insira o conteúdo desejado dentro da variável `texto`.
2. Salve o arquivo (`Ctrl + S`).
3. Execute o script no terminal:
   ```bash
   python main.py
   ```
4. Durante a contagem regressiva de **5 segundos**, clique no campo de texto de destino (navegador, editor de código ou documento) e aguarde a conclusão da digitação.

---

## 🛠️ Personalização

Você pode ajustar o comportamento da digitação diretamente no arquivo `main.py`:

- **Velocidade de digitação:** Altere os valores mínimo e máximo (em segundos) na linha:
  ```python
  time.sleep(random.uniform(0.03, 0.07))
  ```
  *Valores menores aumentam a velocidade; valores maiores tornam a digitação mais lenta.*

- **Tempo de espera inicial:** Altere o primeiro parâmetro do `range()` para aumentar ou diminuir a contagem regressiva:
  ```python
  for i in range(5, 0, -1):
  ```

---

## ⚠️ Aviso de Uso

Esta ferramenta foi desenvolvida para fins de produtividade, demonstrações em vídeo, testes de interface e acessibilidade. Utilize-a de forma ética e em conformidade com os termos de uso das plataformas em que for aplicada.