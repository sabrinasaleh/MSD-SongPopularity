##### Capstone Project by Sabrina Saleh | Talent Path | July 2021

# **Song Popularity Prediction: ML Classification**

### Project Summary
* The objective of this project is to build an **_interactive app_**, where the users can select a set of artist's features and song's features from the input option and as the outcome, the app will generate a song's popularity prediction based on the selected features. 
* The key users of this app are mostly from the **_music industry_**, which is forecasted to be a 61.82 billion dollar market globally and 22.61 billion dollar market in the United States for the year 2021.
* The project utilizes the “Million Song Dataset” (MSD); after the exploratory data analysis and data pre-processing, the final dataset contains a total of **_581909 observations_** with **_12 features_** and 1 target column **_(song_popularity where 1=popular and 0=not_popular)_**.   
* As the machine learning classification model, the **_Random Forest Classifier_** gives the best accuracy score of **_80%_** and ROC accuracy score of **_87.40%_**.    

### Introduction
Music is an integral part of our daily lives. Each year, thousands of music albums are released in the national and world markets. According to the Statista Research Report, the total revenue of the music industry is forecasted to be 61.82 billion dollar globally and 22.61 billion dollar in the United States for the year 2021. The objective of this capstone project is to build an interactive app, which the musicians, music lovers, sound engineers, and various other stakeholders can utilize in conducting songs' popularity prediction. The app will help the diverse stakeholders in learning about artists' (singers') features as well as songs' features that are critical for a song to be declared "popular" by the music industry. The powerful entities of the music industry such as Spotify, MusicBrainz, Echo Nest, and so forth have defined a set of artist's and song's feature-indices in the “Million Song Dataset” (MSD). In order to build the interactive app, I have conducted an extensive data analsis of the MSD feature-indices and incorporated them in developing a machine learning classification model for song's popularity prediction. In brief, the business questions of this project are as follows:

### Business Questions
* What are the artist's features and song's features that determine songs' popularity in the music industry?
* Which machine learning model can best simulate the artists' features and songs' features in predicting songs’ popularity with higher accuracy?  
![screen-1](ScreenShots/screen_target_features_I.PNG)


### Data Collection
The MSD dataset is a collection of metadata of a million contemporary music tracks from 1920 to 2010. It started as a collaborative project between the Echo Nest (now owned by Spotify) and LabROSA of Columbia University. The original dataset contains a total of 1 million observations of unique tracks with 53 feature columns and 1 target column (song_hotness). Important links for the MSD dataset are provided below:
* [Thierry Bertin-Mahieux, Daniel P.W. Ellis, Brian Whitman, and Paul Lamere. The Million Song Dataset. In Proceedings of the 12th International Society for Music Information Retrieval Conference (ISMIR 2011), 2011.](https://www.researchgate.net/publication/220723656_The_Million_Song_Dataset)
* [Million Song Dataset Official Website](http://millionsongdataset.com/)
* [Million Song Dataset HDF5 to CSV Converter, Alexis Greenstreet.](https://github.com/AGeoCoder/Million-Song-Dataset-HDF5-to-CSV) 


### Exploratory Data Analysis
Among the 53 feature of the original dataset, 20 features have been selected to initiate the exploratory data analysis. This selection is guided by the field experts with domain knowledge. The target variable, ‘song_hotness’ is measured on a scale from 0 to 1. This measure is transformed to a binary format, where the new column ‘song_popularity’ is defined by 0=not_popular and 1=popular. **_For the ‘song_hotness’ score below the mean 0.35605, zero (0) is assigned as 'not_popular' and for the ‘song_hotness’ score above the mean 0.35605, one (1) is assigned as 'popular'_**. 

![screen-3](ScreenShots/screen_msd_feature_table.PNG)

#### Definition of Features & Target 
* track_id: Unique ID for each song
* song_title: Title of each song
* release_id: Unique ID for each release (108172)
* release: Title of each release/album
* year: Year when the song was released, according to musicbrainz.org
#### Artist Features
* artist_id: Unique ID for each artist (51751)
* artist_name: Name of each artist
* artist_familiarity: On a scale of 0 and 1, the familiarity index of the artist according to The Echo Nest 
* artist_hotness: On a scale of 0 and 1, the hotness index of the artist according to The Echo Nest
* artist_location: Location (countries/cities) of artist's origin 
#### Song Features
* duration: Duration of the track in seconds
* end_of_fade_in: End time of the fade in (in seconds), at the beginning of the song, according to The Echo Nest
* start_of_fade_out: Start time of the fade out (in seconds), at the end of the song, according to The Echo Nest 
* tempo: Tempo in BPM according to The Echo Nest
* loudness: General loudness of the track where the maximum decibels in mixing is represented as 0
* key: A key is the major or minor scale around which a song revolves; estimation of the key the song is in by The Echo Nest: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
* key_confidence: Confidence level of the key estimation
* mode: A mode is a type of musical scale coupled with a set of characteristic melodic and harmonic behaviors; estimation of the mode the song is in by The Echo Nest: 0, 1
* mode_confidence: Confidence level of the mode estimation
* time_signature: Usual number of beats per bar; time signature of the song according to The Echo Nest: 0, 1, 3, 4, 5, 7
* time_signature_confidence: Confidence level of the time signature estimation
#### Target Variable
* song_hotness: On a scale of 0 and 1, the hotness index of the song according to The Echo Nest 
* song_popularity: 0 = not_popular vs. 1 = popular
#### Missing Data Analysis
* artist_location: Drop the entire column due to 48.71% missing data
* song_hotness: Drop the rows with 41.80% missing data 
![image-1](Images/missing_data.png)
#### Target Variable (Pre_Binary Conversion): "song_hotness"


#### Target Variable (Post_Binary Conversion): "song_popularity"
### Machine Learning Modeling (Classification)

### Key Insights

### Limitations & Future Improvement


