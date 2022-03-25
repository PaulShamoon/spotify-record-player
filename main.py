import requests
from refresh import Refresh
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class Player:
    def __init__(self):
        self.spotify_playlist_url = 'https://api.spotify.com/v1/me/player/play'
        self.access_token = ""

    def play_album(self, song):
        self.refresh_token()
        response = requests.put(
            self.spotify_playlist_url,
            headers={
                "Authorization": f"Bearer {self.access_token}"
            },
            json={
                "context_uri": song
            } 
        )
        return response

    def refresh_token(self):
        #print("refreshing token")
        refresh_caller = Refresh()
        self.access_token = refresh_caller.refresh()

    def read_rfid(self):
        reader = SimpleMFRC522()
        try:
            self.id_code = reader.read()[0]
            return self.id_code
        finally:
            GPIO.cleanup()

def main():
    player = Player()
    player.read_rfid()
    while True: 
        id_code = player.read_rfid()
        #enter RFID number as an integer
        if id_code == :
            #enter URI associated with the album
            song = 'spotify:album:'
        #add songs
        elif id_code == :
            song = 'spotify:album:'
        elif id_code == :
            song = 'spotify:album:'
        else:
            print("error")
            exit(1)
        player.play_album(song)
        print(f"playing: {Player.play_album}")
        
if __name__ == "__main__":
    main()