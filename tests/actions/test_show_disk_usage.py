from pro_filer.actions.main_actions import show_disk_usage
import os


def write_file(tmp_path, file_name, content=""):
    file_path = tmp_path / file_name
    with open(file_path, "w") as file:
        file.write(content)
    return file_path


def test_show_details_all_info(capsys, tmp_path, monkeypatch):
    file_1_path = write_file(tmp_path, "my_app.py", "Conteúdo do meu arquivo")
    file_2_path = write_file(tmp_path, "new_file.py")

    context = {"all_files": [file_1_path, file_2_path]}

    total_size = os.path.getsize(file_1_path) + os.path.getsize(file_2_path)

    show_disk_usage(context)

    # Mock função _get_printable_file_path
    def mock_get_printable_file_path(file_path):
        file_path_str = str(file_path)
        if len(file_path_str) > 60:
            return file_path_str[:27] + "..." + file_path_str[-30:]
        else:
            return file_path_str

    monkeypatch.setattr(
        "pro_filer.cli_helpers._get_printable_file_path",
        mock_get_printable_file_path,
    )

    captured = capsys.readouterr()

    expect_result = (
        f"'{mock_get_printable_file_path(file_1_path)}':".ljust(70)
        + f"{os.path.getsize(file_1_path)} (100%)\n"
        + f"'{mock_get_printable_file_path(file_2_path)}':".ljust(70)
        + f"{os.path.getsize(file_2_path)} (0%)\n"
        + f"Total size: {total_size}\n"
    )

    assert captured.out == expect_result
