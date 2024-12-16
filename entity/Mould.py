class mould:
    def __init__(self, id, year, mould_serial, leader, stylist, create_date, finish_date):
        # 成员变量 id
        self.id = id
        # 成员变量 year
        self.year = year
        # 成员变量 mould_serial
        self.mould_serial = mould_serial
        # 成员变量 leader
        self.leader = leader
        self.stylist = stylist
        self.create_date = create_date
        self.finish_date = finish_date

    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Year: {self.year}")
        print(f"Mould Serial: {self.mould_serial}")
        print(f"Leader: {self.leader}")
