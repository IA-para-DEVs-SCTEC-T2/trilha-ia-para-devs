def validar_senha(senha):
    if len(senha) < 8:
        return False

    if senha.islower():
        return False

    if senha.isalpha():
        return False

    return True