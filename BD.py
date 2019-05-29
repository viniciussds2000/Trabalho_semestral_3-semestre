def validar_login(cursor,login,senha):
    cursor.execute(f'select id from usuarios WHERE usuario = "{login}" and senha = "{senha}"')

    idlogin= cursor.fetchone()


    cursor.close()


    return idlogin

def busca(cursor,pesquisa):
    cursor.execute(f'SELECT carros.nome,carros.marca,carros.ano,carros.cor,carros.cambio,carros.preço,carros.placa '
                   f'from carros WHERE nome = "{pesquisa}"')
    pesq = cursor.fetchall()

    return pesq


def incluir_user(cursor,conn,login,senha):
    cursor.execute(f'INSERT into `semestral3.`.`usuarios` (usuario,senha) VALUES ("{login}","{senha}")')
    conn.commit()

def excluir_user(cursor,conn,login,senha):
    cursor.execute(f'DELETE FROM `semestral3.`.`usuarios` WHERE usuario = "{login}" and senha = "{senha}"')
    conn.commit()

def incluir_anuncio(cursor,conn,nome,marca,ano,cor,cambio,preço,placa,top10):
    cursor.execute(f'INSERT into `semestral3.`.`carros` (nome,marca,ano,cor,cambio,preço,placa,top10) VALUES ("{nome}","{marca}","{ano}","{cor}","{cambio}","{preço}","{placa}","{top10}")')
    conn.commit()

def excluir_anuncio(cursor,conn,placa):
    cursor.execute(f'DELETE FROM `semestral3.`.`carros` WHERE placa = "{placa}"')
    conn.commit()

def get_carros(cursor):

    # Executar o SQL
    cursor.execute(f'SELECT carros.nome,carros.marca,carros.ano,carros.cor,carros.cambio,carros.preço,carros.placa,carros.top10 '
                   'FROM carros')

    # Recuperando o retorno do BD
    carros = cursor.fetchall()

    # Retornar os dados
    return carros

def get_top10(cursor):
    cursor.execute(f'SELECT carros.nome,carros.marca,carros.ano,carros.cor,carros.cambio,carros.preço,carros.placa '
                   'FROM carros WHERE top10 = "1"')

    top10 = cursor.fetchall()

    return top10

def edit_top10(cursor,conn,top,placa):
    cursor.execute(f'UPDATE carros SET top10 = "{top}" WHERE placa = "{placa}"')
    conn.commit()


def adicionar_imagem(cursor,conn,data):
    cursor.execute(f'INSERT INTO data VALUES LOAD_FILE("{data}"))')
    conn.commit()




