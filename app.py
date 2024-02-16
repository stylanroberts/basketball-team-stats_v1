import copy
from constants import PLAYERS, TEAMS

players = copy.deepcopy(PLAYERS)
team_length = len(PLAYERS) // len(TEAMS)
panthers = []
bandits = []
warriors = []
team_list = [panthers, bandits, warriors]
experienced = []
not_experienced = [] 


def clean_data(players):
    cleaned = []
    players = copy.deepcopy(players)
    for user in players:
        fixed = {}
        fixed['name'] = user['name']
        fixed['height'] = int(user['height'].split(' ')[0])
        if len(user['guardians']) > 1:
            fixed['guardians'] = user['guardians'].split(' and ')
        else:
            fixed['guardians'] = user['guardians']
        if user['experience'] == "YES":
            fixed['experience'] = True
        else:
            fixed['experience'] = False
        cleaned.append(fixed)
    return cleaned


def exp_or_not(players):
    players_clean = clean_data(players)
    for player in players_clean:
        if player.get('experience') == True:
            experienced.append(player)
        else:
            not_experienced.append(player)


def balance_teams():
    exp_or_not(players)
    exp_per_team = len(experienced) // len(team_list)
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


def main():
    balance_teams()
    print("\n---------------------")
    print("\nBASKETBALL STATS TOOL\n")
    print("---------------------\n")
    print("\n----MENU----")
    print("\nHere are your options:\n")
    print("    1) Display Team Stats")
    print("    2) Quit")
    while True:
        response = input("\nEnter an option:    ")
        if response == "1":
            choose_team()
            break
        elif response == "2":
            print("Goodbye!")
            exit()
        else:
            print("\nNot a valid input, try again.")
            

def choose_team():
    print('\nTeam list:\n')
    for index, team in enumerate(TEAMS, 1):
        print(f"    {index}) {team}")
    while True:
        try:
            response = int(input("\nChoose a team:    "))-1
            if response not in range(0, len(TEAMS)):
                print("Out of range, try again.")
            else:
                break
        except ValueError:
            print("Please pick a number assigned to a team on the list.")
    picked_team_name = TEAMS[response]
    picked_team = team_list[response]
    print(f"\nTeam {picked_team_name}")
    print("-------------")
    get_name(picked_team)
    player_stats(picked_team)


def get_name(team):
    team_names = []
    for player in team:
        player_name = player.get('name')
        team_names.append(player_name)
    clean_team_names = (', ').join(team_names)
    print(f"\nPlayers: {clean_team_names}\n")
    team_stats(team)


def team_stats(team):
    print("\nTeam stats:")
    total_players = len(team)
    total_height = 0
    experienced_num = 0
    not_experienced_num = 0
    guardian_list = []
    for player in team:
        guardian_names = player.get('guardians')
        for guardian in guardian_names:
            guardian_list.append(guardian)
        
        if player.get('experience') == True:
            experienced_num+=1
        else:
            not_experienced_num+=1
        player_height = player.get('height')
        total_height+=player_height
    avg_height = total_height // len(team)
    print(f"    Total players: {total_players}")
    print(f"    Experienced players: {experienced_num}")
    print(f"    Non-experienced players: {not_experienced_num}")
    print(f"    Average height: {avg_height}")
    print(f"    Guardians: {', '.join(guardian_list)}")


def player_stats(team):
    print("\nWould you like to see the stats of any of this team's players?")
    while True:
        response = input("\nType in their first and last name. If you want to go back to menu, press ENTER!    ")
        player_response = response.title()
        if response == "":
            main()
        # this link helped explain how to check for key names in list of dicts
        # https://stackoverflow.com/questions/3897499/check-if-value-already-exists-within-list-of-dictionaries-in-python
        if not any(player['name'] == player_response for player in team):
            print("Sorry not in the team, we need a player on THIS team!")
        else:
            break
    for player in team:
        player_guardians = player.get('guardians')
        if len(player_guardians) > 1:
            player_guardians = ', '.join(player_guardians)
        player_name = player.get('name')
        player_height = player.get('height')
        if  response.title() == player.get('name'):
            print(f"\nStats for {player_name}:\n")
            print(f"Height: {player_height}")
            if len(player_guardians) == 1:
                for guardian in player_guardians:
                    print(f"Guardian: {guardian}")
            else:
                print(f"Guardians: {player_guardians}")
            if player['experience'] == False:
                print("Experience: Low")
            else:
                print("Experience: High")
            to_menu = input("\nPress 'S' to get another player's stats. To go back to menu, press ENTER!   \n")
            if to_menu == '':
                main()
            if to_menu.lower() == 's':
                get_name(team)
                player_stats(team)
        

if __name__ == "__main__":
    main()



