puts 'ECRA accepts members whenever but you have a higher chance to get in if you apply at the beginning of a season.'

def ask(prompt)
  print prompt
  gets&.strip
end

listOfECRAMembers = ask('Do you want a list of all ECRA members ranked?(yes/no): ')

creepRank = 1
ennardRank = 2
ennardRank2026 = 2
reapRank = 3
reapRank2025 = 3
divisionRank = 4
divisionRank2025 = 4
gigglesRank = 5
gigglesRank2025 = 5
quilverRank = 7
creepYTRank = 9
r3zzignationRank = 11
dashRank = 13
xxfunRank = 14
finxllyRank = 6
batchiRank = 12
aXc3LRank = 8
xRayzRank = 10
quilverRank2025 = 7
creepYTRank2025 = 9
r3zzignationRank2025 = 11
dashRank2025 = 13
xxfunRank2025 = 14
finxllyRank2025 = 6
batchiRank2025 = 12
aXc3LRank2025 = 8
xRayzRank2025 = 10
joc3eRank = 15
joc3eRank2025 = 15
members2025 = 11

if listOfECRAMembers == 'yes'
  puts '1. CreepSplotion'
  puts '2. Ennard'
  puts '3. ReapSplotion'
  puts '4. Division'
  puts '5. Giggles'
  puts '6. Finxlly'
  puts '7. Quilver'
  puts '8. aXc3L'
  puts '9. CreepYT'
  puts '10. XRayz'
  puts '11. R3zzignation'
  puts '12. Batchi'
  puts '13. Dash'
  puts '14. XxFun'
  puts '15. Joc3e'
end

ifacceptanceRate = ask('Do you want to see a timeline of ECRA acceptance?(yes/no): ')

if ifacceptanceRate == 'yes'
  puts "ECRA had 3 members initially, accepted 1 member in 2018, 0 members in 2019, 0 members in 2020, 0 members in 2021, 0 members in 2022, 0 members in 2023, 0 members in 2024, and #{members2025} members in 2025."
end

userPlayer = ask('What player would you like to see the stats of?: ')

case userPlayer
when 'CreepSplotion'
  puts "CreepSplotion's username is ECRAYungyBot"
  puts "CreepSplotion is rank ##{creepRank} out of all ECRA members"
  creepRankHistory = ask("Do you want to see CreepSplotion's rank history?(yes/no): ")
  if creepRankHistory == 'yes'
    puts 'CreepSplotion has only been in the #1 placement'
  end
  creepPastUsernames = ask("Do you want to see CreepSplotion's past usernames?(yes/no): ")
  if creepPastUsernames == 'yes'
    puts 'ECRACreeperBot'
    puts 'ECRAShadowCreep'
    puts 'ECRACreep'
    puts 'CreepSplotionYT'
  end
  creepSkinMC = ask("Do you want to see CreepSplotion's Skin MC account?(yes/no): ")
  puts 'https://namemc.com/profile/ECRAYungyBot.1' if creepSkinMC == 'yes'
when 'ReapSplotion'
  puts "ReapSplotion's username is ECRAReap"
  puts "ReapSplotion is rank ##{reapRank} out of all ECRA members"
  reapRankHistory = ask("Do you want to see ReapSplotion's rank history?(yes/no): ")
  if reapRankHistory == 'yes'
    puts '2018: #2'
    puts '2023: #3'
    puts '2024: #4'
    puts "2025: ##{reapRank2025}"
  end
  reapPastUsernames = ask("Do you want to see ReapSplotion's past usernames?(yes/no): ")
  puts 'ReapSplotion has no past usernames' if reapPastUsernames == 'yes'
