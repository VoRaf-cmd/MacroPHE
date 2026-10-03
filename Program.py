import time
import tkinter as tk
from tkinter import messagebox
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key

# Inicializa controladores do mouse e do teclado
mouse = Controller()
interromper_macro = False

def monitorar_teclado():
    """Escuta o teclado em segundo plano para parar o macro caso o Esc seja pressionado."""
    global interromper_macro
    def ao_pressionar(tecla):
        global interromper_macro
        if tecla == Key.esc:
            interromper_macro = True
            return False  # Encerra o listener

    with Listener(on_press=ao_pressionar) as listener:
        listener.join()

def rotina_cliques(quantidade, delay):
    global interromper_macro
    interromper_macro = False

    # Inicia o monitor de teclado para o botão de emergência (Esc)
    threading.Thread(target=monitorar_teclado, daemon=True).start()

    try:
        # Contagem regressiva para você posicionar o mouse no alvo
        for i in range(3, 0, -1):
            label_status.config(text=f"Começando em {i} segundos...\nPosicione o mouse no alvo!")
            janela.update()
            time.sleep(1)

        label_status.config(text="🔥 Clicando... Pressione ESC para parar!")
        janela.update()

        cliques_feitos = 0
        for _ in range(quantidade):
            if interromper_macro:
                label_status.config(text="❌ Interrompido pelo usuário!")
                break

            mouse.click(Button.left, 1)
            cliques_feitos += 1

            # Se o delay for muito baixo (ex: 0.001), ele clica na velocidade máxima permitida pelo sistema
            if delay > 0:
                time.sleep(delay)

        if not interromper_macro:
            label_status.config(text=f"Concluído! {cliques_feitos} cliques feitos.")
            messagebox.showinfo("Sucesso", f"O macro realizou {cliques_feitos} cliques!")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
        label_status.config(text="Status: Aguardando")
    finally:
        btn_executar.config(state=tk.NORMAL)

def disparar_macro():
    try:
        quantidade = int(entry_quantidade.get())
        delay = float(entry_delay.get())
    except ValueError:
        messagebox.showwarning("Aviso", "A quantidade e o intervalo devem ser números válidos!")
        return

    # Desativa o botão para evitar cliques duplos na interface
    btn_executar.config(state=tk.DISABLED)

    # Executa em uma Thread separada para não travar a interface
    threading.Thread(target=rotina_cliques, args=(quantidade, delay), daemon=True).start()

# --- INTERFACE GRÁFICA ---
janela = tk.Tk()
janela.title("Auto Clicker Fedora")
janela.geometry("380x300")
janela.resizable(False, False)

tk.Label(janela, text="⚡ Auto Clicker Ultra Rápido", font=("Arial", 14, "bold"), fg="#0066CC").pack(pady=15)

# Campo 1: Quantidade de cliques
tk.Label(janela, text="Quantidade de cliques:", font=("Arial", 10, "bold")).pack(pady=(5, 2))
entry_quantidade = tk.Entry(janela, width=15, justify="center")
entry_quantidade.pack()
entry_quantidade.insert(0, "100")

# Campo 2: Delay/Intervalo entre cliques
tk.Label(janela, text="Intervalo entre cliques (em segundos):\n(Use 0.001 para velocidade máxima)", font=("Arial", 10, "bold")).pack(pady=(15, 2))
entry_delay = tk.Entry(janela, width=15, justify="center")
entry_delay.pack()
entry_delay.insert(0, "0.01")

# Botão de Disparo
btn_executar = tk.Button(
    janela, text="Iniciar Cliques", command=disparar_macro,
    bg="#0066CC", fg="white", font=("Arial", 11, "bold"), padx=20, pady=5
)
btn_executar.pack(pady=20)

# Mensagem de Status e Instrução de Emergência
label_status = tk.Label(janela, text="Status: Aguardando comando", font=("Arial", 10, "italic"), fg="gray")
label_status.pack()

janela.mainloop()
