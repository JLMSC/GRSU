from random import uniform
from dataclasses import dataclass, field

@dataclass
class Trashbin:
    """Representa uma lixeira inteligente."""

    # O volume máximo da lixeira inteligente.
    max_volume: float = field(default_factory=float)
    # O volume atual da lixeira inteligente.
    current_volume: float = field(init=False, default_factory=float)
    # As coordenadas da lixeira inteligente.
    coordinates: list[float] = field(default_factory=list)

    def generate_random_volume(self) -> float:
        """Gera um volume aleatório para a lixeira inteligente.

        Returns:
            float: Um valor fracionário entre zero e o volume máximo da lixeira.
        """
        return uniform(0, self.max_volume)

    def is_full(self) -> bool:
        """Verifica se a lixeira inteligente está cheia.

        Returns:
            bool: Se a lixeira ultrapassou o limite.
        """
        return self.current_volume >= (self.max_volume * 80.0) / 100.0

    def get_coordinates(self) -> list[float]:
        """Retorna as coordenadas da lixeira inteligente.

        Returns:
            list[float]: As coordenadas da lixeira inteligente.
        """
        return self.coordinates

    def __post_init__(self):
        """Inicializa os demais atributos."""
        self.current_volume = self.generate_random_volume()
