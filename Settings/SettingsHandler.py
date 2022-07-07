from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

class SettingsHandler:
    """Classe responsável pelo carregamento do arquivo '.env'."""

    # Caminho do arquivo '.env'.
    dotenv_path: str | bytes = ""

    # Token de acesso do 'OpenRouteService'.
    open_route_service_token: str | None = ""

    def __init__(self):
        """Carrega as variáveis de ambiente."""
        try:
            self.dotenv_path = join(dirname(__file__), '.env')
            load_dotenv(self.dotenv_path)
            # Carrega as informações do '.env' na variável da classe.
            self.open_route_service_token = environ.get("OPEN_ROUTE_TOKEN")
        except Exception:
            raise Exception("Algo inesperado aconteceu.")
        finally:
            if self.open_route_service_token is None:
                raise ValueError("Não foi possível carregar o token do OpenRouteService.")

