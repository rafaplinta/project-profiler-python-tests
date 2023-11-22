"""Arquivo que estudantes devem editar"""


# essa função recebe o caminho de parâmetro e conta os /
def count_slashes(path):
    return path.count("/")


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = max(context["all_files"], key=count_slashes)
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive:
            file_name.lower()
            search_term.lower()

        if search_term in file_name:
            found_files.append(path)

    return found_files


# Exemplo 1:
context1 = {
    "all_files": [
        "/home/trybe/Downloads/trybe_logo_pequena.png",
        "/home/trybe/Documents/aula/python/tests.txt",
    ]
}

show_deepest_file(context1)
# Saída esperada:
# Deepest file: /home/trybe/Documents/aula/python/tests.txt
