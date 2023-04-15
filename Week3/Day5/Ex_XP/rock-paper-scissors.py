import game

def get_user_menu_choice():
    choice = ''
    while choice not in ['g', 'x']:
        choice = input("Menu:\n(g) Play a new game\n(x) Show scores and exit\nYour choice: ")
        return choice
    

def print_results(results):
    print(f"Game results:\nWin: {results['win']}\nLoss: {results['loss']}\nDraw: {results['draw']}")


def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while True:
        i = get_user_menu_choice()
        if i == 'g':
            obj = game.Game()
            results[obj.play()] += 1
        else:
            print_results(results)
    

main()
