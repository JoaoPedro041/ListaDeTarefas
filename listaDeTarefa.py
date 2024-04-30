#João Pedro Fonseca 30/04/2024
#Para rodar instale o "PySimpleGUI", digite o comando "pip install pysimplegui" ou "pip3 install pysimplegui"

import PySimpleGUI as sg

def criar_nova_janela():
    sg.theme('GrayGrayGray')
    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas',layout=linha,key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]
    return sg.Window('Lista de Tarefas',layout=layout,finalize=True)

janela = criar_nova_janela()

while True:
    event, values= janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_nova_janela()