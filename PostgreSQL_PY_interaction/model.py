import psycopg2
import time

class Model:
    #connection to PostgreSQL server
    def __init__(self):
        try:
            self.connection = psycopg2.connect( user = "postgres",
                                          password = "postgres",
                                          host = "127.0.0.1",
                                          port = "5432",
                                          database = "Comand_Match" )
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    #show data from tables
    def showTable(self, sql_select_query, tab, record, bool):
        try:
            self.cursor = self.connection.cursor()
            if bool:
                beg = int(time.time() * 1000)
            self.cursor.execute(sql_select_query, record)
            if bool:
                end = int(time.time() * 1000) - beg
                print("Time of request", end, " ms")
            records = self.cursor.fetchall()
            #print_table(records, tab)
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
            self.connection.rollback()
        finally:
            if self.connection:
                self.cursor.close()
            return records

    #update table row
    def updateTable(self, records, sql_update_query):
        try:
            cursor = self.connection.cursor()
            cursor.executemany(sql_update_query, records)
            self.connection.commit()
            row_count = cursor.rowcount
            print(row_count, "Records Updated")
        except (Exception, psycopg2.Error) as error :
            print("Failed updating record of the table {}", error)
            self.connection.rollback()
        finally:
            if self.connection:
                cursor.close()

    #add table row
    def addTable(self, records, sql_insert_query):
        try:
            cursor = self.connection.cursor()
            cursor.executemany(sql_insert_query, records)
            self.connection.commit()
            print(cursor.rowcount, "Record successfully inserted")
        except (Exception, psycopg2.Error) as error :
            print("Failed inserting record into table {}".format(error))
            self.connection.rollback()
        finally:
            if self.connection:
                cursor.close()

    #delete table row
    def delTable(self, records, sql_delete_query):
        try:
            cursor = self.connection.cursor()
            cursor.executemany(sql_delete_query, records)
            self.connection.commit()
            print(cursor.rowcount, "Record deleted")
        except (Exception, psycopg2.Error) as error :
            print("Failed deleting record into table {}".format(error))
            self.connection.rollback()
        finally:
            if self.connection:
                cursor.close()

    def only_possible(self, val, num):
        try:
            rec = [(val, )]
            sql_origin = self.origin_type(num)
            curs = self.connection.cursor()
            curs.execute(sql_origin, rec)
            records = curs.fetchall()
            if records[0] == None:
                for row in records:
                    print("There is row with id: ", row[0])
        except (Exception, psycopg2.Error) as error:
            print("Failed, there are no records with such id: {}".format(error))
            self.if_exit()
        finally:
            if self.connection:
                curs.close()

    #close connection of Postgre table
    def close_connect(self):
        if self.connection:
            self.connection.close()
            print("PostgreSQL connection is closed")

    # choose command to insert data to specific table
    def insert_type(self, table_num):
        if table_num == '1':
            sql_insert_query = """ INSERT INTO match (match_id, opp_score, own_score)
            VALUES (%s, %s, %s)"""
        elif table_num == '2':
            sql_insert_query = """ INSERT INTO stadium (stadium_id, name, city)
            VALUES (%s, %s, %s)"""
        elif table_num == '3':
            sql_insert_query = """ INSERT INTO startdate (team_id, match_id, start_date)
            VALUES (%s, %s, %s)"""
        elif table_num == '4':
            sql_insert_query = """ INSERT INTO team (team_id, name, opponent, coach, stadium_id)
            VALUES (%s, %s, %s, %s, %s)"""
        return sql_insert_query

    # choose command to update data of specific table
    def update_type(self, table_num):
        if table_num == '1':
            sql_update_query = """UPDATE match set opp_score = %s, own_score = %s
            WHERE "match_id" = %s """
        elif table_num == '2':
            sql_update_query = """UPDATE stadium set name = %s, city = %s
            WHERE "stadium_id" = %s """
        elif table_num == '3':
            sql_update_query = """UPDATE startdate set start_date = %s
            WHERE team_id = %s AND match_id = %s"""
        elif table_num == '4':
            sql_update_query = """UPDATE team set name = %s, opponent = %s, coach = %s, stadium_id = %s
              WHERE team_id = %s """
        return sql_update_query

    # choose command to delete data of specific table
    def delete_type(self, table_num):
        if table_num == '1':
            sql_delete_query = """ DELETE FROM match WHERE match_id = %s"""
        elif table_num == '2':
            sql_delete_query = """ DELETE FROM stadium WHERE stadium_id = %s"""
        elif table_num == '3':
            sql_delete_query = """ DELETE FROM startdate WHERE team_id = %s AND match_id = %s"""
        elif table_num == '4':
            sql_delete_query = """ DELETE FROM team WHERE team_id = %s"""
        return sql_delete_query

    def select_type(self, table_num):
        if table_num == '1':
            sql_select_query = """ SELECT * FROM match ORDER BY match_id"""
        elif table_num == '2':
            sql_select_query = """ SELECT * FROM stadium ORDER BY stadium_id"""
        elif table_num == '3':
            sql_select_query = """ SELECT * FROM startdate ORDER BY team_id, match_id"""
        elif table_num == '4':
            sql_select_query = """ SELECT * FROM team ORDER BY team_id"""
        return sql_select_query

    def origin_type(self, table_num):
        if table_num == 1:
            sql_origin_val = """ SELECT stadium.stadium_id FROM stadium WHERE stadium_id = %s """
        elif table_num == 2:
            sql_origin_val = """ SELECT team.team_id FROM team WHERE team_id = %s """
        elif table_num == 3:
            sql_origin_val = """ SELECT match.match_id FROM match WHERE match_id = %s """
        elif table_num == 4:
            sql_origin_val = """ SELECT count(a) FROM (
                            SELECT team_id, match_id FROM startdate 
                            WHERE team_id = %s AND match_id = %s) as a """
        return sql_origin_val

    def random_type(self, table_num):
        if table_num == '1':
            sql_random_query = """ INSERT INTO match (opp_score, own_score)
            SELECT
                  trunc(random()*1000)::int,
                  trunc(random()*1000)::int
            FROM
                generate_series(1, %s)  
            """
        elif table_num == '2':
            sql_random_query = """ INSERT INTO stadium (name, city)
            SELECT
                    chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) ||
                    chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) ||
                    chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int),
                    chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) ||
                    chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) ||
                    chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int)
            FROM
                generate_series(1, %s)  
            """
        elif table_num == '3':
            sql_random_query = """ INSERT INTO startdate (team_id, match_id, start_date)
            SELECT team_id, match_id, dat FROM
            (SELECT 
            team_id, match_id,
            date '2000-01-10' + trunc(random()*10 * (date '2020-05-20' - date '2010-01-10'))::int as dat
            FROM team, match tablesample BERNOULLI(100)
            ORDER BY random()) k ,generate_series(1, 10000) LIMIT %s
            """
        elif table_num == '4':
            sql_random_query = """ INSERT INTO team (name, opponent, coach, stadium_id)
            SELECT nam, opp, coach, stadium_id FROM 
            (SELECT md5((random()*1)::text) as nam,
                md5((random()*2)::text) as opp,
                md5((random()*3)::text) as coach,
                stadium_id
            FROM stadium tablesample BERNOULLI(100)
            ORDER BY random()) k, generate_series(1, 10000) LIMIT %s
            """
        return sql_random_query

    # def random_generator():

    def specific_type(self, table_num):
        if table_num == '1':
            sql_specific_query = """ SELECT team_id, name as team_name, coach, opponent, stadium_name 
            FROM team  AS a INNER JOIN
            (SELECT name AS stadium_name, stadium_id FROM stadium WHERE name LIKE %s) AS aa
            ON a.stadium_id=aa.stadium_id
            WHERE opponent != %s AND team_id in (SELECT team_id FROM startdate WHERE start_date > %s) 
            """
        elif table_num == '2':
            sql_specific_query = """ WITH t_n AS (SELECT team_id FROM team WHERE length(name) < %s 
            AND name NOT SIMILAR TO %s)
            SELECT start_date, opp_score, own_score FROM startdate  AS a INNER JOIN
            (SELECT match_id, opp_score, own_score FROM 
            match WHERE opp_score = own_score OR opp_score - own_score = %s) as aa
            ON a.match_id=aa.match_id 
            WHERE team_id IN (SELECT team_id FROM t_n) 
            """
        elif table_num == '3':
            sql_specific_query = """ SELECT tid AS team_id,  sum(cnt) sum_team, cc.n AS team_name, 
            cc.o AS opponent_name FROM (
            SELECT team_id tid, count(team_id) cnt, n, o FROM startdate INNER JOIN 
            (SELECT team_id, name AS n, opponent AS o FROM team WHERE name LIKE %s) AS t USING (team_id) 
            WHERE start_date BETWEEN %s AND %s
            GROUP BY team_id, t.n, t.o) cc
            WHERE tid < %s
            GROUP BY tid, cc.n, cc.o
            ORDER BY tid
            """
        return sql_specific_query

    # check if int is valid
    def Repr_init(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    # check if void input
    def catch_void(self, inp):
        try:
            inp
            return "True"
        except SyntaxError:
            inp = None

    def check_default(self, times):
        if times == 'd':
            times = 100000
            return times
        else:
            return times



