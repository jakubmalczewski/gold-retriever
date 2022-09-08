import random, requests, time
import numpy as np
import pickle

n = 30

def dig(game, dig_loc):
    time.sleep(0.5)

    response = requests.post(
        url=f'https://api.gaimbot.com/games/gold-retriever/{game["id"]}/dig',
        params={'cell': dig_loc}
    )
    game.update(response.json())
    game["score_hist"].append(game["score"])
    game["loc_hist"].append(dig_loc)
    game["field"][dig_loc//n, dig_loc%n] = game["score_hist"][-1] - game["score_hist"][-2]
    return game


def playGame(algo = lambda : np.random.randint(0,900), dir="./data"):
    # Instantiate a new game
    game = {}
    response = requests.post("https://api.gaimbot.com/games/gold-retriever/new")
    game.update(response.json())
    game["score_hist"] = [0,]
    game["loc_hist"] = []
    game["field"] = np.zeros((n,n))

    # Print the game message
    print(game['id'])
    print("   ",game['message'])

    while game['digs_remaining'] > 0:
        game = dig(game, algo())
        print("   ",game['message'])

    with open(f"{dir}/{game['id']}.pk","wb") as file:
        pickle.dump(game, file)

