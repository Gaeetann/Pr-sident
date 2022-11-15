from models import PresidentGame

nb_players = input("Nombre de joueur :")
nb_players = int(nb_players)
print(f"Le nombre de joueur est :{nb_players}")


def print_ln():
    print('\n')


def game_loop(g: PresidentGame):
    """
    The main game loop.
    Loops in circle until the user wants to quit the application.
    Args:
        g: The President Game instance.
    """

    global plays
    wanna_continue = True
    winner = 0
    while wanna_continue:
        players_in_game = [x for x in g.players]
        players_active = [x for x in g.players]
        print("vous jouer contre :")
        for i in g.ai_players:
            print(f"{i.name} qui a : {len(i.hand)} cartes")
        print('Your current deck is : ')
        # print(g.main_player.hand, )
        print_ln()
        print(g.main_player.hand, )

        choice = '0'
        i = winner
        plays = None
        while len(players_in_game) > 1:
            if len(players_in_game) - 1 < i:
                i = 0
            player = players_in_game[i]

            if player is g.main_player:
                print(g.main_player.hand, )
                plays = g.main_player.play(plays)
                print(plays)
                print(f"You play {plays}")

            else:
                if plays is None:
                    nb_cards = 1

                else:
                    nb_cards = len(plays)
                    choice = plays[0].symbol
                plays = player.play(choice, nb_cards)
                print(player.name,plays)

            if len(plays) == 0:
                players_in_game.remove(player)

            elif len(player.hand) == 0:
                if len(players_active) == len(player):
                    player.president = True
                players_in_game.remove(player)
                players_active.remove(player)

            else:
                i = i+1



        # print("vous jouer contre :")
        # for i in g.ai_players:
        #     print(f"{i.name} qui a : {len(i.hand)} cartes")
        # print('Your current deck is : ')
        # # print(g.main_player.hand, )
        # print_ln()
        # print(g.main_player.hand, )
        # while g.main_player.has_symbol(choice) == 0:
        #     choice = input('What value do you wish to play ? ')
        #     if g.main_player.infer(choice, plays[0].symbol):
        #         plays = g.main_player.play(choice)
        #
        # print(plays)
        # print(f"You play {plays}")

        wanna_continue = input('Do you want to continue playing (y/N)? ')
        wanna_continue = (wanna_continue == 'Y' or wanna_continue == 'y')
        print()
        print("*******************************************************************")


if __name__ == '__main__':
    print_ln()
    print(
        """        *********************************************
        *** President : The cards game (TM) v.0.1 ***
        ********************************************* """)
    g = PresidentGame(nb_players)
    g.distribute_cards()
    game_loop(g)
    print('Thank you for playing. I hope you enjoyed !')

# quand choix multiple, pas les bonnes cartes qui sont pop
# quand choix multiple, vérifier que l'utilisateur ne choissent pas 0
