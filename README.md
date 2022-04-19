# harmonicSimilarityProject
This project is a research project for MUSI 7100 in Spring 2022.
## Database
A Chinese Pop music database with 200 Chinese pop songs includes twenty most popular songs in each year from 2012 to 2021 with chord progression information. 
Besides the chord progression information, the database also contains the name, ranking year, singer, beat, original key, and the data key of a song. To keep the consistency of the data information, all chord progressions are recorded in major keys.
### Top 20 song database
*Data Info:*
+ Sampling Source: Chinese hottest search top20 popular music in past 10 years (200 songs in total)
+ Data Content: Song Name, Singer, Beat, key (song key & data key), chord progression groups
+ Creator: Jiaying Li, 2022/03/23
The top 20 song information is shown as below:
![image](https://github.com/JiayingLi0803/harmonicSimilarityProject_2022/blob/main/Images/data_information.png)

### Top 10 song database
*Data Info:*
+ Sampling Source: Chinese hottest search top10 popular music in past 10 years (102 songs in total)
+ Data Content: Song Name, Singer, Beat, key (song key & data key), chord progression groups
+ Creator: Jiaying Li, 2022/02/23

The top 10 song information is shown as below:
![image](https://github.com/JiayingLi0803/harmonicSimilarityProject_2022/blob/main/Images/top10data.png)
## Chord Progression Similarity Index Based on the Markov Model
In `python_analysis` folder, `similarity_index_calculation.py` can be used to calculate the similarity index based on the Morkov Model. 
Data analysis of top 10 and top 20 songs can be viewed in `python_analysis` folder.
