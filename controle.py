from PyQt5 import uic, QtWidgets
import sqlite3
from datetime import date


def procurar_produto():
    # Pegar o produto desejado da interface
    nome_produto = lista_produtos.lineEdit.text().upper()
    if len(nome_produto) == 0:
        # listar todos os produtos na tabela
        listar_produtos()
    else:
        # criar banco
        banco = sqlite3.connect('banco')
        # operacoes no banco
        cursor = banco.cursor()
        # ler dados da tabela PRODUTOS
        cursor.execute("SELECT NOME FROM PRODUTOS")
        # armazenar dados
        dados_tabela = cursor.fetchall()  # obs: os dados estão em forma de matriz 2D
        # selecionar dado da tabela
        cursor.execute("SELECT * FROM PRODUTOS WHERE NOME=?", (nome_produto,))
        # pegar dados da linha
        produto = cursor.fetchall()
        if len(produto) == 0:
            print('Não foi possível encontrar o Produto')
        else:
            # Limpar dados na tabela da tela e deixar apenas uma linha
            lista_produtos.tableWidget.setRowCount(1)
            # mostrar os dados na tabela
            lista_produtos.tableWidget.setItem(
                0, 0, QtWidgets.QTableWidgetItem(str(produto[0][0])))
            lista_produtos.tableWidget.setItem(
                0, 1, QtWidgets.QTableWidgetItem(str(produto[0][1])))
            lista_produtos.tableWidget.setItem(
                0, 2, QtWidgets.QTableWidgetItem(str(produto[0][2])))
            # fechar conexão com o bd
            cursor.close()


def procurar_venda():
    # Pegar o produto desejado da interface
    nome_produto = lista_vendas.lineEdit.text().upper()
    if len(nome_produto) == 0:
        # listar todos os produtos na tabela
        listar_vendas()
    else:
        # criar banco
        banco = sqlite3.connect('banco')
        # operacoes no banco
        cursor = banco.cursor()
        # ler dados da tabela VENDAS
        cursor.execute("SELECT NOME FROM VENDAS")
        # armazenar dados
        dados_tabela = cursor.fetchall()  # obs: os dados estão em forma de matriz 2D
        # selecionar dado da tabela
        cursor.execute("SELECT * FROM VENDAS WHERE NOME=?", (nome_produto,))
        # pegar dados da linha
        produto = cursor.fetchall()
        if len(produto) == 0:
            print('Não foi possível encontrar o Produto')
        else:
            # Limpar dados na tabela da tela e deixar apenas uma linha
            lista_vendas.tableWidget.setRowCount(1)
            # mostrar os dados na tabela
            lista_vendas.tableWidget.setItem(
                0, 0, QtWidgets.QTableWidgetItem(str(produto[0][0])))
            lista_vendas.tableWidget.setItem(
                0, 1, QtWidgets.QTableWidgetItem(str(produto[0][1])))
            lista_vendas.tableWidget.setItem(
                0, 2, QtWidgets.QTableWidgetItem(str(produto[0][2])))
            # fechar conexão com o bd
            cursor.close()


def carregar_campos_tabela_tela_editar_venda():
    # numero da linha selecionada
    linha = lista_vendas.tableWidget.currentRow()
    # criar banco
    banco = sqlite3.connect('banco')
    # operacoes no banco
    cursor = banco.cursor()
    # ler dados da tabela PRODUTOS
    cursor.execute("SELECT NOME FROM VENDAS")
    # armazenar dados
    dados_tabela = cursor.fetchall()  # obs: os dados estão em forma de matriz 2D
    # selecionar dado da tabela
    cursor.execute("SELECT * FROM VENDAS WHERE NOME=?",
                   (dados_tabela[linha][0],))
    # pegar dados da linha
    produto = cursor.fetchall()
    # mostrar os campos preenchidos na tela
    tela_editar_venda.lineEdit.setText(str(produto[0][0]))
    tela_editar_venda.lineEdit_2.setText(str(produto[0][1]))
    tela_editar_venda.lineEdit_3.setText(str(produto[0][2]))
    tela_editar_venda.lineEdit_4.setText(str(produto[0][3]))
    tela_editar_venda.lineEdit_5.setText(str(produto[0][4]))


