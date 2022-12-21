import positive_elements

def test_output(capfd, monkeypatch):
    input = ['[(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)]']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    positive_elements.print_positive_tuple_elements()
    out, err = capfd.readouterr()
    assert "[(4, 5, 9)]" in out


def test_output2(capfd, monkeypatch):
    input = ['[(-4, 5, 9), (-1, -2, 3), (-7, 5, 6), (4, -10)]']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    positive_elements.print_positive_tuple_elements()
    out, err = capfd.readouterr()
    assert "[]" in out


def test_edgecase(capfd, monkeypatch):
    input = ['[(0, 0)]']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    positive_elements.print_positive_tuple_elements()
    out, err = capfd.readouterr()
    assert "[]" in out
