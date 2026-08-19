from src.controllers import BancoUsuario, Validacoes
from src.models import Usuario
from getpass import getpass

class Index(Validacoes):
    def __init__(self) -> None:
        self.__acoes_print = {
            '1': 'Salvar um novo usuário e senha.',
            '2': 'Buscar usuário e senha pelo ID',
            '3': 'Buscar usuario e senha pelo nm_usuario',
            '4': 'Buscar todos usuários',
            '5': 'Excluír usuário pelo ID',
            '0': 'Sair'
        }
        self.__exec_acoes = None

    def inicio(self) -> None:
        self.__db = BancoUsuario()
        self.__db.criar_banco()
        print('=' * 25 + 'Cofre de Senhas' + '=' *25)
        while True:
            print('=' * 25 + '=' * len('Cofre de Senhas') + '=' *25)
            for chave, valor in self.__acoes_print.items():
                print(f'{chave} - {valor}')
            
            print('=' * 25 + '=' * len('Cofre de Senhas') + '=' *25)

            acao = input('Digite qual Ação: ')

            if not self._e_inteiro(numero=acao):
                raise ValueError('Necessário informa um número inteiro!')
            
            self.__exec_acoes = {
                '1': lambda: self.__salvar_usuario(),
                '2': lambda: self.__pesquisa_usario_id(),
                '3': lambda: self.__pesquisa_usuario_nm_usuario(),
                '4': lambda: self.__db.pesquisar_usuarios(),
                '5': lambda: self.__excluir_usuairo_id(),
                '0': lambda: exit()
            }

            exec_acao = self.__exec_acoes.get(acao) if \
                self.__exec_acoes.get(acao) is not None else \
                    self.__exec_acoes['0']

            if exec_acao is not None:
                exec_acao()

    def __salvar_usuario(self):
        nm_site = input('Site: ')
        nm_usuario = input('Usuario: ')
        nm_senha = getpass('Senha: ')
        self.__db.gravar_usuario(Usuario(nm_usuario, nm_senha, nm_site))
        
    def __pesquisa_usario_id(self):
        id_usuario = input('Digite id usuario: ')
        id_usuario = self.__convert_numero_str_para_inteiro(id_usuario)
        self.__db.pesquisar_usuario(id_usuario=id_usuario, nm_usuario=None)

    def __pesquisa_usuario_nm_usuario(self):
        nm_usuario = input('Digite seu usuario: ')
        self.__db.pesquisar_usuario(id_usuario=None, nm_usuario=nm_usuario)

    def __excluir_usuairo_id(self):
        id_usuario = input('Digite id usuario: ')
        id_usuario = self.__convert_numero_str_para_inteiro(id_usuario)
        self.__db.excluir_usuario(id_usuario)

    def __convert_numero_str_para_inteiro(self, nr_texto: str) -> int:
        if not self._e_inteiro(nr_texto):
            print(
                'Não foi possível converter o valor informado em um número inteiro'
            )
        
        return int(nr_texto)




if __name__ == '__main__':
    Index().inicio()
        
        

    