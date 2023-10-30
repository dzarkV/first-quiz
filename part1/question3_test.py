from question3 import alchemy_combine, make_oven


def test_alchemy_combine():
    assert alchemy_combine(make_oven(), ["lead", "mercury"], 5000) == "gold"

    assert alchemy_combine(make_oven(), ["water", "air"], -100) == "snow"

    assert alchemy_combine(make_oven(), ["cheese", "dough", "tomato"], 150) == "pizza"

    assert (
        alchemy_combine(make_oven(), ["beans", "pig foot", "salt"], 60)
        == "mixing beans, pig foot, salt"
    )

    assert (
        alchemy_combine(make_oven(), ["beans", "pig foot", "salt"], 120)
        == "boiled beans, pig foot, salt"
    )
