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
        if times == '0':
            self.if_exit()
        self.check_times(times)
        record_to_insert = ""
        if opt == '1':
            for i in range(int(times)):
                self.view.print_text("Enter values following this sequence: Match_id, opp_score, own_score")
                m_id = self.view.display("Match_id: ")
                self.non_null_check(m_id, True)
                self.Repr_int(m_id)
                opp = self.view.display("opp_score: ")
                self.non_null_check(opp, True)
                self.Repr_int(opp)
                own = self.view.display("own_score: ")
                self.non_null_check(own, True)
                self.Repr_int(own)
                record_to_insert = (m_id, opp, own)
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
                record_to_insert = (s_id, n, c)
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
                record_to_insert = (t_id, m_id, s_date)
        elif opt == '4':
            for i in range(int(times)):
                self.view.print_text("Enter values following this sequence: Team_id, Name, Opponent, Coach, Stadium_id")
                team_id = self.view.display("Team_id: ")
                self.non_null_check(team_id, True)
                self.Repr_int(team_id)
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
                record_to_insert = (team_id, name, opon, coach, st_id)
        return record_to_insert

    # enter new data to update the specific table
    def update_query(self, opt):
        times = self.view.display("What number of rows do you want to update? - ")
        if times == '0':
            self.if_exit()
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
                record_to_update = (opp, own, m_id)
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
                record_to_update = (n, c, s_id)
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
                record_to_update = (s_date, t_id, m_id)
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
                record_to_update = (name, opon, coach, st_id, team_id)
        return record_to_update

    # enter data for deletion of specific table
    def delete_query(self, opt):
        times = self.view.display("What number of row do you want to delete? - ")
        if times == '0':
            self.if_exit()
        self.check_times(times)
        record_to_delete = ""
        if opt == '1':
            for i in range(int(times)):
                m_id = self.view.display("Enter value that marks Match_id:")
                self.non_null_check(m_id, True)
                self.Repr_int(m_id)
                self.model.only_possible(m_id, 3)
                record_to_delete = (m_id,)
        elif opt == '2':
            for i in range(int(times)):
                s_id = self.view.display("Enter value that marks Stadium_id:")
                self.non_null_check(s_id, True)
                self.Repr_int(s_id)
                self.model.only_possible(s_id, 1)
                record_to_delete = (s_id,)
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
                record_to_delete = (t_id, m_id)
        elif opt == '4':
            for i in range(int(times)):
                team_id = self.view.display("Enter value that mark Team_id:")
                self.non_null_check(team_id, True)
                self.Repr_int(team_id)
                self.model.only_possible(team_id, 2)
                record_to_delete = (team_id,)
        return record_to_delete

    # main menu function
    def input_get(self):
        opt = self.input_start()
        self.check_option(opt)
        if opt == "1":
            table = self.table_choose()
            while True:
                record = self.insert_query(table)
                sql_insert = self.model.insert_type(table, record)
                self.model.addTable(sql_insert)
                if self.to_continue() is False:
                    break
            self.if_exit()
        elif opt == "2":
            table = self.table_choose()
            while True:
                record = self.update_query(table)
                sql_update = self.model.update_type(table, record)
                self.model.updateTable()
                if self.to_continue() is False:
                    break
            self.if_exit()

        elif opt == "3":
            table = self.table_choose()
            while True:
                record = self.delete_query(table)
                sql_delete = self.model.delete_type(table, record)
                self.model.delTable(sql_delete)
                if self.to_continue() is False:
                    break
            self.if_exit()
        elif opt == "4":
            table = self.table_choose()
            sql_select = self.model.select_type(table)
            show = self.model.showTable(sql_select)
            self.view.print_table(show, table)
            self.if_exit()

    # input option
    def input_start(self):
        x = input("""Choose option: \nPRESS: 1 to add... 2 to update...  3 to delete... 4 to show_table...\n""")
        return x

    def quantity_put(self):
        return input("What number of row do you want to add? - ")

    # choose specific table
    def table_choose(self):
        table = input(
            "Choose table: \n press 1 - Match...   press 2 - Stadium...   press 3 - StartDate... press 4 - Team\n")
        self.check_table(table, True)
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
