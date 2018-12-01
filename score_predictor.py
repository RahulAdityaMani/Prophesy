'''
Created on Dec 1, 2018
@author: acani
'''
from fileinput import filename
def create_team_data(filename):
    
    file = open(filename, "r")
    
    game_data = {}
    
    
    individual_game_info = [str(line.strip()) for line in file]
    
    
    for i in range(15, 32):
        curr_game_info = individual_game_info[i].split(",")
        game_data[curr_game_info[4]] = [[0, 0, -1, -1], [0, 0, -1, -1], [0, 0, -1, -1], [0, 0, -1, -1], 
                                        [0, 0, -1, -1], [0, 0, -1, -1],[0, 0, -1, -1], [0, 0, -1, -1], 
                                        [0, 0, -1, -1]]
        game_data[curr_game_info[6]] = [[0, 0, -1, -1], [0, 0, -1, -1], [0, 0, -1, -1], [0, 0, -1, -1], 
                                        [0, 0, -1, -1], [0, 0, -1, -1],[0, 0, -1, -1], [0, 0, -1, -1], 
                                        [0, 0, -1, -1]]
        
        
    for curr_game in individual_game_info:
        curr_game_info = curr_game.split(",")
        
        winning_team = curr_game_info[4]
        winning_team_data = curr_game_info[:4]
        winning_team_data.extend(curr_game_info[5:])
        points_for = int(curr_game_info[8])
        points_against = int(curr_game_info[9])
        time_of_day = int(curr_game_info[3].split(":")[0])
        
        game_data[winning_team][0][0] += 1
        if(game_data[winning_team][0][2] == -1):
            game_data[winning_team][0][2] += points_for + 1
            game_data[winning_team][0][3] += points_against + 1
        else:
            game_data[winning_team][0][2] += points_for
            game_data[winning_team][0][3] += points_against
            
        
        if curr_game_info[5] == "@": #Win on the road
            game_data[winning_team][2][0] += 1
            if(game_data[winning_team][2][2] == -1):
                game_data[winning_team][2][2] += points_for + 1
                game_data[winning_team][2][3] += points_against + 1
            else:
                game_data[winning_team][2][2] += points_for
                game_data[winning_team][2][3] += points_against
        else: #Win at home
            game_data[winning_team][1][0] += 1
            if(game_data[winning_team][1][2] == -1):
                game_data[winning_team][1][2] += points_for + 1
                game_data[winning_team][1][3] += points_against + 1
            else:
                game_data[winning_team][1][2] += points_for
                game_data[winning_team][1][3] += points_against
            
            
        if curr_game_info[1] == "Thu":
            game_data[winning_team][3][0] += 1
            if(game_data[winning_team][3][2] == -1):
                game_data[winning_team][3][2] += points_for + 1
                game_data[winning_team][3][3] += points_against + 1
            else:
                game_data[winning_team][3][2] += points_for
                game_data[winning_team][3][3] += points_against
        elif curr_game_info[1] == "Sun" or curr_game_info[1] == "Sat":
            game_data[winning_team][4][0] += 1
            if(game_data[winning_team][4][2] == -1):
                game_data[winning_team][4][2] += points_for + 1
                game_data[winning_team][4][3] += points_against + 1
            else:
                game_data[winning_team][4][2] += points_for
                game_data[winning_team][4][3] += points_against
        elif curr_game_info[1] == "Mon":
            game_data[winning_team][5][0] += 1
            if(game_data[winning_team][5][2] == -1):
                game_data[winning_team][5][2] += points_for + 1
                game_data[winning_team][5][3] += points_against + 1
            else:
                game_data[winning_team][5][2] += points_for
                game_data[winning_team][5][3] += points_against
            
            
        if time_of_day == 9 or time_of_day == 12 or time_of_day == 1:
            game_data[winning_team][6][0] += 1
            if(game_data[winning_team][6][2] == -1):
                game_data[winning_team][6][2] += points_for + 1
                game_data[winning_team][6][3] += points_against + 1
            else:
                game_data[winning_team][6][2] += points_for
                game_data[winning_team][6][3] += points_against
        elif time_of_day == 4:
            game_data[winning_team][7][0] += 1
            if(game_data[winning_team][7][2] == -1):
                game_data[winning_team][7][2] += points_for + 1
                game_data[winning_team][7][3] += points_against + 1
            else:
                game_data[winning_team][7][2] += points_for
                game_data[winning_team][7][3] += points_against
        elif time_of_day == 7 or time_of_day == 8 or time_of_day == 10:
            game_data[winning_team][8][0] += 1
            if(game_data[winning_team][8][2] == -1):
                game_data[winning_team][8][2] += points_for + 1
                game_data[winning_team][8][3] += points_against + 1
            else:
                game_data[winning_team][8][2] += points_for
                game_data[winning_team][8][3] += points_against
            
            
                             
        
        losing_team = curr_game_info[6]
        losing_team_data = curr_game_info[:6]
        losing_team_data.extend(curr_game_info[7:])
        
        points_for = int(curr_game_info[9])
        points_against = int(curr_game_info[8])
        
        game_data[losing_team][0][1] += 1
        if(game_data[losing_team][0][2] == -1):
            game_data[losing_team][0][2] += points_for + 1
            game_data[losing_team][0][3] += points_against + 1
        else:
            game_data[losing_team][0][2] += points_for
            game_data[losing_team][0][3] += points_against
        
        if curr_game_info[5] == "@": #Loss at home
            game_data[losing_team][1][1] += 1
            if(game_data[losing_team][1][2] == -1):
                game_data[losing_team][1][2] += points_for + 1
                game_data[losing_team][1][3] += points_against + 1
            else:
                game_data[losing_team][1][2] += points_for
                game_data[losing_team][1][3] += points_against
        else: #Loss on the road
            game_data[losing_team][2][1] += 1
            if(game_data[losing_team][2][2] == -1):
                game_data[losing_team][2][2] += points_for + 1
                game_data[losing_team][2][3] += points_against + 1
            else:
                game_data[losing_team][2][2] += points_for
                game_data[losing_team][2][3] += points_against
            
            
        if curr_game_info[1] == "Thu":
            game_data[losing_team][3][1] += 1
            if(game_data[losing_team][3][2] == -1):
                game_data[losing_team][3][2] += points_for + 1
                game_data[losing_team][3][3] += points_against + 1
            else:
                game_data[losing_team][3][2] += points_for
                game_data[losing_team][3][3] += points_against
        elif curr_game_info[1] == "Sun" or curr_game_info[1] == "Sat":
            game_data[losing_team][4][1] += 1
            if(game_data[losing_team][4][2] == -1):
                game_data[losing_team][4][2] += points_for + 1
                game_data[losing_team][4][3] += points_against + 1
            else:
                game_data[losing_team][4][2] += points_for
                game_data[losing_team][4][3] += points_against
        elif curr_game_info[1] == "Mon":
            game_data[losing_team][5][1] += 1
            if(game_data[losing_team][5][2] == -1):
                game_data[losing_team][5][2] += points_for + 1
                game_data[losing_team][5][3] += points_against + 1
            else:
                game_data[losing_team][5][2] += points_for
                game_data[losing_team][5][3] += points_against
        
            
            
        if time_of_day == 9 or time_of_day == 12 or time_of_day == 1:
            game_data[losing_team][6][1] += 1
            if(game_data[losing_team][6][2] == -1):
                game_data[losing_team][6][2] += points_for + 1
                game_data[losing_team][6][3] += points_against + 1
            else:
                game_data[losing_team][6][2] += points_for
                game_data[losing_team][6][3] += points_against
        elif time_of_day == 4:
            game_data[losing_team][7][1] += 1
            if(game_data[losing_team][7][2] == -1):
                game_data[losing_team][7][2] += points_for + 1
                game_data[losing_team][7][3] += points_against + 1
            else:
                game_data[losing_team][7][2] += points_for
                game_data[losing_team][7][3] += points_against
        elif time_of_day == 7 or time_of_day == 8 or time_of_day == 10:
            game_data[losing_team][8][1] += 1
            if(game_data[losing_team][8][2] == -1):
                game_data[losing_team][8][2] += points_for + 1
                game_data[losing_team][8][3] += points_against + 1
            else:
                game_data[losing_team][8][2] += points_for
                game_data[losing_team][8][3] += points_against

    return game_data

