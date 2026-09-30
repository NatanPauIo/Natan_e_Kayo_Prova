from __future__ import annotations
from datetime import date
import dis
class QuantidadeInvalidaError(Exception):
    """Exceção para quantidade inválida."""
class MedicamentoVencidoError(Exception):
    """Exceção para medicamento vencido."""


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
    def quantidade(self, quantia: int) -> None:
       
        if quantia <= 0:
            raise ValueError("A quantidade não pode ser um número negativo.")
        self._quantidade = quantia
        return

    @valor.setter
    def valor(self, quantia: float) -> None:
        if quantia <= 0:
            raise ValueError("O valor do medicamento deve ser positivo.")
        self._valor = quantia
        return

    @staticmethod
    def dias_para_vencer(data_validade: date) -> int:
        return data_validade - date.today()

    def __str__(self) -> str:
        return f"Medicamento: {self.nome}; Lote: {self.lote}; Quantidade: {self.quantidade}; Validade: {self.validade}"


    @classmethod
    def de_registro(cls, texto: str) -> Medicamento:
        nome, lote, validade, quantidade, valor = texto.split(";")
        ano, mes, dia = validade.split("-")
        validade = date(int(ano), int(mes), int(dia))
        return cls(nome, lote, validade, int(quantidade), float(valor))

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Medicamento):
            return NotImplemented

        return (self.lote == value.lote and self.nome == value.nome )

    def __repr__(self) -> str:
        return f"Medicamento(nome={self.nome!r}, " \
                f"valor={self.valor!r})"

    def dispensar(self,quantidade: int) -> None:
       if quantidade <= 0:
           raise QuantidadeInvalidaError("A quantidade a dispensar deve ser positiva.")
       if self.quantidade < quantidade:
           raise QuantidadeInvalidaError("Quantidade insuficiente em estoque.")
       if self.validade < date.today():
           raise MedicamentoVencidoError("O medicamento está vencido.")
       
       self.quantidade -= quantidade
       return 

    def repor(self,quantidade: int) -> None:
         if quantidade <= 0:
              raise ValueError("A quantidade a repor deve ser positiva.")
         
         self.quantidade += quantidade
         return

    def __lt__(self, outro: Medicamento) -> bool:
        if not isinstance(outro, Medicamento):
            return NotImplemented
        return self.validade < outro.validade

if __name__ == "__main__":
  
    #print(m1)  
    print("\n")
    m1 = Medicamento("Dipirona 500mg", "L2026A", date(2026, 12, 31), 100, 12.50)
    m2 = Medicamento.de_registro("Amoxicilina 500mg;L2026B;2026-10-15;40;18.90")
    print(f"Dados de m1: {m1}") # ex.: Dipirona 500mg (L2026A) - 100 un. - val. 31/12/2026
    print(f"Dados de m2: {m2}") # ex.: Amoxicilina 500mg (L2026B) - 40 un. - val. 15/10/2026

    print("\n")
    print("Dispensando 20 medicamentos de m1")
    m1.dispensar(20)
    print(f"Quantidade de m1: {m1.quantidade}")

    print("\n")
    try:
        m2.dispensar(999)
    except QuantidadeInvalidaError as erro:
        print(f"Erro esperado: {erro}")

    print("\n")
    vencido = Medicamento("Soro Fisiológico", "L2025X", date(2025, 1, 10), 10, 5.0)
    try:
        vencido.dispensar(1)
    except MedicamentoVencidoError as erro:
        print(f"Erro esperado: {erro}")

    print("\n")
    outro = Medicamento("Dipirona 500mg", "L2026A", date(2026, 1, 1), 1, 1.0)
    print(f"m1 é igual a outro? {m1 == outro}")

    print("\n")
    estoque = [m1, m2, vencido, outro]
    print("Exibindo lista ordenada por data (mais antigos primeiro): ")
    for lote in sorted(estoque):
        print(lote)
    
    print("\n")
    try:
        m1.quantidade = -5
    except ValueError as erro:
        print(f"Erro esperado: {erro}")
    
   