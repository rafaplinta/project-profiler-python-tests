from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest

# Perguntar na mentoria se tem um jeito de fazer com parametrize!!


# teste para arquivos que não existem
def test_find_duplicate_no_files():
    mock = {
        "all_files": [
            ".gitignore",
            "src/app.py",
            "src/utils/__init__.py",
        ]
    }
    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(mock)


# teste para arquivos diferentes
def test_find_duplicate_files_all_different(tmp_path):
    # crio um caminho para o arquivo
    mock_1 = tmp_path / "mock_1.txt"
    mock_2 = tmp_path / "mock_2.txt"

    # crio, efetivamente, o arquivo. Se não houver nada escrito nele,
    # ele não existe
    # https://docs.pytest.org/en/7.1.x/how-to/tmp_path.html
    mock_1.write_text("content1")
    mock_2.write_text("content2")

    context = {"all_files": [mock_1, mock_2]}
    result = find_duplicate_files(context)

    assert result == []


# verifica os arquivos duplicados, ou seja, que possuem o mesmo conteúdo
def test_find_duplicate_files_all_equal(tmp_path):
    mock_1 = tmp_path / "mock_1.txt"
    mock_2 = tmp_path / "mock_2.txt"

    content = "same_content"
    mock_1.write_text(content)
    mock_2.write_text(content)

    context = {"all_files": [mock_1, mock_2]}
    result = find_duplicate_files(context)
    expected_result = [(mock_1, mock_2)]

    assert result == expected_result
