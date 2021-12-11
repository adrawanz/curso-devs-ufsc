<<<<<<< HEAD
from ctypes import alignment, sizeof
from os import system
from tkinter import font
import PySimpleGUI as sg

ARQUIVO_PACIENTES = "pacientes.pkl"
pacientes = {}

def carrega_arquivo_com_pickle():
    import pickle
    import os
    global pacientes
    if not os.path.exists(ARQUIVO_PACIENTES):
        grava_arquivo_com_pickle()
    arquivo_pacientes = open(ARQUIVO_PACIENTES, 'rb')
    pacientes = pickle.load(arquivo_pacientes)

def grava_arquivo_com_pickle():
    import pickle
    arquivo_pacientes = open(ARQUIVO_PACIENTES, 'wb')
    pickle.dump(pacientes, arquivo_pacientes)

def menu_principal():
    layout = [[sg.Text("Sistema Clínica", font=("Arial 14 bold"), pad=(0,10), expand_x= True)], 
              [sg.Button("Cadastrar", key="cadastrar", size=(40, 2))],
              [sg.Button("Listar", key="listar", size=(40, 2))]]

    janela = sg.Window("Sistema Clínica", layout, text_justification="center")
    botao, valores = janela.read()
    janela.close()

    return botao

def cadastra():
    layout = [[sg.Text("Cadastrar Paciente", font=("Arial 14 bold"), pad=(0,10), expand_x= True, justification="center")],
              [sg.Text("CPF:", size= (18,1)), sg.Input(key="cpf", size=(28,1))],
              [sg.Text("Nome:", size= (18,1)), sg.Input(key="nome", size=(28,1))],
              [sg.Text("Telefone:", size= (18,1)), sg.Input(key="telefone", size=(28,1))],
              [sg.Text("Endereço:", size= (18,1)), sg.Input(key="endereco", size=(28,1))],
              [sg.Button("Cadastrar", key="cadastra", size=(21,1)), sg.Button("Cancelar", key="cancela", size=(21,1))]]

    janela = sg.Window("Cadastrar", layout)
    botao, dados_paciente = janela.read()
    janela.close()

    if botao == "cadastra":
        cpf_paciente = dados_paciente.pop("cpf")
        try:
            cpf_paciente = int(cpf_paciente)
            if cpf_paciente not in pacientes.keys():
                pacientes[cpf_paciente] = dados_paciente
            else:
                sg.Popup("Já existe um paciente com este CPF")
        except ValueError:
            sg.Popup("Valor inválido, digite um número")
    elif botao != "cancela":
        raise SystemExit

def cria_tabela(cpfs):
    matriz = []
    for cpf in cpfs:
        paciente = pacientes[cpf]
        linha = [cpf, paciente["nome"], paciente["telefone"], paciente ["endereco"]]
        matriz.append(linha)
    if len(matriz) == 0:
        tamanho_automatico = False
    else:
        tamanho_automatico = True
    return sg.Table(matriz, ["CPF", "Nome", "Telefone", "Endereço"], auto_size_columns = tamanho_automatico, expand_x= True, justification="center")

def lista_pacientes():
    tabela = cria_tabela(pacientes.keys())
    layout = [[sg.Text("Lista de pacientes", font=("Arial 14 bold"), pad=(0,10), expand_x= True)],
              [tabela],             
              [sg.Button("Voltar", key="voltar", expand_x=True)]]

    janela = sg.Window("Lista de pacientes", layout, text_justification="center")
    opcao, valores = janela.read()
    janela.close()

    if opcao != "voltar":
        raise SystemExit

def main():
    sg.theme("BrownBlue")
    carrega_arquivo_com_pickle()
    while True:
        opcao = menu_principal()
        try:
            match opcao:
                case 'cadastrar':
                    cadastra()
                case 'listar':
                    lista_pacientes()
                case _:
                    grava_arquivo_com_pickle()
                    break
        except SystemExit:
            grava_arquivo_com_pickle()
            exit()
                
if __name__ == '__main__':
    main()
