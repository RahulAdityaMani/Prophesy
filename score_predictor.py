'''
Created on Dec 1, 2018

@author: acani
'''
def create_team_data(filename):
    
    file = open(filename, "r")
    
    game_data = {}
    
    
    individual_game_info = [str(line.strip()) for line in file]
    
    
    for i in range(15, 32):
        curr_game_info = individual_game_info[i].split(",")
        game_data[curr_game_info[4]] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 
                                        [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 
                                        [0, 0, 0, 0]]
        game_data[curr_game_info[6]] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 
                                        [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 
                                        [0, 0, 0, 0]]
        
        
    for curr_game in individual_game_info:
        curr_game_info = curr_game.split(",")
        
        winning_team = curr_game_info[4]
        winning_team_data = curr_game_info[:4]
        winning_team_data.extend(curr_game_info[5:])
        
        points_for = int(curr_game_info[8])
        points_against = int(curr_game_info[9])
        time_of_day = int(curr_game_info[3].split(":")[0])
        
        game_data[winning_team][0][0] += 1
        game_data[winning_team][0][2] += points_for
        game_data[winning_team][0][3] += points_against
        
        if curr_game_info[5] == "@": #Win on the road
            game_data[winning_team][2][0] += 1
            game_data[winning_team][2][2] += points_for
            game_data[winning_team][2][3] += points_against
        else: #Win at home
            game_data[winning_team][1][0] += 1
            game_data[winning_team][1][2] += points_for
            game_data[winning_team][1][3] += points_against
            
            
        if curr_game_info[1] == "Thu":
            game_data[winning_team][3][0] += 1
            game_data[winning_team][3][2] += points_for
            game_data[winning_team][3][3] += points_against
        elif curr_game_info[1] == "Sun" or curr_game_info[1] == "Sat":
            game_data[winning_team][4][0] += 1
            game_data[winning_team][4][2] += points_for
            game_data[winning_team][4][3] += points_against
        elif curr_game_info[1] == "Mon":
            game_data[winning_team][5][0] += 1
            game_data[winning_team][5][2] += points_for
            game_data[winning_team][5][3] += points_against
            
            
        if time_of_day == 9 or time_of_day == 12 or time_of_day == 1:
            game_data[winning_team][6][0] += 1
            game_data[winning_team][6][2] += points_for
            game_data[winning_team][6][3] += points_against
        elif time_of_day == 4:
            game_data[winning_team][7][0] += 1
            game_data[winning_team][7][2] += points_for
            game_data[winning_team][7][3] += points_against
        elif time_of_day == 7 or time_of_day == 8 or time_of_day == 10:
            game_data[winning_team][7][0] += 1
            game_data[winning_team][7][2] += points_for
            game_data[winning_team][7][3] += points_against
            
            
                             
        
        losing_team = curr_game_info[6]
        losing_team_data = curr_game_info[:6]
        losing_team_data.extend(curr_game_info[7:])
        
        points_for = int(curr_game_info[9])
        points_against = int(curr_game_info[8])
        
        game_data[losing_team][0][1] += 1
        game_data[losing_team][0][2] += points_for
        game_data[losing_team][0][3] += points_against
        
        if curr_game_info[5] == "@": #Loss at home
            game_data[losing_team][1][1] += 1
            game_data[losing_team][1][2] += points_for
            game_data[losing_team][1][3] += points_against
        else: #Loss on the road
            game_data[losing_team][2][1] += 1
            game_data[losing_team][2][2] += points_for
            game_data[losing_team][2][3] += points_against
            
            
        if curr_game_info[1] == "Thu":
            game_data[losing_team][3][1] += 1
            game_data[losing_team][3][2] += points_for
            game_data[losing_team][3][3] += points_against 
        elif curr_game_info[1] == "Sun" or curr_game_info[1] == "Sat":
            game_data[losing_team][4][1] += 1
            game_data[losing_team][4][2] += points_for
            game_data[losing_team][4][3] += points_against
        elif curr_game_info[1] == "Mon":
            game_data[losing_team][5][1] += 1
            game_data[losing_team][5][2] += points_for
            game_data[losing_team][5][3] += points_against   
            
            
        if time_of_day == 9 or time_of_day == 12 or time_of_day == 1:
            game_data[losing_team][6][1] += 1
            game_data[losing_team][6][2] += points_for
            game_data[losing_team][6][3] += points_against 
        elif time_of_day == 4:
            game_data[losing_team][7][1] += 1
            game_data[losing_team][7][2] += points_for
            game_data[losing_team][7][3] += points_against 
        elif time_of_day == 7 or time_of_day == 8 or time_of_day == 10:
            game_data[losing_team][8][1] += 1
            game_data[losing_team][8][2] += points_for
            game_data[losing_team][8][3] += points_against 
            
                
    return game_data

def predict_score(team_data, home_team, road_team, day_of_week, time_of_day):
    home_points_for = team_data[home_team][0][2]/16
    home_points_allowed = team_data[home_team][0][3]/16
    road_points_for = team_data[road_team][0][2]/16
    road_points_allowed = team_data[road_team][0][3]/16
    
    home_points = (home_points_for + road_points_allowed)/2
    road_points = (home_points_allowed + road_points_for)/2
    return [home_points, road_points]



if __name__ == '__main__':
    array = [1, 2, 3]
    team_data = create_team_data("seasonData.txt")
    #for i in team_data["Arizona Cardinals"]:
    print("[[W, L, PF, PA], [HW, HL, HPF, HPA], [RW, RL, RPF, RPA], [TW, TL, TPF, TPA], [SW, SL, SPF, SPA], [MW, ML, MPF, MPA], [1W, 1L, 1PF, 1PA], [4W, 4L, 4PF, 4PA], [8W, 8L, 8PF, 8PA]")
    print(team_data["Arizona Cardinals"])
    print(team_data["Seattle Seahawks"])
    print(predict_score(team_data, "Arizona Cardinals", "Seattle Seahawks", "Sun", 1))