# **GRSU**
**Otimização de rotas**, através da obtenção de informações geradas,
**entre diversos pontos**, pelo **OpenRouteService**.

## **Dependências**
```py
requests==2.25.1
```

## **Arquivo '.env'.**
O Token de autenticação deve ser inserido dentro da pasta "*Settings*", 
feito isto, basta inicializar a classe "*SettingsHandler*" que a variável 
de ambiente alvo será carregada.

# TODO
[X] Arrumar as coordenadas, trocar a ordem.
[X] Ver se da para fazer uma rota com várias coordenadas.
[X] Fazer um request das matrizes de distancia e tempo.
[X] Armazenar as matrizes de distancia e tempo.
[X] Gerar uma lista de prioridades das lixeiras com volumes >= 80%.
[] Pegar as coordenadas priorizadas pelo o volume da lixeira.
(OpenRouteService ja faz isso, mas devemos testar antes.)
[] Gerar um rota entre as lixeiras, priorizando a que tem mais volume.
[] Otimizar a rota.
(Opcional)
[] Alternativas para otimização de rota.
[] Mostrar a rota em um mapa.
