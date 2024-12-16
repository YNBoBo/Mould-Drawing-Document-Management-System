import tkinter as tk
from tkinter.font import Font

from mysql.connector.aio import MySQLConnection

from UI.CreateMouldUI import CreateMouldUI
from util import MysqlConnectUtil


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("模具图档管理系统")
        self.root.geometry("800x600")  # 设置窗口的初始大小为 800x600
        self.root.resizable(False, False)  # 禁止窗口的水平和垂直拉伸，即禁止最大化
        self.create_main_frame()

    def create_main_frame(self):
        # 清除之前的界面
        for widget in self.root.winfo_children():
            widget.destroy()
        # 创建主界面
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        # 计算按钮的大小，使其长宽比例接近黄金分割比
        button_width = 236  # 约为 800 / 1.618
        button_height = 146  # 约为 600 / 1.618
        # 计算按钮的位置，使其位于中心
        x = (800 - button_width) // 2
        y = (600 - 2 * button_height - 20) // 2
        button_font = Font(size=20)  # 字体大小设置为 20
        button1 = tk.Button(main_frame, text="开模", command=self.create_create_mould_frame, font=button_font)
        button1.place(x=x, y=y, width=button_width, height=button_height)
        y += button_height + 20  # 调整第二个按钮的位置
        button2 = tk.Button(main_frame, text="加工", command=self.create_third_frame, font=button_font)
        button2.place(x=x, y=y, width=button_width, height=button_height)

    def create_create_mould_frame(self):
        second_page = CreateMouldUI(self.root,self.create_main_frame)
        second_page.create_frame()

    def create_third_frame(self):
        # 清除之前的界面
        for widget in self.root.winfo_children():
            widget.destroy()
        # 创建第三个界面
        third_frame = tk.Frame(self.root)
        third_frame.pack(fill=tk.BOTH, expand=True)
        label = tk.Label(third_frame, text="This is the third interface")
        label.pack(pady=20)
        back_button = tk.Button(third_frame, text="Back", command=self.create_main_frame)
        back_button.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    MysqlConnectUtil.connect_to_mysql()
    root.mainloop()
