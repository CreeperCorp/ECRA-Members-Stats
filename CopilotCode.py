# Refactored ECRA Members Stats using lists and dictionaries
# Now with improved error handling and input validation

import sys

def yes_no_prompt(prompt):
    """Prompt user for a yes/no answer and validate."""
    while True:
        try:
            answer = input(prompt).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nInput interrupted. Exiting.")
            sys.exit()
        if answer in ('yes', 'no'):
            return answer == 'yes'
        print("Please enter 'yes' or 'no'.")

def get_input(prompt):
    """Get user input, handle EOF/interrupt."""
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted. Exiting.")
        sys.exit()

print('ECRA accepts members whenever but you have a higher chance to get in if you apply at the beginning of a season.')

# Member data
members = [
    {
        "name": "CreepSplotion",
        "username": "ECRAYungyBot",
        "rank": 1,
        "rank2025": 1,
        "rank_history": ["#1"],
        "past_usernames": ["ECRACreeperBot", "ECRAShadowCreep", "ECRACreep", "CreepSplotionYT"],
        "skin_mc": "https://namemc.com/profile/ECRAYungyBot.1",
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 1, "Fortnite": 1, "Roblox": 1, "Geometry Dash": 1}
    },
    {
        "name": "Ennard",
        "username": "ECRAExoticEnnard",
        "rank": 2,
        "rank2025": 2,
        "rank_history": ["2018: #4", "2024: #2"],
        "past_usernames": ["EqqqEnnard", "ExoticEnnardGG", "EXENNJJERD", "ECRAEnnard", "ECRAMrFeast", "ECRAEnnard", "ECRAExoticEnnard", "OffHandIsA", "IWalkWithQ"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 2, "Fortnite": 2, "Roblox": 2, "Geometry Dash": 2}
    },
    {
        "name": "ReapSplotion",
        "username": "ECRAReap",
        "rank": 3,
        "rank2025": 3,
        "rank_history": ["2018: #2", "2023: #3", "2024: #4", "2025: #3"],
        "past_usernames": [],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 3, "Fortnite": 4, "Roblox": 3, "Geometry Dash": 3}
    },
    {
        "name": "Division",
        "username": "ECRADividedByE",
        "rank": 4,
        "rank2025": 4,
        "rank_history": ["2018: #3", "2023: #2", "2024: #3", "2025: #4"],
        "past_usernames": ["BetterCreep", "DivideBy78", "Division404", "ExoticDivision", "CSDivision", "ReaperD", "ECRANo", "ECRAyes", "ECRABestMember", "CreepSplotionYT", "ECRADivision", "12LengthTab"],
        "skin_mc": None,
        "best_game": "Fortnite",
        "ranks_by_game": {"Minecraft": 4, "Fortnite": 3, "Roblox": 4, "Geometry Dash": 4}
    },
    {
        "name": "Giggles",
        "username": "ECRAGiggles",
        "rank": 5,
        "rank2025": 5,
        "rank_history": ["2025: #5 (joined Spring 2025)"],
        "past_usernames": ["ExoticGiggles (He wasn't actually in EC)", "ECRAGiggles", "ECRANumber5", "ECRANumber3 (He was 3rd in ranking after a bet but lost it to more bets)", "ECRANumber4", "ECRANumber"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 5, "Fortnite": 5, "Roblox": 5, "Geometry Dash": 6}
    },
    {
        "name": "Finxlly",
        "username": "ECRAFinxlly",
        "rank": 6,
        "rank2025": 6,
        "rank_history": ["2025: #6 (joined Fall 2025)"],
        "past_usernames": ["FinxllyForever", "FinxllyNever", "FinxllyAI", "FinxllyMC", "F3nxlly", "F3_Finxlly", "CSFinxlly", "FinxllyECRA", "F3nxllyECRA", "CreepSplotionYT"],
        "skin_mc": None,
        "best_game": "Fortnite",
        "ranks_by_game": {"Minecraft": 7, "Fortnite": 6, "Roblox": 6, "Geometry Dash": 7}
    },
    {
        "name": "Quilver",
        "username": "ECRAQuiliest",
        "rank": 7,
        "rank2025": 7,
        "rank_history": ["2025: #7 (joined Fall 2025)"],
        "past_usernames": ["Quilver", "Quilverest", "SDQuil", "GhostQuil", "Quilvire", "Quilver", "Quilverest", "QuilRS (Reaper Squad)", "QuilverestRS", "EZQuil", "RCQuil (Reaper Clan)", "Quilver", "C"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 8, "Fortnite": 7, "Roblox": 7, "Geometry Dash": 8}
    },
    {
        "name": "aXc3L",
        "username": "ECRAaXc3L",
        "rank": 8,
        "rank2025": 8,
        "rank_history": ["2025: #8 (joined Fall 2025)"],
        "past_usernames": ["aXc3L", "CSaXc3L", "ReaperaXc3L", "ExoticaXc3L", "aXc3L", "0OPaXc3L", "CSaXc3L", "aXc3L", "ExoticaXc3L"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 9, "Fortnite": 11, "Roblox": 12, "Geometry Dash": 11}
    },
    {
        "name": "CreepYT",
        "username": "CreepYT8451",
        "rank": 9,
        "rank2025": 9,
        "rank_history": ["2025: #9 (joined Summer 2025)"],
        "past_usernames": [],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 6, "Fortnite": 10, "Roblox": 8, "Geometry Dash": 9}
    },
    {
        "name": "XRayz",
        "username": "ECRAXRayz",
        "rank": 10,
        "rank2025": 10,
        "rank_history": ["2025: #10 (joined Fall 2025)"],
        "past_usernames": ["IXRayForFun", "XRayz", "Xrayz", "XRayzAM", "ISeeThroughWalls", "XRaaaaaaayz", "XXRayz", "RSXRayz", "RCXRayz", "CRXRayz", "CRXRaaaaaaayz"],
        "skin_mc": None,
        "best_game": "Fortnite",
        "ranks_by_game": {"Minecraft": 10, "Fortnite": 8, "Roblox": 10, "Geometry Dash": 10}
    },
    {
        "name": "R3zzignation",
        "username": "ECRAXR3zz",
        "rank": 11,
        "rank2025": 11,
        "rank_history": ["2025: #11 (joined Fall 2025)"],
        "past_usernames": ["R3zzignation has been in the most clans out of all ECRA members (24 clans)", "R3zzignation", "R3zz", "POR3zz", "POSTR3zz", "BuddyR3zz", "WOODR3zz", "KOR3zz", "LOSTR3zz", "E"],
        "skin_mc": None,
        "best_game": "Fortnite",
        "ranks_by_game": {"Minecraft": 12, "Fortnite": 9, "Roblox": 13, "Geometry Dash": 12}
    },
    {
        "name": "Batchi",
        "username": "ECRABatchi",
        "rank": 12,
        "rank2025": 12,
        "rank_history": ["2025: #12 (joined Fall 2025)"],
        "past_usernames": ["Batch3sBatchi", "BatchesBatchi", "BatchiBatchi", "CabresBatchi", "BBBatchi", "YWNBatchi", "JSBatchi", "HHBATCHI", "CSBatchi", "ReaperBatchi"],
        "skin_mc": None,
        "best_game": "Fortnite",
        "ranks_by_game": {"Minecraft": 13, "Fortnite": 12, "Roblox": 14, "Geometry Dash": 13}
    },
    {
        "name": "Dash",
        "username": "Dashturle09",
        "rank": 13,
        "rank2025": 13,
        "rank_history": ["2025: #13 (joined Winter 2025)"],
        "past_usernames": [],
        "skin_mc": None,
        "best_game": "Roblox",
        "ranks_by_game": {"Minecraft": 15, "Fortnite": 13, "Roblox": 9, "Geometry Dash": 15}
    },
    {
        "name": "XxFun",
        "username": "XxFunWasTaken",
        "rank": 14,
        "rank2025": 14,
        "rank_history": ["2025: #14 (joined Winter 2025)"],
        "past_usernames": [],
        "skin_mc": None,
        "best_game": "Geometry Dash",
        "ranks_by_game": {"Minecraft": 14, "Fortnite": 14, "Roblox": 11, "Geometry Dash": 5}
    },
    {
        "name": "Joc3e",
        "username": "ECRAJoc3e",
        "rank": 15,
        "rank2025": 15,
        "rank_history": ["2025: #15 (joined Fall 2025)"],
        "past_usernames": ["Joc3e", "FFJoc3e", "PRJoc3e", "QRJoc3e", "RSJoc3e", "RCJoc3e"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 11, "Fortnite": 15, "Roblox": 15, "Geometry Dash": 14}
    }
]

