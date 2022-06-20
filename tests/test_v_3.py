from ten_thousand.game import Game
from tests.flo import diff

def test_cheater():
    game = Game()
    diffs = diff(game.play, 'tests/version_3/cheat_and_fix.sim.txt')
    # print(diffs,"testing *************************************************")
    assert not diffs, diffs


def test_hot_dice():
    game = Game()
    diffs = diff(game.play, 'tests/version_3/hot_dice.sim.txt')
    # print(diffs,"testing *************************************************")
    assert not diffs, diffs

def test_zilcher():
    game = Game()
    diffs = diff(game.play, 'tests/version_3/zilcher.sim.txt')
    # print(diffs,"testing *************************************************")
    assert not diffs, diffs


def test_repeat_rolling():
    game = Game()
    diffs = diff(game.play, 'tests/version_3/repeat_roller.sim.txt')
    # print(diffs,"testing *************************************************")
    assert not diffs, diffs