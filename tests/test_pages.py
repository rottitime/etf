from etf.evaluation import pages


def test_get_prev_next_page_name_first():
    page_name = "intro"
    result = pages.get_prev_next_page_name(page_name, evaluation_types=["flibble"])
    expected = (None, "title")
    assert result == expected, result


def test_get_prev_next_page_name_middle():
    page_name = "ethics"
    result = pages.get_prev_next_page_name(page_name, evaluation_types=["flibble"])
    expected = ("other-measures", "processes-standards")
    assert result == expected, result


def test_get_prev_next_page_name_middle_impact():
    page_name = "ethics"
    result = pages.get_prev_next_page_name(page_name, evaluation_types=["IMPACT"])
    expected = ("other-measures", "impact-findings")
    assert result == expected, result


def test_get_prev_next_page_name_penultimate():
    page_name = "visibility"
    result = pages.get_prev_next_page_name(page_name, evaluation_types=["flibble"])
    expected = ("links", "end")
    assert result == expected, result


def test_get_prev_next_page_name_last():
    page_name = "end"
    result = pages.get_prev_next_page_name(page_name, evaluation_types=["flibble"])
    expected = ("visibility", None)
    assert result == expected, result


def test_get_page_name_and_order():
    page_names_and_order = pages.get_page_name_and_order(["flibble"])
    assert len(page_names_and_order) == 17, len(page_names_and_order)
    assert "impact-analysis" not in page_names_and_order

    page_names_and_order = pages.get_page_name_and_order(["IMPACT"])
    assert len(page_names_and_order) == 20, len(page_names_and_order)
    assert "impact-analysis" in page_names_and_order
