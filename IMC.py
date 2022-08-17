from tkinter import *

#Funções----------------------------------------------------------------------
def calcular():
    peso = float(text_box1.get())
    altura = float(text_box2.get())
    imc = peso/(altura**2)
    if imc < 16:
        resultado_texto['text']='Magreza Grau III'
    elif 16 <= imc < 16.9:
        resultado_texto['text']='Magreza Grau II'
    elif 17 <= imc < 18.4:
        resultado_texto['text']='Magreza Grau I'
    elif 18.5 <= imc < 24.9:
        resultado_texto['text']='Peso Ideal!'
    elif 25 <= imc < 29.9:
        resultado_texto['text']='Pré-obeso'
    elif 30 <= imc < 34.9:
        resultado_texto['text']='Obesidade Grau I'
    elif 35 <= imc < 39.9:
        resultado_texto['text']='Obesidade Grau II'
    elif imc >= 40:
        resultado_texto['text']='Obesidade Grau III'
    
    resultado_imc['text']=(f"O seu IMC é: {imc:.2f}") 

def limpar():
    text_box1.delete(0,END)
    text_box2.delete(0,END)
    resultado_imc.config(text="")
    resultado_texto.config(text="")

#GUI-----------------------------------------------------------
app = Tk()
app.title('IMC')
app.geometry('245x350')
app.resizable(False,False)
app['bg']= '#BC8F8F'

#Widgets--------------------------------------------------------
lbl1 = Label(app, text='Calculadora de IMC', 
            font ='arial 19', 
            relief ='ridge', 
            bd = 10,
            fg = 'black',
            bg = '#20B2AA')
lbl_space1 = Label(app, height=2, bg='#BC8F8F')

lbl2 = Label(app, text='Insira o seu peso em kg', font='Arial 13', relief='groove',bd= 5)
text_box1 = Entry(app)

lbl3 = Label(app, text='Insira a sua altura em metros', font='arial 13', relief='groove',bd= 5)
text_box2 = Entry(app)
lbl_space2 = Label(app, height=1,bg='#BC8F8F')

btn = Button(app, text='Resultado', font='arial 13', command=calcular)
btn1 = Button(app, text='Limpar', font='arial 13', command=limpar)

resultado_imc = Label(app, text='', font='times 12',bg='#BC8F8F')
resultado_texto = Label(app, text='', font='times 12',bg='#BC8F8F')
     
#Layout---------------------------------------------------------
lbl1.grid()
lbl_space1.grid()
lbl2.grid()
text_box1.grid()
lbl3.grid()
text_box2.grid()
lbl_space2.grid()
btn.grid()
btn1.grid()
resultado_imc.grid()
resultado_texto.grid()

text_box1.focus()

app.mainloop()
