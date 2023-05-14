from main import  print_menu


def test_print_menu(capsys):
    print_menu()
    captured = capsys.readouterr()
    expected_output = (
        "Welcome to Kapuut! The Kahoot karbon kopy multiple choice quiz game made in Python!!!\n"
        "Please choose from one of the following options:\n"
        "1) Start the Game\n"
        "2) View Leaderboard\n"
        "3) Exit the Game\n"
    )

    assert captured.out == expected_output