def carregar_campos_tabela_tela_editar_produto():
    # numero da linha selecionada
    linha = lista_produtos.tableWidget.currentRow()
    # criar banco
    banco = sqlite3.connect('banco')
    # operacoes no banco
    cursor = banco.cursor()
    # ler dados da tabela PRODUTOS
    cursor.execute("SELECT NOME FROM PRODUTOS")
    # armazenar dados
    dados_tabela = cursor.fetchall()  # obs: os dados estão em forma de matriz 2D
    # selecionar dado da tabela
    cursor.execute("SELECT * FROM PRODUTOS WHERE NOME=?",
                   (dados_tabela[linha][0],))
    # pegar dados da linha
    produto = cursor.fetchall()
    # mostrar os campos preenchidos na tela
    tela_editar_produto.lineEdit_2.setText(str(produto[0][0]))
    tela_editar_produto.lineEdit_3.setText(str(produto[0][1]))
    tela_editar_produto.lineEdit_4.setText(str(produto[0][2]))

#global n_linha


def editar_produto():
    # numero da linha selecionada
    linha = lista_produtos.tableWidget.currentRow()
    # criar banco
    banco = sqlite3.connect('banco')
    # operacoes no banco
    cursor = banco.cursor()
    # ler dados da tabela PRODUTOS
    cursor.execute("SELECT NOME FROM PRODUTOS")
    # armazenar dados
    dados_tabela = cursor.fetchall()  # obs: os dados estão em forma de matriz 2D
    # selecionar dado da tabela
    cursor.execute("SELECT * FROM PRODUTOS WHERE NOME=?",
                   (dados_tabela[linha][0],))
    # pegar dados da linha
    produto = cursor.fetchall()
    # pegando os dados da tela
    nome_produto = tela_editar_produto.lineEdit_2.text().upper()
    valor_produto = tela_editar_produto.lineEdit_3.text().upper()
    quantidade_produto = tela_editar_produto.lineEdit_4.text().upper()
    if len(nome_produto) > 0 and len(valor_produto) > 0 and len(quantidade_produto) > 0:
        # atualizar linha da tabela
        cursor.execute("UPDATE PRODUTOS SET NOME = ? , VALOR = ? , QUANTIDADE = ? WHERE NOME = ?",
                       (nome_produto, valor_produto, quantidade_produto, produto[0][0],))
        # confirmar comando
        banco.commit()
        # fechar a tela de editar produto
        tela_editar_produto.close()
        # mostrar novos valores na tabela
        listar_produtos()
        # feedback usuario
        print('Sucesso ao atualizar a linha!')
    else:
        # feedback usuario
        print('Preencher todos os campos para a linha!')


def editar_venda():
    # numero da linha selecionada
    linha = lista_vendas.tableWidget.currentRow()
    # criar banco
    banco = sqlite3.connect('banco')
    # operacoes no banco
    cursor = banco.cursor()
    # ler dados da tabela VENDAS
    cursor.execute("SELECT NOME FROM VENDAS")
    # armazenar dados
    dados_tabela = cursor.fetchall()  # obs: os dados estão em forma de matriz 2D
    # selecionar dado da tabela
    cursor.execute("SELECT * FROM VENDAS WHERE NOME=?",
                   (dados_tabela[linha][0],))
    # pegar dados da linha
    produto = cursor.fetchall()
    # pegando os dados da tela
    data_de_venda = tela_editar_venda.lineEdit.text().upper()
    nome_produto = tela_editar_venda.lineEdit_2.text().upper()
    quantidade_produto = tela_editar_venda.lineEdit_3.text().upper()
    valor_produto = tela_editar_venda.lineEdit_4.text().upper()
    cliente = tela_editar_venda.lineEdit_5.text().upper()
    if len(data_de_venda) > 0 and len(nome_produto) > 0 and len(valor_produto) > 0 and len(quantidade_produto) > 0 and len(cliente) > 0:
        # atualizar linha da tabela
        cursor.execute("UPDATE VENDAS SET DATAV = ? , NOME = ? , VALOR = ? , QUANTIDADE = ? , CLIENTE = ? WHERE NOME = ?",
                       (data_de_venda, nome_produto, quantidade_produto, valor_produto, cliente, produto[0][1],))
        # confirmar comando
        banco.commit()
        # fechar a tela de editar produto
        tela_editar_venda.close()
        # mostrar novos valores na tabela
        listar_vendas()
        # feedback usuario
        print('Sucesso ao atualizar a linha!')
    else:
        # feedback usuario
        print('Preencher todos os campos para a linha!')


