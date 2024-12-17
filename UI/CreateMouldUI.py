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

            # 创建一个水平布局管理器
            row1_frame = tk.Frame(second_frame)
            row1_frame.pack(side=tk.TOP, pady=10)
            tk.Label(row1_frame, text="模具编号:").pack(side=tk.LEFT, padx=(10, 5))
            self.mould_serial = tk.Entry(row1_frame, width=20)
            self.mould_serial.pack(side=tk.LEFT, padx=(0, 10), expand=True)

            row2_frame = tk.Frame(second_frame)
            row2_frame.pack(side=tk.TOP, pady=10)
            tk.Label(row2_frame, text="班组长:").pack(side=tk.LEFT, padx=(10, 5))
            self.leader = tk.Entry(row2_frame, width=20)
            self.leader.pack(side=tk.LEFT, padx=(0, 10), expand=True)

            row3_frame = tk.Frame(second_frame)
            row3_frame.pack(side=tk.TOP, pady=10)
            tk.Label(row3_frame, text="造型:").pack(side=tk.LEFT, padx=(10, 5))
            self.stylist = tk.Entry(row3_frame, width=20)
            self.stylist.pack(side=tk.LEFT, padx=(0, 10), expand=True)

            open_button = tk.Button(second_frame, text="创建", command=self.create_mould)
            open_button.pack(pady=10)
            cancel_button = tk.Button(second_frame, text="取消", command=self.go_back)
            cancel_button.pack(pady=10)

    def create_mould(self):
        (id, year) = MouldSerialParseUtil.parse(self.mould_serial.get())
        MysqlConnectUtil.insert_data(
            f"insert into mould (id,year,mould_serial, leader, stylist,create_date,finish_date) values ({id}, {year}, '{self.mould_serial.get()}', '{self.leader.get()}', '{self.stylist.get()}','{TimeUtil.get_today()}',null)")
        self.go_back()