when 'Ennard'
  puts "Ennard's username is ECRAExoticEnnard"
  puts "Ennard is rank ##{ennardRank} out of all ECRA members"
  ennardRankHistory = ask("Do you want to see Ennard's rank history?(yes/no): ")
  if ennardRankHistory == 'yes'
    puts '2018: #4'
    puts '2024: #2'
  end
  ennardPastUsernames = ask("Do you want to see Ennard's past usernames?(yes/no): ")
  if ennardPastUsernames == 'yes'
    puts 'EqqqEnnard'
    puts 'ExoticEnnardGG'
    puts 'EXENNJJERD'
    puts 'ECRAEnnard'
    puts 'ECRAMrFeast'
    puts 'ECRAEnnard'
    puts 'ECRAExoticEnnard'
    puts 'OffHandIsA'
    puts 'IWalkWithQ'
  end
when 'Division'
  puts "Division's username is ECRADividedByE"
  puts "Division is rank ##{divisionRank} out of all ECRA members"
  puts "Division joined late 2018 after ECRA's creation"
  divisionRankHistory = ask("Do you want to see Division's rank history?(yes/no): ")
  if divisionRankHistory == 'yes'
    puts '2018: #3'
    puts '2023: #2'
    puts '2024: #3'
    puts "2025: ##{divisionRank2025}"
  end
  divisionPastUsernames = ask("Do you want to see Division's past usernames?(yes/no): ")
  if divisionPastUsernames == 'yes'
    puts 'BetterCreep'
    puts 'DivideBy78'
    puts 'Division404'
    puts 'ExoticDivision'
    puts 'CSDivision'
    puts 'ReaperD'
    puts 'ECRANo'
    puts 'ECRAyes'
    puts 'ECRABestMember'
    puts 'CreepSplotionYT'
    puts 'ECRADivision'
    puts '12LengthTables'
    puts 'ECRAFiftyFour'
    puts 'HistoricalName'
    puts 'ImportantFile'
    puts 'GoodUsername'
    puts 'ECRAFinally'
    puts 'ECRADivision'
    puts 'EnnardViolateCode'
  end
when 'Giggles'
  puts "Giggles' username is ECRAGiggles"
  puts "Giggles is rank ##{gigglesRank} out of all ECRA members"
  gigglesRankHistory = ask("Do you want to see Giggles' rank history?(yes/no): ")
  if gigglesRankHistory == 'yes'
    puts 'Giggles joined Spring 2025'
    puts "2025: ##{gigglesRank2025}"
  end
  gigglesPastUsernames = ask("Do you want to see Giggles' past usernames?(yes/no): ")
  if gigglesPastUsernames == 'yes'
    puts "ExoticGiggles (He wasn't actually in EC)"
    puts 'ECRAGiggles'
    puts 'ECRANumber5'
    puts 'ECRANumber3 (He was 3rd in ranking after a bet but lost it to more bets)'
    puts 'ECRANumber4'
    puts 'ECRANumber5'
    puts 'ExoticGiggles'
  end
when 'CreepYT'
  puts "CreepYT's username is CreepYT8451"
  puts "CreepYT is rank ##{creepYTRank} out of all ECRA members"
  puts "From now on we'll refer to CreepYT as his real name which is Cillian"
  cillianRankHistory = ask("Do you want to see Cillian's rank history?(yes/no): ")
  if cillianRankHistory == 'yes'
    puts 'Cillian joined Summer 2025'
    puts "2025: ##{creepYTRank2025}"
  end
  cillianPastUsernames = ask("Do you want to see Cillian's past usernames?(yes/no): ")
  puts 'Cillian has no past usernames' if cillianPastUsernames == 'yes'
when 'Dash'
  puts "Dash's username is Dashturle09"
  puts "Dash is rank ##{dashRank} out of all ECRA members"
  dashRankHistory = ask("Do you want to see Dash's rank history?(yes/no): ")
  if dashRankHistory == 'yes'
    puts 'Dash joined Winter 2025'
    puts "2025: ##{dashRank2025}"
  end
  dashPastUsernames = ask("Do you want to see Dash's past usernames?(yes/no): ")
  puts 'Dash has no past usernames' if dashPastUsernames == 'yes'
