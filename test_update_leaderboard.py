from quiz import update_leaderboard

def test_update_leaderboard():
    score = 100
    player_name = 'Jacob'
    high_score = 90
    leaderboard = [(95, 'Bob'), (90, 'Marley')]
    num_correct = 10
    num = 10

    result = update_leaderboard(score, player_name, high_score, leaderboard, num_correct, num)

    assert result == score
    assert leaderboard == [(100, 'Jacob'), (95, 'Bob'), (90, 'Marley')]

    with open('leaderboard.txt', 'w') as f:
        f.write('')