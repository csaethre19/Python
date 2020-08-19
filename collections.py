favMusicians = ["BANKS", "Alt-J", "RadioHead", "Doja Cat", "Sol Rising"]

songs = ['underdog', 'matilda', 'idioteque', 'Rules', 'Misty Morning']


def mapSongToArtist(favMusicians, songs):
    songMap = {}
    i = 0
    for artist in favMusicians:
        songMap[artist] = songs[i]
        i += 1
    return songMap

cacheValley = (38.7250, 109.5212)
places = [cacheValley, (47.7504, 90.3343), (40.7648, 111.8910)]

myAttributes = {
    "height": 62,
    "hairColor": "Blonde",
    "eyeColor": "Blue",
    "favAuthor": "Megan Miranda",
    "favColor": "Lavender"
}

def getUserQuestion():
    question = ""
    while (question != "q"):
        question = input("Type height, color, or author to find out more about me. Type q to quit")
        if (question == 'height'):
            print(myAttributes['height'])
        elif (question == 'color'):
            print(myAttributes['favColor'])
        elif (question == 'author'):
            print(myAttributes['favAuthor'])
        elif (question == 'q'):
            print("goodbye")
        else:
            print("not an option!")

#getUserQuestion()
songMap = mapSongToArtist(favMusicians, songs)
print(songMap)