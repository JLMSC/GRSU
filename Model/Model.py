from dataclasses import dataclass, field
from Model.Trashbin.Trashbin import Trashbin

# Coordenadas do ponto de partida.
SOURCE = [-38.500499900597745, -3.7769178589442527]

# Coordenadas das lixeiras inteligentes.
TRASHBIN_COORDINATES = [
    SOURCE,
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

@dataclass
class Model:
    """Responsável pelas operações principais."""

    # Armazena todas as lixeiras inteligentes que foram inicializadas.
    trashbins: list[Trashbin] = field(init=False, default_factory=list)

    def _generate_sample_trashbins(self):
        """Gera um exemplar das lixeiras inteligentes para cada coordenada."""
        for coordinates in TRASHBIN_COORDINATES[1:]:
            self.trashbins.append(Trashbin(max_volume=120.0, coordinates=coordinates))

    def _priorize_trashbins_by_volume(self) -> list[Trashbin]:
        """Pega os volumes das lixeiras inteligentes e prioriza-os.

        Returns:
            list[Trashbin]: Uma lista priozirada, pelo volume das lixeiras inteligentes.
        """
        # Pega somente as lixeiras que precisam ser coletadas.
        trashbins_to_collect: list[Trashbin] = [
            trashbin for trashbin in self.trashbins if trashbin.is_full()
        ]
        # Organiza a ordem das lixeiras baseado no volume delas.
        return sorted(trashbins_to_collect, key=lambda trashbin: trashbin.current_volume, reverse=True)

    def get_coordinates(self) -> list[list[float]]:
        """Pega as coordenadas, das lixeiras inteligentes ordenadas pelo volume.

        Returns:
            list[list[float]]: As coordendas priorizadas.
        """
        # Coordenadas priorizadas das lixeiras inteligentes.
        coordinates = [
            coordinates.coordinates 
            for coordinates in self._priorize_trashbins_by_volume()
        ]
        return coordinates
    
    def add_source_coordinate(self, coordinates: list[list[float]]) -> list[list[float]]:
        """Adiciona as coordenadas da origem as coordenadas.

        Args:
            coordinates (list[list[float]]): As coordenadas priorizadas.

        Returns:
            list[list[float]]: As coordenadas incluindo a origem e o destino.
        """
        # Adiciona as coordenadas da origem e do destino.
        coordinates.insert(0, SOURCE)
        coordinates.append(SOURCE)
        return coordinates
    
    def generate_route_view(self, coordinates: list[list[float]]) -> str:
        """Gera uma 'URL' do Google Maps das coordenadas.

        Args:
            coordinates (list[list[float]]): As coordenadas a serem visitadas.

        Returns:
            str: Uma 'URL' do Google Maps, contendo informações sobre as coordenadas.
        """
        # 'URL' a ser modificada pelas coordenadas inseridas.
        url = "https://www.google.com.br/maps/dir/"
        # Adiciona as coordenadas à 'URL'.
        for coordinate in coordinates:
            url += ','.join(str(_) for _ in coordinate[::-1]) + '/'
        # Adiciona um 'zoom', na coordenada origem, à 'URL'.
        url += '@' + ','.join(str(_) for _ in coordinates[0][::-1]) + '/'
        return url

    def __post_init__(self):
        """Inicializa os demais atributos."""
        self._generate_sample_trashbins()