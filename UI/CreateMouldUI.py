import tkinter as tk

from util import MysqlConnectUtil, MouldSerialParseUtil, TimeUtil


class CreateMouldUI:
    def __init__(self, root, go_back):
        self.root = root
        self.go_back = go_back
        self.create_frame()

    def create_frame(self):
        # 清除之前的界面
        for widget in self.root.winfo_children():
            widget.destroy()
            # 创建第二个界面
            second_frame = tk.Frame(self.root)
            second_frame.pack(fill=tk.BOTH, expand=True)
            tk.Label(second_frame, text="模具编号:").pack(pady=10)
            self.mould_serial = tk.Entry(second_frame)
            self.mould_serial.pack(pady=10)
            tk.Label(second_frame, text="班组长:").pack(pady=10)
            self.leader = tk.Entry(second_frame)
            self.leader.pack(pady=10)
            tk.Label(second_frame, text="造型:").pack(pady=10)
            self.stylist = tk.Entry(second_frame)
            self.stylist.pack(pady=10)
            open_button = tk.Button(second_frame, text="Open Mold", command=self.create_mould)
            open_button.pack(pady=10)
            cancel_button = tk.Button(second_frame, text="Cancel", command=self.go_back)
            cancel_button.pack(pady=10)

    def create_mould(self):
        (id, year) = MouldSerialParseUtil.parse(self.mould_serial.get())
        MysqlConnectUtil.insert_data(
            f"insert into mould (id,year,mould_serial, leader, stylist,create_date,finish_date) values ({id}, {year}, '{self.mould_serial.get()}', '{self.leader.get()}', '{self.stylist.get()}','{TimeUtil.get_today()}',null)")
        self.go_back()
