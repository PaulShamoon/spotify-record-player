# spotify-record-player
This RFID record player lets you tap your album cover over the box, and automatically begins playing an album on Spotify using the Spotify API. Inside the box is a Raspberry Pi and an MFRC522 RFID scanner, and inside the albums are RFID stickers. The RFID scanner is connected to a Raspberry Pi that is running a Python script. The script plays an album when the RFID number associated with the album is scanned onto the RFID scanner. This script constantly refreshes your access token, so you never have to worry about requestion a new one. 

https://user-images.githubusercontent.com/80371052/160514056-48ce6b12-1848-49d5-abe7-5c1f46e8aa87.mov

