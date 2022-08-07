from ortools.constraint_solver import pywrapcp, routing_enums_pb2

# Fonte :.
# https://developers.google.com/optimization/routing/tsp#dist_matrix_data

class NoSolutionFound(Exception):
    """Exceção retornada caso nenhuma solução seja gerada."""
    pass

def _create_data(time_matrix: list[list[float]]) -> dict:
    """Registra os dados do 'TSP'.

    Args:
        time_matrix (list[list[float]]): A matriz contendo o tempo entre
        as coordenadas.

    Returns:
        dict: O dado que acabou de ser craido.
    """

    # Converte os valores de 'time_matrix' para inteiro.
    converted_matrix = [list(map(int, i)) for i in time_matrix]
    return {
        # A matriz de tempo entre as coordenadas.
        'matrix': converted_matrix,
        # A quantidade de veículos.
        'num_vehicles': 1,
        # O índice da coordenada de origem e destino.
        'depot': 0
    }

def _get_routes(solution, routing, manager) -> list[int]:
    """Gera uma lista contendo a rota de cada veículo.

    Returns:
        list[int]: Uma lista contendo a ordem da rota.
    """
    routes = []
    for route_nbr in range(routing.vehicles()):
        index = routing.Start(route_nbr)
        route = [manager.IndexToNode(index)]
        while not routing.IsEnd(index):
            index = solution.Value(routing.NextVar(index))
            route.append(manager.IndexToNode(index))
            routes.append(route)
    return routes[0]

def TSP(time_matrix: list[list[float]]) -> list[int]:
    """Otimiza a ordem de coleta das lixeiras inteligentes.

    Args:
        time_matrix (list[list[float]]): A matriz de tempo entre as coordenadas.

    Returns:
        list[int]: Uma lista contendo a ordem da rota.
    """

    # Define os dados do problema, o 'manager' e o responsável pela rota.
    data = _create_data(time_matrix)
    manager = pywrapcp.RoutingIndexManager(
        len(data['matrix']), data['num_vehicles'], data['depot']
    )
    routing = pywrapcp.RoutingModel(manager)

    def callback(from_index, to_index):
        """Realiza a conversão de índice para objeto."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['matrix'][from_node][to_node]
    # Responsável por 'traduzir' os índices.
    transit_callback_index = routing.RegisterTransitCallback(callback)

    # Define os pesos das arestas.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Define os parâmetros de busca, focando no caminho de menor custo possível.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    # Tenta resolver o 'TSP' usando os parâmetros de busca.
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        return _get_routes(solution, routing, manager)
    raise NoSolutionFound(
        "[TSP.py] Não foi possível gerar uma solução."
    )

