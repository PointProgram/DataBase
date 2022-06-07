from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
class Model:
    #connection to PostgreSQL server
    Base = declarative_base()
    def __init__(self):
        try:
            self.engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/Comand_Match')
            self.Session = sessionmaker(bind=self.engine)
            self.s = self.Session()
        except exc.SQLAlchemyError as e:
            print(type(e))

    #show data from tables
    def showTable(self, sql_select_query):
        try:
           records = sql_select_query.all()
        except exc.SQLAlchemyError as error:
            print("Error while fetching data from PostgreSQL", error)
            self.s.rollback()
        return records

    #update table row
    def updateTable(self):
        try:
            self.s.commit()
            print("Successfully updated")
        except exc.SQLAlchemyError as error :
            print("Failed updating record of the table {}", error)
            self.s.rollback()

    #add table row
    def addTable(self, sql_insert_query):
        try:
            self.s.add(sql_insert_query)
            self.s.commit()
            print("Successfully inserted")
        except exc.SQLAlchemyError as error :
            print("Failed inserting record into table {}".format(error))
            self.s.rollback()


    #delete table row
    def delTable(self, sql_delete_query):
        try:
            self.s.delete(sql_delete_query)
            self.s.commit()
            print("Successfully deleted")
        except exc.SQLAlchemyError as error:
            print("Failed deleting record into table {}".format(error))
            self.s.rollback()

    def only_possible(self, val, num):
        try:
            sql_origin = self.origin_type(num, val)
            if sql_origin is None:
                raise exc.SQLAlchemyError
                print("Failed, there are no records with such id")
        except exc.SQLAlchemyError as error:
            pass

    #close connection of Postgre table
    def close_connect(self):
        if self.s:
            self.s.close()
            print("PostgreSQL connection is closed")

    # choose command to insert data to specific table
    def insert_type(self, table_num, rec):
        if table_num == '1':
            sql_insert_query = Match(rec[0], rec[1], rec[2])
        elif table_num == '2':
            sql_insert_query = Stadium(rec[0], rec[1], rec[2])
        elif table_num == '3':
            sql_insert_query = Startdate(rec[1], rec[0], rec[2])
        elif table_num == '4':
            sql_insert_query = Team(rec[0], rec[1], rec[2], rec[3], rec[4])
        return sql_insert_query

    # choose command to update data of specific table
    def update_type(self, table_num, val):
        if table_num == '1':
            sql_update_query = self.s.query(Match).filter(Match.match_id == val[2]).\
                update({Match.opp_score: val[0], Match.own_score: val[1]})
        elif table_num == '2':
            sql_update_query = self.s.query(Stadium).filter(Stadium.stadium_id == val[2]). \
                update({Stadium.name: val[0], Stadium.city: val[1]})
        elif table_num == '3':
            sql_update_query = self.s.query(Startdate).filter(Startdate.team_id == val[1], \
                Startdate.match_id == val[2]).update({Startdate.start_date: val[0]})
        elif table_num == '4':
            sql_update_query = self.s.query(Team).filter(Team.team_id == val[4]). \
                update({Team.name: val[0], Team.opponent: val[1], Team.coach: val[2], Team.stadium_id: val[3]})
        return sql_update_query

    # choose command to delete data of specific table
    def delete_type(self, table_num, rec):
        sql_delete_query = ''
        try:
            if table_num == '1':
                sql_delete_query = self.s.query(Match).filter_by(match_id=rec[0]).one()
            elif table_num == '2':
                sql_delete_query = self.s.query(Stadium).filter_by(stadium_id=rec[0]).one()
            elif table_num == '3':
                sql_delete_query = self.s.query(Startdate).filter(Startdate.team_id == rec[0],\
                    Startdate.match_id == rec[1]).one()
            elif table_num == '4':
                sql_delete_query = self.s.query(Team).filter_by(team_id=rec[0]).one()
        except exc.SQLAlchemyError as error:
            print("Failed deleting record from table {}".format(error))
        finally:
            return sql_delete_query

    def select_type(self, table_num):
        if table_num == '1':
            sql_select_query = self.s.query(Match)
        elif table_num == '2':
            sql_select_query = self.s.query(Stadium)
        elif table_num == '3':
            sql_select_query = self.s.query(Startdate)
        elif table_num == '4':
            sql_select_query = self.s.query(Team)
        return sql_select_query

    def origin_type(self, table_num, val):
        if table_num == 1:
            sql_origin_val = self.s.query(Stadium).filter_by(stadium_id=val)
        elif table_num == 2:
            sql_origin_val = self.s.query(Team).filter_by(team_id=val)
        elif table_num == 3:
            sql_origin_val = self.s.query(Match).filter_by(match_id=val)
        return sql_origin_val
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


class Startdate(Model.Base):
    __tablename__ = 'startdate'
    match_id = Column(Integer, ForeignKey('match.match_id'), primary_key=True)
    team_id = Column(Integer, ForeignKey('team.team_id'), primary_key=True)
    start_date = Column(Date)
    match_r = relationship("Match", back_populates="team_s")
    team_r = relationship("Team", back_populates="match_s")

    def __init__(self, match_id, team_id, start_date):
        self.team_id = team_id
        self.match_id = match_id
        self.start_date = start_date

class Match(Model.Base):
    __tablename__ = 'match'
    match_id = Column(Integer, primary_key=True)
    opp_score = Column(Integer)
    own_score = Column(Integer)
    team_s = relationship("Startdate", back_populates="match_r")

    def __init__(self, match_id, opp_score, own_score):
        self.match_id = match_id
        self.opp_score = opp_score
        self.own_score = own_score

class Team(Model.Base):
    __tablename__ = 'team'
    team_id = Column(Integer, primary_key=True)
    name = Column(String(32))
    opponent = Column(String(32))
    coach = Column(String(32))
    stadium_id = Column(Integer, ForeignKey('stadium.stadium_id'))
    stadium = relationship("Stadium")
    match_s = relationship("Startdate", back_populates="team_r")

    def __init__(self, team_id, name, opponent, coach, stadium_id):
        self.team_id = team_id
        self.name = name
        self.opponent = opponent
        self.coach = coach
        self.stadium_id = stadium_id

class Stadium(Model.Base):
    __tablename__ = 'stadium'
    stadium_id = Column(Integer, primary_key=True)
    name = Column(String(32))
    city = Column(String(32))

    def __init__(self, stadium_id, name, city):
        self.stadium_id = stadium_id
        self.name = name
        self.city = city

