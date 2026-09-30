from __future__ import annotations
from datetime import date

class Medicamento:
    def __init__(self, nome: str, lote: str, validade: date, quantidade: int, valor: float):
        self.nome = nome
        self.lote = lote
        self.validade = validade
        self.quantidade = quantidade
        self.valor = valor

    @property
    def quantidade(self) -> int:
        return self._quantidade
    @property
    def valor(self) -> float:
        return self._valor

    @quantidade.setter
    def quantidade(self, disponivel: int) -> None:
        if disponivel <= 0:
            raise ValueError("A quantidade não pode ser um número negativo.")
        self._quantidade = disponivel

    