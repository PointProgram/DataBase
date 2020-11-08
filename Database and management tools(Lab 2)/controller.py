from model import Model
from view import View
import datetime
class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
    # enter new data for insertion for specific table
    def insert_query(self, opt):
        times = self.quantity_put()
        self.check_times(times)
        record_to_insert = ""
        if opt == '1':
            for i in range(int(times)):
                self.print_text("Enter values following this sequence: Match_id, opp_score, own_score")
                m_id = self.view.display("Match_id: ")
                self.non_null_check(m_id, True)
                self.Repr_int(m_id)
                opp = self.view.display("opp_score: ")
                self.non_null_check(opp, True)
                self.Repr_int(opp)
                own = self.view.display("own_score: ")
                self.non_null_check(own, True)
                self.Repr_int(own)
                record_to_insert = [(m_id, opp, own)]
        elif opt == '2':
            for i in range(int(times)):
                self.view.print_text("Enter values following this sequence: Stadium_id, Name, City")
                s_id = self.view.display("Stadium_id: ")
                self.non_null_check(s_id, True)
                self.Repr_int(s_id)
                n = self.view.display("Name: ")
                self.non_null_check(n, True)
                self.Repr_char(n)
                c = self.view.display("City: ")
                self.non_null_check(n, True)
                self.Repr_char(n)
                record_to_insert = [(s_id, n, c)]
        elif opt == '3':
            for i in range(int(times)):
                self.view.print_text("Enter values following this sequence: Team_id, Match_id, Start_date(yyyy-mm-dd)")
                t_id = self.view.display("Team_id: ")
                self.non_null_check(t_id, True)
                self.Repr_int(t_id)
                self.model.only_possible(t_id, 2)
                m_id = self.view.display("Match_id: ")
                self.non_null_check(m_id, True)
                self.Repr_int(m_id)
                self.model.only_possible(m_id, 3)
                s_date = self.view.display("Start_date: ")
                self.non_null_check(s_date, True)
                self.Repr_date(s_date)
                record_to_insert = [(t_id, m_id, s_date)]
        elif opt == '4':
            for i in range(int(times)):
                self.view.print_text("Enter values following this sequence: Team_id, Name, Opponent, Coach, Stadium_id")
                team_id = self.display("Team_id: ")
                self.non_null_check(team_id, True)
                self.Repr_int(team_id)
                name = self.view.display("Name: ")
                self.non_null_check(name, True)
                self.Repr_char(name)
                opon = self.display("Opponent: ")
                self.non_null_check(opon, True)
                self.Repr_char(opon)
                coach = self.view.display("Coach: ")
                if self.non_null_check(coach, False):
                    self.Repr_char(coach)
                st_id = self.view.display("Stadium_id: ")
                self.non_null_check(st_id, True)
                self.Repr_int(st_id)
                self.model.only_possible(st_id, 1)
                record_to_insert = [(team_id, name, opon, coach, st_id)]
        return record_to_insert

    # enter new data to update the specific table
    def update_query(self, opt):
        times = self.view.display("What number of rows do you want to update? - ")
        self.check_times(times)
        record_to_update = ""
        if opt == '1':
            for i in range(int(times)):
                self.view.print_text("Enter values following this sequence opp_score, own_score, Match_id:")
                opp = self.view.display("opp_score: ")
                self.non_null_check(opp, True)
                self.Repr_int(opp)
                own = self.view.display("own_score: ")
                self.non_null_check(own, True)
                self.Repr_int(own)
                m_id = self.view.display("Match_id: ")
                self.non_null_check(m_id, True)
                self.Repr_int(m_id)
                self.model.only_possible(m_id, 3)
                record_to_update = [(opp, own, m_id)]
        elif opt == '2':
            for i in range(int(times)):
                self.view.print_text("Enter values following this sequence Name, City, Stadium_id:")
                n = self.view.display("Name: ")
                self.non_null_check(n, True)
                self.Repr_char(n)
                c = self.view.display("City: ")
                self.non_null_check(c, True)
                self.Repr_char(c)
                s_id = self.view.display("Stadium_id: ")
                self.non_null_check(s_id, True)
                self.Repr_int(s_id)
                self.model.only_possible(s_id, 1)
                record_to_update = [(n, c, s_id)]
        elif opt == '3':
            for i in range(int(times)):
                self.view.print_text("Enter values following this sequence Start_date(yyyy-mm-dd), Team_id, Match_id:")
                s_date = self.view.display("Start_date: ")
                self.Repr_date(s_date)
                t_id = self.view.display("Team_id: ")
                self.non_null_check(t_id, True)
                self.Repr_int(t_id)
                self.model.only_possible(t_id, 2)
                m_id = self.view.display("Match_id: ")
                self.non_null_check(m_id, True)
                self.Repr_int(m_id)
                self.model.only_possible(m_id, 3)
                record_to_update = [(s_date, t_id, m_id)]
        elif opt == '4':
            for i in range(int(times)):
                self.view.print_text("Enter values following this sequence Name, Opponent, Coach, Stadium_id, Team_id:")
                name = self.view.display("Name: ")
                self.non_null_check(name, True)
                self.Repr_char(name)
                opon = self.view.display("Opponent: ")
                self.non_null_check(opon, True)
                self.Repr_char(opon)
                coach = self.view.display("Coach: ")
                if self.non_null_check(coach, False):
                    self.Repr_char(coach)
                st_id = self.view.display("Stadium_id: ")
                self.non_null_check(st_id, True)
                self.Repr_int(st_id)
                self.model.only_possible(st_id, 1)
                team_id = self.view.display("Team_id: ")
                self.non_null_check(team_id, True)
                self.Repr_int(team_id)
                self.model.only_possible(team_id, 2)
                record_to_update = [(name, opon, coach, st_id, team_id)]
        return record_to_update

    def specific_query(self, opt):
        if opt == '1':
            self.view.print_text("Enter values following this sequence stadium_name, opponent, start_date:")
            sn = self.view.display("stadium_name: ")
            if self.non_null_check(sn, False):
                self.Repr_char(sn)
            op = self.view.display("opponent: ")
            if self.non_null_check(op, False):
                self.Repr_char(op)
            sd = self.view.display("start_date: ")
            self.Repr_date(sd)
            record_to_specific = (sn, op, sd)
        elif opt == '2':
            self.view.print_text("Enter values following this sequence len_name, team_name, diff_score:")
            ng = self.view.display("len_name: ")
            self.non_null_check(ng, True)
            self.Repr_int(ng)
            lt = self.view.display("team_name: ")
            if self.non_null_check(lt, False):
                self.Repr_char(lt)
            tn = self.view.display("diff_score: ")
            self.non_null_check(tn, True)
            self.Repr_int(tn)
            record_to_specific = (ng, lt, tn)
        elif opt == '3':
            self.view.print_text("Enter values following this sequence team_name, date_start, date_finish, team_id:")
            tn = self.view.display("team_name: ")
            if self.non_null_check(tn, False):
                self.Repr_char(tn)
            ds = self.view.display("date_start: ")
            self.Repr_date(ds)
            df = self.view.display("date_finish: ")
            self.Repr_date(df)
            ti = self.view.display("team_id: ")
            self.non_null_check(ti, True)
            self.Repr_int(ti)
            record_to_specific = (tn, ds, df, ti)
        return record_to_specific

    # enter data for deletion of specific table
    def delete_query(self, opt):
        times = self.view.display("What number of row do you want to delete? - ")
        self.check_times(times)
        record_to_delete = ""
        if opt == '1':
            for i in range(int(times)):
                m_id = self.view.display("Enter value that marks Match_id:")
                self.non_null_check(m_id, True)
                self.Repr_int(m_id)
                self.model.only_possible(m_id, 3)
                record_to_delete = [(m_id,)]
        elif opt == '2':
            for i in range(int(times)):
                s_id = self.view.display("Enter value that marks Stadium_id:")
                self.non_null_check(s_id, True)
                self.Repr_int(s_id)
                self.model.only_possible(s_id, 1)
                record_to_delete = [(s_id,)]
        elif opt == '3':
            for i in range(int(times)):
                self.view.print_text("Enter values following this sequence team_id, match_id:")
                t_id = self.view.display("team_id: ")
                self.non_null_check(t_id, True)
                self.Repr_int(t_id)
                self.model.only_possible(t_id, 2)
                m_id = self.view.display("match_id: ")
                self.non_null_check(m_id, True)
                self.Repr_int(m_id)
                self.model.only_possible(m_id, 3)
                record_to_delete = [(t_id, m_id)]
        elif opt == '4':
            for i in range(int(times)):
                team_id = self.view.display("Enter value that mark Team_id:")
                self.non_null_check(team_id, True)
                self.Repr_int(team_id)
                self.model.only_possible(team_id, 2)
                record_to_delete = [(team_id,)]
        return record_to_delete

    # main menu function
    def input_get(self):
        opt = self.input_start()
        self.check_option(opt)
        if opt == "1":
            table = self.table_choose()
            if_rand = self.view.display("Do you want to insert rows manually or randomly? \nPress M if manually, R if randomly: ")
            self.to_random(if_rand)
            if if_rand == 'M':
                while True:
                    sql_insert = self.model.insert_type(table)
                    record = self.insert_query(table)
                    self.model.addTable(record, sql_insert)
                    if self.to_continue() is False:
                        break
            elif if_rand == 'R':
                times = self.view.display("What number of row do you want to add(type 'd' to set default)? - ")
                times = self.model.check_default(times)
                self.check_times(times)
                sql_random = self.model.random_type(table)
                self.model.addTable([(times,)], sql_random)
            self.if_exit()
        elif opt == "2":
            table = self.table_choose()
            while True:
                sql_update = self.model.update_type(table)
                record = self.update_query(table)
                self.model.updateTable(record, sql_update)
                if self.to_continue() is False:
                    break
            self.if_exit()

        elif opt == "3":
            table = self.table_choose()
            while True:
                sql_delete = self.model.delete_type(table)
                record = self.delete_query(table)
                self.model.delTable(record, sql_delete)
                if self.to_continue() is False:
                    break
            self.if_exit()
        elif opt == "4":
            table = self.spec_choose()
            tab = str(int(table) + 4)
            record = self.specific_query(table)
            sql_spec = self.model.specific_type(table)
            show = self.model.showTable(sql_spec, tab, record, True)
            self.view.print_table(show, tab)
            self.if_exit()
        elif opt == "5":
            table = self.table_choose()
            sql_select = self.model.select_type(table)
            show = self.model.showTable(sql_select, table, None, False)
            self.view.print_table(show, table)
            self.if_exit()

    # input option
    def input_start(self):
        x = input("""Choose option: \nPRESS: 1 to add... 2 to update...  3 to delete...  4 to specific_select... 5 to show_table...\n""")
        return x

    def quantity_put(self):
        return input("What number of row do you want to add? - ")

    # choose specific table
    def table_choose(self):
        table = input(
            "Choose table: \n press 1 - Match...   press 2 - Stadium...   press 3 - StartDate... press 4 - Team\n")
        self.check_table(table, True)
        return table

    def spec_choose(self):
        print("""1) Show all info about team(name, coach, opponent), which played game on specific 'stadium', but 
                      not with that 'opponent', when matches took place later than that 'date'.
                      """)

        print("""2) Show date, opp_score, own_score from those teams that have a draw or the difference between  
                      home and away teams in 'number of goal' and the length of home team is less then 'that number', 
                      except of 'such team'.
                      """)

        print("""3) Show team_id, sum_team, team_name, opponent_name from those teams that have 'specific name', 
                      where match took place between 'date_1' and 'date_2' and team_id is less than 'that number'
                      """)
        table = input(
            "Choose table: \nPress: 1 or 2 or 3\n")
        self.check_table(table, False)
        return table

    def to_random(self, opt):
        if opt != 'M' and opt != 'R':
            print("You entered wrong value")
            self.if_exit()

    def non_null_check(self, var_t, boool):
        if var_t is None or var_t == '' and boool:
            print("Error that column cannot contain NULL values!")
            self.if_exit()
        elif var_t is None or var_t == '' and boool is False:
            return False
        return True

    # check option validation
    def check_option(self, opti):
        if opti != '1' and opti != '2' and opti != '3' and opti != '4' and opti != '5' or self.model.catch_void(opti) != "True":
            print("You entered wrong character!")
            self.if_exit()

    # check table validation
    def check_table(self, tab, bl):
        if bl:
            if tab != '1' and tab != '2' and tab != '3' and tab != '4' or self.model.catch_void(tab) != "True":
                print("You entered wrong character!")
                self.if_exit()
        if bl is False:
            if tab != '1' and tab != '2' and tab != '3' or self.model.catch_void(tab) != "True":
                print("You entered wrong character!")
                self.if_exit()

    # ask if exit
    def if_exit(self):
        ext = input("Do you want to exit? Press M to go to the main menu, or E to exit: ")
        if ext == 'M':
            self.input_get()
        elif ext == 'E':
            self.model.close_connect()
            exit()
        else:
            print("You entered wrong character...")
            self.if_exit()

    def Repr_date(self, date):
        year = ""
        month = ""
        day = ""
        if len(date) != 10 or date[4] != '-' and date[7] != '-':
            print("You entered wrong date value, please try again!")
            self.if_exit()
        for i in (0, 1, 2, 3):
            year += date[i]
        for i in (5, 6):
            month += date[i]
        for i in (8, 9):
            day += date[i]
        try:
            d = datetime.date(int(year), int(month), int(day))
        except ValueError:
            print("You entered wrong date value, please try again!")
            self.if_exit()

    def Repr_int(self, n):
        try:
            int(n)
        except ValueError:
            print("You entered wrong instance, please try again!")
            self.if_exit()

    def Repr_char(self, ch):
        if len(ch) > 50:
            print("You entered wrong value only 50 symbols allowed, please try again!")
            self.if_exit()
        try:
            str(ch)
        except ValueError:
            print("You entered wrong value, please try again!")
            self.if_exit()

    # check if number for loop is valid
    def check_times(self, times):
        if self.model.Repr_init(times):
            return True
        else:
            print("You entered wrong instance, please try again!")
            self.if_exit()
            return False

    # ask if continue
    def to_continue(self):
        cont = input("Do you want to continue? Press Y if yes, N if no: ")
        if cont == 'Y':
            return True
        elif cont == 'N':
            return False
        else:
            print("You entered wrong value, please try again")
            self.to_continue()
