'''
Created on Dec 1, 2018
@author: acanino & rahulmani
'''
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
    

    weights = get_weights(curr_game_info[1], time_of_day)
    points_for_weight = weights[0]
    points_against_weight = weights[1]
    points_for_home_weight = weights[2]
    points_against_home_weight = weights[3]
    points_for_road_weight = weights[4]
    points_against_road_weight = weights[5]
    points_for_day_weight = weights[6]
    points_against_day_weight = weights[7]
    points_for_time_weight = weights[8]
    points_against_time_weight = weights[9]
        
        
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
    
    #past_scores = create_team_matchups("seasonData.txt")
    

        
        
    home_points_for *= points_for_weight
    road_points_for *= points_for_weight
    home_points_allowed *= points_against_weight
    road_points_allowed *= points_against_weight
    home_points_for_at_home *= points_for_home_weight
    road_points_for_on_road *= points_for_road_weight
    home_points_against_at_home *= points_against_home_weight
    road_points_against_on_road *= points_against_road_weight
    home_points_for_on_day_of_week *= points_for_day_weight
    road_points_for_on_day_of_week *= points_for_day_weight
    home_points_against_on_day_of_week *= points_against_day_weight
    road_points_against_on_day_of_week *= points_against_day_weight
    home_points_for_at_time_of_day *= points_for_time_weight
    road_points_for_at_time_of_day *= points_for_time_weight
    home_points_against_at_time_of_day *= points_against_time_weight
    road_points_against_at_time_of_day *= points_against_time_weight
    
    home_points = (home_points_for + road_points_allowed + home_points_for_at_home + road_points_against_on_road + home_points_for_on_day_of_week + road_points_against_on_day_of_week + home_points_for_at_time_of_day + road_points_against_at_time_of_day)/8
    road_points = (road_points_for + home_points_allowed + road_points_for_on_road + home_points_against_at_home + road_points_for_on_day_of_week + home_points_against_on_day_of_week + road_points_for_at_time_of_day + home_points_against_at_time_of_day)/8
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
    

def get_weights(day_of_week, time_of_day):
    points_for_weight = 1/16.57988911
    points_against_weight = 1/7.809475806
    points_for_home_weight = 1/17.9500378
    points_against_home_weight = 1/12.08209425
    points_for_road_weight = 1/22.85225554
    points_against_road_weight = 1/18.23229587
    points_for_thu_weight = 1/135.7006048
    points_against_thu_weight = 1/131.6602823
    points_for_sun_weight = 1/17.12467952
    points_against_sun_weight = 1/9.143297173
    points_for_mon_weight = 1/132.516129
    points_against_mon_weight = 1/120.8324093
    points_for_one_weight = 1/35.33302647
    points_against_one_weight = 1/34.16551639
    points_for_four_weight = 1/48.90442876
    points_against_four_weight = 1/60.71823413
    points_for_eight_weight = 1/88.36398718
    points_against_eight_weight = 79.50043879
    if day_of_week == "Thu":
        points_for_day_weight = points_for_thu_weight
        points_against_day_weight = points_against_thu_weight
    elif day_of_week == "Mon":
        points_for_day_weight = points_for_mon_weight
        points_against_day_weight = points_against_mon_weight  
    else:
        points_for_day_weight = points_for_sun_weight
        points_against_day_weight = points_against_sun_weight
        
    if time_of_day == 1:
        points_for_time_weight = points_for_one_weight
        points_against_time_weight = points_against_one_weight
    elif time_of_day == 4:
        points_for_time_weight = points_for_four_weight
        points_against_time_weight = points_against_four_weight
    else:
        points_for_time_weight = points_for_eight_weight
        points_against_time_weight = points_against_eight_weight
        
    weight_sum = points_for_weight + points_against_weight + points_for_home_weight + points_against_home_weight + points_for_road_weight + points_against_road_weight + points_for_day_weight + points_against_day_weight + points_for_time_weight + points_against_time_weight           
    points_for_weight *= 8/weight_sum
    points_against_weight *= 8/weight_sum
    points_for_home_weight *= 8/weight_sum
    points_against_home_weight *= 8/weight_sum
    points_for_road_weight *= 8/weight_sum
    points_against_road_weight *= 8/weight_sum
    points_for_day_weight *= 8/weight_sum
    points_against_day_weight *= 8/weight_sum
    points_for_time_weight *= 8/weight_sum
    points_against_time_weight *= 8/weight_sum
    return [points_for_weight, points_against_weight, points_for_home_weight, points_against_home_weight, points_for_road_weight, points_against_road_weight, points_for_day_weight, points_against_day_weight, points_for_time_weight, points_against_time_weight]

if __name__ == '__main__':
    array = [1, 2, 3]
    team_data = create_team_data("seasonData.txt")
    team_matchups = create_team_matchups("seasonData.txt")

    file = open("InputData.txt", "r")
    
    
    individual_game_info = [str(line.strip()) for line in file]
    file.close()
    
    output = open('Output.txt', 'w')
    for curr_game in individual_game_info:
        curr_game_info = curr_game.split(",")
        predicted_score = predict_score(team_data, str(curr_game_info[0]), str(curr_game_info[1]), str(curr_game_info[2]), int(curr_game_info[3]))
        output.write(str(predicted_score[0]) + "," + str(predicted_score[1]) + '\n')
        
       
       
       