def excluir_venda():
    # numero da linha selecionada
    linha = lista_vendas.tableWidget.currentRow()
    # remover linha da tabela visualmente
    lista_vendas.tableWidget.removeRow(linha)
    # criar banco
    banco = sqlite3.connect('banco')
    # operacoes no banco
    cursor = banco.cursor()
    # ler dados da tabela PRODUTOS
    cursor.execute("SELECT * FROM VENDAS")
    # armazenar dados
    dados_tabela = cursor.fetchall()  # obs: os dados estão em forma de matriz 2D
    # deletar dado da tabela
    cursor.execute("DELETE FROM VENDAS WHERE NOME=?",
                   (dados_tabela[linha][1],))
    # confirmar comando
    banco.commit()
    # feedback usuario
    print('Sucesso ao excluir a linha!')
    # fechar conexão com o bd
    cursor.close()


def excluir_produto():
    # numero da linha selecionada
    linha = lista_produtos.tableWidget.currentRow()
    # remover linha da tabela visualmente
    lista_produtos.tableWidget.removeRow(linha)
    # criar banco
    banco = sqlite3.connect('banco')
    # operacoes no banco
    cursor = banco.cursor()
    # ler dados da tabela PRODUTOS
    cursor.execute("SELECT * FROM PRODUTOS")
    # armazenar dados
    dados_tabela = cursor.fetchall()  # obs: os dados estão em forma de matriz 2D
    # deletar dado da tabela
    cursor.execute("DELETE FROM PRODUTOS WHERE NOME=?",
                   (dados_tabela[linha][0],))
    # confirmar comando
    banco.commit()
    # feedback usuario
    print('Sucesso ao excluir a linha!')
    # fechar conexão com o bd
    cursor.close()


def listar_vendas():
    # variavel quantidade de colunas
    numero_colunas = 5
    # criar banco
    banco = sqlite3.connect('banco')
    # operacoes no banco
    cursor = banco.cursor()
    # ler dados da tabela VENDAS
    cursor.execute("SELECT * FROM VENDAS")
    # armazenar dados
    dados_tabela = cursor.fetchall()  # obs: os dados estão em forma de matriz 2D
    # Numero de linhas da tabela
    lista_vendas.tableWidget.setRowCount(len(dados_tabela))
    # Numero de colunas = 5
    lista_vendas.tableWidget.setColumnCount(numero_colunas)
    # quantidade de linhas
    qtd_linhas = len(dados_tabela)
    # mostrar dados na tabela da tela
    for i in range(0, qtd_linhas):
        for j in range(numero_colunas):
            lista_vendas.tableWidget.setItem(
                i, j, QtWidgets.QTableWidgetItem(str(dados_tabela[i][j])))
    # fechar conexão com o bd
    cursor.close()


def listar_produtos():
    # variavel quantidade de colunas
    numero_colunas = 3
    # criar banco
    banco = sqlite3.connect('banco')
    # operacoes no banco
    cursor = banco.cursor()
    # ler dados da tabela PRODUTOS
    cursor.execute("SELECT * FROM PRODUTOS")
    # armazenar dados
    dados_tabela = cursor.fetchall()  # obs: os dados estão em forma de matriz 2D
    # Numero de linhas da tabela
    lista_produtos.tableWidget.setRowCount(len(dados_tabela))
    # Numero de colunas = 3
    lista_produtos.tableWidget.setColumnCount(numero_colunas)
    # quantidade de linhas
    qtd_linhas = len(dados_tabela)
    # mostrar dados na tabela da tela
    for i in range(0, qtd_linhas):
        for j in range(numero_colunas):
            lista_produtos.tableWidget.setItem(
                i, j, QtWidgets.QTableWidgetItem(str(dados_tabela[i][j])))
    # fechar conexão com o bd
    cursor.close()