# Timeline of member acceptance
acceptance_timeline = [
    {"year": "initial", "accepted": 3},
    {"year": 2018, "accepted": 1},
    {"year": 2019, "accepted": 0},
    {"year": 2020, "accepted": 0},
    {"year": 2021, "accepted": 0},
    {"year": 2022, "accepted": 0},
    {"year": 2023, "accepted": 0},
    {"year": 2024, "accepted": 0},
    {"year": 2025, "accepted": 11},
]

def print_ranked_members():
    print("ECRA Members Ranked:")
    try:
        for m in sorted(members, key=lambda x: x.get("rank", float('inf'))):
            print(f"{m.get('rank', '?')}. {m.get('name', 'Unknown')}")
    except Exception as e:
        print(f"Error printing ranked members: {e}")

def print_acceptance_timeline():
    print("ECRA Acceptance Timeline:")
    try:
        for entry in acceptance_timeline:
            year = entry.get('year', 'Unknown')
            accepted = entry.get('accepted', 0)
            print(f"{year}: {accepted} member(s) accepted")
    except Exception as e:
        print(f"Error printing acceptance timeline: {e}")

def find_member(name):
    for m in members:
        try:
            if m["name"].lower() == name.lower():
                return m
        except Exception:
            continue
    return None

def print_member_stats(member):
    try:
        print(f"{member.get('name', 'Unknown')}'s username is {member.get('username', 'N/A')}")
        print(f"{member.get('name', 'Unknown')} is rank #{member.get('rank', '?')} out of all ECRA members")
        if member.get('rank_history'):
            if yes_no_prompt(f"Do you want to see {member.get('name', 'Unknown')}'s rank history?(yes/no): "):
                for rh in member.get('rank_history', []):
                    print(rh)
        if member.get('past_usernames'):
            if yes_no_prompt(f"Do you want to see {member.get('name', 'Unknown')}'s past usernames?(yes/no): "):
                for pn in member.get('past_usernames', []):
                    print(pn)
        if member.get('skin_mc'):
            if yes_no_prompt(f"Do you want to see {member.get('name', 'Unknown')}'s Skin MC account?(yes/no): "):
                print(member.get('skin_mc'))
    except Exception as e:
        print(f"Error printing member stats: {e}")

