from tkinter import *


class JogoDamas:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo de Damas")

        self.tabuleiro = [["" for _ in range(8)] for _ in range(8)]
        self.turno = 1
        self.peca_selecionada = None

        self.criar_tabuleiro()

        self.lbl_status = Label(master, text="Vez do jogador 1")
        self.lbl_status.grid(row=8, columnspan=8)

    def criar_tabuleiro(self):
        for i in range(8):
            for j in range(8):
                cor = "white" if (i + j) % 2 == 0 else "black"
                self.tabuleiro[i][j] = Button(self.master, bg=cor, width=5, height=2,
                                              command=lambda i=i, j=j: self.clicar_peca(i, j))
                self.tabuleiro[i][j].grid(row=i, column=j)

        # Posicionar as peças iniciais
        for i in range(0, 3):
            for j in range(8):
                if (i + j) % 2 != 0:
                    self.tabuleiro[i][j].config(text="O", fg="red", font=("Helvetica", 20))

        for i in range(5, 8):
            for j in range(8):
                if (i + j) % 2 != 0:
                    self.tabuleiro[i][j].config(text="X", fg="black", font=("Helvetica", 20))

    def clicar_peca(self, i, j):
        peca = self.tabuleiro[i][j]

        if self.peca_selecionada is None:
            if peca.cget("text") != "":
                if (self.turno == 1 and peca.cget("text") == "O") or (self.turno == 2 and peca.cget("text") == "X"):
                    peca.config(relief=SUNKEN)
                    self.peca_selecionada = (i, j)
        else:
            peca_selecionada_i, peca_selecionada_j = self.peca_selecionada

            if (i + j) % 2 != 0 and peca.cget("text") == "":
                self.tabuleiro[peca_selecionada_i][peca_selecionada_j].config(text="")
                peca.config(text="O" if self.turno == 1 else "X", fg="red" if self.turno == 1 else "black",
                            font=("Helvetica", 20))
                self.peca_selecionada = None
                self.tabuleiro[peca_selecionada_i][peca_selecionada_j].config(relief=RAISED)
                self.turno = 2 if self.turno == 1 else 1
                self.lbl_status.config(text=f"Vez do jogador {self.turno}")
            else:
                self.tabuleiro[peca_selecionada_i][peca_selecionada_j].config(relief=RAISED)
                self.peca_selecionada = None


root = Tk()
jogo = JogoDamas(root)
root.mainloop()
