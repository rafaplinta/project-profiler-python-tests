# Pro Filer 🕵️‍♂️

## Sobre:

O Pro Filer é uma aplicação de linha de comando (CLI) que gera relatórios com base em um caminho (diretório ou arquivo) fornecido como entrada. Este projeto foi desenvolvido como parte das avaliações do curso de Desenvolvimento Web da Trybe - Especialização em Python.

Meus objetivos principais foram:
- Identificar e corrigir bugs nas funções já implementadas `show_deepest_file` e `find_file_by_name`.
- Desenvolver testes usando o **pytest** para as funções já implementadas `show_preview`, `show_details`, `show_disk_usage` e `find_duplicate_files`.

## Iniciando o projeto:

1. Clone o repositório:

    ```bash
    git clone git@github.com:rafaplinta/project-profiler-python-tests.git
    ```

2. Crie e acesse o ambiente virtual `venv`:

    ```bash
    python3 -m venv .venv && source .venv/bin/activate
    ```

3. Instale as dependências:

    ```bash
    python3 -m pip install -r dev-requirements.txt
    ```

## Executando a aplicação:

1. Configure o auto-complete da aplicação:

    ```bash
    pro-filer --install-completion
    ```

    Reinicie o terminal.

2. Execute o comando `pro-filer` seguido de um caminho (diretório ou arquivo) e uma ação. Por exemplo:

    ```bash
    pro-filer . preview
    ```

    Isso gerará um relatório de pré-visualização para o diretório atual.

---

**Observação**: Certifique-se de adaptar os comandos e URLs para refletir o seu repositório e a sua estrutura de projeto.