def cadastrar_venda():
    # pegando os dados da tela
    data_venda = date.today()
    nome_produto = cadastro_vendas.lineEdit.text()
    valor_produto = cadastro_vendas.lineEdit_2.text()
    quantidade_produto = cadastro_vendas.lineEdit_3.text()
    nome_cliente = cadastro_vendas.lineEdit_4.text()
    # limpar os campos da tela
    cadastro_vendas.lineEdit.setText("")
    cadastro_vendas.lineEdit_2.setText("")
    cadastro_vendas.lineEdit_3.setText("")
    cadastro_vendas.lineEdit_4.setText("")
    # criar banco
    banco = sqlite3.connect('banco')
    # operacoes no banco
    cursor = banco.cursor()
    # criar tabela PRODUTOS
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS VENDAS (DATAV TEXT, NOME TEXT, VALOR NUMBER, QUANTIDADE INTEGER, CLIENTE TEXT)")
    # inserir dados na tabela
    cursor.execute("INSERT INTO VENDAS (DATAV, NOME, VALOR, QUANTIDADE, CLIENTE) VALUES (?, ?, ?, ?, ?)",
                   (data_venda, nome_produto.upper(), valor_produto, quantidade_produto, nome_cliente.upper()))
    # confirmar comando
    banco.commit()
    # sucesso feedback usuario
    print('Sucesso ao cadastrar venda!')
    # fechar conexão com o bd
    cursor.close()


def cadastrar_produto():
    # pegando os dados da tela
    nome_produto = cadastro_produtos.lineEdit.text()
    valor_produto = cadastro_produtos.lineEdit_2.text()
    quantidade_produto = cadastro_produtos.lineEdit_3.text()
    # limpar os campos da tela
    cadastro_produtos.lineEdit.setText("")
    cadastro_produtos.lineEdit_2.setText("")
    cadastro_produtos.lineEdit_3.setText("")
    # criar banco
    banco = sqlite3.connect('banco')
    # operacoes no banco
    cursor = banco.cursor()
    # criar tabela PRODUTOS
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS PRODUTOS (NOME TEXT, VALOR NUMBER, QUANTIDADE INTEGER)")
    # inserir dados na tabela
    cursor.execute("INSERT INTO PRODUTOS (NOME, VALOR, QUANTIDADE) VALUES (?, ?, ?)",
                   (nome_produto.upper(), valor_produto, quantidade_produto))
    # confirmar comando
    banco.commit()
    # sucesso feedback usuario
    print('Sucesso ao cadastrar produto!')
    # fechar conexão com o bd
    cursor.close()


def mostrar_tela_cadastro_produtos():
    # mostrar tela
    cadastro_produtos.show()
    # fechar tela principal
    tela_principal.close()


def mostrar_tela_lista_produtos():
    # mostrar tela
    lista_produtos.show()
    # carregar produtos na tela
    listar_produtos()
    # fechar tela principal
    tela_principal.close()


def mostrar_tela_lista_vendas():
    # mostrar tela
    lista_vendas.show()
    # carregar vendas na tela
    listar_vendas()
    # fechar tela principal
    tela_principal.close()


def mostrar_tela_cadastro_vendas():
    # mostrar tela
    cadastro_vendas.show()
    # fechar tela principal
    tela_principal.close()


def mostrar_tela_principal():
    # mostrar tela
    tela_principal.show()
    # fechar tela login
    login_adm.close()


def mostrar_editar_venda():
    # mostrar tela
    tela_editar_venda.show()


