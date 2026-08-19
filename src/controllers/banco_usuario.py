import os
import sys
import json
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.models import Usuario
from src.controllers.validacoes import Validacoes
from src.controllers.senhas import Senhas

class BancoUsuario(Validacoes):
    def __init__(self) -> None:
        self.__usuario = None
        self.__caminho_db =  Path.home()/'Documents'/'cofreSenha'/'db_usuario.json'
        self.__lista_usuarios = list()

    def criar_banco(self) -> None:
        if not os.path.exists(self.__caminho_db.parent):
            os.mkdir(self.__caminho_db.parent)

        if not os.path.exists(self.__caminho_db):
            with open(self.__caminho_db, 'x') as arquivo:
                print('Arquivo de Dados Criado Com Sucesso!')

    def gravar_usuario(self, usuario: Usuario) -> None:
        self.__usuario = usuario
        if os.path.exists(self.__caminho_db):
            self.__ler_usuarios()
            self.__lista_usuarios.append(
                {
                    "site": self.__usuario.nm_obs,
                    "usuario": self.__usuario.nm_usuario,
                    "senha": Senhas().codificar_senha(self.__usuario.nm_senha)
                }
            )
            self.__salvar_usuarios_json()

    def pesquisar_usuario(self, id_usuario: int|None, nm_usuario: str|None) -> None:
        self.__ler_usuarios()
        if id_usuario is not None:
            if not self._valida_numero_inteiro(id_usuario):
                print('O id_usuario inválido, Necessário informar um número inteiro!')
            self.__get_usuario_id(id_usuario)
            return None
        if nm_usuario is not None:
            if not self._valida_string(nm_usuario):
                print('O nm_usuario inválido, Necessário informar um texto!')
                return None
            self.__get_usuario_nm_usuario(nm_usuario)
        return None

    def pesquisar_usuarios(self) -> None:
        self.__ler_usuarios()
        if not self._valida_lista_vazia(self.__lista_usuarios):
            for id, user in enumerate(self.__lista_usuarios):
                self.__print_usuario(id + 1, user)

    def excluir_usuario(self, id_usuario: int) -> None:
        if os.path.exists(self.__caminho_db):

            self.__ler_usuarios()

            if not self._existe_indice_lista(self.__lista_usuarios, id_usuario - 1):
                print('ID usuário não existe!')
                return None
            
            if not self._valida_lista_vazia(self.__lista_usuarios):
                self.__lista_usuarios.pop(id_usuario - 1)
                self.__salvar_usuarios_json()

    def __ler_usuarios(self) -> None:
        if os.path.getsize(self.__caminho_db) > 0:
            with open(self.__caminho_db, 'r') as arquivo:
                self.__lista_usuarios = json.load(arquivo)

    def __salvar_usuarios_json(self) -> None:
         with open(self.__caminho_db, 'w') as arquivo:
            json.dump(
                self.__lista_usuarios,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

    def __get_usuario_id(self, id_usuario: int) -> None:
        if not self._valida_numero_inteiro(id_usuario):
            print('O id_usuario inválido, Necessário informar um número inteiro!')
            return None
        if self._valida_lista_vazia(self.__lista_usuarios):
            print(f'"id_usuario" não existe!')
            return None
        if not self._existe_indice_lista(self.__lista_usuarios, id_usuario - 1):
            print(f'ID informado não existe!')
            return None
        self.__print_usuario(id_usuario, dict())
        return None

    def __get_usuario_nm_usuario(self, nm_usuario: str) -> None:
        if not self._valida_string(nm_usuario):
            print('O nm_usuario inválido, Necessário informar um texto!')
            return None
        
        fl_nao_existe = True

        for id, usuario in enumerate(self.__lista_usuarios):
            if self._existe_valor_dicionario(usuario, nm_usuario):
                fl_nao_existe = False
                self.__print_usuario(id, usuario)
                break
            fl_nao_existe = True

        if fl_nao_existe:
            print(f'Usuário não localizado.')
            return None

    def __print_usuario(self, id: int, usuario: dict):
        if not usuario:
            print('*' * 50)
            print(f'ID: {id}')
            print('Site: ', self.__lista_usuarios[id - 1]['site'])
            print('Usuario: ', self.__lista_usuarios[id - 1]['usuario'])
            print('Senha: ', Senhas().decodificando_senha(
                    self.__lista_usuarios[id - 1]['senha']
                )
            )
            print('*' * 50)
        else:
            print('*' * 50)
            print(f'ID: {id}')
            print(f'Site: {usuario['site']}')
            print(f'Usuario: {usuario['usuario']}')
            print(f'Senha: {Senhas().decodificando_senha(usuario['senha'])}')
            print('*' * 50)


