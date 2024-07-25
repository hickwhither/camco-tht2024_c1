import tkinter
import os, json
from interactor import Interactor

import random

os.system('g++ code1.cpp -o code1.out')
os.system('g++ code2.cpp -o code2.out')
print("Compiling success")

team1 = Interactor('code1.out')
team2 = Interactor('code2.out')

MOVES = {
    'MOVE_UP': [0, -1],
    'MOVE_DOWN': [0, 1],
    'MOVE_LEFT': [-1, 0],
    'MOVE_RIGHT': [1, 0],
}

random_team = random.randint(0, 1)
if random_team:
    team1_team = 'UP'
    team1_pos = [39, 0]
    team2_team = 'DOWN'
    team2_pos = [39, 39]
else:
    team2_team = 'UP'
    team2_pos = [39, 0]
    team1_team = 'DOWN'
    team1_pos = [39, 39]

T = random.randint(1, 1600)
board = list(list(random.randint(-1, 10) for j in range(40)) for i in range(40))
flag = list(list(0 for i in range(40)) for i in range(40))
board_text = '\n'.join(' '.join(str(j) for j in i) for i in board)

data = {
    'T': T,
    'board': board,
    'steps': []
}

team1.writeline(team1_team)
team1.writeline(T)
team1.writeline(board_text)

team2.writeline(team2_team)
team2.writeline(T)
team2.writeline(board_text)

print(f"steps: {T}")

for i in range(T):
    
    team1_move = team1.readline()
    team2_move = team2.readline()
    team1.writeline(team2_move)
    team2.writeline(team1_move)
    if team1_move != "PLACE_FLAG":
        team1_pos[0] = max(min(team1_pos[0]+MOVES[team1_move][0], 39),0)
        team1_pos[1] = max(min(team1_pos[0]+MOVES[team1_move][1], 39),0)
        print(team1_pos)
        if board[team1_pos[0]][team1_pos[1]] == -1:
            team1_pos[0] = max(min(team1_pos[0]-MOVES[team1_move][0], 39),0)
            team1_pos[1] = max(min(team1_pos[1]-MOVES[team1_move][1], 39),0)
    if team2_move != "PLACE_FLAG":
        team2_pos[0] = max(min(team2_pos[0]+MOVES[team2_move][0], 39),0)
        team2_pos[1] = max(min(team2_pos[1]+MOVES[team2_move][1], 39),0)
        print(team2_pos)
        if board[team2_pos[0]][team2_pos[1]] == -1:
            team2_pos[0] = max(min(team2_pos[0]-MOVES[team2_move][0], 39),0)
            team2_pos[1] = max(min(team2_pos[1]-MOVES[team2_move][1], 39),0)
    
    if team1_move == "PLACE_FLAG" and team2_move == "PLACE_FLAG" and team1_pos == team2_pos:
        pass
    else:
        if team1_move == "PLACE_FLAG" and flag[team1_pos[0]][team1_pos[1]]==0:
            flag[team1_pos[0]][team1_pos[1]] = 1
        if team2_move == "PLACE_FLAG" and flag[team2_pos[0]][team2_pos[1]]==0:
            flag[team2_pos[0]][team2_pos[1]] = 2
    
    print(team1_move, team2_move)

    step_data = {
        'team1_move': team1_move,
        'team2_move': team2_move,
        'flag_placement': flag
    }
    data['steps'].append(step_data)

team1_point = 0
team2_point = 0

for i in range(40):
    for j in range(40):
        if flag[i][j] == 1: 
            team1_point += board[i][j]
        elif flag[i][j]==2:
            team2_point += board[i][j]

data['team1_point'] = team1_point
data['team2_point'] = team2_point

with open("result.txt", "w", encoding='utf-8') as f:
    json.dump(data, f)

print(f"Team 1: {team1_team} - {team1_point}")
print(f"Team 2: {team2_team} - {team2_point}")

if team1_point == team2_point:
    print("DRAW!")
elif team1_point > team2_point:
    print("Team 1 Wins!")
else:
    print("Team 2 Wins!")

