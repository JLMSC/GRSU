from typing import Any, Dict, NoReturn, List
from Source.Config.Settings import Settings
from Source.Models.Model import Model
from Source.Scripts.TSP import TSP
from Source.Tools.Caller import Caller


def main(ors_api: Caller, model: Model) -> NoReturn:
    """Função principal.

    Args:
        ors_api (Caller): Responsável pelas requisições na 'API' do
        'OpenRouteService'.
        model (Model): Responsável pela manipulação de objetos gerados,
        tanto pelas chamas na 'API', como nas otimizações referentes à
        roteamento.
    """

    # Pega as coordenadas das lixeiras inteligentes que estão 'cheias'.
    trashbins_coords: List[List[float]] = model.get_trashbins_coords(
        trashbins=model.get_trashbins_by_volume()
    )

    # Requisita uma matriz de distância e tempo entre as coordenadas.
    # Matriz de distância : matrix['distances']
    # Matriz de tempo : matrix['durations']
    matrix: Any = ors_api.request_matrix(coordinates=trashbins_coords)

    # Todas as 'n' rotas para os 'n' veículos.
    vehicle_routes: Dict[int, List[int]] = TSP(
        time_matrix=matrix["durations"],
        # FIXME: Automatizar a quantia de veículos, ou solicitar "input".
        vehicle_quantity=2,
    )

    # Por fim, gera uma 'URL' de visualização e navegação, em tempo real,
    # no Google Maps, para cada 'n' veículos, baseando-se na ordem estabelecida
    # pelo algoritmo de 'TSP'.
    #for vehicle_id, vehicle_route in vehicle_routes.items():
    #    vehicle_route_url: str = model.gen_googlemaps_view(
    #        coordinates=trashbins_coords, order=vehicle_route
    #    )
    #    print(f"URL da Rota do Veículo #{vehicle_id}\n: {vehicle_route_url}\n")


if __name__ == "__main__":
    # Executa a função principal, incializando a classe 'Caller' já com o
    # Token de acesso da 'API' do 'OpenRouteService'.
    main(ors_api=Caller(token=Settings.load_ors_token()), model=Model())
