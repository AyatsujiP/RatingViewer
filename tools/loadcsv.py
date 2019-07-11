import os
import csv
import sqlite3
import contextlib


def main():
    filenames = ['excel\\NCS201905.csv','excel\\NCS201906.csv','excel\\NCS201907.csv']
    dates = ['2019-05-01','2019-06-01','2019-07-01']
    ratings = []
    dbname = 'ratingviewer\\db.sqlite3'

    with contextlib.closing(sqlite3.connect(dbname)) as conn:

        for f in filenames:
            ratings.append(read_csv(f))
        
        for r,d in zip(ratings, dates):
            insert_data_into_rating_table(conn,r,d)
        
        #insert_data_into_members(conn,ratings)



def create_member_table(conn):
    cur = conn.cursor()
    cur.execute('CREATE TABLE members' + 
                '(id INTEGER PRIMARY KEY AUTOINCREMENT,' +
                'name_alphabet STRING,' +
                'name_kanji STRING,' +
                'ncs_id STRING)')
                
    conn.commit()


def create_rating_table(conn):
    cur = conn.cursor()
    cur.execute('CREATE TABLE ratings' + 
                '(id INTEGER PRIMARY KEY AUTOINCREMENT,' + 
                'ncs_id STRING,' + 
                'rating INTEGER,' + 
                'update_month STRING)')
    
    conn.commit()


def insert_data_into_rating_table(conn,ratings,date):
    cur = conn.cursor()
    cur.executemany('INSERT INTO visualizer_ratings(ncs_id, rating, update_month) VALUES (?,?,?)',
                [(r[0],r[3],date) for r in ratings])
    
    conn.commit()
    
    
def insert_data_into_members(conn,ratings):
    cur = conn.cursor()
    unique_member_ids = []
    unique_members = []
    
    for each_rating in ratings:
        for e in each_rating:
            if not e[0] in unique_member_ids:
                unique_member_ids.append(e[0])
                unique_members.append((e[0],e[1],e[2]))
    
    cur.executemany('INSERT INTO visualizer_members(ncs_id,name_alphabet,name_kanji) VALUES (?,?,?)',
                    unique_members)
    
    conn.commit()


def read_csv(filename):
    ret = []
    with open(filename,'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for r in reader:
            ret.append(r[0:4])
    
    return ret


if __name__ == "__main__":
    main()
    
