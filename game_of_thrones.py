#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd

# Load your dataset
Game_of_thrones = pd.read_csv('C:/Users/Abhinav/Desktop/DataAnalysisCourseMaterials/DataAnalysis/data/game_of_thrones.csv')
Game_of_thrones



# In[42]:


# 1. Remove episodes with missing IMDb ratings
Game_of_thrones = Game_of_thrones.dropna(subset=['Imdb rating'])
Game_of_thrones


# In[39]:


# 2. Convert 'Original air date' to a datetime object
Game_of_thrones['Original air date'] = pd.to_datetime(Game_of_thrones['Original air date'], errors='coerce')
Game_of_thrones


# In[40]:


# 3. Fill missing viewers with 0
Game_of_thrones['U.S. viewers(millions)'].fillna(0, inplace=True)
Game_of_thrones



# In[53]:


import matplotlib.pyplot as plt
import seaborn as sns

# Sort the DataFrame by IMDb rating in ascending order to get lowest-rated episodes
lowest_rated_episodes = Game_of_thrones.sort_values('Imdb rating').head(10)

# Sort the DataFrame by IMDb rating in descending order to get highest-rated episodes
highest_rated_episodes = Game_of_thrones.sort_values('Imdb rating', ascending=False).head(10)

# Create a bar plot for the lowest-rated episodes with a bright color palette
plt.figure(figsize=(12, 6))
sns.barplot(x='Imdb rating', y='Title', data=lowest_rated_episodes, palette='YlOrRd')
plt.xlabel('IMDb Rating')
plt.ylabel('Episode Title')
plt.title('Top 10 Lowest Rated Episodes')
plt.xlim(0, 10)  # Set the rating scale from 0 to 10
plt.show()

# Create a bar plot for the highest-rated episodes with a bright color palette
plt.figure(figsize=(12, 6))
sns.barplot(x='Imdb rating', y='Title', data=highest_rated_episodes, palette='YlGnBu')
plt.xlabel('IMDb Rating')
plt.ylabel('Episode Title')
plt.title('Top 10 Highest Rated Episodes')
plt.xlim(0, 10)  # Set the rating scale from 0 to 10
plt.show()


# In[44]:


import seaborn as sns

# Group the data by season and calculate the total viewers
season_viewers = Game_of_thrones.groupby('Season')['U.S. viewers(millions)'].sum()

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=season_viewers.index, y=season_viewers.values, palette='viridis')
plt.xlabel('Season')
plt.ylabel('Total Viewers (Millions)')
plt.title('Total Viewers per Season')
plt.show()


# In[58]:


import matplotlib.pyplot as plt

# Count the number of episodes adapted from each novel
novel_counts = Game_of_thrones['Novel(s) adapted'].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(novel_counts, labels=novel_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Episodes by Novel Adaptation')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[45]:


# Group the data by director and count the number of episodes
director_episodes = Game_of_thrones.groupby('Directed by')['Title'].count().reset_index()

# Sort by the number of episodes directed
director_episodes = director_episodes.sort_values(by='Title', ascending=False)

# Create a bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x=director_episodes['Directed by'], y=director_episodes['Title'], palette='rocket')
plt.xlabel('Director')
plt.ylabel('Number of Episodes Directed')
plt.title('Number of Episodes Directed by Directors')
plt.xticks(rotation=90)
plt.show()


# In[48]:


# Calculate the mean IMDb rating for each director
director_ratings = Game_of_thrones.groupby('Directed by')['Imdb rating'].mean().reset_index()

# Sort by mean IMDb rating
director_ratings = director_ratings.sort_values(by='Imdb rating', ascending=False)

# Create a bar plot for directors with the highest ratings
plt.figure(figsize=(12, 6))
sns.barplot(x=director_ratings['Imdb rating'], y=director_ratings['Directed by'], palette='coolwarm')
plt.xlabel('Mean IMDb Rating')
plt.ylabel('Director')
plt.title('Directors with Highest Mean IMDb Rating')
plt.show()

# Create a bar plot for directors with the lowest ratings
director_ratings_lowest = director_ratings.tail(10)  # Adjust the number as needed
plt.figure(figsize=(12, 6))
sns.barplot(x=director_ratings_lowest['Imdb rating'], y=director_ratings_lowest['Directed by'], palette='coolwarm')
plt.xlabel('Mean IMDb Rating')
plt.ylabel('Director')
plt.title('Directors with Lowest Mean IMDb Rating')
plt.show()


# In[57]:


import matplotlib.pyplot as plt
import seaborn as sns

# Create a box plot for IMDb ratings by season
plt.figure(figsize=(10, 6))
sns.boxplot(x='Season', y='Imdb rating', data=Game_of_thrones, palette='Set2')
plt.xlabel('Season')
plt.ylabel('IMDb Rating')
plt.title('IMDb Ratings by Season')
plt.show()


# In[55]:


import matplotlib.pyplot as plt
import pandas as pd

# Convert the "Original air date" column to a datetime format
Game_of_thrones['Original air date'] = pd.to_datetime(Game_of_thrones['Original air date'])

# Group episodes by their air date and sum the viewers for each date
viewers_time_series = Game_of_thrones.groupby('Original air date')['U.S. viewers(millions)'].sum()

# Create a time series plot
plt.figure(figsize=(12, 6))
plt.plot(viewers_time_series.index, viewers_time_series.values)
plt.xlabel('Air Date')
plt.ylabel('U.S. Viewers (millions)')
plt.title('U.S. Viewers Over Time')
plt.xticks(rotation=45)
plt.show()


# In[ ]:




