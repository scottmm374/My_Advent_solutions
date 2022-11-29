
from main import calc_surface_area, calc_extra_paper, calc_total_paper


def test_surface_area():
    assert calc_surface_area([[20, 3, 11]]) == 626;
    assert calc_surface_area([[15, 27, 5]]) == 1230;
    assert calc_surface_area([[2, 3, 4]]) == 52;
    assert calc_surface_area([[1, 1, 10]]) == 42;


def test_should_be_three():
    assert calc_extra_paper([[20, 3, 11]]) == 33;
    assert calc_extra_paper([[15, 27, 5]]) == 75;
    assert calc_extra_paper([[2, 3, 4]]) == 6;
    assert calc_extra_paper([[1, 1, 10]]) == 1;

def test_total_paper():
    assert calc_total_paper(626, 33) == 659;
    assert calc_total_paper(1230, 75) == 1305;
    assert calc_total_paper(52, 6) == 58;
    assert calc_total_paper(42, 1) == 43;




