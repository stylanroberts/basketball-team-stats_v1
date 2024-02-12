import copy
from constants import PLAYERS, TEAMS

players = copy.deepcopy(PLAYERS)

team_length = len(PLAYERS) // len(TEAMS)

panthers = []
bandits = []
warriors = []

# team_list =[]

# maybe idk if this will work yet

def sort_teams():
    for team in TEAMS:
        team = []
        if len(team) < team_length:
            for player in players:
                team.append(player)
        team_list.append(team)
    return team_list
    


team_list = [panthers, bandits, warriors]

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


def balance_teams():
    players_clean = clean_data(PLAYERS)
    for player in players_clean:
        if len(panthers) < team_length:
            panthers.append(player)
        elif len(bandits) < team_length:
            bandits.append(player)
        elif len(warriors) < team_length:
            warriors.append(player)


def get_name(team):
    team_names = []
    for player in team:
        
        player_name = player.get('name')
        team_names.append(player_name)
    print(team_names)
    

def get_stats(team):
    print("\nWould you like to see the stats of any of this team's players?")
    response = input("\nIf so, type in there first and last name, if not, press Q!    ")
    if response.lower() == "q".lower():
        print('Goodbye!')
        exit()

    for player in team:

        player_height = player.get('height')
        player_guardians = player.get('guardians')
        player_name = player.get('name')

        if response.title() not in player.values():
            response = input("\nSorry they aren't on the team, try another player!:    ")


        elif  response.title() in player.values():
            print(f"\nStats for {player_name}:\n")
            print(f"Height: {player_height}")
            
            print(f"Parent(s): {player_guardians}")
            if player['experience'] == False:
                print("Experience: low")
            else:
                print("Experience: high")
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
    picked_team = TEAMS[response]

    # if response in range(0, len(TEAMS)):
    print(f"\nTeam {picked_team}:")
    print("\n----------")
    print(f"Total players: {len(team_list[response])}")
    # elif response not in range(0, len(TEAMS)):
    #     response = int(input("Out of range, try again:    "))
    if picked_team == TEAMS[0]:
        
        get_name(panthers)
        get_stats(panthers)
    elif picked_team == TEAMS[1]:
        get_name(warriors)
        get_stats(warriors)
    elif picked_team == TEAMS[2]:
        get_name(bandits)
        get_stats(bandits)
        
    else: 
        response = int(input("That is not a choice. Try again"))

    # print("\nPlayers on team:")
    # print(f"\n{picked_team}")
   
    # # function that takes picked team and shows stats or players or something like that
    

def clean_data(players):
    cleaned = []
    players = copy.deepcopy(players)
    for user in players:
        fixed = {}
        fixed['guardians'] = user['guardians'].split('and')
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