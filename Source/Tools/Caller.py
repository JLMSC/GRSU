from dataclasses import dataclass, field
from json import loads
from typing import Any, NoReturn

from requests import Response, post

# Endpoint da API de matrizes, do 'OpenRouteService'.
# MATRIX_DOMAIN: str = f"https://api.openrouteservice.org/v2/matrix/driving-hgv"
#MATRIX_DOMAIN: str = f"https://api.openrouteservice.org/v2/matrix/driving-car"
MATRIX_DOMAIN: str = f"http://localhost:8080/ors/v2/matrix/driving-car"


class HTTPResponseError(Exception):
    """Exceção relacionada ao código de resposta dos 'requests'."""

    pass


class NoTrashToCollect(Exception):
    """Exceção relacionada à não existência de lixeiras inteligentes que
    precisam ser coletadas."""

    pass


@dataclass
class Caller:
    """Responsável pelas requisições na 'API' do 'OpenRouteService'."""

    # Token de acesso à 'API' do 'OpenRouteService'.
    token: str = field(default_factory=str)

    def _check_request_status(self, status_code: int) -> bool:
        """Verifica o código de status de uma requisição.

        Args:
            status_code (int): O valor do código de status de uma requisição.

        Raises:
            HTTPResponseError: Caso o código de status de uma requisição
            seja diferente de 'OK'.

        Returns:
            bool: Verdadeiro se o código de status for 'OK'.
        """

        if status_code == 200:
            return True
        raise HTTPResponseError(
            f"[Caller.py] " + f"Chamada inválida, código retornado: {status_code}"
        )

    def request_matrix(self, coordinates: list[list[float]]) -> Any:
        """Faz a requisição de uma matriz, com a distância e tempo
        entre todas as coordenadas.

        Args:
            coordinates (list[list[float]]): As coordenadas.

        Returns:
            Any: A distância (em metros) e o tempo (em segundos).
        """

        # Indica que as coordenadas não possuem nenhuma lixeira inteligente.
        if len(coordinates) == 2:
            raise NoTrashToCollect(
                "[Caller.py] Nenhuma lixeira precisa ser coletada no momento."
            )

        # Parâmetros adicionais referentes à requisição da matriz.
        additional_parameters: dict = {
            "locations": coordinates,
            "metrics": ["distance", "duration"],
        }
        # Faz a chamada passando os parâmetros adicionais.
        response: Response = post(
            MATRIX_DOMAIN, json=additional_parameters, headers=self.headers
        )
        #print(response.text)
        if self._check_request_status(response.status_code):
            return loads(response.text)

    def __post_init__(self) -> None:
        """Configura os 'headers' pós inicialização da classe."""

        # Configura os 'headers'.
        self.headers = {
            "Accept": "application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8",
            "Authorization": self.token,
            "Content-Type": "application/json; charset=utf-8",
        }
