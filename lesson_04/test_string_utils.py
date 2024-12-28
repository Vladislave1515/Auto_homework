import pytest
from string_utils import StringUtils

processor = StringUtils()


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello", "Hello"),
        ("Hello", "Hello"),
        ("hello world", "Hello world"),
    ],
)
def test_process_positive_01(input_text, expected_output):
    assert processor.capitilize(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", ""),
        ("    ", "    "),
    ],
)
def test_process_negative_01(input_text, expected_output):
    assert processor.capitilize(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("   hello", "hello"),
        ("hello", "hello"),
        ("  hello world", "hello world"),
    ],
)
def test_process_positive_02(input_text, expected_output):
    assert processor.trim(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello world   ", "hello world   "),
        ("   ", ""),
    ],
)
def test_process_negative_02(input_text, expected_output):
    assert processor.trim(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, delimiter, expected_output",
    [
        ("h,e,l,o", ",", ["h", "e", "l", "o"]),
        ("10:20:30", ":", ["10", "20", "30"]),
        ("  ,  ", ",", ["  ", "  "]),
    ],
)
def test_process_positive_03(input_text, delimiter, expected_output):
    assert processor.to_list(input_text, delimiter) == expected_output


@pytest.mark.parametrize(
    "input_text, delimiter, expected_output",
    [
        ("h,,e,,l,,o", ",", ["h", "", "e", "", "l", "", "o",]),
        ("h,e,l,o", "l", ['h,e,', ',o']),
        ("h,e,l,o", "", ValueError),
        ("h e l o", " ", ["h", "e", "l", "o"]),
    ],
)
def test_process_negative_03(input_text, delimiter, expected_output):
    if expected_output is ValueError:
        with pytest.raises(ValueError):
            processor.to_list(input_text, delimiter)
    else:
        assert processor.to_list(input_text, delimiter) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Hello", "l", True),
        ("Hello", "L", False),
        ("Hello", "H", True),
    ],
)
def test_process_positive_04(input_text, symbol, expected_output):
    assert processor.contains(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Hello", "", True),
        ("", "o", False),
        ("HELLO", "LO", True),
        ("", " ", False),
        ("", "", True),
        ("", "a", False),
    ],
)
def test_process_negative_04(input_text, symbol, expected_output):
    assert processor.contains(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Hello", "l", "Heo"),
        ("Hello", "L", "Hello"),
        ("Hello", "Hell", "o"),
    ],
)
def test_process_positive_05(input_text, symbol, expected_output):
    assert processor.delete_symbol(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Hello", "", "Hello"),
        ("Hello", "L", "Hello"),
        ("Hello", "HHell", "Hello"),
        ("", "o", ""),
        ("", " ", ""),
        ("", "", ""),
        ("", "a", ""),
    ],
)
def test_process_negative_05(input_text, symbol, expected_output):
    assert processor.delete_symbol(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Hello", "H", True),
        ("Hello", "e", False),
        ("hh.ru", "h", True),
    ],
)
def test_process_positive_06(input_text, symbol, expected_output):
    assert processor.starts_with(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("  Hello", "H", False),
        ("1235", "1", True),
        ("hello Hello", "H", False),
        ("", "H", False),
        ("Hello ", " ", False),
        (" ", " ", True),
    ],
)
def test_process_negative_06(input_text, symbol, expected_output):
    assert processor.starts_with(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Hello", "o", True),
        ("Hello", "l", False),
        ("12345", "5", True),
    ],
)
def test_process_positive_07(input_text, symbol, expected_output):
    assert processor.end_with(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("  Hello", "H", False),
        ("1235.", "5", False),
        ("hello Hello", " ", False),
        ("", "H", False),
        ("Hello ", " ", True),
        (" ", " ", True),
    ],
)
def test_process_negative_07(input_text, symbol, expected_output):
    assert processor.end_with(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", True),
        ("  ", True),
        ("12345", False),
    ],
)
def test_process_positive_08(input_text, expected_output):
    assert processor.is_empty(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("    H", False),
        ("1235    ", False),
        ("   hello   Hello   ", False),
    ],
)
def test_process_negative_08(input_text, expected_output):
    assert processor.is_empty(input_text) == expected_output


@pytest.mark.parametrize(
    "input_list, joiner, expected_output",
    [
        ([10, 20, 30, 40, "Hello"], "10, 20, 30, 40, Hello"),
        (["Hello", "Bye"], "Hello, Bye"),
        (["Hel", "Lo"], "-", "Hel-Lo"),
    ],
)
def test_process_positive_09(input_list, joiner, expected_output):
    assert processor.list_to_string(input_list, joiner) == expected_output


@pytest.mark.parametrize(
    "input_list, joiner, expected_output",
    [
        ([], ", ", ""),
        (["Hello", "hello", "Hello"], " 1 ", "Hello 1 hello 1 Hello"),
    ],
)
def test_process_negative_09(input_list, joiner, expected_output):
    assert processor.list_to_string(input_list, joiner) == expected_output
