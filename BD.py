def validar_login(cursor,login,senha):
    cursor.execute(f'select id from usuarios WHERE usuario = "{login}" and senha = "{senha}"')

    idlogin= cursor.fetchone()


    cursor.close()


    return idlogin


def busca(cursor,pesquisa):
    cursor.execute(f'SELECT * from carros WHERE nome = "{pesquisa}" AND reserva = "0"')
    pesq = cursor.fetchall()

    return pesq

def reservar(cursor,conn,reserva,placa):
    cursor.execute(f'UPDATE carros SET reserva = "{reserva}" WHERE placa = "{placa}"')
    conn.commit()

def ad_comprador(cursor, conn,nome,cpf,telefone):
        cursor.execute(f'INSERT into `semestral3.`.`reservistas` (nome,cpf,telefone) VALUES ("{nome}","{cpf}","{telefone}")')
        conn.commit()


def get_detalhes(cursor,placa):
    cursor.execute(f'SELECT * FROM carros WHERE placa = "{placa}"')
    detalhes= cursor.fetchall()

    return detalhes

def incluir_user(cursor,conn,login,senha):
    cursor.execute(f'INSERT into `semestral3.`.`usuarios` (usuario,senha) VALUES ("{login}","{senha}")')
    conn.commit()

def excluir_user(cursor,conn,login,senha):
    cursor.execute(f'DELETE FROM `semestral3.`.`usuarios` WHERE usuario = "{login}" and senha = "{senha}"')
    conn.commit()

def incluir_anuncio(cursor,conn,nome,marca,ano,cor,cambio,preço,placa,top10,reserva,data):
    cursor.execute(f'INSERT into `semestral3.`.`carros` (nome,marca,ano,cor,cambio,preço,placa,top10,reserva,url) VALUES ("{nome}","{marca}","{ano}","{cor}","{cambio}","{preço}","{placa}","{top10}","{reserva}","{data}")')
    conn.commit()




def excluir_anuncio(cursor,conn,placa):
    cursor.execute(f'DELETE FROM `semestral3.`.`carros` WHERE placa = "{placa}"')
    conn.commit()

def get_carros(cursor):

    # Executar o SQL
    cursor.execute(f'SELECT * '
                   'FROM carros where reserva = "0"')

    # Recuperando o retorno do BD
    carros = cursor.fetchall()

    # Retornar os dados
    return carros

def get_carro_id(cursor,numero_carro):

    # Executar o SQL
    cursor.execute(f'SELECT * FROM carros WHERE id = "{numero_carro}"')

    # Recuperando o retorno do BD
    carros = cursor.fetchall()

    # Retornar os dados
    return carros


def get_top10(cursor):
    cursor.execute(f'SELECT * '
                   'FROM carros WHERE top10 = "1" and reserva = "0"')

    top10 = cursor.fetchall()

    return top10

def edit_top10(cursor,conn,top,placa):
    cursor.execute(f'UPDATE carros SET top10 = "{top}" WHERE placa = "{placa}"')
    conn.commit()

def get_carros_reservados(cursor):
    cursor.execute(f'SELECT * FROM carros WHERE reserva = "1"')
    carros=cursor.fetchall()

    return carros



def call_imagem(cursor,conn,carro):
    cursor.execute(f'SELECT url FROM carros WHERE nome = "{carro}"')
    conn.commit()





