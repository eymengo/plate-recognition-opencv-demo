

import sqlite3 as sql

def main():
    try:
       db = sql.connect('Database/PlateRecognition.db')
       print("Veri tabanı oluşturuldu.")
    except:
        print("Veri tabanı oluşturulamadı.")
    finally:
        db.close()

if __name__ == "__main__":
    main()