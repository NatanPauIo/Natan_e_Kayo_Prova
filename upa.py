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

    @classmethod
    def de_registro(cls, texto: str) -> Medicamento:
        nome, lote, validade, quantidade, valor = texto.split(";")
        d, m, a = validade.split("/")
        return cls(nome, lote, date(int(a), int(m), int(d)), int(quantidade), float(valor))

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Medicamento):
            return NotImplemented

        return (self.lote == value.lote and self.nome == value.nome )

    def __repr__(self) -> str:
        return f"Medicamento(nome={self.nome!r}, " \
                f"preco={self.preco!r})"

if __name__ == "__main__":
    m1 = Medicamento("Dipirona", "A123", date(2024, 12, 31), 10, 5.0)
    m2 = Medicamento("Dipirona", "A123", date(2024, 12, 31), 10, 5.0)
    print(m1 == m2)  # True
    print([m1])        # Medicamento(nome='Dipirona', preco=5.0)
    