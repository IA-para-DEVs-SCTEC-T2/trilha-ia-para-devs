def classificar_chamado(tipo_problema, cliente_premium):

    if tipo_problema == "sem_sinal":
        return "alta"

    if tipo_problema == "cobranca" and cliente_premium:
        return "alta"

    if tipo_problema == "cobranca":
        return "media"

    return "baixa"
