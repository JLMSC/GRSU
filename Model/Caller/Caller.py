from json import loads
from typing import Any
from requests import Response, post
from dataclasses import dataclass, field

# URL base do OpenRouteService.
ORS_BASE_URL = "https://api.openrouteservice.org"

# Endpoint das matrizes de distância e tempo.
ORS_MATRIX = f"{ORS_BASE_URL}/v2/matrix/driving-hgv"

# Endpoint da geração de rota.
ORS_ROUTE = f"{ORS_BASE_URL}/v2/directions/driving-hgv"

class HTTPResponseError(Exception):
    """Exceção relacionada as respostas dos 'requests'."""
    pass

@dataclass
class Caller:
    """Responsável pelos 'requests' no OpenRouteService."""

    # Token de acesso da API do OpenRouteService.
    token: str = field(default_factory=str)
    # Parâmetros de acesso ao OpenRouteService.
    headers: dict[str, str | bytes] = field(init=False, default_factory=dict)

    def _is_response_valid(self, response: Response) -> Any:
        """Verifica o código de resposta do 'request'.

        Args:
            response (Response): A resposta do 'request'.

        Raises:
            HTTPResponseError: Caso o código de resposta do 'request' seja inválido.

        Returns:
            Any: Retorna o conteúdo do 'request' se o código de resposta estiver válido.
        """
        if response.status_code == 200:
            return loads(response.text)
        raise HTTPResponseError(f"[Caller] Código retornado: {response.status_code}")

    def _update_headers(self):
        """Atualiza os 'headers'."""
        self.headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
            'Authorization': self.token,
            'Content-Type': 'application/json; charset=utf-8'
        }
    
    def request_matrix(self, coordinates: list[list[float]]) -> Any:
        """Retorna a matriz de tempo e distância entre as coordenadas.

        Args:
            coordinates (list[list[float]]): As coordenadas das lixeiras inteligentes.

        Returns:
            Response: Retorna o conteúdo do 'request', contendo os tempos e as distâncias.
        """
        # Parâmetros adicionais do 'request' da matriz de tempo e distância entre as coordenadas.
        body_parameters = {
            # As coordenadas.
            'locations': coordinates,
            # As informações que serão incluidas na matriz.
            'metrics': ['distance', 'duration']
        }
        return self._is_response_valid(
            post(
                ORS_MATRIX,
                json=body_parameters,
                headers=self.headers
            )
        )
    
    def request_route(self, coordinates: list[list[float]]) -> Any:
        """Gera uma rota para todas as coordenadas.

        Args:
            coordinates (list[list[float]]): As coordenadas.

        Returns:
            Any: Retorna o conteúdo do 'request', contendo a rota gerada.
        """
        # Parâmetros adicionais do 'request' da rota.
        body_parameters = {
            # As coordenadas.
            'coordinates': coordinates
        }
        return self._is_response_valid(
            post(
                ORS_ROUTE,
                json=body_parameters,
                headers=self.headers
            )
        )

    def __post_init__(self):
        """Inicializa os principais métodos e atributos."""
        self._update_headers()