def predict_score(team_data, home_team, road_team, day_of_week, time_of_day):
    home_points_for = team_data[home_team][0][2]/16
    home_points_allowed = team_data[home_team][0][3]/16
    road_points_for = team_data[road_team][0][2]/16
    road_points_allowed = team_data[road_team][0][3]/16
    home_points_for_at_home = team_data[home_team][1][2]/8
    home_points_against_at_home = team_data[home_team][1][3]/8
    road_points_for_on_road = team_data[road_team][2][2]/8
    road_points_against_on_road = team_data[road_team][2][3]/8
    home_points_for_on_day_of_week = 0.0
    road_points_for_on_day_of_week = 0.0
    home_points_against_on_day_of_week = 0.0
    road_points_against_on_day_of_week = 0.0
    home_points_for_at_time_of_day = 0.0
    road_points_for_at_time_of_day = 0.0
    home_points_against_at_time_of_day = 0.0
    road_points_against_at_time_of_day = 0.0
    if(day_of_week == "Thu"):
        if(team_data[home_team][3][2] == -1):
            home_points_for_on_day_of_week = team_data[home_team][0][2]/16
            home_points_against_on_day_of_week = team_data[home_team][0][3]/16
        else:
            home_points_for_on_day_of_week = team_data[home_team][3][2]/(team_data[home_team][3][0] + team_data[home_team][3][1])
            home_points_against_on_day_of_week = team_data[home_team][3][3]/(team_data[home_team][3][0] + team_data[home_team][3][1])
        if(team_data[road_team][3][2] == -1):
            road_points_for_on_day_of_week = team_data[road_team][0][2]/16
            road_points_against_on_day_of_week = team_data[road_team][0][3]/16
        else:
            road_points_for_on_day_of_week = team_data[road_team][3][2]/(team_data[road_team][3][0] + team_data[road_team][3][1])
            road_points_against_on_day_of_week = team_data[road_team][3][3]/(team_data[road_team][3][0] + team_data[road_team][3][1])     
    elif(day_of_week == "Sun" or day_of_week == "Sat"):
        if(team_data[home_team][4][2] == -1):
            home_points_for_on_day_of_week = team_data[home_team][0][2]/16
            home_points_against_on_day_of_week = team_data[home_team][0][3]/16
        else:
            home_points_for_on_day_of_week = team_data[home_team][4][2]/(team_data[home_team][4][0] + team_data[home_team][4][1])
            home_points_against_on_day_of_week = team_data[home_team][4][3]/(team_data[home_team][4][0] + team_data[home_team][4][1])
        if(team_data[road_team][4][2] == -1):
            road_points_for_on_day_of_week = team_data[road_team][0][2]/16
            road_points_against_on_day_of_week = team_data[road_team][0][3]/16
        else:
            road_points_for_on_day_of_week = team_data[road_team][4][2]/(team_data[road_team][4][0] + team_data[road_team][4][1])
            road_points_against_on_day_of_week = team_data[road_team][4][3]/(team_data[road_team][4][0] + team_data[road_team][4][1])
    else:
        if(team_data[home_team][5][2] == -1):
            home_points_for_on_day_of_week = team_data[home_team][0][2]/16
            home_points_against_on_day_of_week = team_data[home_team][0][3]/16
        else:
            home_points_for_on_day_of_week = team_data[home_team][5][2]/(team_data[home_team][5][0] + team_data[home_team][5][1])
            home_points_against_on_day_of_week = team_data[home_team][5][3]/(team_data[home_team][5][0] + team_data[home_team][5][1])
        if(team_data[road_team][5][2] == -1):
            road_points_for_on_day_of_week = team_data[road_team][0][2]/16
            road_points_against_on_day_of_week = team_data[road_team][0][3]/16
        else:
            road_points_for_on_day_of_week = team_data[road_team][5][2]/(team_data[road_team][5][0] + team_data[road_team][5][1])
            road_points_against_on_day_of_week = team_data[road_team][5][3]/(team_data[road_team][5][0] + team_data[road_team][5][1])
            
    if time_of_day == 9 or time_of_day == 12 or time_of_day == 1:
        if(team_data[home_team][6][2] == -1):
            home_points_for_at_time_of_day = team_data[home_team][0][2]/16
            home_points_against_at_time_of_day = team_data[home_team][0][3]/16
        else:
            home_points_for_at_time_of_day = team_data[home_team][6][2]/(team_data[home_team][6][0] + team_data[home_team][6][1])
            home_points_against_at_time_of_day = team_data[home_team][6][3]/(team_data[home_team][6][0] + team_data[home_team][6][1])
        if(team_data[road_team][6][2] == -1):
            road_points_for_at_time_of_day = team_data[road_team][0][2]/16
            road_points_against_at_time_of_day = team_data[road_team][0][3]/16
        else:
            road_points_for_at_time_of_day = team_data[road_team][6][2]/(team_data[road_team][6][0] + team_data[road_team][6][1])
            road_points_against_at_time_of_day = team_data[road_team][6][3]/(team_data[road_team][6][0] + team_data[road_team][6][1])
    elif time_of_day == 4:
        if(team_data[home_team][7][2] == -1):
            home_points_for_at_time_of_day = team_data[home_team][0][2]/16
            home_points_against_at_time_of_day = team_data[home_team][0][3]/16
        else:
            home_points_for_at_time_of_day = team_data[home_team][7][2]/(team_data[home_team][7][0] + team_data[home_team][7][1])
            home_points_against_at_time_of_day = team_data[home_team][7][3]/(team_data[home_team][7][0] + team_data[home_team][7][1])
        if(team_data[road_team][7][2] == -1):
            road_points_for_at_time_of_day = team_data[road_team][0][2]/16
            road_points_against_at_time_of_day = team_data[road_team][0][3]/16
        else:
            road_points_for_at_time_of_day = team_data[road_team][7][2]/(team_data[road_team][7][0] + team_data[road_team][7][1])
            road_points_against_at_time_of_day = team_data[road_team][7][3]/(team_data[road_team][7][0] + team_data[road_team][7][1])  
    else:
        if(team_data[home_team][8][2] == -1):
            home_points_for_at_time_of_day = team_data[home_team][0][2]/16
            home_points_against_at_time_of_day = team_data[home_team][0][3]/16
        else:
            home_points_for_at_time_of_day = team_data[home_team][8][2]/(team_data[home_team][8][0] + team_data[home_team][8][1])
            home_points_against_at_time_of_day = team_data[home_team][8][3]/(team_data[home_team][8][0] + team_data[home_team][8][1])
        if(team_data[road_team][8][2] == -1):
            road_points_for_at_time_of_day = team_data[road_team][0][2]/16
            road_points_against_at_time_of_day = team_data[road_team][0][3]/16
        else:
            road_points_for_at_time_of_day = team_data[road_team][8][2]/(team_data[road_team][8][0] + team_data[road_team][8][1])
            road_points_against_at_time_of_day = team_data[road_team][8][3]/(team_data[road_team][8][0] + team_data[road_team][8][1])
    
    past_scores = create_team_matchups("seasonData.txt")
    try:
        home_past_points_for = past_scores[home_team][road_team][0]
        home_past_points_against = past_scores[home_team][road_team][1]
        road_past_points_for = past_scores[road_team][home_team][0]
        road_past_points_against = past_scores[road_team][home_team][1]
        home_points = (home_past_points_for + road_past_points_against + home_points_for_at_home + road_points_against_on_road + home_points_for_on_day_of_week + road_points_against_on_day_of_week + home_points_for_at_time_of_day + road_points_against_at_time_of_day) / 8
        road_points = (road_past_points_for + home_past_points_against + road_points_for_on_road + home_points_against_at_home + road_points_for_on_day_of_week + home_points_against_on_day_of_week + road_points_for_at_time_of_day + home_points_against_at_time_of_day) / 8
    except KeyError:
        home_points = (home_points_for + road_points_allowed + home_points_for_at_home + road_points_against_on_road + home_points_for_on_day_of_week + road_points_against_on_day_of_week + home_points_for_at_time_of_day + road_points_against_at_time_of_day)/8
        road_points = (home_points_allowed + road_points_for+ road_points_for_on_road + home_points_against_at_home + road_points_for_on_day_of_week + home_points_against_on_day_of_week + road_points_for_at_time_of_day + home_points_against_at_time_of_day)/8
    return [home_points, road_points]

