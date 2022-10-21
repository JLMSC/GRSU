from typing import Any, Dict, List, Union
from ortools.constraint_solver import pywrapcp, routing_enums_pb2

# Fonte :.
# https://developers.google.com/optimization/routing/tsp#dist_matrix_data
# https://developers.google.com/optimization/routing/vrp


class NoSolutionFound(Exception):
    """Exceção retornada caso nenhuma solução seja gerada."""

    pass


def _create_data(
    time_matrix: List[List[float]], vehicle_quantity: int
) -> Dict[str, Any]:
    """Registra os dados necessários para o 'TSP'.

    Args:
        time_matrix (List[List[float]]): A matriz contendo o tempo
        entre todas as coordenadas.
        vehicle_quantity (int): A quantidade de veículos.

    Returns:
        Dict[str, Any]: Um dicionário contendo as rotas para cada 'n'
        veículos.
    """
    # Converte os valores de 'time_matrix' para inteiro.
    converted_matrix = [list(map(int, i)) for i in time_matrix]
    return {
        # A matriz de tempo entre as coordenadas.
        "matrix": converted_matrix,
        # A quantidade de veículos.
        "num_vehicles": vehicle_quantity,
        # O índice (padrão) da coordenada de origem e destino.
        "depot": 0,
    }


def _get_routes(
    data: Any, solution: Any, routing: Any, manager: Any
) -> Dict[int, List[int]]:
    """Gera uma lista contendo a rota de cada veículo.

    Args:
        data (Any): Os dados gerados por '_create_data'.
        solution (Any): A solução encontrada.
        routing (Any): Variável responsável pelas rotas (grafos).
        manager (Any): Variável responsável pela definição das demais
        variáveis.

    Returns:
        Dict[List[int]]: Um dicionário contendo as rotas dos 'n' veículos.
    """
    # Dicionário, o qual conterá as rotas de todos os 'n' veículos.
    vehicle_routes = {}
    # Itera sobre os 'n' veículos.
    for vehicle_id in range(data["num_vehicles"]):
        # Cria uma lista para determinado veículo.
        vehicle_routes[vehicle_id] = []
        # O índice de começo da rota.
        index = routing.Start(vehicle_id)
        # Itera ate o índice ser o final da rota.
        while not routing.IsEnd(index):
            # Adiciona a próxima coordenada a ser visitada
            # à lista da rota de um determinado veículo.
            vehicle_routes[vehicle_id].append(manager.IndexToNode(index))
            # Altera o índice da posição atual (na rota).
            index = solution.Value(routing.NextVar(index))
        # Adiciona o útlimo índice (posição final) da rota.
        vehicle_routes[vehicle_id].append(manager.IndexToNode(index))
    return vehicle_routes


def TSP(time_matrix: List[List[float]], vehicle_quantity: int) -> Dict[int, List[int]]:
    """Otimiza a ordem de coleta das lixeiras inteligentes.

    Args:
        time_matrix (List[List[float]]): A matriz de tempo entre as coordenadas.
        vehicle_quantity (int): A quantidade de veículos.

    Raises:
        NoSolutionFound: Caso o algoritmo não encontra nenhuma solução
        para determinado trajeto com 'n' veículos.

    Returns:
        Dict[List[int]]: Um dicionário contendo as rotas dos 'n' veículos.
    """

    # Define os dados do problema, o 'manager' e o responsável pela rota.
    data = _create_data(time_matrix, vehicle_quantity)
    manager = pywrapcp.RoutingIndexManager(
        len(data["matrix"]), data["num_vehicles"], data["depot"]
    )
    routing = pywrapcp.RoutingModel(manager)

    def callback(from_index: Any, to_index: Any) -> Union[int, float]:
        """Realiza a conversão de índice para objeto."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["matrix"][from_node][to_node]

    # Responsável por 'traduzir' os índices.
    transit_callback_index = routing.RegisterTransitCallback(callback)

    # Define os pesos das arestas.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Adiciona a restrição de tempo.
    dimension_name = "Time"
    routing.AddDimension(
        transit_callback_index,
        0,  # Sem voltar.
        # FIXME: Definir uma maneira de se gerar um "tempo máximo de rota" para os 'n' veículos.
        10000,  # Tempo máximo atribuído a cada veículo.
        True,  # Começar do 'depot'.
        dimension_name,
    )
    time_dimension = routing.GetDimensionOrDie(dimension_name)
    time_dimension.SetGlobalSpanCostCoefficient(100)

    # Adiciona a primeira heurísitca à solução.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    # Soluciona o problema.
    solution = routing.SolveWithParameters(search_parameters)

    # Informa a solução, se houver.
    if solution:
        return _get_routes(data, solution, routing, manager)
    raise NoSolutionFound("[TSP.py] Não foi possível gerar uma solução.")
