from typing import Any, Dict, NoReturn, List, Optional
from Source.Config.Settings import Settings
from Source.Models.Model import Model
from Source.Scripts.TSP import TSP
from Source.Tools.Caller import Caller

from time import time, sleep
from multiprocessing import Process


def main(ors_api: Caller, model: Model, n: int) -> NoReturn:
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
        trashbins=model.get_fixed_trashbins(n)
    )

    start_time = time()
    # Requisita uma matriz de distância e tempo entre as coordenadas.
    # Matriz de distância : matrix['distances']
    # Matriz de tempo : matrix['durations']
    matrix: Any = ors_api.request_matrix(coordinates=trashbins_coords)
    print(f"Matrix time: {time() - start_time}s")

    start_time = time()
    # Todas as 'n' rotas para os 'n' veículos.
    vehicle_routes: Dict[int, List[int]] = TSP(
        time_matrix=matrix["durations"],
        # FIXME: Automatizar a quantia de veículos, ou solicitar "input".
        vehicle_quantity=2,
    )
    print(f"Algorithm time: {time() - start_time}s")

def test_maximum(start: int, end: int, limit: int, verbose: bool = True) -> Optional[int]:
    for i in range(start, end):
        proc = Process(target=main, args=(Caller(Settings.load_ors_token()), Model(), i))
        # start process (and timer)
        start_time = time()
        proc.start()
        # join when limit is reached (or before)
        proc.join(limit)
        # calculate timer result (for verbose)
        result_time = time() - start_time
        # if it is still running, the maximum was reached
        if result_time > limit:
            proc.terminate()
            return i
        # guarantee the process is terminated
        proc.terminate()
        while proc.is_alive():
            pass
        # print result (if verbose is true)
        if verbose:
            print(f"{i}: {result_time}")
    return None


if __name__ == "__main__":
    max_reached: Optional[int] = test_maximum(start=1, end=300, limit=3000)
    print(f"Maximum reached: {max_reached or 'No limit was reached'}")
