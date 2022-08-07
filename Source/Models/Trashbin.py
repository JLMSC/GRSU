from dataclasses import dataclass, field
from random import uniform


@dataclass
class Trashbin:
    """Representação de uma lixeira inteligente."""

    max_volume: float = field(default_factory=float)
    coordinates: list[float] = field(default_factory=list)
    current_volume: float = field(init=False, default_factory=float)

    def _generate_random_volume(self) -> None:
        """Gera um volume aleatório à lixeira inteligente."""
        self.current_volume = uniform(0, self.max_volume)
    
    def is_full(self) -> bool:
        """Verifica se a lixeira inteligente está cheia.

        Returns:
            bool: Se o volume ultrapassou o limite.
        """
        return self.current_volume >= (self.max_volume * 80.0) / 100.0
    
    def get_coordinates(self) -> list[float]:
        """Retorna as coordenadas da lixeira inteligente.

        Returns:
            list[float]: As coordenadas da lixeira inteligente.
        """
        return self.coordinates
    
    def __post_init__(self) -> None:
        """Atualiza o volume da lixeira inteligente após inicializado."""
        self._generate_random_volume()
