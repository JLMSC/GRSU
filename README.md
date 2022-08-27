# **GRSU**
**Otimização de rotas**, através da obtenção de informações geradas, 
**entre diversas coordenadas**, pelo 
[**OpenRouteService**](https://openrouteservice.org/)

## **Dependências**
```py
requests==2.25.1
python-dotenv==0.20.0
ortools==9.3.10497
```
~ Foi utilizado **Python 3.10.4** para o desenvolvimento.

## **Sobre o arquivo '.env'.**
O **Token** de autenticação da **API** do 
[**OpenRouteService**](https://openrouteservice.org/), nomeado como 
"**OPEN_ROUTE_SERVICE_TOKEN**", deve ser inserido dentro da 
pasta "**Source/Config/**", feito isto, basta chamar o método
"**load_ors_token()** da classe "**Settings**", do arquivo 
"**Source/Config/Settings.py**" que a variável de ambiente alvo 
será carregada.

Também deve ser criado outro arquivo na pasta "**grsu/**" com um valor para a 
[secret key](https://docs.djangoproject.com/en/4.1/ref/settings/#secret-key)
do projeto, nomeado como "**SECRET_KEY**".

## **Otimização de Rotas**
A **otimização de rotas** é realizada através de um algoritmo voltado
ao ["**Problema do Caixeiro-Viajante**"](https://pt.wikipedia.org/wiki/Problema_do_caixeiro-viajante):
"*o qual tenta determinar a menor rota para percorrer uma série de cidades,
visitando-as uma única vez e, por fim, retornando a cidade origem.*". Foi
utilizado a biblioteca ["**OR-TOOLS**"](https://developers.google.com/optimization)
para resolução do 
["**Problema do Caixeiro-Viajante**"](https://pt.wikipedia.org/wiki/Problema_do_caixeiro-viajante), 
dada a sua definição.

## **Visualização de Rotas**
Após coletado as informações sobre as coordenadas e otimizado-as, gera-se 
uma **URL**, do [**Google Maps**](https://www.google.com.br/maps/), 
contendo a rota na ordem em que a mesma foi definida.

## **API**
O framework [django](https://www.djangoproject.com) é usado para rodar a API.
Se já estiver instalado, deve usar o seguinte comando para iniciar o servidor:
```
py manage.py runserver
```
