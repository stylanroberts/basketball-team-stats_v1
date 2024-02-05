import copy
from constants import PLAYERS, TEAMS



def stats_tool():
    print("BASKETBALL STATS TOOL\n")
    print("\n----MENU----\n")
    # function to start game
    start_or_quit()
    # start_or_quit here maybe or might put in dunder


def start_or_quit():
    print("\nHere are your options:\n")
    print("A) Display Team Stats")
    print("B) Quit")
    response = input("\nEnter an option:    ")

    if response.upper() == "A":
        choose_team()
    elif response.upper() == "B":
        print("Goodbye!")
        exit()
    else:
        print("\nNot a valid input, try again.")
        start_or_quit()


def choose_team():
    for team in TEAMS:
        print(f"\n{int(TEAMS.index(team))+1}) { team}")
    print(range(len(TEAMS)))
    response = int(input("\nChoose a team:    "))
    if response in range(1, len(TEAMS)):
        print(f"Team {team[response+1]}")


def player_to_team():
    for team in TEAMS:
        for player in PLAYERS:
            # for team in TEAMS:
                team = []
                players_copy = copy.deepcopy(PLAYERS)
                # players_list = PLAYERS.split(",")
                player = [name.get("name") for name in PLAYERS]
                if len(team) < ( len(PLAYERS) // len(TEAMS) ):
                    sorted_team = team.append(player)
                else:
                    continue
                    

                    



        print(sorted_team)


if __name__ == "__main__":
    player_to_team()
    stats_tool()


