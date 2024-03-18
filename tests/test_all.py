from auxiliar import are_all_the_same, slurp, file_as_list_of_lines, head, string_to_lines
import os


def file1_path():
    return os.path.join("tests", "files", "file1" + ".txt")


def test_are_all_the_same():
    a = [0, 1]
    b = [0, 0]
    assert not are_all_the_same(a)
    assert are_all_the_same(b)


def test_slurp():
    filepath = file1_path()
    read = ""
    slurped = ""
    with open(filepath, "r") as file:
        read = file.read()
    slurped = slurp(filepath)
    assert slurped == read


def test_file_as_list_of_lines():
    filepath = file1_path()
    lines = file_as_list_of_lines(filepath)
    assert "line 1" == lines[0]
    assert "line 2" == lines[1]
    assert 2 == len(lines)


def test_head():
    filepath = file1_path()
    lines = string_to_lines(head(filepath, 1))
    assert "line 1" == lines[0]
    assert 1 == len(lines)
