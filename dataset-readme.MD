## Dataset Guidelines

The dataset includes 3 folders :
- trailers: It has all the videos which have been downloaded from YouTube
- frames: It has the corresponding frames for each second for all the trailers downloaded from YouTube
- data: It has the corresponding information of gender and emotion detected at each frame for the video

The dataset also includes the following files :
- movie-list.csv: It has a list of all the movies which have been released from 2008 to 2017
- data.csv: It has gender and emotion information for each of the trailers in the dataset. It has the following columns :
  - frame_number - the frame number of the trailer in which emotion and gender detection occurred
  - man/woman - whether the detected person was a man or a woman
  - emotion - the emotion potrayed by the man/woman detected in the image
  - year - the year in which the movie was released
  - movie_name - the name of the movie

### Example:
- The movie Raees (released in the year 2017) has a folder by the name 2017-raees in the data folder. This folder has the trailer of the movie. (Eg - data/2017-raees/2017-raees.mp4)
- The individual frames for the video can be found in the folder by the name 2017-raees in the frames folder. (Eg - frames/2017-raees/frame0.jpg , frames/2017-raees/frame1.jpg ....)
- The gender and emotion information for each frame whenever the detection was successful can be found in the folder by the name 2017-raees in the data folder. This folder has a .csv file which has all the data. (Eg - data/2017-raees/2017-raees.csv)


### More information
- 880 videos in the videos directory
- 880 frames folder for each video in the video directory
- 880 data files for each video in the video directory
