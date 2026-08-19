import base64

class Senhas:
    
    @classmethod
    def codificar_senha(cls, senha):
        senha_bytes = senha.encode('utf-8')
        bytes_base64 = base64.b64encode(senha_bytes)
        senha_base64 = bytes_base64.decode('ascii')
        return senha_base64

    @classmethod
    def decodificando_senha(cls, senha_codificada):
        bytes_base64 = senha_codificada.encode('ascii')
        bytes_senha = base64.b64decode(bytes_base64)
        senha = bytes_senha.decode('utf-8')
        return senha

