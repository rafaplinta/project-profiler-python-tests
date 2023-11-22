from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest


@pytest.mark.parametrize(
    "context, expected_result",
    [
        (
            {"all_files": [], "all_dirs": []},
            "Found 0 files and 0 directories\n",
        ),
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                ],
                "all_dirs": ["src", "src/utils"],
            },
            "Found 2 files and 2 directories\n"
            "First 5 files: ['src/__init__.py', 'src/app.py']\n"
            "First 5 directories: ['src', 'src/utils']\n",
        ),
    ],
)
def test_show_preview(capsys, context, expected_result):
    # o capsys vai capturar a saída padrão stdout
    show_preview(context)
    
    captured = capsys.readouterr()
    assert captured.out == expected_result
