import sqlite3
import sys

import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.options.display.width = 0


def update_or_insert_entry(db_path, name, firstName, adhesion, entreprise):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Check if entry exists
    c.execute("SELECT * FROM gestion_adherent WHERE name=? AND firstName=?", (name, firstName))
    existing_entry = c.fetchone()

    if existing_entry:
        c.execute("UPDATE gestion_adherent SET adhesion=?, entreprise=? WHERE name=? AND firstName=?", 
                  (adhesion, entreprise, name, firstName))
        print(f"Updated adhesion for {name} {firstName}")
    else:
        c.execute("INSERT INTO gestion_adherent (name, firstName, adhesion, entreprise) VALUES (?, ?, ?, ?)", (name, firstName, adhesion, entreprise))
        print(f"Inserted new adhesion for {name} {firstName}")

    # Commit changes and close connection
    conn.commit()
    conn.close()


def main(file_path, db_path):

    df = pd.read_excel(file_path)
    df['Name'] = df['nomA'].str.upper()
    df['FirstName'] = df['prenomA'].str.title()

    df['Name'] = df['Name'].fillna( df['nomR'].str.upper() )
    df['FirstName'] = df['FirstName'].fillna(df['prenomR'].str.title())

    df['FullName'] = df['Name'] + " " + df['FirstName']
    df.drop_duplicates('FullName', inplace = True)

    for i in range(0, df.shape[0]):
        update_or_insert_entry(db_path, df['Name'].iloc[i], df['FirstName'].iloc[i], int(sys.argv[2]), df['entreprise'].iloc[i],)


if __name__ == '__main__':
    main(sys.argv[1], '../db.sqlite3')
