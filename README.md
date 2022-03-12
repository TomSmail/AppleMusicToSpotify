# Apple Music / Itunes to Spotify playlist converter
This short project has been created for user's who want to move their old Apple based playlists over to Spotify using Python. This is a very simplistic first try but should work effectively if it is a little hacky. 
# Step 1: Install Python and Spotipy
These are the two prerequisites for this project, assuming you already have python installed run: 

$ pip3 install spotipy

Or install it from here https://spotipy.readthedocs.io/en/2.19.0/#installation

# Step 2: Creating a Spotify App
Wait! This is really easy and is the hackiest thing this project will require. 
First go to https://developer.spotify.com/dashboard/applications and login. 
Then we need to create a new app and add a user. This user needs to have the same email address as the account you want to add the playlists to. 
![image](https://user-images.githubusercontent.com/67635582/158023989-0d651b27-25de-4424-9095-e6ab48a7d127.png)

From here we want to keep this tab open so we can get the client secret and client ID later. 

# Step 3: Exporting a playlist
The program takes a text file and searches for the songs on spotify, then adds them to a playlist. Thus, we need to create this text file. This is done by going to apple music or itunes (File -> Library -> Export Playlist -> Text File) Take this text file and get it's file path. 

<img width="514" alt="Screenshot 2022-03-12 at 15 13 24" src="https://user-images.githubusercontent.com/67635582/158023686-2246a517-ade4-45ee-b635-3b916612cfd3.png">


# Step 4: Run the program
The program should start up and ask for the username of the account you want to upload to (this can be found in the app by clicking on your profile), then it will ask for the file path from earlier. Next you need to enter your client secret and client ID copy these from the Spotify app page from earlier.
Then click enter and you should see the program start to run, once is says "FINISHED!" Check your spotify and hopefully you should have a new playlist there!
