# ⚡ MacroPHE

O **MacroPHE** é um Auto Clicker ultra rápido, leve e configurável desenvolvido em Python com interface gráfica (Tkinter). Ele foi projetado especificamente para sistemas **Linux** (como Fedora, Ubuntu e Linux Mint), garantindo total compatibilidade mesmo sob o servidor gráfico **Wayland**.

---

## ✨ Funcionalidades

* 🎛️ **Interface Simples:** Configure tudo de forma totalmente visual.
* 🕒 **Contagem Regressiva:** Delay de 3 segundos antes de iniciar os cliques para dar tempo de você posicionar o mouse no alvo correto.
* 🚀 **Velocidade Extrema:** Suporta intervalos de milissegundos para cliques massivos.
* 🛑 **Botão de Pânico (ESC):** Interrupção imediata dos cliques pressionando a tecla `Esc` no teclado por motivos de segurança.
* 🧵 **Segurança de Interface:** Roda o macro em segundo plano (*threading*), impedindo que a janelinha congele ou trave o sistema enquanto executa.

---

## 🚀 Como Usar o Executável (Sem instalar nada)

Você pode baixar a versão pronta para uso diretamente na aba de [Releases](https://github.com).

Após baixar o arquivo `MacroPHE-v1.0.0-linux-x64`, abra o seu terminal e execute os comandos abaixo para dar permissão e rodar o programa:

```bash
# 1. Dê permissão de execução ao binário
chmod +x MacroPHE-v1.0.0-linux-x64

# 2. Inicie o programa
./MacroPHE-v1.0.0-linux-x64
```

---

## 🛠️ Como Executar a partir do Código Fonte

Se preferir rodar ou modificar o código direto pelo script Python, siga os passos abaixo no seu Linux (exemplo baseado no Fedora):

### 1. Instalar as dependências do sistema
```bash
sudo dnf install python3-tkinter python3-devel python3-evdev
```

### 2. Instalar a biblioteca de simulação do mouse
```bash
pip install pynput
```

### 3. Rodar o programa
```bash
python3 Program.py
```

---

## 📝 Configurações Recomendadas

* **Quantidade de cliques:** Quantas vezes o mouse vai clicar.
* **Intervalo entre cliques:** O tempo de espera entre um clique e outro. 
  * Para **velocidade máxima**, configure como `0.001` ou até mesmo `0.0` (velocidade máxima permitida pelo processador).

---

## ⚖️ Licença

Este projeto está sob a licença MIT. Sinta-se livre para clonar, modificar e distribuir.
