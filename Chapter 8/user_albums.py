#   8-8. User Albums: Start with your program from Exercise 8-7. Write a while
#   loop that allows users to enter an album’s artist and title. Once you have
#   that information, call make_album() with the user’s input and print the
#   dictionary that’s created. Be sure to include a quit value in the while
#   loop.

def make_album(artist_name, album_title): 
    """Build a dictionary describing a music album""" 
    music_album = {
        'Artist': artist_name.title(),
        'Album': album_title.title()
        }
    return music_album

album_prompt = "Please enter an album title. Enter 'q' at any time to exit. "
artist_prompt = "Please enter an artist name. Enter 'q' at any time to exit. "


while True: 
    album = input(album_prompt)
    if album == 'q':
        break
    artist = input(artist_prompt)
    if artist == 'q': 
        break 
    new_album = make_album(artist_name = artist, album_title = album)
    print(new_album)
