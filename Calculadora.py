from tkinter import *

janela = Tk()

janela.title('Calculadora')

def enviarNumeroPara(char):

    global CalculoOperacoes

    CalculoOperacoes += str(char)
    textoDeEntrada.set(CalculoOperacoes)

def deletarNumero():

    global CalculoOperacoes

    textoSemUltimoDigito = CalculoOperacoes[:-1]
    CalculoOperacoes = textoSemUltimoDigito
    textoDeEntrada.set(CalculoOperacoes)

def LimparTudo():

    global CalculoOperacoes

    CalculoOperacoes = ""
    textoDeEntrada.set(CalculoOperacoes)

def funcaoIgual():

    global CalculoOperacoes

    resultadoCalculo = str(eval(CalculoOperacoes))
    textoDeEntrada.set(resultadoCalculo)

    CalculoOperacoes = resultadoCalculo

CalculoOperacoes = ""
textoDeEntrada = StringVar()

textoExibirOperacaoResultado = Entry(janela, font=("Arial 20 bold"),
                                     textvariable=textoDeEntrada,
                                     border=5,
                                     bg="#BBB",
                                     fg="black",
                                     ).grid(row=1, columnspan=5, padx=10, pady=10)

botaoNumero0 = Button(janela,
                      text="0",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara("0")).grid(row=5, column=0, sticky="NSEW")

botaoNumero1 = Button(janela,
                      text="1",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara("1")).grid(row=4, column=0, sticky="NSEW")

botaoNumero2 = Button(janela,
                      text="2",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara("2")).grid(row=4, column=1, sticky="NSEW")

botaoNumero3 = Button(janela,
                      text="3",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara("3")).grid(row=4, column=2, sticky="NSEW")

botaoNumero4 = Button(janela,
                      text="4",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara("4")).grid(row=3, column=0, sticky="NSEW")

botaoNumero5 = Button(janela,
                      text="5",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara("5")).grid(row=3, column=1, sticky="NSEW")

botaoNumero6 = Button(janela,
                      text="6",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara("6")).grid(row=3, column=2, sticky="NSEW")

botaoNumero7 = Button(janela,
                      text="7",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara("7")).grid(row=2, column=0, sticky="NSEW")

botaoNumero8 = Button(janela,
                      text="8",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara("8")).grid(row=2, column=1, sticky="NSEW")

botaoNumero9 = Button(janela,
                      text="9",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara("9")).grid(row=2, column=2, sticky="NSEW")

botaoPonto = Button(janela,
                      text=".",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara(".")).grid(row=5, column=1, sticky="NSEW")

botaoAdicao = Button(janela,
                      text="+",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara("+")).grid(row=4, column=3, sticky="NSEW")

botaoSubtracao = Button(janela,
                      text="-",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara("-")).grid(row=4, column=4, sticky="NSEW")

botaoMultiplicacao = Button(janela,
                      text="*",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara("*")).grid(row=3, column=3, sticky="NSEW")

botaoDivisao = Button(janela,
                      text="/",
                      border=5,
                      bg="#BBB",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= lambda:enviarNumeroPara("/")).grid(row=3, column=4, sticky="NSEW")

botaoNumeroDelete = Button(janela,
                      text="DEL",
                      border=5,
                      bg="#f7a541",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= deletarNumero).grid(row=2, column=3, sticky="NSEW")

botaoNumeroLimpar = Button(janela,
                      text="ACL",
                      border=5,
                      bg="#f45d4c",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= LimparTudo).grid(row=2, column=4, sticky="NSEW")

botaoIgual = Button(janela,
                      text="=",
                      border=5,
                      bg="#a1dbb2",
                      fg="black",
                      font=("Arial 20 bold"),
                      command= funcaoIgual).grid(row=5, column=2, columnspan=3, sticky="NSEW")

janela.mainloop()