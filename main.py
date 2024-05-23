from game_field import GameField


def main():
    game = GameField()
    game_loop(game)
    if game.game_finished():
        print("YOU WON !")
    else:
        print("BYE LOOOOSEr !")


def game_loop(game: GameField):
    while not game.game_finished():
        print(game)
        direction = input("Enter move: ")
        try:
            if direction == 'u':
                game.up()
            if direction == 'd':
                game.down()
            if direction == 'l':
                game.left()
            if direction == 'r':
                game.right()
            if direction == 'x':
                break
        except:
            print("Incorrect move")


if __name__ == "__main__":
    main()

