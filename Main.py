import requests
from json import loads
from Settings.SettingsHandler import SettingsHandler
from Model.Trashbin.Trashbin import TrashBin

# Extrai o Token do 'OpenRouteService'.
OPEN_ROUTE_SERVICE_TOKEN = SettingsHandler().open_route_service_token

# Coordenadas do ponto de partida.
SOURCE = [-38.500499900597745, -3.7769178589442527]

# Coordenadas das lixeiras inteligentes.
TRASHBIN_COORDINATES = [
    SOURCE, # Coordenadas do Ponto de partida.
    [-38.53866577, -3.75756748],
    [-38.49557877, -3.76585371],
    [-38.55128288, -3.76354128],
    [-38.56484413, -3.74589811],
    [-38.55600357, -3.74238656],
    [-38.53360176, -3.76525419],
    [-38.50090027, -3.74093055],
    [-38.53639126, -3.71943269],
    [-38.56304169, -3.77424691],
    [-38.54261398, -3.77210579]
]

# Lista contendo todas as lixeiras cadastradas.
TRASHBINS = []

# Headers referentes aos requests em 'OpenRouteService'.
HEADERS = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': OPEN_ROUTE_SERVICE_TOKEN,
    'Content-Type': 'application/json; charset=utf-8'
}

# URL do 'OpenRouteService'.
OPEN_ROUTE_SERVICE = "https://api.openrouteservice.org"

class Model:
    """Classe principal."""

    def load_trashbins(self):
        """Inicializa os objeto 'Trashbin' armazenando-os."""
        for coordinates in TRASHBIN_COORDINATES:
            TRASHBINS.append(TrashBin(max_volume=120.0, coordinates=",".join(str(coords) for coords in coordinates)))
    
    def load_distances_and_times(self) -> dict:
        """Gera as distâncias e os tempos entre as lixeiras através do 'OpenRouteService'."""
        # Parâmetros dos requests das distâncias e do tempo em 'OpenRouteService'.
        body = {
            'locations': TRASHBIN_COORDINATES,
            'metrics': ['distance', 'duration']
        }
        call = requests.post(f"{OPEN_ROUTE_SERVICE}/v2/matrix/driving-car", json=body, headers=HEADERS)
        # Verifica se o request foi bem executado.
        if call.status_code != 200:
            raise ValueError(f"Erro retornado: {call.reason}")
        else:
            return loads(call.text)
        
    def load_trashbin_volumes(self):
        """Pega os volumes das lixeiras e prioriza-os."""
        need_to_collect = []
        for trashbin in TRASHBINS:
            # Verifica se a lixeira precisa ser coletada.
            if trashbin.check_volume():
                need_to_collect.append(trashbin)
        # Prioriza as lixeiras com maiores volumes.
        return sorted(need_to_collect, key=lambda trashbin: trashbin.trashbin_current_volume, reverse=True)


if __name__ == "__main__":
    model = Model()
    # Carrega as lixeiras.
    model.load_trashbins()
    # Extrai as distâncias e os tempos em matrizes diferentes.
    model_distance_and_time = model.load_distances_and_times()
    model_distance = model_distance_and_time["distances"]
    model_time = model_distance_and_time["durations"]
    # Define a ordem de prioridade para coleta das lixeiras.
    priorized_collection_order = model.load_trashbin_volumes()
