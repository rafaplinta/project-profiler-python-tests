from pro_filer.actions.main_actions import show_disk_usage
import os
import math


def test_show_disk_usage_no_file(capsys):
    mock = {"all_files": []}
    show_disk_usage(mock)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"


def test_show_disk_usage_calculates_total_space_correctly(
    tmp_path, capsys, monkeypatch
):
    # crio os paths
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    # escrevo conteúdo nos meus arquivos temporários
    file1.write_text("Meu arquivo")
    file2.write_text("Conteúdo do arquivo 2")

    # converto eles de PosixPath para string
    file_1_path_str = str(file1)
    file_2_path_str = str(file2)

    context = {"all_files": [file_1_path_str, file_2_path_str]}

    total_size = os.path.getsize(file1) + os.path.getsize(file2)

    # Mock função _get_printable_file_path
    def mock_get_printable_file_path(file_path):
        file_path_str = str(file_path)
        if len(file_path_str) > 60:
            return file_path_str[:27] + "..." + file_path_str[-30:]
        else:
            return file_path_str + " " * (60 - len(file_path_str))

    monkeypatch.setattr(
        "pro_filer.cli_helpers._get_printable_file_path",
        mock_get_printable_file_path,
    )

    # instancio minha função com o contexto criado
    show_disk_usage(context)
    # capturo saída padrão com o capsys
    captured = capsys.readouterr()

    # aqui eu calculo a porcentagem e arrendondo para baixo com o math.floor
    file1_percentage = math.floor((os.path.getsize(file1) / total_size) * 100)
    file2_percentage = math.floor((os.path.getsize(file2) / total_size) * 100)

    # crio uma tupla com o path do arquivo e o seu tamanho,
    # pela qual vou iterar para encontrar a maior e a menor
    # percentagem
    file_percentages = [(file1, file1_percentage), (file2, file2_percentage)]

    # função para extrair a percentagem (index 1), de cada tupla
    def get_percentage(tuple_element):
        return tuple_element[1]

    # encontra o maior elemento
    largest_file, largest_percentage = max(
        file_percentages, key=get_percentage
    )

    # encontra o menor elemento
    smallest_file, smallest_percentage = min(
        file_percentages, key=get_percentage
    )
    # O método format() é usado para substituir os espaços reservados {}
    # em uma string pelos valores fornecidos como argumentos para o método.
    # https://www.w3schools.com/python/ref_string_format.asp
    expect_result = "'{}': {} ({}%)\n'{}': {} ({}%)\nTotal size: {}\n".format(
        mock_get_printable_file_path(largest_file),
        os.path.getsize(largest_file),
        largest_percentage,
        mock_get_printable_file_path(smallest_file),
        os.path.getsize(smallest_file),
        smallest_percentage,
        total_size,
    )

    # verifica se a saída capturada é igual à saída esperada,
    # ignorando espaços em branco
    assert captured.out.replace(" ", "") == expect_result.replace(" ", "")
