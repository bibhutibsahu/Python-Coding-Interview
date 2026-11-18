"""Pareto-style analysis helpers.

1. Which customers make up 80% of the total credit exposure?
2. In which month does cumulative revenue cross 50% of the annual total?
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping


def top_contributors(
    values: Mapping[str, float], share: float = 0.8
) -> tuple[list[str], float, float]:
    """Return the fewest keys whose values cover at least `share` of the total.

    Returns (chosen_keys, covered_amount, total).
    """
    if not 0 < share <= 1:
        raise ValueError("share must be in (0, 1]")

    total = sum(values.values())
    running = 0.0
    chosen: list[str] = []
    for key, amount in sorted(values.items(), key=lambda kv: kv[1], reverse=True):
        running += amount
        chosen.append(key)
        if running >= share * total:
            break
    return chosen, running, total


def crossing_point(
    labels: Iterable[str], values: Iterable[float], share: float = 0.5
) -> tuple[str, float] | None:
    """Return (label, cumulative_value) where the running sum first reaches `share` of the total."""
    labels, values = list(labels), list(values)
    if len(labels) != len(values):
        raise ValueError("labels and values must be the same length")

    threshold = share * sum(values)
    cumulative = 0.0
    for label, value in zip(labels, values):
        cumulative += value
        if cumulative >= threshold:
            return label, cumulative
    return None


def main() -> None:
    exposure = {  # Rs lakh
        "C101": 120, "C102": 15, "C103": 340, "C104": 60,
        "C105": 25, "C106": 210, "C107": 10, "C108": 220,
    }  # fmt: skip
    chosen, running, total = top_contributors(exposure)
    print("total_exposure =", total)
    print("running_exposure =", running)
    print("customers covering 80%:", len(chosen), chosen)
    print("share covered:", round(100 * running / total, 2), "%")

    months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]
    revenue = [8, 9, 7, 10, 12, 11, 9, 14, 13, 15, 16, 26]
    result = crossing_point(months, revenue)
    print("Total revenue:", sum(revenue), "| half:", sum(revenue) / 2)
    if result:
        month, cumulative = result
        print("50% crossed in", month, "with cumulative", cumulative)


if __name__ == "__main__":
    main()
