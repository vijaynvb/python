# Node Class
class Node:
    def __init__(self, song):
        self.song = song
        self.next = None


 
song1 = Node("Song A")
song2 = Node("Song B")
song3 = Node("Song C")

 
song1.next = song2
song2.next = song3

 
current = song1

print("Music Playlist:")

while current:
    print(current.song)
    current = current.next