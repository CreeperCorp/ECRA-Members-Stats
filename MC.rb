def yes_no_prompt(prompt)
  loop do
    print prompt
    answer = gets&.strip&.downcase
    if answer == 'yes'
      return true
    elsif answer == 'no'
      return false
    elsif answer.nil?
      puts "\nInput interrupted. Exiting."
      exit
    else
      puts "Please enter 'yes' or 'no'."
    end
  end
end

def get_input(prompt)
  print prompt
  input = gets
  if input.nil?
    puts "\nInput interrupted. Exiting."
    exit
  end
  input.chomp
end

puts 'ECRA accepts members whenever but you have a higher chance to get in if you apply at the beginning of a season.'

members = [
  {
    "name" => "CreepSplotion",
    "username" => "ECRAYungyBot",
    "rank" => 1,
    "rank2025" => 1,
    "rank_history" => ["#1"],
    "past_usernames" => ["ECRACreeperBot", "ECRAShadowCreep", "ECRACreep", "CreepSplotionYT"],
    "skin_mc" => "https://namemc.com/profile/ECRAYungyBot.1",
    "best_game" => "Minecraft",
    "ranks_by_game" => {"Minecraft" => 1, "Fortnite" => 1, "Roblox" => 1, "Geometry Dash" => 1}
  },
  {
    "name" => "Ennard",
    "username" => "ECRAExoticEnnard",
    "rank" => 2,
    "rank2025" => 2,
    "rank_history" => ["2018: #4", "2024: #2"],
    "past_usernames" => ["EqqqEnnard", "ExoticEnnardGG", "EXENNJJERD", "ECRAEnnard", "ECRAMrFeast", "ECRAEnnard", "ECRAExoticEnnard", "OffHandIsA", "IWalkWithQ"],
    "skin_mc" => nil,
    "best_game" => "Minecraft",
    "ranks_by_game" => {"Minecraft" => 2, "Fortnite" => 2, "Roblox" => 2, "Geometry Dash" => 2}
  },
  {
    "name" => "ReapSplotion",
    "username" => "ECRAReap",
    "rank" => 3,
    "rank2025" => 3,
    "rank_history" => ["2018: #2", "2023: #3", "2024: #4", "2025: #3"],
    "past_usernames" => [],
    "skin_mc" => nil,
    "best_game" => "Minecraft",
    "ranks_by_game" => {"Minecraft" => 3, "Fortnite" => 4, "Roblox" => 3, "Geometry Dash" => 3}
  },
  {
    "name" => "Division",
    "username" => "ECRADividedByE",
    "rank" => 4,
    "rank2025" => 4,
    "rank_history" => ["2018: #3", "2023: #2", "2024: #3", "2025: #4"],
    "past_usernames" => ["BetterCreep", "DivideBy78", "Division404", "ExoticDivision", "CSDivision", "ReaperD", "ECRANo", "ECRAyes", "ECRABestMember", "CreepSplotionYT", "ECRADivision", "12LengthTab"],
    "skin_mc" => nil,
    "best_game" => "Fortnite",
    "ranks_by_game" => {"Minecraft" => 4, "Fortnite" => 3, "Roblox" => 4, "Geometry Dash" => 4}
  },
  {
    "name" => "Giggles",
    "username" => "ECRAGiggles",
    "rank" => 5,
    "rank2025" => 5,
    "rank_history" => ["2025: #5 (joined Spring 2025)"],
    "past_usernames" => ["ExoticGiggles (He wasn't actually in EC)", "ECRAGiggles", "ECRANumber5", "ECRANumber3 (He was 3rd in ranking after a bet but lost it to more bets)", "ECRANumber4"],
    "skin_mc" => nil,
    "best_game" => "Minecraft",
    "ranks_by_game" => {"Minecraft" => 5, "Fortnite" => 5, "Roblox" => 5, "Geometry Dash" => 6}
  },
  {
    "name" => "Finxlly",
    "username" => "ECRAFinxlly",
    "rank" => 6,
    "rank2025" => 6,
    "rank_history" => ["2025: #6 (joined Fall 2025)"],
    "past_usernames" => ["FinxllyForever", "FinxllyNever", "FinxllyAI", "FinxllyMC", "F3nxlly", "F3_Finxlly", "CSFinxlly", "FinxllyECRA", "F3nxllyECRA", "CreepSplotionYT"],
    "skin_mc" => nil,
    "best_game" => "Fortnite",
    "ranks_by_game" => {"Minecraft" => 7, "Fortnite" => 6, "Roblox" => 6, "Geometry Dash" => 7}
  },
  {
    "name" => "Quilver",
    "username" => "ECRAQuiliest",
    "rank" => 7,
    "rank2025" => 7,
    "rank_history" => ["2025: #7 (joined Fall 2025)"],
    "past_usernames" => ["Quilver", "Quilverest", "SDQuil", "GhostQuil", "Quilvire", "Quilver", "Quilverest", "QuilRS (Reaper Squad)", "QuilverestRS", "EZQuil", "RCQuil (Reaper Clan)", "Quilver"],
    "skin_mc" => nil,
    "best_game" => "Minecraft",
    "ranks_by_game" => {"Minecraft" => 8, "Fortnite" => 7, "Roblox" => 7, "Geometry Dash" => 8}
  },
  {
    "name" => "Temp0rary",
    "username" => "ECRATemp0rary",
    "rank" => 8,
    "rank2025" => 8,
    "rank_history" => ["2025: #8 (joined Fall 2025)"],
    "past_usernames" => ["Temperaturist", "Telephrist", "GHOSTTemp", "ECTemp0rary"],
    "skin_mc" => nil,
    "best_game" => "Minecraft",
    "ranks_by_game" => {"Minecraft" => 9, "Fortnite" => 10, "Roblox" => 8, "Geometry Dash" => 11}
  },
  {
    "name" => "aXc3L",
    "username" => "ECRAaXc3L",
    "rank" => 9,
    "rank2025" => 9,
    "rank_history" => ["2025: #9 (joined Fall 2025)"],
    "past_usernames" => ["aXc3L", "CSaXc3L", "ReaperaXc3L", "ExoticaXc3L", "aXc3L", "0OPaXc3L", "CSaXc3L", "aXc3L", "ExoticaXc3L"],
    "skin_mc" => nil,
    "best_game" => "Minecraft",
    "ranks_by_game" => {"Minecraft" => 10, "Fortnite" => 12, "Roblox" => 13, "Geometry Dash" => 12}
  },
  {
    "name" => "CreepYT",
    "username" => "CreepYT8451",
    "rank" => 10,
    "rank2025" => 10,
    "rank_history" => ["2025: #10 (joined Summer 2025)"],
    "past_usernames" => [],
    "skin_mc" => nil,
    "best_game" => "Minecraft",
    "ranks_by_game" => {"Minecraft" => 6, "Fortnite" => 11, "Roblox" => 9, "Geometry Dash" => 9}
  },
  {
    "name" => "XRayz",
    "username" => "ECRAXRayz",
    "rank" => 11,
    "rank2025" => 11,
    "rank_history" => ["2025: #11 (joined Fall 2025)"],
    "past_usernames" => ["IXRayForFun", "XRayz", "Xrayz", "XRayzAM", "ISeeThroughWalls", "XRaaaaaaayz", "XXRayz", "RSXRayz", "RCXRayz", "CRXRayz", "CRXRaaaaaaayz"],
    "skin_mc" => nil,
    "best_game" => "Fortnite",
    "ranks_by_game" => {"Minecraft" => 11, "Fortnite" => 8, "Roblox" => 11, "Geometry Dash" => 10}
  },
  {
    "name" => "R3zzignation",
    "username" => "ECRAXR3zz",
    "rank" => 12,
    "rank2025" => 12,
    "rank_history" => ["2025: #12 (joined Fall 2025)"],
    "past_usernames" => ["R3zzignation has been in the most clans out of all ECRA members (24 clans)", "R3zzignation", "R3zz", "POR3zz", "POSTR3zz", "BuddyR3zz", "WOODR3zz", "KOR3zz", "LOSTR3zz"],
    "skin_mc" => nil,
    "best_game" => "Fortnite",
    "ranks_by_game" => {"Minecraft" => 13, "Fortnite" => 9, "Roblox" => 14, "Geometry Dash" => 13}
  },
  {
    "name" => "Batchi",
    "username" => "ECRABatchi",
    "rank" => 13,
    "rank2025" => 13,
    "rank_history" => ["2025: #13 (joined Fall 2025)"],
    "past_usernames" => ["Batch3sBatchi", "BatchesBatchi", "BatchiBatchi", "CabresBatchi", "BBBatchi", "YWNBatchi", "JSBatchi", "HHBATCHI", "CSBatchi", "ReaperBatchi"],
    "skin_mc" => nil,
    "best_game" => "Fortnite",
    "ranks_by_game" => {"Minecraft" => 14, "Fortnite" => 13, "Roblox" => 15, "Geometry Dash" => 14}
  },
  {
    "name" => "Dash",
    "username" => "Dashturle09",
    "rank" => 14,
    "rank2025" => 14,
    "rank_history" => ["2025: #14 (joined Winter 2025)"],
    "past_usernames" => [],
    "skin_mc" => nil,
    "best_game" => "Roblox",
    "ranks_by_game" => {"Minecraft" => 16, "Fortnite" => 14, "Roblox" => 10, "Geometry Dash" => 16}
  },
  {
    "name" => "XxFun",
    "username" => "XxFunWasTaken",
    "rank" => 15,
    "rank2025" => 15,
    "rank_history" => ["2025: #15 (joined Winter 2025)"],
    "past_usernames" => [],
    "skin_mc" => nil,
    "best_game" => "Geometry Dash",
    "ranks_by_game" => {"Minecraft" => 15, "Fortnite" => 15, "Roblox" => 12, "Geometry Dash" => 5}
  },
  {
    "name" => "Joc3e",
    "username" => "ECRAJoc3e",
    "rank" => 16,
    "rank2025" => 16,
    "rank_history" => ["2025: #16 (joined Fall 2025)"],
    "past_usernames" => ["Joc3e", "FFJoc3e", "PRJoc3e", "QRJoc3e", "RSJoc3e", "RCJoc3e"],
    "skin_mc" => nil,
    "best_game" => "Minecraft",
    "ranks_by_game" => {"Minecraft" => 12, "Fortnite" => 16, "Roblox" => 16, "Geometry Dash" => 15}
  }
]

