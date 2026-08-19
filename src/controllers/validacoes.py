class Validacoes:
    def __init__(self) -> None:
        pass

    def _valida_lista_vazia(self, lista: list) -> bool:
        if len(lista) == 0:
            return True
        return False

    def _existe_indice_lista(self, lista: list, indice: int) -> bool:
        if indice >= len(lista):
            return False
        return True

    def _existe_valor_dicionario(self, dicionario: dict, valor: str):
        if not valor in dicionario.values():
            return False
        return True

    def _valida_numero_inteiro(self, numero: int):
        if isinstance(numero, int):
            return True
        return False

    def _e_inteiro(self, numero: int|str|float):
        try:
            numero = int(numero)
            return True
        except ValueError:
            return False


    def _valida_string(self, texto: str):
        if isinstance(texto, str):
            return True
        return False