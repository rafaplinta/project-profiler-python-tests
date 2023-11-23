from pro_filer.actions.main_actions import show_disk_usage
import os


# Teste função com parâmetro vazio
def test_show_disk_usage_no_file(capsys):
    mock = {"all_files": []}
    show_disk_usage(mock)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"


# função que cria arquivo
def write_file(tmp_path, file_name, content=""):
    file_path = tmp_path / file_name
    with open(file_path, "w") as file:
        file.write(content)
    return file_path


def test_show_details_all_info(capsys, tmp_path, monkeypatch):
    # passo o path e crio os arquivos temporários
    # isso me retornará objetos do tipo PosixPath
    file_1_path = write_file(tmp_path, "my_app.py", "Conteúdo do meu arquivo")
    file_2_path = write_file(tmp_path, "new_file.py")

    # aqui eu transformo os objetdos gerados do tipo PosixPath em strings para
    # que a função get_printable_file_path os aceite
    file_1_path_str = str(file_1_path)
    file_2_path_str = str(file_2_path)

    # crio o dicionário que será passado como parâmetro
    context = {"all_files": [file_1_path_str, file_2_path_str]}

    # aqui obtenho o tamanho total dos arquivos recebidos como parâmetro
    total_size = os.path.getsize(file_1_path) + os.path.getsize(file_2_path)

    # Mock função _get_printable_file_path
    def mock_get_printable_file_path(file_path):
        file_path_str = str(file_path)
        if len(file_path_str) > 60:
            return file_path_str[:27] + "..." + file_path_str[-30:]
        else:
            return file_path_str

    # ordena os arquivos com base no tamanho
    sorted_files = sorted(
        context["all_files"],
        key=lambda file_path: os.path.getsize(file_path),
        reverse=True,
    )

    # substitui a lista original pela versão ordenada
    context["all_files"] = sorted_files

    # chamo a função mockada no lugar da real usando o monkeypatch
    monkeypatch.setattr(
        "pro_filer.cli_helpers._get_printable_file_path",
        mock_get_printable_file_path,
    )

    # instancio minha função
    show_disk_usage(context)
    # leio a saída padrão com o capsys
    captured = capsys.readouterr()

    expect_result = (
        f"'{mock_get_printable_file_path(file_1_path)}': "
        + f"{os.path.getsize(file_1_path)} (100%)\n"
        + f"'{mock_get_printable_file_path(file_2_path)}': "
        + f"{os.path.getsize(file_2_path)} (0%)\n"
        + f"Total size: {total_size}\n"
    )

    # verifica se todas as linhas da saída esperada estão presentes na saída
    assert all(
        # remove espaços em branco e verifica se a presença da saida esperada
        line.strip() in captured.out.replace(" ", "").strip()
        # itera sobre cada linha da saída esperada
        for line in expect_result.replace(" ", "").strip().split("\n")
    )
