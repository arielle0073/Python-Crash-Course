#   8-7. Album: Write a function called make_album() that builds a dictionary
#   describing a music album. The function should take in an artist name and an
#   album title, and it should return a dictionary containing these two pieces
#   of information. Use the function to make three dictionaries representing
#   different albums. Print each return value to show that the dictionaries are
#   storing the album information correctly. Use None to add an optional
#   parameter to make_album() that allows you to store the number of songs on an
#   album. If the calling line includes a value for the number of songs, add
#   that value to the album’s dictionary. Make at least one new function call
#   that includes the number of songs on an album.

#   PART ONE

def make_album(artist_name, album_title): 
    """Build a dictionary describing a music album""" 
    music_album = {
        'Artist': artist_name.title(),
        'Album': album_title.title()
        }
    return music_album

print("Here's Part One:")
cardi = make_album('cardi b', 'invasion of privacy')
print(cardi)

jhene = make_album('jhene aiko', 'souled out')
print(jhene)

lennon = make_album('lennon stella', 'three. two. one.')
print(lennon)

#   PART TWO
def make_album_two(artist_name, album_title, number_of_songs= None): 
    """Build a dictionary describing a music album""" 
    music_album = {'Artist': artist_name.title(),
        'Album': album_title.title()}
    if number_of_songs:
        music_album['Number of Songs'] = number_of_songs
    return music_album

print("\nHere's Part Two:")
cardi = make_album_two('cardi b', 'invasion of privacy')
print(cardi)

jhene = make_album_two('jhene aiko', 'souled out')
print(jhene)

lennon = make_album_two('lennon stella', 'three. two. one.', 13)
print(lennon)


