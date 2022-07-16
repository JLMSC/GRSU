from random import uniform

class TrashBin:
    """Classe responsável pela representação de uma lixeira inteligente."""

    # Volume máximo da lixeira.
    trashbin_max_volume: float = 0.0

    # Volume atual da lixeira.
    trashbin_current_volume: float = 0.0

    # Coordenadas da lixeira.
    trashbin_coordinates: str = ""

    def __init__(self, max_volume: float = -1, coordinates: str = ""):
        """Inicializa as principais variáveis da lixeira."""
        if max_volume == -1:
            raise ValueError("O volume máximo da lixeira não foi definido.")
        if coordinates == "":
            raise ValueError("As coordenadas da lixeira não foram definidas.")
        
        self.trashbin_max_volume = max_volume
        self.trashbin_coordinates = coordinates
        self.trashbin_current_volume = self.generate_random_volume()

    def generate_random_volume(self) -> float:
        """Gera um volume aleatório para a lixeira."""
        return uniform(0, self.trashbin_max_volume)

    def check_volume(self) -> bool:
        """Verifica se a lixeira precisa ser coletada."""
        # Definido parâmetro de coleta se o volume for mair ou igual a 80% do total.
        trashbin_volume_limit = (self.trashbin_max_volume * 80.0) / 100.0
        return self.trashbin_current_volume >= trashbin_volume_limit
    
    def get_trashbin_coordinates(self) -> list[float]:
        """Retorna as coordenadas da lixeira."""
        return list(map(float, self.trashbin_coordinates.split(',')))
