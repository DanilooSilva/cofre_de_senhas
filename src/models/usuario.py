class Usuario:
    def __init__(self, nm_usuario: str, nm_senha: str, nm_obs: str|None) -> None:
        self.__nm_usuario = nm_usuario
        self.__nm_senha = nm_senha
        self.__nm_site = nm_obs

    @property
    def nm_usuario(self):
        return self.__nm_usuario
    
    @nm_usuario.setter
    def nm_usuario(self, nm_usuario):
        self.__nm_usuario = nm_usuario

    @property
    def nm_senha(self):
        return self.__nm_senha
    
    @nm_senha.setter
    def nm_senha(self, nm_senha):
        self.__nm_senha = nm_senha

    @property
    def nm_obs(self):
        return self.__nm_site

    @nm_obs.setter
    def nm_obs(self, nm_obs):
        self.__nm_site = nm_obs

    
    
    

    

