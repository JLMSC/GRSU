from dataclasses import dataclass, field
<<<<<<< HEAD

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
=======
from typing import NoReturn, List

from Source.Models.Trashbin import Trashbin

COORDINATES: List[List[float]] = [
    # Coordenadas da origem.
    [-38.500499900597745, -3.7769178589442527],
    [-38.485596, -3.728529],
    [-38.489837, -3.729235],
    [-38.497568, -3.744028],
    [-38.509628, -3.750246],
    [-38.517185, -3.72683],
    [-38.575009, -3.705599],
    [-38.584382, -3.700758],
    [-38.583979, -3.707453],
    [-38.576503, -3.714424],
    [-38.588304, -3.713773],
    [-38.588952, -3.720129],
    [-38.59588, -3.709786],
    [-38.598539, -3.716256],
    [-38.604429, -3.719157],
    [-38.597742, -3.720147],
    [-38.589704, -3.746484],
    [-38.601653, -3.75347],
    [-38.603646, -3.767475],
    [-38.607192, -3.77685],
    [-38.591755, -3.775734],
    [-38.588736, -3.767998],
    [-38.580939, -3.756302],
    [-38.572965, -3.75015],
    [-38.578092, -3.770069],
    [-38.569356, -3.776666],
    [-38.57729, -3.7956],
    [-38.608341, -3.807188],
    [-38.61623, -3.795641],
    [-38.619226, -3.782649],
    [-38.629466, -3.804112],
    [-38.61924, -3.820276],
    [-38.588063, -3.8286],
    [-38.583397, -3.817522],
    [-38.5726, -3.819555],
    [-38.527197, -3.833639],
    [-38.521889, -3.850392],
    [-38.52022, -3.852948],
    [-38.517684, -3.843694],
    [-38.514596, -3.835837],
    [-38.507194, -3.826283],
    [-38.508936, -3.820275],
    [-38.511315, -3.816186],
    [-38.509048, -3.814728],
    [-38.509474, -3.81304],
    [-38.545105, -3.803329],
    [-38.548523, -3.794352],
    [-38.543553, -3.787967],
    [-38.528932, -3.79119],
    [-38.523507, -3.786663],
    [-38.514741, -3.772355],
    # Coordenadas do destino.
    [-38.500499900597745, -3.7769178589442527],
>>>>>>> bfa5ccc (Imp. rotas para N veiculos e novas coordenadas.)
]


@dataclass
class Model:
    """Responsável pela manipulação das lixeiras inteligentes."""

<<<<<<< HEAD
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
=======
    trashbins: List[Trashbin] = field(init=False, default_factory=list)

    def _generate_sample(self) -> NoReturn:
        """Gera um exemplar das lixeiras inteligentes
        para cada coordenada, ignorando a origem."""
        for coord in COORDINATES[1:]:
            self.trashbins.append(Trashbin(max_volume=120.0, coordinates=coord))

    def get_trashbins_coords(
        self, trashbins: List[Trashbin] = list()
    ) -> List[List[float]]:
>>>>>>> bfa5ccc (Imp. rotas para N veiculos e novas coordenadas.)
        """Retorna as coordenadas de determinadas, ou todas, as lixeiras
        inteligentes, juntamente com a origem.

        Args:
<<<<<<< HEAD
            trashbins (list[Trashbin], optional): As lixeiras inteligentes,
=======
            trashbins (List[Trashbin], optional): As lixeiras inteligentes,
>>>>>>> bfa5ccc (Imp. rotas para N veiculos e novas coordenadas.)
            as quais serão coletadas suas coordenadas, caso nenhuma seja
            fornecida, todas as lixeiras inteligentes serão usadas.

        Returns:
<<<<<<< HEAD
            list[list[float]]: Uma lista contendo as coordenadas da origem e 
=======
            List[List[float]]: Uma lista contendo as coordenadas da origem e
>>>>>>> bfa5ccc (Imp. rotas para N veiculos e novas coordenadas.)
            das lixeiras inteligentes, respectivamente.
        """
        return [
            COORDINATES[0],
<<<<<<< HEAD
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
=======
            *[  # Descompacta os elementos da lista.
                trashbin.coordinates for trashbin in trashbins or self.trashbins
            ],
        ]

    def get_trashbins_by_volume(self) -> List[Trashbin]:
        """Pega as lixeiras inteligentes que estão 'cheias'.

        Returns:
            List[Trashbin]: Uma lista com todas as lixeiras inteligentes
            'cheias'.
        """

        return [trashbin for trashbin in self.trashbins if trashbin.is_full()]

    def gen_googlemaps_view(
        self, coordinates: List[List[float]], order: List[int]
    ) -> str:
>>>>>>> bfa5ccc (Imp. rotas para N veiculos e novas coordenadas.)
        """Gera uma 'URL', do Google Maps, para visualização e navegação em
        tempo real.

        Args:
<<<<<<< HEAD
            coordinates (list[list[float]]): As coordenadas das lixeiras
            inteligentes que foram filtradas, ou seja, 'cheias'.
            order (list[int]): A ordem a ser visitada as lixeiras
=======
            coordinates (List[List[float]]): As coordenadas das lixeiras
            inteligentes que foram filtradas, ou seja, 'cheias'.
            order (List[int]): A ordem a ser visitada as lixeiras
>>>>>>> bfa5ccc (Imp. rotas para N veiculos e novas coordenadas.)
            inteligentes.

        Returns:
            str: Retorna a 'URL' do Google Maps.
        """
<<<<<<< HEAD
        
        # 'URL' base do Google Maps.
        url = "https://www.google.com.br/maps/dir/"
        # Adiciona as coordenadas, na ordem, à 'URL' do Google Maps.
        for index in order:
            url += ','.join(str(_) for _ in coordinates[index][::-1]) + '/'
        # Por fim, adiciona a coordenada a ser focada quando utilizado a 'URL'.
        url += '@' + ','.join(str(_) for _ in coordinates[0][::-1]) + '/'
        return url

    def __post_init__(self) -> None:
=======
        # 'URL' base do Google Maps.
        url: str = "https://www.google.com.br/maps/dir/"
        # Adiciona as coordenadas, na ordem, à 'URL' do Google Maps.
        for index in order:
            url += ",".join(str(_) for _ in coordinates[index][::-1]) + "/"
        # Por fim, adiciona a coordenada a ser focada quando utilizado a 'URL'.
        url += "@" + ",".join(str(_) for _ in coordinates[0][::-1]) + "/"
        return url

    def __post_init__(self) -> NoReturn:
>>>>>>> bfa5ccc (Imp. rotas para N veiculos e novas coordenadas.)
        """Gera um exemplar de lixeiras inteligentes pós inicialização
        da classe."""
        self._generate_sample()
