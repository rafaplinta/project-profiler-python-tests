from pro_filer.actions.main_actions import show_preview
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
                "all_files": ["src/__init__.py", "src/app.py"],
                "all_dirs": ["src", "src/utils"],
            },
            "Found 2 files and 2 directories\n"
            "First 5 files: ['src/__init__.py', 'src/app.py']\n"
            "First 5 directories: ['src', 'src/utils']\n",
        ),
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/f1.py",
                    "src/utils/f2.py",
                    "src/utils/f3.py",
                    "src/utils/f4.py",
                    "src/utils/f5.py",
                    "src/utils/f6.py",
                ],
                "all_dirs": ["src", "src/utils"],
            },
            "Found 8 files and 2 directories\n"
            "First 5 files: ['src/__init__.py', 'src/app.py', "
            "'src/utils/f1.py', 'src/utils/f2.py', 'src/utils/f3.py']\n"
            "First 5 directories: ['src', 'src/utils']\n",
        ),
        (
            {
                "all_files": ["src/__init__.py", "src/app.py"],
                "all_dirs": [
                    "src/utils/dir1",
                    "src/utils/dir2",
                    "src/utils/dir3",
                    "src/utils/dir4",
                    "src/utils/dir5",
                ],
            },
            "Found 2 files and 5 directories\n"
            "First 5 files: ['src/__init__.py', 'src/app.py']\n"
            "First 5 directories: ['src/utils/dir1', 'src/utils/dir2', "
            "'src/utils/dir3', 'src/utils/dir4', 'src/utils/dir5']\n",
        ),
    ],
)
def test_show_preview(capsys, context, expected_result):
    # O capsys vai capturar a saída padrão stdout
    show_preview(context)

    captured = capsys.readouterr()
    assert captured.out == expected_result
