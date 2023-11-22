from pro_filer.actions.main_actions import show_details
import os  # o módulo os interage com o sistema operacional
# https://docs.python.org/3/library/os.path.html
from datetime import datetime


# teste para quando o arquivo não existe
def test_show_details_file_not_exists(capsys):
    mock = {"base_path": "/nonexistent_file.txt"}
    show_details(mock)
    captured = capsys.readouterr()
    assert captured.out == "File 'nonexistent_file.txt' does not exist\n"


# teste para quando o arquivo existe e está tudo certo
def test_show_details_all_info(capsys, tmp_path):
    # aqui crio um file temorário no meu diretório temporário
    tmp_file_path = tmp_path / "my_file.txt"
    with open(tmp_file_path, "w") as tmp_file:
        # aqui obtenho a data de última modificação formatada como string
        last_modified_date = datetime.fromtimestamp(
            os.path.getmtime(tmp_file_path)
        ).strftime("%Y-%m-%d")
        tmp_file.write(
            f"File name: my_file.txt\n"
            f"File size in bytes: {os.path.getsize(tmp_file_path)}\n"
            "File type: file\n"
            "File extension: .txt\n"
            f"Last modified date: {last_modified_date}\n"
        )
    # chama a função a passa como padrão o caminho do arquivo temporário
    show_details({"base_path": str(tmp_file_path)})

    # captura a saída padrão
    captured = capsys.readouterr()
    expected_output = (
        f"File name: my_file.txt\n"
        f"File size in bytes: {os.path.getsize(tmp_file_path)}\n"
        "File type: file\n"
        "File extension: .txt\n"
        f"Last modified date: {last_modified_date}\n"
    )
    assert captured.out == expected_output


# test para caso de arquivo sem extensão
def test_show_details_no_extension(capsys, tmp_path):
    tmp_file_path = tmp_path / "no_extension"
    with open(tmp_file_path, "w") as tmp_file:
        last_modified_date = datetime.fromtimestamp(
            os.path.getmtime(tmp_file_path)
        ).strftime("%Y-%m-%d")
        tmp_file.write(
            f"File name: no_extension\n"
            f"File size in bytes: {os.path.getsize(tmp_file_path)}\n"
            "File type: file\n"
            "File extension: [no extension]\n"
            f"Last modified date: {last_modified_date}\n"
        )
    show_details({"base_path": str(tmp_file_path)})

    captured = capsys.readouterr()
    expected_output = (
        f"File name: no_extension\n"
        f"File size in bytes: {os.path.getsize(tmp_file_path)}\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        f"Last modified date: {last_modified_date}\n"
    )
    assert captured.out == expected_output
