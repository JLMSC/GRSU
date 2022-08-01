from typing import Any
from Model.Model import Model
from Model.Caller.Caller import Caller
from Settings.Settings import Settings


def main(settings: Settings, model: Model):
    """Função principal.

    Args:
        settings (Settings): Carrega as variáveis de ambiente.
        model (Model): Carrega a classe responsável pelos principais métodos.
    """
    # Responsável pelas 'requests' no OpenRouteService.
    ors_caller: Caller = settings.open_route_service_token
    # Pega as coordenadas ordenadas pelo volume das lixeiras.
    coordinates: list[list[float]] = model.add_source_coordinate(model.get_coordinates())
    # Pega a matriz da distância e tempo entre as coordenadas.
    matrix_info: Any = ors_caller.request_matrix(coordinates)

    # TODO: Otimizar a rota (coordenadas) baseado no tempo e distância.

    distances: list[float] = matrix_info['distances']
    durations: list[float] = matrix_info['durations']
    # Gera uma 'URL' do Google Maps.
    google_maps_url: str = model.generate_route_view(coordinates)
    print(google_maps_url)

    # TODO: Não faz muito sentido pedir essa informação,
    # pq ele percorre na ordem que é fornecido as coordenadas,
    # basicamente não otimiza a rota, só segue na ordem.
    # route_info = ors_caller.request_route(coordinates)

if __name__ == "__main__":
    main(Settings(), Model())