def print_best_games():
    print("Best Game for Each Member:")
    try:
        for m in members:
            print(f"{m.get('name', 'Unknown')}: {m.get('best_game', 'Unknown')}")
    except Exception as e:
        print(f"Error printing best games: {e}")

def print_game_ranking(game):
    print(f"Ranking for {game}:")
    try:
        # Show only those who have a rank for that game
        game_ranks = []
        for m in members:
            name = m.get("name", "Unknown")
            ranks_by_game = m.get("ranks_by_game", {})
            rank = ranks_by_game.get(game, 99)
            game_ranks.append((name, rank))
        for name, rank in sorted(game_ranks, key=lambda x: x[1]):
            print(f"#{rank} {name}")
    except Exception as e:
        print(f"Error printing game ranking for {game}: {e}")

# Main interaction loop with error handling
try:
    if yes_no_prompt('Do you want a list of all ECRA members ranked?(yes/no): '):
        print_ranked_members()

    if yes_no_prompt('Do you want to see a timeline of ECRA acceptance?(yes/no): '):
        print_acceptance_timeline()

    userPlayer = get_input('What player would you like to see the stats of?: ').strip()
    if not userPlayer:
        print("You must enter a player name.")
    else:
        member = find_member(userPlayer)
        if member:
            print_member_stats(member)
        else:
            print("Player not found.")

    if yes_no_prompt("Do you want to see the game everyone is best at?(yes/no): "):
        print_best_games()
    else:
        sys.exit()

    if yes_no_prompt('Do you want to see everyone ranked in Minecraft?(yes/no): '):
        print_game_ranking("Minecraft")

    if yes_no_prompt('Do you want to see everyone ranked in Fortnite?(yes/no): '):
        print_game_ranking("Fortnite")

    if yes_no_prompt('Do you want to see everyone ranked in Roblox?(yes/no): '):
        print_game_ranking("Roblox")

    if yes_no_prompt('Do you want to see everyone ranked in Geometry Dash?(yes/no): '):
        print_game_ranking("Geometry Dash")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
