'''
Created on Dec 1, 2018

@author: acani
'''
def create_map(filename):
    
    file = open(filename, "r")
    
    team_data = {}
    
    individual_teams_info = [str(line.strip()) for line in file]
    
    for curr_team in individual_teams_info:
        curr_team_info = curr_team.split()
        team_data[curr_team_info[0]] = curr_team_info[1]
    return team_data

def predict_score():
    x = 1



if __name__ == '__main__':
    array = [1, 2, 3]
    team_data = create_map("footballNumbers.txt")