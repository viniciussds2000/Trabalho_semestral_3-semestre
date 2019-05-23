def validar_login(cursor,login,senha):
    cursor.execute(f'select id from usuarios WHERE usuario = "{login}" and senha = "{senha}"')

    idlogin= cursor.fetchone()


    cursor.close()


    return idlogin


def incluir_user(cursor,conn,login,senha):
    cursor.execute(f'INSERT into semestral3.usuarios (usuario,senha) VALUES ("{login}","{senha}")')
    conn.commit()

def excluir_user(cursor,conn,login,senha):
    cursor.execute(f'DELETE FROM `semestral3`.`usuarios` WHERE usuario = "{login}" and senha = "{senha}"')
    conn.commit()

def incluir_anuncio(cursor,conn,nome,marca,ano,cor,cambio,preço,placa):
    cursor.execute(f'INSERT into semestral3.carros (nome,marca,ano,cor,cambio,preço,placa) VALUES ("{nome}","{marca}","{ano}","{cor}","{cambio}","{preço}","{placa}")')
    conn.commit()

def excluir_anuncio(cursor,conn,placa):
    cursor.execute(f'DELETE FROM `semestral3`.`carros` WHERE placa = "{placa}"')
    conn.commit()

def get_carros(cursor):

    # Executar o SQL
    cursor.execute('SELECT carros.nome,carros.marca,carros.ano,carros.cor,carros.cambio,carros.preço,carros.placa FROM carros')

    # Recuperando o retorno do BD
    carros = cursor.fetchall()

    # Retornar os dados
    return carros

def adicionar_imagem(cursor,conn,data):
    cursor.execute(f'INSERT INTO data VALUES LOAD_FILE("{data}"))')
    conn.commit




