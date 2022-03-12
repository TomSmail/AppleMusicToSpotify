import spotipy
from spotipy.oauth2 import SpotifyOAuth

def setup_inputs():

    print("Read the README document to see how to use this program!\n")
    userID = input("Input your User ID:") 
    playlistName =  input("Enter the filepath of your playlist: ") 
    clientID = input("Enter your Client ID: ") 
    clientSecret = input("Enter your Client Secret: ") 
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope = "user-read-recently-played,playlist-modify-private,playlist-modify-public",client_id = clientID, client_secret = clientSecret, redirect_uri = "http://localhost:8080"))
    setup_list = [userID, playlistName, spotify]
    return setup_list


def create_album(spotify, userID, playlistName):
    with open(playlistName, "r") as file:
        lines = file.readlines()
    spotify.user_playlist_create(user = userID , name="New Playlist", public=True, collaborative=False, description="AppleMusicToSpotify")
    playlists = spotify.current_user_playlists() 
    playlistNames = []
    playlistIDs = []

    for i, item in enumerate(playlists['items']): 
        playlistNames.append(item["name"])
        playlistIDs.append(item["id"])
    positionIndex = playlistNames.index("Best")
    song_list = []
    for i in range(len(lines)):
        sub_list = []
        print(lines[i])
        if i != 0:
            line_list = lines[i].split("\t")
            sub_list.append(line_list[0]) # extracts artists and song title
            sub_list.append(line_list[1])
            song_list.append(sub_list)
            
    print(song_list)    
    tracks = []
    for i in range(len(song_list)):
        item = spotify.search(q="artist:" + song_list[i][1]+ " track:" + song_list[i][0], type="track")
        
        
        try: 
            print(f"--- ID OF SONG {i} ---\n")
            print(item["tracks"]["items"][0]["id"])
            tracks.append(item["tracks"]["items"][0]["id"])
            
        except:
            pass
    spotify.playlist_add_items(playlist_id = playlistIDs[positionIndex], items = tracks)
    print("\n   FINISHED!   \n")

if __name__ == "__main__":
    setup_list = setup_inputs()
    create_album(setup_list[2], setup_list[0], setup_list[1])

