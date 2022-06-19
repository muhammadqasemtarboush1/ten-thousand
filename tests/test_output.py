# from ten_thousand.game import Game
# from tests.flo import diff
#
# def test_one_and_done():
#     game = Game()
#     diffs = diff(game.play, 'tests/version_2/one_and_done.sim.txt')
#     # print(diffs,"testing *************************************************")
#     assert not diffs, diffs
#
# def test_quitter():
#     game = Game()
#     diffs = diff(game.play, 'tests/version_2/quitter.sim.txt')
#     assert not diffs, diffs
#
# def test_repeat_rolling():
#         game = Game()
#         diffs = diff(game.play, 'tests/version_2/repeat_roller.sim.txt')
#         assert not diffs, diffs
#
#
# def test_bank_one():
#     game = Game()
#     diffs = diff(game.play, 'tests/version_2/bank_one_roll_then_quit.sim.txt')
#     assert not diffs,  diffs
#
# def test_bank_two():
#         game = Game()
#         diffs = diff(game.play, 'tests/version_2/bank_first_for_two_rounds.sim.txt')
#         assert not diffs, diffs
