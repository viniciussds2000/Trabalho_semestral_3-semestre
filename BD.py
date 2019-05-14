def validar_login(cursor,login,senha):
    cursor.execute(f'select id from usuarios WHERE usuario = "{login} " and senha = "{senha}"')

    idlogin= cursor.fetchone()

    cursor.close()


    return idlogin


def incluir_user(cursor,login,senha):
    cursor.execute(f'INSERT into usuarios (login,senha) VALUES ({login},{senha}')

    cursor.commit()
