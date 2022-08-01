# **GRSU**
**Otimização de rotas**, através da obtenção de informações geradas, **entre diversas coordenadas**, pelo [**OpenRouteService**](https://openrouteservice.org/)

## **Autor**
Joan Lucas Marques de Sousa Chaves

## **Dependências**
```py
requests==2.25.1
python-dotenv==0.20.0
```

## **Arquivo '.env'.**
O **Token** de autenticação, nomeado como "**OPEN_ROUTE_SERVICE_TOKEN**", deve ser inserido dentro da pasta "***Settings***", feito isto, basta inicializar a classe "***Settings***" que a variável de ambiente alvo será carregada.

## **Visualização de Rotas**
Após coletado as informações sobre as coordenadas e otimizado-as, gera-se uma **URL**, do [**Google Maps**](https://www.google.com.br/maps/), contendo a rota na ordem em que a mesma foi definida.