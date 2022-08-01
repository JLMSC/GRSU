from os import environ
from dotenv import load_dotenv
from os.path import join, dirname
from Model.Caller.Caller import Caller
from dataclasses import dataclass, field

class MissingDotEnv(Exception):
    """Exceção relacionada à não existência do arquivo '.env'."""
    pass

class ORSTokenNotFound(Exception):
    """Exceção relacionada a um valor nulo do Token de Acesso do OpenRouteService."""
    pass

@dataclass
class Settings:
    """Responsável pelo carregamente das variáveis de ambiente."""

    # Token de acesso da API do OpenRouteService.
    open_route_service_token: Caller = field(init=False)

    def _update_ors_token(self, token: str | None):
        """Atualiza o token de acesso do OpenRouteService.

        Args:
            token (str | None): O novo Token de acesso.

        Raises:
            ORSTokenNotFound: Caso o Token de acesso não seja encontrado.
        """
        if token:
            self.open_route_service_token = Caller(token=token)
        else:
            raise ORSTokenNotFound("[Settings] Não foi possível carregar o Token de acesso do OpenRouteService.")

    def _dotenv_exists(self) -> bool:
        """Verifica se o arquivos .env existe.

        Raises:
            MissingDotEnv: Caso o arquivo '.env' não seja encontrado.

        Returns:
            bool: Retorna verdadeiro se as informações carregadas estejam corretas.
        """
        if environ.get("OPEN_ROUTE_SERVICE_TOKEN"):
            return True
        raise MissingDotEnv("[Settings] O arquivo '.env' não foi encontrado.")

    def __post_init__(self):
        """Carrega as variáveis de ambientes do arquivo .env."""
        # Carrega as variáveis do '.env' nas variáveis de ambiente.
        load_dotenv(join(dirname(__file__), '.env'))
        self._dotenv_exists()
        self._update_ors_token(environ.get("OPEN_ROUTE_SERVICE_TOKEN"))