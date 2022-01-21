import genanki
import pandas as pd
import sql_util as sql


def create():
    df = sql.read_db()

    my_deck = genanki.Deck(
        1543353429,
        'KorEng Words'
    )

    for i in range(len(df)):
        entry = df.iloc[i]

        my_deck.add_note(genanki.Note(
            model=genanki.BASIC_AND_REVERSED_CARD_MODEL,
            fields=[str(entry.kor), str(entry.eng)]
        ))

    genanki.Package(my_deck).write_to_file('./anki/KorEng-Words.apkg')


if __name__ == "__main__":
    create()
