class View:
    def print_table(self, records, tab):
        if tab == '1':
            self.print_text("Match_id   opp_score   own_score ")
            for sql_row in records:
                print("{:<10}".format(sql_row.match_id), "{:<10}".format(sql_row.opp_score), "{:<10}".format(sql_row.own_score))
        elif tab == '2':
            self.print_text("Stadium_id    Name    City ")
            for sql_row in records:
                print("{:<10}".format(sql_row.stadium_id), "{:<10}".format(sql_row.name), "{:<10}".format(sql_row.city))
        elif tab == '3':
            self.print_text("Team_id    Match_id       Start_date")
            for sql_row in records:
                print("{:<10}".format(sql_row.team_id), "{:<10}".format(sql_row.match_id), "   ", sql_row.start_date)
        elif tab == '4':
            self.print_text("Team_id    Name     Opponent      Coach      Stadium_id")
            for sql_row in records:
                print("{:<10}".format(sql_row.team_id), "{:<10}".format(sql_row.name), "{:<10}".format(sql_row.opponent), "{:<15}".format(sql_row.coach), "{:<15}".format(sql_row.stadium_id))
        elif tab == '5':
            self.print_text("team_id   team_name   coach   opponent   stadium_name ")
            for sql_row in records:
                print("{:<10}".format(sql_row[0]), "{:<10}".format(sql_row[1]), "{:<10}".format(sql_row[2]), "{:<10}".format(sql_row[3]), "{:<10}".format(sql_row[4]))
        elif tab == '6':
            self.print_text("start_date    own_score     opp_score ")
            for sql_row in records:
                print(sql_row[0], "       {:<10}".format(sql_row[1]), "{:<10}".format(sql_row[2]))
        elif tab == '7':
            self.print_text("team_id    sum_team     team_name     opponent_name")
            for sql_row in records:
                print("{:<10}".format(sql_row[0]), "{:<10}".format(sql_row[1]), "{:<10}".format(sql_row[2]), "{:<10}".format(sql_row[3]))

    def display(self, txt):
        return input(txt)

    def print_text(self, txt):
        print(str(txt))