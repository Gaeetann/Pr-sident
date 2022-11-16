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
    while wanna_continue:
        winner = 0

        players_active = [x for x in g.players]
        print("vous jouer contre :")
        for i in g.ai_players:
            print(f"{i.name} qui a : {len(i.hand)} cartes")
        while len(players_active) > 1:

            players_in_game = [x for x in players_active]
            print_ln()

            choice = 0
            i = winner
            plays = None
            card_on_table = None
            while len(players_in_game) > 1:


                if len(players_in_game) - 1 < i:
                    i = 0
                player = players_in_game[i]

                if player is g.main_player:
                    print('Your current deck is : ')
                    print(player)
                    print(g.main_player.hand, )
                    plays = g.main_player.play(card_on_table)
                    if len(plays) > 0:
                        card_on_table = plays
                    print_ln()
                    print(f"You play {plays}")

                else:
                    if card_on_table is None:
                        nb_cards = 1
                    else:
                        nb_cards = len(card_on_table)
                        choice = card_on_table[0].symbol
                    plays = player.play(choice, nb_cards)
                    if len(plays) > 0:
                        card_on_table = plays
                    print_ln()
                    print(player.name,plays)

                if len(plays) == 0:
                    players_in_game.remove(player)


                elif len(player.hand) == 0:
                    print(player,players_in_game)
                    if len(players_active) == len(g.players):
                        player.president = True
                        g.president = player
                    players_in_game.remove(player)
                    players_active.remove(player)
                    print(players_in_game)

                else:
                    i = i+1
            j = 0
            for player_active in players_active:
                if player_active == players_in_game[0]:
                   winner = j
                j += 1

        print("Le président est :", g.president)
        g.trouduc = players_active[0]
        print("Le trouDuc est :", g.trouduc)
        players_active[0]._hand = []
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
    game_loop(g)
    print('Thank you for playing. I hope you enjoyed !')

# quand choix multiple, pas les bonnes cartes qui sont pop
# quand choix multiple, vérifier que l'utilisateur ne choissent pas 0
