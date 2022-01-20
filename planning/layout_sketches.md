# Planning for the app I want to make.

This will have the color scheme I want to use, mock ups of the frames, todo lists, etc.

# Data storage paradigm

The app will store the meta-data for the cards (Korean word, english word, korean example sentence, english example sentence, picture filenames, audio clip filenames) in the databases in `dbs` folder. The data itself will be stored in the `images` and `audio-clips` folders.

# App appearance

The app GUI will be a simple window with input boxes to type the english and korean phrases, enter and exit buttons, and buttons to add an image or audio clip.

# Creating anki decks from database

The app will have a module which creates an anki deck from the database. It will also add new cards to the existing deck as cards are added.

# Backups

All the non data parts of the app (that is, not the images, audio-clips and the decks themselves) will be backed up on github. The data itself will be backed up periodically with some kind of backup job. The decks will be backed up in the same way, as well as being backed up on anki web.
