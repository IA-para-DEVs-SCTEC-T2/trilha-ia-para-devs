def pode_acessar(ativo, bloqueado, admin):
    if bloqueado:
        return False

    if admin:
        return True

    return ativo