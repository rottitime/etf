from etf.evaluation import pages


def test_get_prev_next_page_name_first():
    page_name = "intro"
    result = pages.get_prev_next_page_name(page_name)
    expected = (None, "title")
    assert result == expected, result


def test_get_prev_next_page_name_middle():
    page_name = "ethics"
    result = pages.get_prev_next_page_name(page_name)
    expected = ("other-measures", "impact-findings")
    assert result == expected, result


def test_get_prev_next_page_name_penultimate():
    page_name = "status"
    result = pages.get_prev_next_page_name(page_name)
    expected = ("metadata", "end")
    assert result == expected, result


def test_get_prev_next_page_name_last():
    page_name = "end"
    result = pages.get_prev_next_page_name(page_name)
    expected = ("status", None)
    assert result == expected, result
