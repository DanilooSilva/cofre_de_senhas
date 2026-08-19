# dtbasePassword

Este projeto é um aplicativo em Python para armazenar credenciais de forma simples, com interface por terminal. Ele foi desenvolvido exclusivamente para fins de estudos e aprendizagem, como exemplo de organização de código em camadas, usando modelos, views e controllers.

## Objetivo

O projeto demonstra, de forma prática, o uso de:

- programação orientada a objetos em Python;
- separação por camadas (models, views e controllers);
- leitura e gravação de dados em arquivo JSON;
- interação via terminal.

## Funcionalidades

O programa permite:

- cadastrar um novo site, usuário e senha;
- buscar um usuário pelo ID;
- buscar um usuário pelo nome de usuário;
- listar todos os registros cadastrados;
- excluir um usuário pelo ID.

Ao iniciar, o sistema cria automaticamente o arquivo de dados em:

```text
Documents/cofreSenha/db_usuario.json
```

## Estrutura do projeto

```text
main.py
requirements.txt
src/
  controllers/
    banco_usuario.py
    senhas.py
    validacoes.py
  models/
    usuario.py
  views/
    index.py
db/
build/
```

## Requisitos

- Python 3.10 ou superior

## Como executar

Na raiz do projeto, execute:

```bash
python main.py
```

## Como usar

1. Execute o programa.
2. Escolha uma das opções do menu.
3. Para salvar uma senha, informe o site, o usuário e a senha.
4. A senha será solicitada sem exibir o texto digitado no terminal.

## Dependências

Não há dependências externas instaladas via pip neste projeto. O arquivo requirements.txt está presente, mas atualmente sem bibliotecas adicionais.

## Geração de executável

Também é possível gerar um executável com o PyInstaller:

```bash
pyinstaller --onefile main.py -n cofreSenhas
```

## Observação sobre segurança

Este projeto foi criado apenas para fins didáticos e de estudo.

As senhas são codificadas em Base64, o que não constitui uma proteção real para armazenamento de credenciais. Por isso:

- não use este projeto para guardar senhas reais;
- não confie neste sistema como uma solução segura de gerenciamento de senhas;
- trate a aplicação apenas como uma demonstração de lógica e organização de código.

