#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pandas matplotlib seaborn


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


# Load the data
file_path = 'C:/Users/PC/OneDrive/Desktop/MLBB_Draft_Data3.1.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')


# In[6]:


# Win Rate Analysis
win_rate_df = df[['BLUE_TEAM', 'RED_TEAM', 'WINNING_TEAM']].copy()
win_rate_df['WINNING_TEAM'] = win_rate_df['WINNING_TEAM'].apply(lambda x: x.strip())
teams = pd.concat([win_rate_df['BLUE_TEAM'], win_rate_df['RED_TEAM']]).unique()

win_rates = []
for team in teams:
    total_matches = len(win_rate_df[(win_rate_df['BLUE_TEAM'] == team) | (win_rate_df['RED_TEAM'] == team)])
    wins = len(win_rate_df[win_rate_df['WINNING_TEAM'] == team])
    win_rate = wins / total_matches if total_matches > 0 else 0
    win_rates.append({'Team': team, 'Win Rate': win_rate})

win_rate_df = pd.DataFrame(win_rates)

# Plotting Win Rates
plt.figure(figsize=(12, 6))
sns.barplot(x='Win Rate', y='Team', data=win_rate_df.sort_values('Win Rate', ascending=False))
plt.title('Team Win Rates')
plt.xlabel('Win Rate')
plt.ylabel('Team')
plt.show()


# In[7]:


# Ban/Pick Analysis
ban_columns = ['BLUE_1STBAN', 'RED_1STBAN', 'BLUE_2NDBAN', 'RED_2NDBAN', 'BLUE_3RDBAN', 'RED_3RDBAN', 'RED_4THBAN', 'BLUE_4THBAN', 'RED_5THBAN', 'BLUE_5THBAN']
pick_columns = ['BLUE_1STPICK', 'RED_1ST PICK', 'RED_2NDPICK', 'BLUE_2NDPICK', 'BLUE_3RDPICK', 'RED_3RDPICK', 'RED_4THPICK', 'BLUE_4THPICK', 'BLUE_5THPICK', 'RED_5THPICK']

ban_frequencies = df[ban_columns].apply(pd.Series.value_counts).fillna(0).sum(axis=1).sort_values(ascending=False)
pick_frequencies = df[pick_columns].apply(pd.Series.value_counts).fillna(0).sum(axis=1).sort_values(ascending=False)

# Plotting Ban Frequencies
plt.figure(figsize=(12, 6))
sns.barplot(x=ban_frequencies.values, y=ban_frequencies.index)
plt.title('Hero Ban Frequencies')
plt.xlabel('Frequency')
plt.ylabel('Hero')
plt.show()


# In[8]:


# Plotting Pick Frequencies
plt.figure(figsize=(12, 6))
sns.barplot(x=pick_frequencies.values, y=pick_frequencies.index)
plt.title('Hero Pick Frequencies')
plt.xlabel('Frequency')
plt.ylabel('Hero')
plt.show()


# In[13]:


# Calculate the number of wins for blue and red teams
blue_team_wins = df['BLUE TEAM WIN'].sum()
red_team_wins = df['RED TEAM WIN'].sum()
total_matches = len(df)

# Plot the number of wins for blue and red teams
plt.figure(figsize=(12, 6))
plt.bar(['Blue Team Wins', 'Red Team Wins'], [blue_team_wins, red_team_wins], color=['blue', 'red'])
plt.axhline(y=total_matches, color='gray', linestyle='--', label=f'Total Matches ({total_matches})')
plt.title('Number of Wins for Blue Team and Red Team')
plt.xlabel('Team')
plt.ylabel('Number of Wins')
plt.legend()
plt.show()


# In[18]:


# Define the pick role columns
pick_role_columns = [
    'BLUE_1STPICK_ROLE', 'RED_1ST PICK_ROLE', 'RED_2NDPICK_ROLE', 'BLUE_2NDPICK_ROLE',
    'BLUE_3RDPICK_ROLE', 'RED_3RDPICK_ROLE', 'RED_4THPICK_ROLE', 'BLUE_4THPICK_ROLE',
    'BLUE_5THPICK_ROLE', 'RED_5THPICK_ROLE'
]

# Plot the distribution of roles for each pick position
for column in pick_role_columns:
    role_counts = df[column].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=role_counts.index, y=role_counts.values, palette='viridis')
    plt.title(f'Distribution of Roles in {column.replace("_", " ")}')
    plt.xlabel('Role')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()


# In[19]:


# Define the pick columns
pick_columns = [
    'BLUE_1STPICK', 'RED_1ST PICK', 'RED_2NDPICK', 'BLUE_2NDPICK',
    'BLUE_3RDPICK', 'RED_3RDPICK', 'RED_4THPICK', 'BLUE_4THPICK',
    'BLUE_5THPICK', 'RED_5THPICK'
]

# Plot the frequencies of hero picks for each pick phase
for column in pick_columns:
    hero_counts = df[column].value_counts()
    plt.figure(figsize=(12, 6))
    sns.barplot(x=hero_counts.values, y=hero_counts.index, palette='viridis')
    plt.title(f'Hero Pick Frequencies in {column.replace("_", " ").replace("PICK", " Pick")}')
    plt.xlabel('Frequency')
    plt.ylabel('Hero')
    plt.show()


# In[ ]:




