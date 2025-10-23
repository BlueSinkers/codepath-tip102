class SongNode:
    def __init__(self, song, artist=None, next=None):
        self.song = song
        self.artist = artist
        self.next = next


def print_linked_list(node):
    current = node
    while current:
        if current.artist:
            print((current.song, current.artist), end=" -> " if current.next else "")
        else:
            print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()


# Problem 1
node3 = SongNode("Bad Romance")
node2 = SongNode("Party Rock Anthem", next=node3)
top_hits_2010s = SongNode("Uptown Funk", next=node2)


"""
Problem 1: Building a Playlist

Pseudocode:
Make the last song first, then connect each new song to the one after it until the playlist forms.  

Two Questions:
Should we build it from a list or just hardcode it?  
Does the order always go from start to finish like normal?
"""


# Problem 2
def get_artist_frequency(playlist):
    artist_count = {}
    current = playlist
    while current:
        artist = current.artist
        artist_count[artist] = artist_count.get(artist, 0) + 1
        current = current.next
    return artist_count


"""
Problem 2: Top Artists

Pseudocode:
Go through each song, count how often each artist shows up, and store it all in a dictionary.  

Two Questions:
Do we treat names with different cases as the same artist?  
What if the playlist’s empty?
"""


# Problem 3
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next
    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next
            return playlist_head
        current = current.next
    return playlist_head

"""
Problem 3: Glitching Out

Pseudocode:
If the song’s at the start, skip it; otherwise, find it and link around it so it’s gone.  

Two Questions:
Do we delete only the first match or every copy?  
If the song isn’t found, do we just leave it alone?
"""


# Problem 4
def on_repeat(playlist_head):
    slow = playlist_head
    fast = playlist_head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


"""
Problem 4: On Repeat

Pseudocode:
Move one pointer slow and one fast — if they ever meet, the playlist loops.  

Two Questions:
Does one song looping on itself count?  
We’re not changing the links, right?
"""

# Problem 5
def loop_length(playlist_head):
    slow = playlist_head
    fast = playlist_head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 1
            fast = fast.next
            while slow != fast:
                count += 1
                fast = fast.next
            return count
    return 0



"""
Problem 5: Looped

Pseudocode:
Use two pointers to find the loop, then count how many steps it takes to circle back.  

Two Questions:
If there’s no loop, just return zero?  
Do we need to worry about performance on really long playlists?
"""

# Test Cases

print("Problem 1:")
print_linked_list(top_hits_2010s)

print("\nProblem 2:")
playlist = SongNode("Saturn", "SZA",
            SongNode("Who", "Jimin",
                SongNode("Espresso", "Sabrina Carpenter",
                    SongNode("Snooze", "SZA"))))
print(get_artist_frequency(playlist))

print("\nProblem 3:")
playlist = SongNode("SOS", "ABBA",
            SongNode("Simple Twist of Fate", "Bob Dylan",
                SongNode("Dreams", "Fleetwood Mac",
                    SongNode("Lovely Day", "Bill Withers"))))
print_linked_list(remove_song(playlist, "Dreams"))

print("\nProblem 4:")
song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2
print(on_repeat(song1))

print("\nProblem 5:")
song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2
print(loop_length(song1))














