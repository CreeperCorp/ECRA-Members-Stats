const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function ask(question) {
  return new Promise((resolve) => {
    rl.question(question, (answer) => resolve(answer.trim()));
  });
}

async function main() {
  console.log('ECRA accepts members whenever but you have a higher chance to get in if you apply at the beginning of a season.');

  let listOfECRAMembers = await ask('Do you want a list of all ECRA members ranked?(yes/no): ');

  const ranks = {
    creepRank: 1,
    ennardRank: 2,
    ennardRank2026: 2,
    reapRank: 3,
    reapRank2025: 3,
    divisionRank: 4,
    divisionRank2025: 4,
    gigglesRank: 5,
    gigglesRank2025: 5,
    quilverRank: 7,
    creepYTRank: 9,
    r3zzignationRank: 11,
    dashRank: 13,
    xxfunRank: 14,
    finxllyRank: 6,
    batchiRank: 12,
    aXc3LRank: 8,
    xRayzRank: 10,
    quilverRank2025: 7,
    creepYTRank2025: 9,
    r3zzignationRank2025: 11,
    dashRank2025: 13,
    xxfunRank2025: 14,
    finxllyRank2025: 6,
    batchiRank2025: 12,
    aXc3LRank2025: 8,
    xRayzRank2025: 10,
    joc3eRank: 15,
    joc3eRank2025: 15,
    members2025: 11
  };

  if (listOfECRAMembers.toLowerCase() === 'yes') {
    console.log('1. CreepSplotion');
    console.log('2. Ennard');
    console.log('3. ReapSplotion');
    console.log('4. Division');
    console.log('5. Giggles');
    console.log('6. Finxlly');
    console.log('7. Quilver');
    console.log('8. aXc3L');
    console.log('9. CreepYT');
    console.log('10. XRayz');
    console.log('11. R3zzignation');
    console.log('12. Batchi');
    console.log('13. Dash');
    console.log('14. XxFun');
    console.log('15. Joc3e');
  }

  let ifacceptanceRate = await ask('Do you want to see a timeline of ECRA acceptance?(yes/no): ');
  if (ifacceptanceRate.toLowerCase() === 'yes') {
    console.log(`ECRA had 3 members initially, accepted 1 member in 2018, 0 members in 2019, 0 members in 2020, 0 members in 2021, 0 members in 2022, 0 members in 2023, 0 members in 2024, and ${ranks.members2025} members in 2025.`);
  }

  let userPlayer = await ask('What player would you like to see the stats of?: ');

  userPlayer = userPlayer.trim();

  // Define player info as a map
  const players = {
    "CreepSplotion": {
      username: "ECRAYungyBot",
      rank: ranks.creepRank,
      rankHistory: ["CreepSplotion has only been in the #1 placement"],
      pastUsernames: ["ECRACreeperBot", "ECRAShadowCreep", "ECRACreep", "CreepSplotionYT"],
      skinMC: "https://namemc.com/profile/ECRAYungyBot.1"
    },
    "ReapSplotion": {
      username: "ECRAReap",
      rank: ranks.reapRank,
      rankHistory: ['2018: #2', '2023: #3', '2024: #4', `2025: #${ranks.reapRank2025}`],
      pastUsernames: ["ReapSplotion has no past usernames"]
    },
    "Ennard": {
      username: "ECRAExoticEnnard",
      rank: ranks.ennardRank,
      rankHistory: ['2018: #4', '2024: #2'],
      pastUsernames: ["EqqqEnnard","ExoticEnnardGG","EXENNJJERD","ECRAEnnard","ECRAMrFeast","ECRAEnnard","ECRAExoticEnnard","OffHandIsA","IWalkWithQ"]
    },
    "Division": {
      username: "ECRADividedByE",
      rank: ranks.divisionRank,
      special: "Division joined late 2018 after ECRA's creation",
      rankHistory: ['2018: #3', '2023: #2', '2024: #3', `2025: #${ranks.divisionRank2025}`],
      pastUsernames: ["BetterCreep","DivideBy78","Division404","ExoticDivision","CSDivision","ReaperD","ECRANo","ECRAyes","ECRABestMember","CreepSplotionYT","ECRADivision","12LengthTables","ECRAFiftyFour","HistoricalName","ImportantFile","GoodUsername","ECRAFinally","ECRADivision","EnnardViolateCode"]
    },
    "Giggles": {
      username: "ECRAGiggles",
      rank: ranks.gigglesRank,
      rankHistory: ["Giggles joined Spring 2025", `2025: #${ranks.gigglesRank2025}`],
      pastUsernames: ["ExoticGiggles (He wasn't actually in EC)","ECRAGiggles","ECRANumber5","ECRANumber3 (He was 3rd in ranking after a bet but lost it to more bets)","ECRANumber4","ECRANumber5","ExoticGiggles"]
    },
    "CreepYT": {
      username: "CreepYT8451",
      rank: ranks.creepYTRank,
      special: "From now on we'll refer to CreepYT as his real name which is Cillian",
      rankHistory: ["Cillian joined Summer 2025", `2025: #${ranks.creepYTRank2025}`],
      pastUsernames: ["Cillian has no past usernames"]
    },
    "Dash": {
      username: "Dashturle09",
      rank: ranks.dashRank,
      rankHistory: ["Dash joined Winter 2025", `2025: #${ranks.dashRank2025}`],
      pastUsernames: ["Dash has no past usernames"]
    },
    "XxFun": {
      username: "XxFunWasTaken",
      rank: ranks.xxfunRank,
      rankHistory: ["XxFun joined Winter 2025", `2025: #${ranks.xxfunRank2025}`],
      pastUsernames: ["XxFun has no past usernames"]
    },
    "Finxlly": {
      username: "ECRAFinxlly",
      rank: ranks.finxllyRank,
      rankHistory: ["Finxlly joined Fall 2025", `2025: #${ranks.finxllyRank2025}`],
      pastUsernames: ["FinxllyForever","FinxllyNever","FinxllyAI","FinxllyMC","F3nxlly","F3_Finxlly","CSFinxlly","FinxllyECRA","F3nxllyECRA","CreepSplotionYT"]
    },
    "Batchi": {
      username: "ECRABatchi",
      rank: ranks.batchiRank,
      rankHistory: ["Batchi joined Fall 2025", `2025: #${ranks.batchiRank2025}`],
      pastUsernames: ["Batch3sBatchi","BatchesBatchi","BatchiBatchi","CabresBatchi","BBBatchi","YWNBatchi","JSBatchi","HHBATCHI","CSBatchi","ReaperBatchi"]
    },
    "aXc3L": {
      username: "ECRAaXc3L",
      rank: ranks.aXc3LRank,
      rankHistory: ["aXc3L joined Fall 2025", `2025: #${ranks.aXc3LRank2025}`],
      pastUsernames: ["aXc3L","CSaXc3L","ReaperaXc3L","ExoticaXc3L","aXc3L","0OPaXc3L","CSaXc3L","aXc3L","ExoticaXc3L"]
    },
    "Quilver": {
      username: "ECRAQuiliest",
      rank: ranks.quilverRank,
      rankHistory: ["Quilver joined Fall 2025", `2025: #${ranks.quilverRank2025}`],
      pastUsernames: ["Quilver","Quilverest","SDQuil","GhostQuil","Quilvire","Quilver","Quilverest","QuilRS (Reaper Squad)","QuilverestRS","EZQuil","RCQuil (Reaper Clan)","Quilver","CRQuil (Creep Reap Alliance)","CRQuiliest","CRSilliest","ECQuil","ECQuilver","CRQuilver","Quiliest","QuietestQuil","BannedBruh (Quil lost a bet to ReapSplotion and got banned from CR)","ECRAQuil"]
    },
    "XRayz": {
      username: "ECRAXRayz",
      rank: ranks.xRayzRank,
      rankHistory: ["XRayz joined Fall 2025", `2025: #${ranks.xRayzRank2025}`],
      pastUsernames: ["IXRayForFun","XRayz","Xrayz","XRayzAM","ISeeThroughWalls","XRaaaaaaayz","XXRayz","RSXRayz","RCXRayz","CRXRayz","CRXRaaaaaaayz"]
    },
    "R3zzignation": {
      username: "ECRAXR3zz",
      rank: ranks.r3zzignationRank,
      rankHistory: ["R3zzignation joined Fall 2025", `2025: #${ranks.r3zzignationRank2025}`],
      pastUsernames: ["R3zzignation has been in the most clans out of all ECRA members (24 clans)","R3zzignation","R3zz","POR3zz","POSTR3zz","BuddyR3zz","WOODR3zz","KOR3zz","LOSTR3zz","EXR3zz","QIR3zz","CLLR3zz","GBR3zz","PCR3zz","OKR3zz","CHEZR3zz","RRRR3zz","WSR3zz","BOR3zz","KMR3zz","CSR3zz","PRR3zz","FNR3zz","FCR3zz","DMGR3zz","VCR3zz","RCR3zz","R3zzignation","RCR3zz","Resigned","RCR3zz","RCR3zzz"]
    },
    "Joc3e": {
      username: "ECRAJoc3e",
      rank: ranks.joc3eRank,
      rankHistory: ["Joc3e joined Fall 2025", `2025: #${ranks.joc3eRank2025}`],
      pastUsernames: ["Joc3e","FFJoc3e","PRJoc3e","QRJoc3e","RSJoc3e","RCJoc3e"]
    }
  };

  if (players[userPlayer]) {
    const p = players[userPlayer];
    console.log(`${userPlayer}'s username is ${p.username}`);
    console.log(`${userPlayer} is rank #${p.rank} out of all ECRA members`);
    if (p.special) {
      console.log(p.special);
    }
    let seeRankHistory = await ask(`Do you want to see ${userPlayer}'s rank history?(yes/no): `);
    if (seeRankHistory.toLowerCase() === 'yes') {
      for (let rh of (p.rankHistory || [])) {
        console.log(rh);
      }
    }
    let seePastUsernames = await ask(`Do you want to see ${userPlayer}'s past usernames?(yes/no): `);
    if (seePastUsernames.toLowerCase() === 'yes') {
      for (let pn of (p.pastUsernames || [])) {
        console.log(pn);
      }
    }
    if (p.skinMC) {
      let seeSkin = await ask(`Do you want to see ${userPlayer}'s Skin MC account?(yes/no): `);
      if (seeSkin.toLowerCase() === 'yes') {
        console.log(p.skinMC);
      }
    }
  }

  // Best game for each member
  let playersBestGame = await ask("Do you want to see the game everyone is best at?(yes/no): ");
  if (playersBestGame.toLowerCase() !== 'yes') {
    rl.close();
    return;
  }
  console.log('CreepSplotion: Minecraft');
  console.log('Ennard: Minecraft');
  console.log('ReapSplotion: Minecraft');
  console.log('Division: Fortnite');
  console.log('Giggles: Minecraft');
  console.log('Quilver: Minecraft');
  console.log('aXc3L: Minecraft');
  console.log('XRayz: Fortnite');
  console.log('CreepYT: Minecraft');
  console.log('R3zzignation: Fortnite');
  console.log('Batchi: Fortnite');
  console.log('Dash: Roblox');
  console.log('XxFun: Geometry Dash');
  console.log('Joc3e: Minecraft');
  console.log('Finxlly: Fortnite');

  let playersBestGameRankedMC = await ask('Do you want to see everyone ranked in Minecraft?(yes/no): ');
  if (playersBestGameRankedMC.toLowerCase() === 'yes') {
    console.log('#1 CreepSplotion');
    console.log('#2 Ennard');
    console.log('#3 ReapSplotion');
    console.log('#4 Division');
    console.log('#5 Giggles');
    console.log('#6 CreepYT');
    console.log('#7 Finxlly');
    console.log('#8 Quilver');
    console.log('#9 aXc3L');
    console.log('#10 XRayz');
    console.log('#11 Joc3e');
    console.log('#12 R3zzignation');
    console.log('#13 Batchi');
    console.log('#14 XxFun');
    console.log('#15 Dash');
  }

  let playersBestGameRankedFN = await ask('Do you want to see everyone ranked in Fortnite?(yes/no): ');
  if (playersBestGameRankedFN.toLowerCase() === 'yes') {
    console.log('#1 CreepSplotion');
    console.log('#2 Ennard');
    console.log('#3 Division');
    console.log('#4 ReapSplotion');
    console.log('#5 Giggles');
    console.log('#6 Finxlly');
    console.log('#7 Quilver');
    console.log('#8 XRayz');
    console.log('#9 R3zzignation');
    console.log('10 CreepYT');
    console.log('#11 aXc3L');
    console.log('#12 Batchi');
    console.log('#13 Dash');
    console.log('#14 XxFun');
    console.log('#15 Joc3e');
  }

  let playersBestGameRankedRB = await ask('Do you want to see everyone ranked in Roblox?(yes/no): ');
  if (playersBestGameRankedRB.toLowerCase() === 'yes') {
    console.log('#1 CreepSplotion');
    console.log('#2 Ennard');
    console.log('#3 ReapSplotion');
    console.log('#4 Division');
    console.log('#5 Giggles');
    console.log('#6 Finxlly');
    console.log('#7 Quilver');
    console.log('#8 CreepYT');
    console.log('#9 Dash');
    console.log('#10 XRayz');
    console.log('#11 XxFun');
    console.log('#12 aXc3L');
    console.log('#13 R3zzignation');
    console.log('#14 Batchi');
    console.log('#15 Joc3e');
  }

  let playersBestGameRankedGD = await ask('Do you want to see everyone ranked in Geometry Dash?(yes/no): ');
  if (playersBestGameRankedGD.toLowerCase() === 'yes') {
    console.log('#1 CreepSplotion');
    console.log('#2 Ennard');
    console.log('#3 ReapSplotion');
    console.log('#4 Division');
    console.log('#5 XxFun');
    console.log('#6 Giggles');
    console.log('#7 Finxlly');
    console.log('#8 Quilver');
    console.log('#9 CreepYT');
    console.log('#10 XRayz');
    console.log('#11 aXc3L');
    console.log('#12 R3zzignation');
    console.log('#13 Batchi');
    console.log('#14 Joc3e');
    console.log('#15 Dash');
  }

  rl.close();
}

main();
