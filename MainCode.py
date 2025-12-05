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
        "username": "ECRAClockWise",
        "rank": 1,
        "rank2025": 1,
        "rank_history": ["#1"],
        "past_usernames": ["ECRACreeperBot", "ECRAShadowCreep", "ECRACreep", "CreepSplotionYT", "ECRAYungyBot", "ECRAUnscripted"],
        "skin_mc": "https://namemc.com/profile/ECRAYungyBot.1",
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 1, "Fortnite": 1, "Roblox": 1, "Geometry Dash": 1, "BTDB2": 1},
        "WonderousSMP": "Yes",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "Ennard",
        "username": "ECRAEnnard",
        "rank": 2,
        "rank2025": 2,
        "rank_history": ["2018: #4", "2024: #2"],
        "past_usernames": ["EqqqEnnard", "ExoticEnnardGG", "EXENNJJERD", "ECRAEnnard", "ECRAMrFeast", "ECRAEnnard", "ECRAExoticEnnard", "OffHandIsA", "IWalkWithQ", "ECRAExoticEnnard"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 2, "Fortnite": 2, "Roblox": 2, "Geometry Dash": 2, "BTDB2": 2},
        "WonderousSMP": "Yes",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "ReapSplotion",
        "username": "ECRAReaperBot",
        "rank": 3,
        "rank2025": 3,
        "rank_history": ["2018: #2", "2023: #3", "2024: #4", "2025: #3"],
        "past_usernames": ["ECRAReap"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 3, "Fortnite": 4, "Roblox": 3, "Geometry Dash": 3, "BTDB2": 3},
        "WonderousSMP": "Yes",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "Division",
        "username": "ECRADividend",
        "rank": 4,
        "rank2025": 4,
        "rank_history": ["2018: #3", "2023: #2", "2024: #3", "2025: #4"],
        "past_usernames": ["BetterCreep", "DivideBy78", "Division404", "ExoticDivision", "CSDivision", "ReaperD", "ECRANo", "ECRAyes", "ECRABestMember", "CreepSplotionYT", "ECRADivision", "12LengthTab", "ECRAFiftyFour", "HistoricalName", "ImportantFile", "GoodUsername", "ECRAFinally", "ECRADivision", "EnnardViolateCode", "ECRADividedByE"],
        "skin_mc": None,
        "best_game": "Fortnite",
        "ranks_by_game": {"Minecraft": 4, "Fortnite": 3, "Roblox": 4, "Geometry Dash": 4, "BTDB2": 4},
        "WonderousSMP": "Yes",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "Giggles",
        "username": "ECRAGiggles",
        "rank": 5,
        "rank2025": 5,
        "rank_history": ["2025: #5 (joined Spring 2025)"],
        "past_usernames": ["ExoticGiggles (He wasn't actually in EC)", "ECRAGiggles", "ECRANumber5", "ECRANumber3 (He was 3rd in ranking after a bet but lost it to more bets)", "ECRANumber4", "ECRANumber5", "ExoticGiggles"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 5, "Fortnite": 5, "Roblox": 5, "Geometry Dash": 7, "BTDB2": 8},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "Quotient",
        "username": "ECRAQuotient",
        "rank": 6,
        "rank2025": 6,
        "rank_history": ["2025: #6 (joined Spring 2025)"],
        "past_usernames": ["CCQuotient (He's Quilver's older brother)"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 6, "Fortnite": 6, "Roblox": 6, "Geometry Dash": 6, "BTDB2": 6},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "Finxlly",
        "username": "ECRAFinxlly",
        "rank": 7,
        "rank2025": 7,
        "rank_history": ["2025: #7 (joined Fall 2025)"],
        "past_usernames": ["FinxllyForever", "FinxllyNever", "FinxllyAI", "FinxllyMC", "F3nxlly", "F3_Finxlly", "CSFinxlly", "FinxllyECRA", "F3nxllyECRA", "CreepSplotionYT"],
        "skin_mc": None,
        "best_game": "Fortnite",
        "ranks_by_game": {"Minecraft": 8, "Fortnite": 9, "Roblox": 7, "Geometry Dash": 9, "BTDB2": 9},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "Quilver",
        "username": "ECRAQuiliest",
        "rank": 8,
        "rank2025": 8,
        "rank_history": ["2025: #8 (joined Fall 2025)"],
        "past_usernames": ["Quilver", "Quilverest", "SDQuil", "GhostQuil", "Quilvire", "Quilver", "Quilverest", "QuilRS (Reaper Squad)", "QuilverestRS", "EZQuil", "RCQuil (Reaper Clan)", "Quilver", "CRQuil (Creep Reap Alliance)", "Quilver", "CRQuilliest", "CRSilliest", "ECQuil", "ECQuilver", "CRQuilver", "Quiliest", "QuietestQuil", "BannedBruh (Quil lost a bet to ReapSplotion and got banned from CR", "ECRAQuil"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 9, "Fortnite": 10, "Roblox": 8, "Geometry Dash": 10, "BTDB2": 5},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
    "name": "PolyPePtide",
        "username": "ECRAP0lyPePtide",
        "rank": 9,
        "rank2025": 9,
        "rank_history": ["2025: #9 (joined Fall 2025)"],
        "past_usernames": ["Poly3ptide", "Polyester", "RCPoly3ptide", "RCPolyz", "RCP0lyPeptide", "RCP0lyP3ptide"],
        "skin_mc": None,
        "best_game": "Fortnite",
        "ranks_by_game": {"Minecraft": 15, "Fortnite": 7, "Roblox": 13, "Geometry Dash": 11, "BTDB2": 11},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "Temp0rary",
        "username": "ECRATemp0rary",
        "rank": 10,
        "rank2025": 10,
        "rank_history": ["2025: #10 (joined Fall 2025)"],
        "past_usernames": ["Temperaturist", "Telephrist", "GHOSTTemp", "ECTemp0rary"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 10, "Fortnite": 13, "Roblox": 9, "Geometry Dash": 14, "BTDB2": 13},
        "WonderousSMP": "Yes",
        "Immortal Life": "No",
        "QuantumSMP": "No"
    },
    {
        "name": "UnScr1pted",
        "username": "ECRAUnScr1pted",
        "rank": 11,
        "rank2025": 11,
        "rank_history": ["2025: #11 (joined Fall 2025)"],
        "past_usernames": ["UnScripted", "Unscr3pted", "UnScr1pted", "UNSCR1PTED"],
        "skin_mc": None,
        "best_game": "BTDB2",
        "ranks_by_game": {"Minecraft": 11, "Fortnite": 14, "Roblox": 10, "Geometry Dash": 15, "BTDB2": 7},
        "WonderousSMP": "Yes",
        "Immortal Life": "Yes",
        "QuantumSMP": "Yes"
    },
    {
        "name": "ClockWise",
        "username": "ECRAClocker",
        "rank": 12,
        "rank2025": 12,
        "rank_history": ["2025: #12 (joined Fall 2025)"],
        "past_usernames": ["ClosetCheats", "ClockWise"],
        "skin_mc": None,
        "best_game": "Geometry Dash",
        "ranks_by_game": {"Minecraft": 12, "Fortnite": 15, "Roblox": 12, "Geometry Dash": 8, "BTDB2": 10},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "aXc3L",
        "username": "ECRAaXc3L",
        "rank": 13,
        "rank2025": 13,
        "rank_history": ["2025: #13 (joined Fall 2025)"],
        "past_usernames": ["aXc3L", "CSaXc3L", "ReaperaXc3L", "ExoticaXc3L", "aXc3L", "0OPaXc3L", "CSaXc3L", "aXc3L", "ExoticaXc3L"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 16, "Fortnite": 17, "Roblox": 17, "Geometry Dash": 17, "BTDB2": 12},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "CreepYT",
        "username": "CreepYT8451",
        "rank": 14,
        "rank2025": 14,
        "rank_history": ["2025: #14 (joined Summer 2025)"],
        "past_usernames": [],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 7, "Fortnite": 16, "Roblox": 11, "Geometry Dash": 12, "BTDB2": 14},
        "WonderousSMP": "Yes",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "XRayz",
        "username": "ECRAXRayz",
        "rank": 15,
        "rank2025": 15,
        "rank_history": ["2025: #15 (joined Fall 2025)"],
        "past_usernames": ["IXRayForFun", "XRayz", "Xrayz", "XRayzAM", "ISeeThroughWalls", "XRaaaaaaayz", "XXRayz", "RSXRayz", "RCXRayz", "CRXRayz", "CRXRaaaaaaayz"],
        "skin_mc": None,
        "best_game": "Fortnite",
        "ranks_by_game": {"Minecraft": 18, "Fortnite": 8, "Roblox": 15, "Geometry Dash": 13, "BTDB2": 15},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "R3zzignation",
        "username": "ECRAXR3zz",
        "rank": 16,
        "rank2025": 16,
        "rank_history": ["2025: #16 (joined Fall 2025)"],
        "past_usernames": ["R3zzignation has been in the most clans out of all ECRA members (24 clans)", "R3zzignation", "R3zz", "POR3zz", "POSTR3zz", "BuddyR3zz", "WOODR3zz", "KOR3zz", "LOSTR3zz", "EXR3zz", "QIR3zz", "CLLR3zz", "GBR3zz", "PCR3zz", "OKR3zz", "CHEZR3zz", "RRRR3zz", "WSR3zz", "BOR3zz", "KMR3zz", "CSR3zz", "PRR3zz", "FNR3zz", "FCR3zz", "DMGR3zz", "VCR3zz", "RCR3zz", "R3zzignation", "RCR3zz", "Resigned", "RCR3zz", "RCR3zzz"],
        "skin_mc": None,
        "best_game": "Fortnite",
        "ranks_by_game": {"Minecraft": 20, "Fortnite": 11, "Roblox": 18, "Geometry Dash": 20, "BTDB2": 16},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "R3zz0lution",
        "username": "ECRAR3zz0",
        "rank": 17,
        "rank2025": 17,
        "rank_history": ["2025: #17 (joined Fall 2025)"],
        "past_usernames": ["R3zz0lution has been in every clan R3zzignation has been in except Creeper Squad", "R3zzolution", "R3zz0", "POR3zz0", "POSTR3zz0", "BuddyR3zz0", "WOODR3zz0", "KOR3zz0", "LOSTR3zz0", "EXR3zz0", "QIR3zz0", "CLLR3zz0", "GBR3zz0", "PCR3zz0", "OKR3zz0", "CHEZR3zz0", "RRRR3zz0", "WSR3zz0", "BOR3zz0", "KMR3zz0", "PRR3zz0", "FNR3zz0", "FCR3zz0", "DMGR3zz0", "VCR3zz0", "RCR3zz0"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 13, "Fortnite": 12, "Roblox": 19, "Geometry Dash": 18, "BTDB2": 17},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "Velocity",
        "username": "ECRAVelocity",
        "rank": 18,
        "rank2025": 18,
        "rank_history": ["2025: #18 (joined Fall 2025)"],
        "past_usernames": ["V3loc1ty", "Vwelocity", "CCVelocity"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 17, "Fortnite": 19, "Roblox": 21, "Geometry Dash": 16, "BTDB2": 20},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "Anchor",
        "username": "ECRAAnchor",
        "rank": 19,
        "rank2025": 19,
        "rank_history": ["2025: #19 (joined Fall 2025)"],
        "past_usernames": ["Anchorrrrrr", "Anchorzzz", "ECAnchorrr", "ECRAAnchor", "DoubleABatteries"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 14, "Fortnite": 21, "Roblox": 24, "Geometry Dash": 19, "BTDB2": 18},
        "WonderousSMP": "Yes",
        "Immortal Life": "No",
        "QuantumSMP": "Yes"
    },
    {
        "name": "Batchi",
        "username": "ECRABatchi",
        "rank": 20,
        "rank2025": 20,
        "rank_history": ["2025: #20 (joined Fall 2025)"],
        "past_usernames": ["Batch3sBatchi", "BatchesBatchi", "BatchiBatchi", "CabresBatchi", "BBBatchi", "YWNBatchi", "JSBatchi", "HHBATCHI", "CSBatchi", "ReaperBatchi"],
        "skin_mc": None,
        "best_game": "Fortnite",
        "ranks_by_game": {"Minecraft": 22, "Fortnite": 18, "Roblox": 22, "Geometry Dash": 21, "BTDB2": 19},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "Dash",
        "username": "Dashturle09",
        "rank": 21,
        "rank2025": 21,
        "rank_history": ["2025: #21 (joined Winter 2025)"],
        "past_usernames": [],
        "skin_mc": None,
        "best_game": "Roblox",
        "ranks_by_game": {"Minecraft": 24, "Fortnite": 20, "Roblox": 14, "Geometry Dash": 23, "BTDB2": 23},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "XxFun",
        "username": "XxFunWasTaken",
        "rank": 22,
        "rank2025": 22,
        "rank_history": ["2025: #22 (joined Winter 2025)"],
        "past_usernames": [],
        "skin_mc": None,
        "best_game": "Geometry Dash",
        "ranks_by_game": {"Minecraft": 23, "Fortnite": 23, "Roblox": 16, "Geometry Dash": 5, "BTDB2": 22},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "Joc3e",
        "username": "ECRAJoc3e",
        "rank": 23,
        "rank2025": 23,
        "rank_history": ["2025: 23 (joined Fall 2025)"],
        "past_usernames": ["Joc3e", "FFJoc3e", "PRJoc3e", "QRJoc3e", "RSJoc3e", "RCJoc3e"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 19, "Fortnite": 22, "Roblox": 25, "Geometry Dash": 22, "BTDB2": 21},
        "WonderousSMP": "Yes",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "VeeVanessa",
        "username": "ECRAVee",
        "rank": 24,
        "rank2025": 24,
        "rank_history": ["2025: 24 (joined Fall 2025)"],
        "past_usernames": ["VanessaBB"],
        "skin_mc": None,
        "best_game": "Roblox",
        "ranks_by_game": {"Minecraft": 25, "Fortnite": 25, "Roblox": 20, "Geometry Dash": 24, "BTDB2": 24},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
    },
    {
        "name": "BeatrixBubblyBianca",
        "username": "ECRABee",
        "rank": 25,
        "rank2025": 25,
        "rank_history": ["2025: 25 (joined Fall 2025)"],
        "past_usernames": ["BeatrixBB"],
        "skin_mc": None,
        "best_game": "Minecraft",
        "ranks_by_game": {"Minecraft": 21, "Fortnite": 24, "Roblox": 23, "Geometry Dash": 25, "BTDB2": 25},
        "WonderousSMP": "No",
        "Immortal Life": "Yes",
        "QuantumSMP": "No"
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
    {"year": 2025, "accepted": 21},
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
        # Print SMP statuses
        print(f"WonderousSMP status: {member.get('WonderousSMP', 'Unknown')}")
        print(f"Immortal Life status: {member.get('Immortal Life', 'Unknown')}")
        print(f"QuantumSMP status: {member.get('QuantumSMP', 'Unknown')}")
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

def print_SMP_Count():
    for member in members:
        name = member.get('name', 'Unknown')
        wonderous = member.get('WonderousSMP', 'No')
        immortal = member.get('Immortal Life', 'No')
        quantum = member.get('QuantumSMP', 'No')
        print(f"{name}: WonderousSMP = {wonderous}, Immortal Life = {immortal}, QuantumSMP = {quantum}")

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

    if yes_no_prompt('Do you want to see everyone ranked in Bloons Tower Defense Battles 2?(yes/no): '):
        print_game_ranking("BTDB2")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
