from os import environ
from os.path import dirname, join

from dotenv import load_dotenv


class MissingDotEnv(Exception):
    """Exceção relacionada à não existência do arquivo '.env'."""
    pass

class Settings:
    """Responsável pelo carregamento das variáveis de ambiente."""

    @staticmethod
    def load_ors_token() -> str:
        """Carrega o Token de acesso, do 'OpenRouteService', 
        armazenado no arquivo '.env'.

        Raises:
            MissingDotEnv: Caso o arquivo '.env' não seja encontrado.

        Returns:
            str: O Token de acesso armazenado no arquivo '.env'.
        """

        # Carrega o arquivo '.env', no mesmo diretório deste arquivo.
        load_dotenv(join(dirname(__file__), '.env'))
        # Carrega a informação contida no '.env', com o nome "OPEN_ROUTE..."
        ors_token: str | None = environ.get("OPEN_ROUTE_SERVICE_TOKEN")
        # Verifica se a informação carregada possui algum valor.
        if ors_token:
            return ors_token
        raise MissingDotEnv(
            "[Settings.py]" \
            " O arquivo '.env' em '/Source/Config', não é válido."
        )