def create_team_matchups(filename):
    file = open(filename, "r")
    team_matchups = {}
    individual_team_matchup = [str(line.strip()) for line in file]
    for i in range(15, 32):
        curr_game_info = individual_team_matchup[i].split(",")
        team_matchups[curr_game_info[4]] = {}
        team_matchups[curr_game_info[6]] = {}
    for i in range(0, 255):
        curr_game_info = individual_team_matchup[i].split(",")
        team_matchups[curr_game_info[4]][curr_game_info[6]] = [-1, -1]
        team_matchups[curr_game_info[6]][curr_game_info[4]] = [-1, -1]
    for curr_matchup in individual_team_matchup:
        curr_matchup_info = curr_matchup.split(",")
        winning_team = curr_matchup_info[4]
        winning_team_data = curr_matchup_info[:4]
        winning_team_data.extend(curr_matchup_info[5:])
        winning_points_for = int(curr_matchup_info[8])
        winning_points_against = int(curr_matchup_info[9])
        losing_team = curr_matchup_info[6]
        losing_team_data = curr_matchup_info[:6]
        losing_team_data.extend(curr_matchup_info[7:])
        losing_points_for = int(curr_matchup_info[9])
        losing_points_against = int(curr_matchup_info[8])
        
        if (team_matchups[winning_team][losing_team][0] == -1):
            team_matchups[winning_team][losing_team][0] = winning_points_for
        else:
            team_matchups[winning_team][losing_team][0] = (team_matchups[winning_team][losing_team][0] + winning_points_for) / 2
        
        if (team_matchups[winning_team][losing_team][1] == -1):
            team_matchups[winning_team][losing_team][1] = winning_points_against
        else:
            team_matchups[winning_team][losing_team][1] = (team_matchups[winning_team][losing_team][1] + winning_points_against) / 2
        
        if (team_matchups[losing_team][winning_team][0] == -1):
            team_matchups[losing_team][winning_team][0] = losing_points_for
        else:
            team_matchups[losing_team][winning_team][0] = (team_matchups[losing_team][winning_team][0] + losing_points_for) / 2
        
        if (team_matchups[losing_team][winning_team][1] == -1):
            team_matchups[losing_team][winning_team][1] = losing_points_against
        else:
            team_matchups[losing_team][winning_team][1] = (team_matchups[losing_team][winning_team][1] + losing_points_against) / 2        
    return team_matchups
    