acceptance_timeline = [
  {"year" => "initial", "accepted" => 3},
  {"year" => 2018, "accepted" => 1},
  {"year" => 2019, "accepted" => 0},
  {"year" => 2020, "accepted" => 0},
  {"year" => 2021, "accepted" => 0},
  {"year" => 2022, "accepted" => 0},
  {"year" => 2023, "accepted" => 0},
  {"year" => 2024, "accepted" => 0},
  {"year" => 2025, "accepted" => 12},
]

def print_ranked_members(members)
  puts "ECRA Members Ranked:"
  begin
    members.sort_by { |m| m["rank"] || Float::INFINITY }.each do |m|
      puts "#{m['rank'] || '?'}.\s#{m['name'] || 'Unknown'}"
    end
  rescue => e
    puts "Error printing ranked members: #{e}"
  end
end

def print_acceptance_timeline(acceptance_timeline)
  puts "ECRA Acceptance Timeline:"
  begin
    acceptance_timeline.each do |entry|
      year = entry['year'] || 'Unknown'
      accepted = entry['accepted'] || 0
      puts "#{year}: #{accepted} member(s) accepted"
    end
  rescue => e
    puts "Error printing acceptance timeline: #{e}"
  end
end

def find_member(name, members)
  members.find { |m| m['name']&.downcase == name.downcase }