when 'XxFun'
  puts "XxFun's username is XxFunWasTaken"
  puts "XxFun is rank ##{xxfunRank} out of all ECRA members"
  xxfunRankHistory = ask("Do you want to see XxFun's rank history?(yes/no): ")
  if xxfunRankHistory == 'yes'
    puts 'XxFun joined Winter 2025'
    puts "2025: ##{xxfunRank2025}"
  end
  xxfunPastUsernames = ask("Do you want to see XxFun's past usernames?(yes/no): ")
  puts 'XxFun has no past usernames' if xxfunPastUsernames == 'yes'
when 'Finxlly'
  puts "Finxlly's username is ECRAFinxlly"
  puts "Finxlly is rank ##{finxllyRank} out of all ECRA members"
  finxllyRankHistory = ask("Do you want to see Finxlly's rank history?(yes/no): ")
  if finxllyRankHistory == 'yes'
    puts 'Finxlly joined Fall 2025'
    puts "2025: ##{finxllyRank2025}"
  end
  finxllyPastUsernames = ask("Do you want to see Finxlly's past usernames?(yes/no): ")
  if finxllyPastUsernames == 'yes'
    puts 'FinxllyForever'
    puts 'FinxllyNever'
    puts 'FinxllyAI'
    puts 'FinxllyMC'
    puts 'F3nxlly'
    puts 'F3_Finxlly'
    puts 'CSFinxlly'
    puts 'FinxllyECRA'
    puts 'F3nxllyECRA'
    puts 'CreepSplotionYT'
  end
when 'Batchi'
  puts "Batchi's username is ECRABatchi"
  puts "Batchi is rank ##{batchiRank} out of all ECRA members"
  batchiRankHistory = ask("Do you want to see Batchi's rank history?(yes/no): ")
  if batchiRankHistory == 'yes'
    puts 'Batchi joined Fall 2025'
    puts "2025: ##{batchiRank2025}"
  end
  batchiPastUsernames = ask("Do you want to see Batchi's past usernames?(yes/no): ")
  if batchiPastUsernames == 'yes'
    puts 'Batch3sBatchi'
    puts 'BatchesBatchi'
    puts 'BatchiBatchi'
    puts 'CabresBatchi'
    puts 'BBBatchi'
    puts 'YWNBatchi'
    puts 'JSBatchi'
    puts 'HHBATCHI'
    puts 'CSBatchi'
    puts 'ReaperBatchi'
  end
when 'aXc3L'
  puts "aXc3L's username is ECRAaXc3L"
  puts "aXc3L is rank ##{aXc3LRank} out of all ECRA members"
  aXc3LRankHistory = ask("Do you want to see aXc3L's rank history?(yes/no): ")
  if aXc3LRankHistory == 'yes'
    puts 'aXc3L joined Fall 2025'
    puts "2025: ##{aXc3LRank2025}"
  end
  aXc3LPastUsernames = ask("Do you want to see aXc3L's past usernames?(yes/no): ")
  if aXc3LPastUsernames == 'yes'
    puts 'aXc3L'
    puts 'CSaXc3L'
    puts 'ReaperaXc3L'
    puts 'ExoticaXc3L'
    puts 'aXc3L'
    puts '0OPaXc3L'
    puts 'CSaXc3L'
    puts 'aXc3L'
    puts 'ExoticaXc3L'
  end