if __name__ == '__main__':
    array = [1, 2, 3]
    team_data = create_team_data("seasonData.txt")
    team_matchups = create_team_matchups("seasonData.txt")
    #for i in team_data["Arizona Cardinals"]:
    print("[[W, L, PF, PA], [HW, HL, HPF, HPA], [RW, RL, RPF, RPA], [TW, TL, TPF, TPA], [SW, SL, SPF, SPA], [MW, ML, MPF, MPA], [1W, 1L, 1PF, 1PA], [4W, 4L, 4PF, 4PA], [8W, 8L, 8PF, 8PA]")
    print(team_data["Philadelphia Eagles"])
    print(team_data["Atlanta Falcons"])
    print(predict_score(team_data, "Green Bay Packers", "Seattle Seahawks", "Thur", 8))
    print(predict_score(team_data, "Carolina Panthers", "Dallas Cowboys", "Sun", 4))
    print(team_matchups["Arizona Cardinals"])
    team_data_file = open('TeamData.txt', 'w')
    for team in team_data:
        team_data_file.write(team + ",")
        for type_of_game in range(0, len(team_data[team])):
            for stat in range(0, len(team_data[team][type_of_game])):
                team_data_file.write(str(team_data[team][type_of_game][stat])) 
                if stat != len(team_data[team][type_of_game]) or type_of_game != len(team_data[team]):
                    team_data_file.write(",")
               
        team_data_file.write('\n')