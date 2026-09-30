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

    @valor.setter
    def valor(self, quantia: float) -> None:
        if quantia <= 0:
            raise ValueError("O valor do medicamento deve ser positivo.")
        self._valor = quantia

  #  @classmethod
   # def de_registro(cls, linha: str) -> "Medicamento":
    #    nome, lote, validade, quantidade ,valor_str = linha.split(";")
     #   return cls(int(nome.strip()), lote.strip(), validade.strip(), int(quantidade), float(valor_str.strip()))

    @staticmethod
    def dias_para_vencer(data_validade: date) -> int:
        return data_validade - date.today()

    def __str__(self) -> str:
        return f"Medicamento: {self.nome}; Lote: {self.lote}; Quantidade: {self.quantidade}; Validade: {self.validade}"