when 'Quilver'
  puts "Quilver's username is ECRAQuiliest"
  puts "Quilver is rank ##{quilverRank} out of all ECRA members"
  quilverRankHistory = ask("Do you want to see Quilver's rank history?(yes/no): ")
  if quilverRankHistory == 'yes'
    puts 'Quilver joined Fall 2025'
    puts "2025: ##{quilverRank2025}"
  end
  quilverPastUsernames = ask("Do you want to see Quilver's past usernames?(yes/no): ")
  if quilverPastUsernames == 'yes'
    puts 'Quilver'
    puts 'Quilverest'
    puts 'SDQuil'
    puts 'GhostQuil'
    puts 'Quilvire'
    puts 'Quilver'
    puts 'Quilverest'
    puts 'QuilRS (Reaper Squad)'
    puts 'QuilverestRS'
    puts 'EZQuil'
    puts 'RCQuil (Reaper Clan)'
    puts 'Quilver'
    puts 'CRQuil (Creep Reap Alliance)'
    puts 'CRQuiliest'
    puts 'CRSilliest'
    puts 'ECQuil'
    puts 'ECQuilver'
    puts 'CRQuilver'
    puts 'Quiliest'
    puts 'QuietestQuil'
    puts 'BannedBruh (Quil lost a bet to ReapSplotion and got banned from CR)'
    puts 'ECRAQuil'
  end
when 'XRayz'
  puts "XRayz's username is ECRAXRayz"
  puts "XRayz is rank ##{xRayzRank} out of all ECRA members"
  xRayzRankHistory = ask("Do you want to see XRayz's rank history?(yes/no): ")
  if xRayzRankHistory == 'yes'
    puts 'XRayz joined Fall 2025'
    puts "2025: ##{xRayzRank2025}"
  end
  xRayzPastUsernames = ask("Do you want to see XRayz's past usernames?(yes/no): ")
  if xRayzPastUsernames == 'yes'
    puts 'IXRayForFun'
    puts 'XRayz'
    puts 'Xrayz'
    puts 'XRayzAM'
    puts 'ISeeThroughWalls'
    puts 'XRaaaaaaayz'
    puts 'XXRayz'
    puts 'RSXRayz'
    puts 'RCXRayz'
    puts 'CRXRayz'
    puts 'CRXRaaaaaaayz'
  end
when 'R3zzignation'
  puts "R3zzignation's username is ECRAXR3zz"
  puts "R3zzignation is rank ##{r3zzignationRank} out of all ECRA members"
  r3zzignationRankHistory = ask("Do you want to see R3zzigantion's rank history?(yes/no): ")
  if r3zzignationRankHistory == 'yes'
    puts 'R3zzignation joined Fall 2025'
    puts "2025: ##{r3zzignationRank2025}"
  end
  r3zzignationPastUsernames = ask("Do you want to see r3zzignation's past usernames?(yes/no): ")
  if r3zzignationPastUsernames == 'yes'
    puts 'R3zzignation has been in the most clans out of all ECRA members (24 clans)'
    puts 'R3zzignation'
    puts 'R3zz'
    puts 'POR3zz'
    puts 'POSTR3zz'
    puts 'BuddyR3zz'
    puts 'WOODR3zz'
    puts 'KOR3zz'
    puts 'LOSTR3zz'
    puts 'EXR3zz'
    puts 'QIR3zz'
    puts 'CLLR3zz'
    puts 'GBR3zz'
    puts 'PCR3zz'
    puts 'OKR3zz'
    puts 'CHEZR3zz'
    puts 'RRRR3zz'
    puts 'WSR3zz'
    puts 'BOR3zz'
    puts 'KMR3zz'
    puts 'CSR3zz'
    puts 'PRR3zz'
    puts 'FNR3zz'
    puts 'FCR3zz'
    puts 'DMGR3zz'
    puts 'VCR3zz'
    puts 'RCR3zz'
    puts 'R3zzignation'
    puts 'RCR3zz'
    puts 'Resigned'
    puts 'RCR3zz'
    puts 'RCR3zzz'
  end
