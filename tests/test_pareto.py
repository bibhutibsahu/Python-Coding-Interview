import pytest

from pareto import crossing_point, top_contributors

EXPOSURE = {
    "C101": 120, "C102": 15, "C103": 340, "C104": 60,
    "C105": 25, "C106": 210, "C107": 10, "C108": 220,
}  # fmt: skip


def test_top_contributors_covers_80_percent():
    chosen, running, total = top_contributors(EXPOSURE)
    assert total == 1000
    assert chosen == ["C103", "C108", "C106", "C101"]
    assert running == 890
    assert running >= 0.8 * total


def test_top_contributors_full_share_returns_everyone():
    chosen, _, _ = top_contributors(EXPOSURE, share=1.0)
    assert sorted(chosen) == sorted(EXPOSURE)


@pytest.mark.parametrize("bad_share", [0, -0.1, 1.5])
def test_top_contributors_rejects_bad_share(bad_share):
    with pytest.raises(ValueError):
        top_contributors(EXPOSURE, share=bad_share)


def test_crossing_point_finds_month():
    months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]
    revenue = [8, 9, 7, 10, 12, 11, 9, 14, 13, 15, 16, 26]
    assert crossing_point(months, revenue) == ("Nov", 80)


def test_crossing_point_length_mismatch():
    with pytest.raises(ValueError):
        crossing_point(["a", "b"], [1])
