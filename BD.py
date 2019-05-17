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

def incluir_anuncio(cursor,conn,nome,marca,ano,cor,cambio,preço):
    cursor.execute(f'INSERT into semestral3.carros (nome,marca,ano,cor,cambio,preço) VALUES ("{nome}","{marca}","{ano}","{cor}","{cambio}","{preço}")')
    conn.commit()

def get_carros(cursor):

    # Executar o SQL
    cursor.execute('SELECT carros.nome,carros.marca,carros.ano,carros.cor,carros.cambio,carros.preço FROM carros')

    # Recuperando o retorno do BD
    carros = cursor.fetchall()

    # Retornar os dados
    return carros