when 'Joc3e'
  puts "Joc3e's username is ECRAJoc3e"
  puts "Joc3e is rank ##{joc3eRank} out of all ECRA members"
  joc3eRankHistory = ask("Do you want to see Joc3e's rank history?(yes/no): ")
  if joc3eRankHistory == 'yes'
    puts 'Joc3e joined Fall 2025'
    puts "2025: ##{joc3eRank2025}"
  end
  joc3ePastUsernames = ask("Do you want to see joc3e's past usernames?(yes/no): ")
  if joc3ePastUsernames == 'yes'
    puts 'Joc3e'
    puts 'FFJoc3e'
    puts 'PRJoc3e'
    puts 'QRJoc3e'
    puts 'RSJoc3e'
    puts 'RCJoc3e'
  end
end

playersBestGame = ask("Do you want to see the game everyone is best at?(yes/no): ")
unless playersBestGame == 'yes'
  exit
end

puts 'CreepSplotion: Minecraft'
puts 'Ennard: Minecraft'
puts 'ReapSplotion: Minecraft'
puts 'Division: Fortnite'
puts 'Giggles: Minecraft'
puts 'Quilver: Minecraft'
puts 'aXc3L: Minecraft'
puts 'XRayz: Fortnite'
puts 'CreepYT: Minecraft'
puts 'R3zzignation: Fortnite'
puts 'Batchi: Fortnite'
puts 'Dash: Roblox'
puts 'XxFun: Geometry Dash'
puts 'Joc3e: Minecraft'
puts 'Finxlly: Fortnite'

playersBestGameRankedMC = ask('Do you want to see everyone ranked in Minecraft?(yes/no): ')
if playersBestGameRankedMC == 'yes'
  puts '#1 CreepSplotion'
  puts '#2 Ennard'
  puts '#3 ReapSplotion'
  puts '#4 Division'
  puts '#5 Giggles'
  puts '#6 CreepYT'
  puts '#7 Finxlly'
  puts '#8 Quilver'
  puts '#9 aXc3L'
  puts '#10 XRayz'
  puts '#11 Joc3e'
  puts '#12 R3zzignation'
  puts '#13 Batchi'
  puts '#14 XxFun'
  puts '#15 Dash'
end

playersBestGameRankedFN = ask('Do you want to see everyone ranked in Fortnite?(yes/no): ')
if playersBestGameRankedFN == 'yes'
  puts '#1 CreepSplotion'
  puts '#2 Ennard'
  puts '#3 Division'
  puts '#4 ReapSplotion'
  puts '#5 Giggles'
  puts '#6 Finxlly'
  puts '#7 Quilver'
  puts '#8 XRayz'
  puts '#9 R3zzignation'
  puts '10 CreepYT'
  puts '#11 aXc3L'
  puts '#12 Batchi'
  puts '#13 Dash'
  puts '#14 XxFun'
  puts '#15 Joc3e'
end

playersBestGameRankedRB = ask('Do you want to see everyone ranked in Roblox?(yes/no): ')
if playersBestGameRankedRB == 'yes'
  puts '#1 CreepSplotion'
  puts '#2 Ennard'
  puts '#3 ReapSplotion'
  puts '#4 Division'
  puts '#5 Giggles'
  puts '#6 Finxlly'
  puts '#7 Quilver'
  puts '#8 CreepYT'
  puts '#9 Dash'
  puts '#10 XRayz'
  puts '#11 XxFun'
  puts '#12 aXc3L'
  puts '#13 R3zzignation'
  puts '#14 Batchi'
  puts '#15 Joc3e'
end

playersBestGameRankedGD = ask('Do you want to see everyone ranked in Geometry Dash?(yes/no): ')
if playersBestGameRankedGD == 'yes'
  puts '#1 CreepSplotion'
  puts '#2 Ennard'
  puts '#3 ReapSplotion'
  puts '#4 Division'
  puts '#5 XxFun'
  puts '#6 Giggles'
  puts '#7 Finxlly'
  puts '#8 Quilver'
  puts '#9 CreepYT'
  puts '#10 XRayz'
  puts '#11 aXc3L'
  puts '#12 R3zzignation'
  puts '#13 Batchi'
  puts '#14 Joc3e'
  puts '#15 Dash'
end