end

def print_member_stats(member)
  begin
    puts "#{member['name'] || 'Unknown'}'s username is #{member['username'] || 'N/A'}"
    puts "#{member['name'] || 'Unknown'} is rank ##{member['rank'] || '?'} out of all ECRA members"
    if member['rank_history'] && !member['rank_history'].empty?
      if yes_no_prompt("Do you want to see #{member['name'] || 'Unknown'}'s rank history?(yes/no): ")
        member['rank_history'].each { |rh| puts rh }
      end
    end
    if member['past_usernames'] && !member['past_usernames'].empty?
      if yes_no_prompt("Do you want to see #{member['name'] || 'Unknown'}'s past usernames?(yes/no): ")
        member['past_usernames'].each { |pn| puts pn }
      end
    end
    if member['skin_mc']
      if yes_no_prompt("Do you want to see #{member['name'] || 'Unknown'}'s Skin MC account?(yes/no): ")
        puts member['skin_mc']
      end
    end
  rescue => e
    puts "Error printing member stats: #{e}"
  end
end

def print_best_games(members)
  puts "Best Game for Each Member:"
  begin
    members.each do |m|
      puts "#{m['name'] || 'Unknown'}: #{m['best_game'] || 'Unknown'}"
    end
  rescue => e
    puts "Error printing best games: #{e}"
  end
end

def print_game_ranking(members, game)
  puts "Ranking for #{game}:"
  begin
    game_ranks = []
    members.each do |m|
      name = m['name'] || 'Unknown'
      ranks_by_game = m['ranks_by_game'] || {}
      rank = ranks_by_game[game] || 99
      game_ranks << [name, rank]
    end
    game_ranks.sort_by { |x| x[1] }.each do |name, rank|
      puts "##{rank} #{name}"
    end
  rescue => e
    puts "Error printing game ranking for #{game}: #{e}"
  end
end

# Main interaction loop with error handling
begin
  print_ranked_members(members) if yes_no_prompt('Do you want a list of all ECRA members ranked?(yes/no): ')
  print_acceptance_timeline(acceptance_timeline) if yes_no_prompt('Do you want to see a timeline of ECRA acceptance?(yes/no): ')
  
  userPlayer = get_input('What player would you like to see the stats of?: ').strip
  if userPlayer.empty?
    puts "You must enter a player name."
  else
    member = find_member(userPlayer, members)
    if member
      print_member_stats(member)
    else
      puts "Player not found."
    end
  end

  if yes_no_prompt("Do you want to see the game everyone is best at?(yes/no): ")
    print_best_games(members)
  else
    exit
  end

  print_game_ranking(members, "Minecraft") if yes_no_prompt('Do you want to see everyone ranked in Minecraft?(yes/no): ')
  print_game_ranking(members, "Fortnite") if yes_no_prompt('Do you want to see everyone ranked in Fortnite?(yes/no): ')
  print_game_ranking(members, "Roblox") if yes_no_prompt('Do you want to see everyone ranked in Roblox?(yes/no): ')
  print_game_ranking(members, "Geometry Dash") if yes_no_prompt('Do you want to see everyone ranked in Geometry Dash?(yes/no): ')
rescue => e
  puts "An unexpected error occurred: #{e}"
  exit 1
end