=======
from ctypes import alignment, sizeof
from os import system
from tkinter import font
import PySimpleGUI as sg

ARQUIVO_PACIENTES = "pacientes.pkl"
pacientes = {}

def carrega_arquivo_com_pickle():
    import pickle
    import os
    global pacientes
    if not os.path.exists(ARQUIVO_PACIENTES):
        grava_arquivo_com_pickle()
    arquivo_pacientes = open(ARQUIVO_PACIENTES, 'rb')
    pacientes = pickle.load(arquivo_pacientes)

def grava_arquivo_com_pickle():
    import pickle
    arquivo_pacientes = open(ARQUIVO_PACIENTES, 'wb')
    pickle.dump(pacientes, arquivo_pacientes)

def menu_principal():
    layout = [[sg.Text("Sistema Clínica", font=("Arial 14 bold"), pad=(0,10), expand_x= True)], 
              [sg.Button("Cadastrar", key="cadastrar", size=(40, 2))],
              [sg.Button("Listar", key="listar", size=(40, 2))]]

    janela = sg.Window("Sistema Clínica", layout, text_justification="center")
    botao, valores = janela.read()
    janela.close()

    return botao

def cadastra():
    layout = [[sg.Text("Cadastrar Paciente", font=("Arial 14 bold"), pad=(0,10), expand_x= True, justification="center")],
              [sg.Text("CPF:", size= (18,1)), sg.Input(key="cpf", size=(28,1))],
              [sg.Text("Nome:", size= (18,1)), sg.Input(key="nome", size=(28,1))],
              [sg.Text("Telefone:", size= (18,1)), sg.Input(key="telefone", size=(28,1))],
              [sg.Text("Endereço:", size= (18,1)), sg.Input(key="endereco", size=(28,1))],
              [sg.Button("Cadastrar", key="cadastra", size=(21,1)), sg.Button("Cancelar", key="cancela", size=(21,1))]]

    janela = sg.Window("Cadastrar", layout)
    botao, dados_paciente = janela.read()
    janela.close()

    if botao == "cadastra":
        cpf_paciente = dados_paciente.pop("cpf")
        try:
            cpf_paciente = int(cpf_paciente)
            if cpf_paciente not in pacientes.keys():
                pacientes[cpf_paciente] = dados_paciente
            else:
                sg.Popup("Já existe um paciente com este CPF")
        except ValueError:
            sg.Popup("Valor inválido, digite um número")
    elif botao != "cancela":
        raise SystemExit

def cria_tabela(cpfs):
    matriz = []
    for cpf in cpfs:
        paciente = pacientes[cpf]
        linha = [cpf, paciente["nome"], paciente["telefone"], paciente ["endereco"]]
        matriz.append(linha)
    if len(matriz) == 0:
        tamanho_automatico = False
    else:
        tamanho_automatico = True
    return sg.Table(matriz, ["CPF", "Nome", "Telefone", "Endereço"], auto_size_columns = tamanho_automatico, expand_x= True, justification="center")

def lista_pacientes():
    tabela = cria_tabela(pacientes.keys())
    layout = [[sg.Text("Lista de pacientes", font=("Arial 14 bold"), pad=(0,10), expand_x= True)],
              [tabela],             
              [sg.Button("Voltar", key="voltar", expand_x=True)]]

    janela = sg.Window("Lista de pacientes", layout, text_justification="center")
    opcao, valores = janela.read()
    janela.close()

    if opcao != "voltar":
        raise SystemExit

def main():
    sg.theme("BrownBlue")
    carrega_arquivo_com_pickle()
    while True:
        opcao = menu_principal()
        try:
            match opcao:
                case 'cadastrar':
                    cadastra()
                case 'listar':
                    lista_pacientes()
                case _:
                    grava_arquivo_com_pickle()
                    break
        except SystemExit:
            grava_arquivo_com_pickle()
            exit()
                
if __name__ == '__main__':
    main()
>>>>>>> bb12a5442a140d1a07dbc9cc7d82f324150ef03b