def mostrar_editar_produto():
    # mostrar tela
    tela_editar_produto.show()


def validar_login_adm():
    # pegando os dados da tela
    usuario_adm = login_adm.lineEdit.text()
    senha_adm = login_adm.lineEdit_2.text()

    # validar auth usuario e senha
    if(usuario_adm.upper() == 'ADMIN' and senha_adm.upper() == 'ADMIN'):
        # mostrar tela principal
        mostrar_tela_principal()
    elif (len(usuario_adm) == 0):
        print('preencher o campo usuario adm')
    elif (len(senha_adm) == 0):
        print('preencher o campo senha adm')
    elif(usuario_adm.upper() != 'ADM' and senha_adm.upper() != 'ADM'):
        print('usuário e senha adm inválidos')


def fechar_lista_vendas():
    lista_vendas.close()
    mostrar_tela_principal()


def fechar_lista_produtos():
    lista_produtos.close()
    mostrar_tela_principal()


def fechar_cadastro_produtos():
    cadastro_produtos.close()
    mostrar_tela_principal()


def fechar_cadastro_vendas():
    cadastro_vendas.close()
    mostrar_tela_principal()


def fechar_editar_produto():
    tela_editar_produto.close()


def fechar_editar_venda():
    tela_editar_venda.close()


def mostrar_tela_editar_venda():
    mostrar_editar_venda()
    carregar_campos_tabela_tela_editar_venda()


def mostrar_tela_editar_produto():
    mostrar_editar_produto()
    carregar_campos_tabela_tela_editar_produto()


app = QtWidgets.QApplication([])

############### Telas ###############
login_adm = uic.loadUi("login_adm.ui")
cadastro_produtos = uic.loadUi("cadastro_produtos.ui")
cadastro_vendas = uic.loadUi("cadastro_vendas.ui")
lista_produtos = uic.loadUi("lista_produtos.ui")
lista_vendas = uic.loadUi("lista_vendas.ui")
tela_principal = uic.loadUi("tela_principal.ui")
tela_editar_venda = uic.loadUi("editar_venda.ui")
tela_editar_produto = uic.loadUi("editar_produto.ui")

############### Funções dos botões ###############
login_adm.pushButton.clicked.connect(validar_login_adm)

tela_principal.pushButton_2.clicked.connect(mostrar_tela_lista_produtos)
tela_principal.pushButton_3.clicked.connect(mostrar_tela_cadastro_vendas)
tela_principal.pushButton_4.clicked.connect(mostrar_tela_lista_vendas)
tela_principal.pushButton_5.clicked.connect(mostrar_tela_cadastro_produtos)
lista_produtos.pushButton_2.clicked.connect(mostrar_tela_editar_produto)
lista_vendas.pushButton_2.clicked.connect(mostrar_tela_editar_venda)

cadastro_produtos.pushButton.clicked.connect(cadastrar_produto)
cadastro_vendas.pushButton.clicked.connect(cadastrar_venda)

tela_editar_produto.pushButton.clicked.connect(editar_produto)
tela_editar_venda.pushButton.clicked.connect(editar_venda)

lista_produtos.pushButton_3.clicked.connect(excluir_produto)
lista_vendas.pushButton.clicked.connect(excluir_venda)

lista_vendas.pushButton_3.clicked.connect(fechar_lista_vendas)
lista_produtos.pushButton_4.clicked.connect(fechar_lista_produtos)
cadastro_produtos.pushButton_2.clicked.connect(fechar_cadastro_produtos)
cadastro_vendas.pushButton_2.clicked.connect(fechar_cadastro_vendas)
tela_editar_produto.pushButton_2.clicked.connect(fechar_editar_produto)
tela_editar_produto.pushButton_2.clicked.connect(fechar_editar_produto)
tela_editar_venda.pushButton_2.clicked.connect(fechar_editar_venda)

lista_produtos.pushButton_5.clicked.connect(procurar_produto)
lista_vendas.pushButton_4.clicked.connect(procurar_venda)

############### Executar tela ###############
login_adm.show()
app.exec()
