from typing import Any
from Source.Config.Settings import Settings
from Source.Models.Model import Model
from Source.Scripts.TSP import TSP
from Source.Tools.Caller import Caller


def main() -> dict:
    """Função principal.

    Args:
        ors_api (Caller): Responsável pelas requisições na 'API' do
        'OpenRouteService'.
        model (Model): Responsável pela manipulação de objetos gerados,
        tanto pelas chamas na 'API', como nas otimizações referentes à
        roteamento.
    """

    ors_api = Caller(
        token=Settings.load_ors_token()
    )
    model = Model()

    # Pega as coordenadas das lixeiras inteligentes que estão 'cheias'.
    trashbins_coords: list[list[float]] = model.get_trashbins_coords(
        trashbins=model.get_trashbins_by_volume()
    )

    # Requisita uma matriz de distância e tempo entre as coordenadas.
    # Matriz de distância : matrix['distances']
    # Matriz de tempo : matrix['durations']
    matrix: Any = ors_api.request_matrix(
        coordinates=trashbins_coords
    )

    # Gera uma 'URL' de visualização e navegação, em tempo real,
    # no Google Maps, baseado na ordem estabelecida pelo algoritmo de 'TSP'.
    order = TSP(matrix['durations'])
    url = model.gen_googlemaps_view(
        coordinates=trashbins_coords,
        order=order
    )

    # Cria uma lista com as coordenadas na ordem estabelecida
    order_coords = []
    for trashbin in order:
        order_coords.append({
            "id": trashbin,
            "coordinates": trashbins_coords[trashbin]
        })


    return {
        "order": order_coords,
        "web_url": url
    }

if __name__ == "__main__":
    # Executa a função principal, incializando a classe 'Caller' já com o
    # Token de acesso da 'API' do 'OpenRouteService'.
    result_dict = main()
    print(result_dict)
