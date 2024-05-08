import sqlite3

import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.options.display.width = 0


def update_or_insert_entry(db_path, categorie, name, refImmo, photo):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Check if category exists
    c.execute("SELECT * FROM gestion_gearcat WHERE name=?", (categorie,))
    existing_categorie = c.fetchone()
    if existing_categorie:
        print(f"Existing categorie {categorie} with id {existing_categorie[0]}")
    else:
        # todo, code the levels, this is probably hardcoded based on the category names
        categories: dict = {
            "Bateau": 1,
            "Kayak": 1,
            "Planche": 1,
            "Voile": 2,
            "Kite": 1
        }
        c.execute("INSERT INTO gestion_gearcat (name, level) VALUES (?, ?)", (categorie, categories.get(categorie, 0), ))
        c.execute("SELECT * FROM gestion_gearcat WHERE name=?", (categorie,))
        existing_categorie = c.fetchone()
        print(f"Inserted new categorie for {categorie} with id {existing_categorie[0]}")

    # Check if entry exists
    c.execute("SELECT * FROM gestion_gear WHERE name=? AND category_id=?", (name, existing_categorie[0],))
    existing_entry = c.fetchone()

    if existing_entry:
        # c.execute("UPDATE gestion_adherent SET adhesion=? WHERE name=?", (adhesion, name))
        print(f"TODO Update materiel {name}")
    else:
        if photo == "":
            photo = ""
        else:
            photo = "photos/" + str(photo)
        c.execute("INSERT INTO gestion_gear (name, isInService, photo, codeImo, category_id) VALUES (?, ?, ?, ?, ?)", 
                  (name, True, photo, refImmo, existing_categorie[0]))
        print(f"Inserted new material {name}")

    # Commit changes and close connection
    conn.commit()
    conn.close()

def materiel(file_path, db_path):
    df = pd.read_excel(file_path)
    df = df.fillna("") 
    for i in range(0, df.shape[0]):
        update_or_insert_entry(db_path, df['Categorie'].iloc[i], df['Nom'].iloc[i], df['RefImmo'].iloc[i], df['Photo'].iloc[i])


if __name__ == '__main__':
    materiel('materiel.xlsx', '../db.sqlite3')
