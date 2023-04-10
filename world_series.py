#Michael Sherrer
#CS 175L
#World Series Program

with open('WorldSeriesWinners.txt','r') as inputfile:
    keep_running=True
    while keep_running==True:
        try:
            team_list=[line.rstrip('\n') for line in inputfile]
            input_team=input('Enter the name of the team or Quit: ')
            if input_team=='q'or input_team=='Q':
                keep_running=False
            else:
                ws_wins=team_list.index(input_team)
                print(f'The {input_team} won the world series {ws_wins} times between 1903 and 2009')
        except ValueError:
            team_list_lower=[]
            for x in team_list:
                team_list_lower.append(x.lower())
            input_team_lower=input_team.lower()
            ws_wins=team_list_lower.index(input_team_lower)
            print(f'The {input_team_lower} won the world series {ws_wins} times between 1903 and 2009')
    inputfile.close()
    
