'''
Created on Dec 1, 2018

@author: acani
'''
def create_team_data(filename):
    
    file = open(filename, "r")
    
    game_data = {}
    #For team Data: array = [avg points for, avg points against, wins, losses, 
    #and wins/losses/pointsfor/pointsagainst for the following:
    #home, road, thurs, sun, mon, 1:00, 4:00, 8:00
    
    individual_game_info = [str(line.strip()) for line in file]
    for i in range(15, 32):
        curr_game_info = individual_game_info[i].split(",")
        game_data[curr_game_info[4]] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        game_data[curr_game_info[6]] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for curr_game in individual_game_info:
        curr_game_info = curr_game.split(",")
        winning_team = curr_game_info[4]
        winning_team_data = curr_game_info[:4]
        winning_team_data.extend(curr_game_info[5:])
        points_for = int(curr_game_info[8])
        points_against = int(curr_game_info[9])
        game_data[winning_team][0] += points_for
        game_data[winning_team][1] += points_against
        game_data[winning_team][2] += 1
        if curr_game_info[5] is("@"): #Win on the road
            game_data[winning_team][8] += 1
            game_data[winning_team][10] += points_for
            game_data[winning_team][11] += points_against
        else: #Win at home
            game_data[winning_team][4] += 1
            game_data[winning_team][6] += points_for
            game_data[winning_team][7] += points_against
        
        losing_team = curr_game_info[6]
        losing_team_data = curr_game_info[:6]
        losing_team_data.extend(curr_game_info[7:])
        points_for = int(curr_game_info[9])
        points_against = int(curr_game_info[8])
        game_data[losing_team][0] += points_for
        game_data[losing_team][1] += points_against
        game_data[losing_team][3] += 1
        if curr_game_info[5] is("@"): #Loss at home
            game_data[losing_team][5] += 1
            game_data[losing_team][6] += points_for
            game_data[losing_team][7] += points_against
        else: #Loss on the road
            game_data[losing_team][9] += 1
            game_data[losing_team][10] += points_for
            game_data[losing_team][11] += points_against
    return game_data

def predict_score():
    x = 1



if __name__ == '__main__':
    array = [1, 2, 3]
    team_data = create_team_data("seasonData.txt")
    #for i in team_data["Arizona Cardinals"]:
    print("[PF, PA, W, L, HW, HL, HPF, HPA, RW, RL, RPF, RPA]")
    print(team_data["Arizona Cardinals"])
    print(team_data["Seattle Seahawks"])