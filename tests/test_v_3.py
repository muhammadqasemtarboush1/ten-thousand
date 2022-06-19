from ten_thousand.game import Game
from tests.flo import diff

def test_cheater():
    game = Game()
    diffs = diff(game.play, 'tests/version_3/cheat_and_fix.sim.txt')
    # print(diffs,"testing *************************************************")
    assert not diffs, diffs
