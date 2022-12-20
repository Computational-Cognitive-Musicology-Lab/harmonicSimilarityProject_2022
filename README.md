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

## Methods
In this project, we present a new method to measure the similarity between chord progressions: ***Chord Progression Similarity Index (CPSI)***. 
The main idea to calculate the chord progression similarity index, using hidden Markov models, is a common technique in NLP. 
The chord progression similarity index is calculated from the Euclidean distance of the transition matrix formed by the notes required for the chord formation in the chord progression. 
Compared with the chord alignment method, the advantage of using the transition matrix to calculate the similarity index is that this algorithm can handle chord progressions containing different chord numbers and is not influenced by inversion chords. 
Based on the initial ideas mentioned above, three different transition matrix algorithms are derived, and their differences are mainly in the calculation of the chord weights in the chord progression: 
1. Leading chords have higher weight; 
2. The transition between two similar chord weights lower; 
3. The repeated chord progressions with slightly changes have lower weights.  

Another important thing to consider is how well the similarity index calculated by the algorithm matches the similarity perceived by the human ear. To improve the model, an additional adjacent matrix will be added to match the human perception. 

## Perceptual Experience
Experiment design can be found in `ExperimentalInterface` and `Questionnaire` folders. Experiment data analysis can be found in `python_analysis` folder.

The link for the perceptual experiment can be found [here](https://ccml.gtcmt.gatech.edu/ChordSimilarity/interface.html).

## Several Important Conclusions
1. The leading chord in a chord progression has twice the importance compared to other chords according to our data analysis;
2. The data analysis showed that there are significant differences if we change the chord type in a chord progression, for example, replacing triads with seventh chords;
3. Most people consider the chord progressions different if we shuffle the order of chords in a chord progression, no matter if it’s still the same loop starting from different chords or it’s a different loop. 

