from dataclasses import dataclass, field

from Source.Models.Trashbin import Trashbin

COORDINATES: list[list[float]] = [
    # Coordenadas da origem.
    [-38.500499900597745, -3.7769178589442527],
    # Coordenadas das lixeiras inteligentes.
    [-38.53866577, -3.75756748],
    [-38.49557877, -3.76585371],
    [-38.55128288, -3.76354128],
    [-38.56484413, -3.74589811],
    [-38.55600357, -3.74238656],
    [-38.53360176, -3.76525419],
    [-38.50090027, -3.74093055],
    [-38.53639126, -3.71943269],
    [-38.56304169, -3.77424691],
    [-38.54174979033555, -3.771483854972607],
    [-38.539506, -3.795058],
    [-38.545815, -3.792681],
    [-38.5398346527822, -3.7900433856848474]
]


@dataclass
class Model:
    """Responsável pela manipulação das lixeiras inteligentes."""

    trashbins: list[Trashbin] = field(init=False, default_factory=list)

    def _generate_sample(self) -> None:
        """Gera um exemplar das lixeiras inteligentes 
        para cada coordenada, ignorando a origem."""
        for coord in COORDINATES[1:]:
            self.trashbins.append(
                Trashbin(
                    max_volume=120.0,
                    coordinates=coord
                )
            )
    
    def get_trashbins_coords(self, trashbins: list[Trashbin] = list()) -> list[list[float]]:
        """Retorna as coordenadas de determinadas, ou todas, as lixeiras
        inteligentes, juntamente com a origem.

        Args:
            trashbins (list[Trashbin], optional): As lixeiras inteligentes,
            as quais serão coletadas suas coordenadas, caso nenhuma seja
            fornecida, todas as lixeiras inteligentes serão usadas.

        Returns:
            list[list[float]]: Uma lista contendo as coordenadas da origem e 
            das lixeiras inteligentes, respectivamente.
        """
        return [
            COORDINATES[0],
            *[ # Descompacta os elementos da lista.
                trashbin.coordinates
                for trashbin in trashbins or self.trashbins
            ]
        ]

    def get_trashbins_by_volume(self) -> list[Trashbin]:
        """Pega as lixeiras inteligentes que estão 'cheias'.

        Returns:
            list[Trashbin]: Uma lista com todas as lixeiras inteligentes
            'cheias'.
        """

        return [
            trashbin
            for trashbin in self.trashbins
            if trashbin.is_full()
        ]
    
    def gen_googlemaps_view(self, coordinates: list[list[float]], order: list[int]) -> str:
        """Gera uma 'URL', do Google Maps, para visualização e navegação em
        tempo real.

        Args:
            coordinates (list[list[float]]): As coordenadas das lixeiras
            inteligentes que foram filtradas, ou seja, 'cheias'.
            order (list[int]): A ordem a ser visitada as lixeiras
            inteligentes.

        Returns:
            str: Retorna a 'URL' do Google Maps.
        """
        
        # 'URL' base do Google Maps.
        url = "https://www.google.com.br/maps/dir/"
        # Adiciona as coordenadas, na ordem, à 'URL' do Google Maps.
        for index in order:
            url += ','.join(str(_) for _ in coordinates[index][::-1]) + '/'
        # Por fim, adiciona a coordenada a ser focada quando utilizado a 'URL'.
        url += '@' + ','.join(str(_) for _ in coordinates[0][::-1]) + '/'
        return url

    def __post_init__(self) -> None:
        """Gera um exemplar de lixeiras inteligentes pós inicialização
        da classe."""
        self._generate_sample()
