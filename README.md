# Hackathon CNJ - Equipe Inova Ixtepô

Este repositório contém os códigos da equipe **Inova Ixtepô** envolvendo a reunião de execuções com o foco na Justiça do Trabalho.

## Organização do projeto

O projeto é organizado em três subprojetos:

1. [Pré-processamento da base de dados](#instruções-para-o-subprojeto-de-pré-processamento-da-base-de-dados)
2. [APIs para reunião de execuções](#instruções-para-o-subprojeto-das-apis-para-reunião-de-execuções)
3. [Plataforma Web para interação com o usuário](#instruções-para-o-subprojeto-da-plataforma-web)

Nesse subprojetos utilizamos a linguagem `Python 3` em conjunto com o gerenciador de pacotes `pip` e ambientes virtuais criados utilizando o `conda`.


## Instruções para o subprojeto de *Pré-processamento da base de dados*

1. Descompacte todas as pastas relacionadas a justiça do trabalho.

1. Mova as pastas descompactadas da justiça do trabalho (`processos-trtXX`) para dentro da pasta `database_processing/data/justica_trabalho/`.

1. Mova o arquivo `mpm_serventias.csv` para a pasta `database_processing/data/`

1. Abra um terminal apontando para a pasta `database_processing/`.

1. Crie um ambiente usando o comando e depois ative com os comandos:

    ```
    conda create -n data_proc_env python=3.7 pylint
    conda activate data_proc_env
    ```

1. Instale as dependências com o seguinte comando.

    ```
    pip install -r requirements.txt
    ```

1. Execute o processamento da base utilizando o comando:

    ```
    python database_processing.py
    ```

1. Nessa etapa serão criadas duas bases, sendo uma relacionada a um conjunto de CNPJs fictícios, mas válidos, e outra contendo uma versão mais enxuta da base de dados proveniente do Datajud.

1. Após concluído, mova os arquivos de nome `db.json` e `processos.json` da pasta `database_processing/data/`  para a pasta externa (no primeiro nível) `data/`. 


## Instruções para o subprojeto das *APIs para reunião de execuções*

Para rodar esse subprojeto, siga as seguintes etapas:

1. Abra um terminal apontando para a pasta `web_api/`.

1. Crie um ambiente e depois ative com os comandos:

    ```
    conda create -n web_api_env python=3.7 pylint
    conda activate web_api_env
    ```

1. Instale as dependências com o seguinte comando.

    ```
    pip install -r requirements.txt
    ```

1. Verifique o arquivo `GroupAPI.yaml`, e certifique que o campo `RootDataDir` aponta para a pasta `data` (externa ao diretório atual) e certifique que os arquivos `db.json` e `processos.json` foram copiados para dentro da referida pasta seguindo os passos da seção anterior.

1. Rode a API com o comando:

    ```
    python GroupAPI.py
    ```

1. Mantenha o terminal aberto para poder utilizar a interface de usuário.

1. É possível visualizar a documentação da API acessando o link:
   http://0.0.0.0:5610/

## Instruções para o subprojeto da *Plataforma Web*

1. Para executar essa parte do projeto é necessário ter o NodeJS instalado.

1. Após instalado, abra um terminal na pasta `client`

1. Execute o comando para instalar as dependências

    ```
    npm install
    ```

1. Execute o comando para rodar a plataforma.

    ```
    npm run serve
    ```

1. Então a plataforma inicializará com uma lista pré-carregada de processos e funcionará conforme o vídeo.







