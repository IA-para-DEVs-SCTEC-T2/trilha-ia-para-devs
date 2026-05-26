C4Context
title C4 Contexto - Shop4u

Person(cliente, "Cliente", "Usuário que realiza compras")
System(shop4u, "Shop4u", "E-commerce mobile com recomendações por IA")
System_Ext(ia, "Serviço de IA", "Recomenda produtos")
System_Ext(pagamento, "Gateway de Pagamento", "Processa pagamentos")
System_Ext(notificacoes, "Serviço de Notificações", "Envia confirmações")

Rel(cliente, shop4u, "Usa")
Rel(shop4u, ia, "Consulta recomendações")
Rel(shop4u, pagamento, "Processa pagamentos")
Rel(shop4u, notificacoes, "Envia confirmações")