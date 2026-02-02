import pytest
import sys, os
# Ensure the project root is on sys.path so pytest can import modules in the repo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from simple_jokes import list_categories, tell_category_jokes, ask_rating


def test_list_categories_contains_expected():
    cats = list_categories()
    assert isinstance(cats, list)
    assert "robbers" in cats


def test_tell_category_jokes_outputs(monkeypatch, capsys):
    # simulate pressing enter for the two input prompts per joke
    inputs = iter(["", ""])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    tell_category_jokes("robbers")
    captured = capsys.readouterr()
    assert "Calder police" in captured.out


def test_tell_category_no_jokes(capsys):
    tell_category_jokes("unknown-category")
    captured = capsys.readouterr()
    assert "Sorry, no jokes for that category." in captured.out


def test_ask_rating_valid_then_recommend_yes(monkeypatch, capsys):
    inputs = iter(["5", "yes"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    ask_rating()
    out = capsys.readouterr().out
    assert "50 percent satisfaction rate" in out
    assert "Thanks, we appreciate it." in out


def test_ask_rating_invalid_then_valid(monkeypatch, capsys):
    inputs = iter(["abc", "11", "7", "no"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    ask_rating()
    out = capsys.readouterr().out
    assert "Enter a whole number between 1 and 10." in out
    assert "70 percent satisfaction rate" in out
    assert "Sorry you did not enjoy it." in out
