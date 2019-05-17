def validar_login(cursor,login,senha):
    cursor.execute(f'select id from usuarios WHERE usuario = "{login}" and senha = "{senha}"')

    idlogin= cursor.fetchone()

    cursor.close()


    return idlogin


def incluir_user(cursor,conn,login,senha):
    cursor.execute(f'INSERT into semestral3.usuarios (usuario,senha) VALUES ("{login}","{senha}")')
    conn.commit()

def incluir_anuncio(cursor,nome,marca,ano,cor,cambio):
    cursor.execute(f'INSERT into semestral3.anuncios (nome,marca,ano,cor,cambio) VALUES ("{nome}","{marca}","{ano}","{cor}","{cambio}")')

    nanuncio= cursor.fetchone()

    cursor.close()

    return nanuncio

def get_carros(cursor):

    # Executar o SQL
    cursor.execute('SELECT carros.nome,carros.marca,carros.ano,carros.cor,carros.cambio FROM carros')

    # Recuperando o retorno do BD
    carros = cursor.fetchall()

    # Retornar os dados
    return carros