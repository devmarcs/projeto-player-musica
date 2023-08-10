# ----Importando o TKinter----
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
import os



cor0 = "#f0f3f5" #cinza
cor1 = "#feffff" #branca
cor2 = "#3fb5a3" #verde
cor3 = "#2e2d2c" #preta / black
cor4 = "#403d3d" #preta / black
cor5 = "#4a88e8" #azul / blue


# ----Criando janela----
janela = Tk ()
janela.title("")
janela.geometry('352x255')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

# ----Criando os frames----

frame_esquerda = Frame(janela, width=150, height=150, bg=cor3)
frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_direita = Frame(janela, width=250, height=150, bg=cor3)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

frame_inferior = Frame(janela, width=404, height=100, bg=cor3)
frame_inferior.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=NSEW)


# ----Criando funções----
def play_musica():
    tocando = listbox.get(ACTIVE)
    l_rodando['text'] = tocando
    mixer.music.load(tocando)
    mixer.music.play()


def pusar_musica():
    mixer.music.pause()


def continuar_musica():
    mixer.music.unpause()


def parar_musica():
    mixer.music.stop()

def prox_musica():
    reproduzindo = l_rodando['text']
    index = musicas.index(reproduzindo)
    novo_index = index + 1
    reproduzindo = musicas[novo_index]
    mixer.music.load(reproduzindo)
    mixer.music.play()

    # ----Deletando os elemento da playlist----
    listbox.delete(0,END)

    mostrar()

    listbox.select_set(novo_index)
    listbox.configure(selectmode=SINGLE)
    l_rodando['text'] = reproduzindo


def volta_musica():
    reproduzindo = l_rodando['text']
    index = musicas.index(reproduzindo)
    novo_index = index - 1
    reproduzindo = musicas[novo_index]
    mixer.music.load(reproduzindo)
    mixer.music.play()

    # ----Deletando os elemento da playlist----
    listbox.delete(0,END)

    mostrar()

    listbox.select_set(novo_index)
    listbox.configure(selectmode=SINGLE)
    l_rodando['text'] = reproduzindo




# ----Configurando o frame esquerdo----
img_musica = Image.open('projeto-player-musica/images/music.png')
img_musica = img_musica.resize((100, 100))
img_musica = ImageTk.PhotoImage(img_musica)

l_logo = Label(frame_esquerda, height=130, image=img_musica, compound=LEFT, padx=10, anchor='nw', font=('ivy 16 bold'), background=cor3, fg=cor3)
l_logo.place(x=39, y=30)


# ----Configurando o frame direito----


listbox = Listbox(frame_direita, width=22, height=10, selectmode=SINGLE, font=('arial 9 bold'), bg=cor3, fg=cor1)
listbox.grid(row=0, column=0,)

s_button = Scrollbar(frame_direita)
s_button.grid(row=0, column=1, sticky=NSEW)

listbox.config(yscrollcommand=s_button.set)
s_button.config(command=listbox.yview)



# ----Configurando o frame inferior----
l_rodando = Label(frame_inferior, text='Escolha a musica na lista',width=44, justify=LEFT, anchor='nw', font=('ivy 10'), background=cor1, fg=cor4)
l_rodando.place(x=0, y=1)


# ----Configurando os botões----

# ----Anterior----
img_2 = Image.open('projeto-player-musica/images/2.png')
img_2 = img_2.resize((30, 30))
img_2 = ImageTk.PhotoImage(img_2)

b_anterior = Button(frame_inferior, command=volta_musica, width=40, image=img_2, height=40, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=cor3, fg=cor4)
b_anterior.place(x=38, y=35)


# ----Play----
img_3 = Image.open('projeto-player-musica/images/3.png')
img_3 = img_3.resize((30, 30))
img_3 = ImageTk.PhotoImage(img_3)

b_play = Button(frame_inferior, command=play_musica, width=40, image=img_3, height=40, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=cor3, fg=cor4)
b_play.place(x=84, y=35)


# ----Posterior----
img_4 = Image.open('projeto-player-musica/images/4.png')
img_4 = img_4.resize((30, 30))
img_4 = ImageTk.PhotoImage(img_4)

b_posterior = Button(frame_inferior, command=prox_musica, width=40, image=img_4, height=40, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=cor3, fg=cor4)
b_posterior.place(x=130, y=35)# sempre colocar mais 46 no eixo x, nos outros botões


# ----Pause----
img_5 = Image.open('projeto-player-musica/images/5.png')
img_5 = img_5.resize((30, 30))
img_5 = ImageTk.PhotoImage(img_5)

b_pause = Button(frame_inferior, command=pusar_musica, width=40, image=img_5, height=40, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=cor3, fg=cor4)
b_pause.place(x=176, y=35)


# ----pausar/continuar----
img_6 = Image.open('projeto-player-musica/images/6.png')
img_6 = img_6.resize((30, 30))
img_6 = ImageTk.PhotoImage(img_6)

b_p_continuar = Button(frame_inferior, command=continuar_musica, width=40, image=img_6, height=40, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=cor3, fg=cor4)
b_p_continuar.place(x=222, y=35)


# ----stop----
img_7 = Image.open('projeto-player-musica/images/7.png')
img_7 = img_7.resize((30, 30))
img_7 = ImageTk.PhotoImage(img_7)

b_stop = Button(frame_inferior, command=parar_musica, width=40, image=img_7, height=40, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=cor3, fg=cor4)
b_stop.place(x=268, y=35)


os.chdir(r'C:\Users\Pichau\Documents\Github\player-musica\projeto-player-musica\musics')
musicas = os.listdir()

def mostrar():
    for i in musicas:
        listbox.insert(END, i)

mostrar()


# ----Inicializando o mixer----
mixer.init()



janela.mainloop()