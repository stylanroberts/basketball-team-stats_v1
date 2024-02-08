import copy
from constants import PLAYERS, TEAMS


# def balance_teams(teams_copy, clean_list):
#     teams_copy = copy.deepcopy(teams_copy)
#     for team in teams_copy:
#         team = []
#         player_name = [name["name"] for name in clean_list]
#         if len(team) < 6:
#             team.append(player_name)
#             del player_name
#     print(team)



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

def balanced_teams(teams, players):
    players_copy = copy.deepcopy(players)
    players_clean = clean_data(players_copy)
    for team in teams:
        team = []
        for player in players_clean:
            if len(team) == 0:
                team.append(player)
                players_clean.remove(player)
            elif len(team) < len(players_clean) // len(team):
                team.append(player)
                players_clean.remove(player)
        print(team)
    return balanced_teams



def choose_team():
    for index, team in enumerate(TEAMS, 1):
        print(f"{index}) {team}")
        # print(f"\n{int(TEAMS.index(team))+1}) { team}")
    response = int(input("\nChoose a team:    "))
    picked_team = TEAMS[response-1]
    if response in range(1, len(TEAMS)):
        print(f"\nTeam {picked_team} Stats:")
    # if picked_team == TEAMS[0]:

    # else: 
    #     print("That is not a choice. Try again")
    # print("\n----------")
    # print(f"Total players: {len(picked_team)}")
    # print("\nPlayers on team:")
    # print(f"\n{picked_team}")
   
    # # function that takes picked team and shows stats or players or something like that
    

def clean_data(players):
    cleaned = []
    players = copy.deepcopy(players)
    for user in players:
        fixed = {}
        fixed['name'] = user['name']

        fixed['height'] = int(user['height'].split(' ')[0])
        if user['experience'.lower()] == "yes":
            fixed['experience'] = True
        else:
            fixed['experience'] = False
        cleaned.append(fixed)

    return cleaned




if __name__ == "__main__":
    # balanced_teams(TEAMS, PLAYERS)
    balanced_teams(TEAMS, PLAYERS)
    stats_tool()


# def show_roster(team):
#     team = []
#     for player in team:
#         player_name = player.get('name')
#         team.append(player_name)
