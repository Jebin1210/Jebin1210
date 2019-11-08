import numpy as np
import pandas as pd
matchdf = pd.read_excel("Match.xlsx")

team1lst=matchdf['Team_Name_Id'].value_counts()
team2lst=matchdf['Opponent_Team_Id'].value_counts()
tot=team1lst+team2lst
team1lst=team1lst.sort_index()
team2lst=team2lst.sort_index()
team1lst=team1lst.reset_index()
team2lst=team2lst.reset_index()
tot= tot.reset_index()


print(tot.columns)
tot=tot.rename(columns={'index':'Team_Id',0:'Match_Count_Total'})

match_stat['Team_Id'] = tot['Team_Id']


match_stat['Home_Match_Count']=team1lst['Team_Name_Id']
match_stat['Away_Match_Count']=team2lst['Opponent_Team_Id']

match_stat['Match_Count_Total'] = tot['Match_Count_Total']



nummatcheswon=matchdf['Match_Winner_Id'].value_counts()
nummatcheswon=nummatcheswon.sort_index()
nummatcheswon=nummatcheswon.reset_index()
nummatcheswon=nummatcheswon.rename(columns={'index':'Team_Id'})
match_stat['Matches_Won']=nummatcheswon['Match_Winner_Id']

winpercent= matchdf.groupby('Match_Winner_Id').agg({'Won_By':'count'})
match_stat=match_stat.set_index('Team_Id')
match_stat['Tot_Win_Percent']=winpercent['Won_By']

match_stat['Tot_Win_Percent']=match_stat['Tot_Win_Percent']/match_stat['Match_Count_Total']*100

hometeamwon=matchdf.query('Team_Name_Id==Match_Winner_Id')
awayteamwon=matchdf.query('Opponent_Team_Id==Match_Winner_Id')

homewon=hometeamwon['Match_Winner_Id'].value_counts()
homewon=homewon.sort_index().reset_index().set_index('index')

awaywon=awayteamwon['Match_Winner_Id'].value_counts()
awaywon=awaywon.sort_index().reset_index().set_index('index')

match_stat['Home_Match_Won']=homewon['Match_Winner_Id']
match_stat['Away_Match_Won']=awaywon['Match_Winner_Id']

match_stat['Home_Win_Percent']=match_stat['Home_Match_Won']/match_stat['Home_Match_Count']*100
match_stat['Away_Win_Percent']=match_stat['Away_Match_Won']/match_stat['Away_Match_Count']*100

