import copy
from constants import PLAYERS, TEAMS

players = copy.deepcopy(PLAYERS)

team_length = len(PLAYERS) // len(TEAMS)

panthers = []
bandits = []
warriors = []

experienced = []
not_experienced = []
team_list = [panthers, bandits, warriors]


def exp_or_not(players):
    players_clean = clean_data(players)
    for player in players_clean:

        if player.get('experience') == True:
            experienced.append(player)
        else:
            not_experienced.append(player)


def balance_teams():
    exp_or_not(players)
    exp_per_team = len(experienced) // len(TEAMS)
    for player in experienced:
        if len(panthers) < exp_per_team:
            panthers.append(player)
        elif len(bandits) < exp_per_team:
           bandits.append(player)
        elif len(warriors) < exp_per_team:
            warriors.append(player)

    for player in not_experienced:
        if len(panthers) < team_length:
            panthers.append(player)
        elif len(bandits) < team_length:
            bandits.append(player)
        elif len(warriors) < team_length:
            warriors.append(player)


def stats_tool():
    print("BASKETBALL STATS TOOL\n")
    print("\n----MENU----\n")
    start_or_quit()


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


def get_name(team):
    team_names = []
    for player in team:
        
        player_name = player.get('name')
        team_names.append(player_name)
    for team in team_names:
        print(team, end=', ')
    

def get_stats(team):
    print("\nWould you like to see the stats of any of this team's players?")
    while True:
        response = input("\nType in their first and last name. If you want to quit, press Q!    ")
        player_response = response.title()
        if response.lower() == "q".lower():
            print('Goodbye!')
            exit()
        # this link helped explain how to check for key names in list of dicts
        # https://stackoverflow.com/questions/3897499/check-if-value-already-exists-within-list-of-dictionaries-in-python
        if not any(player['name'] == player_response for player in team):
            print("Sorry not in the team, we need a player on THIS team!")
        else:
            break

    for player in team:

        player_height = player.get('height')
        player_guardians = player.get('guardians')

        if len(player_guardians) > 1:
            player_guardians = ', '.join(player_guardians)
            
        player_name = player.get('name')

        # if response.title() not in player.values():a
        #     response = input("\nSorry they aren't on the team, try another player!:    ")


        if  response.title() == player.get('name'):
            print(f"\nStats for {player_name}:\n")
            print(f"Height: {player_height}")
            
            print(f"Guardian(s): {player_guardians}")
            if player['experience'] == False:
                print("Experience: Low")
            else:
                print("Experience: High")
            exit()



def choose_team():
    for index, team in enumerate(TEAMS, 1):
        print(f"{index}) {team}")
    
    while True:
        response = int(input("\nChoose a team:    "))-1

        if response not in range(0, len(TEAMS)):
            print("Out of range, try again.")
        else:
            break
    picked_team_name = TEAMS[response]
    picked_team = team_list[response]

    # if response in range(0, len(TEAMS)):
    print(f"\nTeam {picked_team_name}:")
    print("\n----------")
    print(f"\nTotal players: {len(team_list[response])}")


    experienced_num = 0
    not_experienced_num = 0
    for player in picked_team:

        if player.get('experience') == True:
            experienced_num+=1
        else:
            not_experienced_num+=1

    print(f"\nNumber of experienced players: {experienced_num}\n")
    get_name(picked_team)
    get_stats(picked_team)


def clean_data(players):
    cleaned = []
    players = copy.deepcopy(players)
    for user in players:
        fixed = {}
        if len(user['guardians']) > 1:
            fixed['guardians'] = user['guardians'].split(' and ')
        else:
            fixed['guardians'] = user['guardians']
        fixed['name'] = user['name']

        fixed['height'] = int(user['height'].split(' ')[0])
        if user['experience'] == "YES":
            fixed['experience'] = True
        else:
            fixed['experience'] = False
        cleaned.append(fixed)
    return cleaned


if __name__ == "__main__":
    balance_teams()
    stats_tool()