# Readme - Aplicação Ettic Project

## Objetivo da aplicação

A aplicação Ettic (Ettic é um portmanteau de Reddit) tem como objetivo permitir que a comunidade da etic_Algarve partilhe informações sobre diferentes temas (spots), incluindo publicações, comentários e avaliações. Os utilizadores podem navegar pelos spots existentes, visualizar publicações e comentários, e também podem criar novas publicações e comentários.

## Justificação técnica da escolha da framework

A escolha da framework Django foi motivada por diversos factores:

- **Produtividade**: Oferece um conjunto abrangente de funcionalidades, como administração de base de dados, autenticação de utilizador e ORM, que ajudam a acelerar o desenvolvimento de aplicações web.

- **Documentação abrangente**: Possui uma documentação detalhada, que ajuda na aprendizagem e na resolução de problemas durante o desenvolvimento.

- **Comunidade ativa**: Possui diversos third party packages que nos permite ter acesso a inúmeras ferramentas para os mais diversos projetos.

- **Segurança**: Este inclui recursos de segurança integrados, como proteção contra injeção de SQL, CSRF, etc, o que ajuda a garantir a segurança da aplicação.

## Funcionalidades

- **Login e Registo de Utilizador**: Os utilizadores podem fazer login nas suas contas existentes ou criar novas contas.

- **Visualização de Spots, Posts e Comentários**: Os utilizadores podem navegar pelos spots existentes, visualizar os posts associados a cada spot e os seus comentários.

- **Criação de Posts**: Os utilizadores podem criar novos posts em spots específicos.

- **Criação de Comentários**: Os utilizadores podem adicionar comentários às postagens existentes.

- **Gestão de Conteúdos em CLI**: Os gestores do serviço poderam, ligados diretamente ao servidor, criar conteúdos para o site sem ser necessário uma UI visual através dos seguintes comandos: info(informação na db sobre spots e posts), createcomment (criação de comentários) e createpost (criação de posts).

## Processo de instalação

### Pré-requisitos

- Python 3.7 ou superior
- Docker

### Instalação

1. Clone o repositório do projeto:

    ```bash
    git clone https://github.com/JoaoCardosoDev/Etticproject-backend-2325
    cd Etticproject-backend-2325
    ```

2. Execute o Docker Compose para iniciar os contentores:

    ```bash
    docker-compose up -d
    ```

3. Aceda através do browser: 127.0.0.1:8000

### Como utilizar a aplicação

1. Ao aceder à aplicação, será direcionado para a página inicial, onde poderá visualizar todos os spots disponíveis.

2. Clique num spot para visualizar as publicações relacionadas a mesmo.

3. Pode criar uma nova publicação utilizando o formulário fornecido.

4. Para visualizar os detalhes de uma publicação específica, clique no título da publicação.

5. Também pode adicionar comentários às publicações existentes utilizando o formulário existente na página do spot.

6. Para encerrar a aplicação, execute o seguinte comando:

    ```bash
    docker-compose down
    ```

