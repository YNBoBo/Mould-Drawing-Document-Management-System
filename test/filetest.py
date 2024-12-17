import tkinter as tk
from tkinter import filedialog
import tkinterdnd2
import logging
import os


def drop(event):
    try:
        file_path = event.data
        print("拖放的文件名称: " + file_path)
    except Exception as e:
        print("文件拖放时出现错误: " + str(e))


def create_drop_area():
    drop_area = tk.Label(root, text="将文件拖放到此区域", bg="lightgray", width=50, height=10)
    drop_area.pack(pady=20)
    # 使用 tkinterdnd2 的 DND_FILES 事件处理文件拖放
    drop_area.drop_target_register(tkinterdnd2.DND_FILES)
    drop_area.dnd_bind('<<Drop>>', drop)
    drop_area.bind("<Enter>", lambda e: drop_area.config(bg='lightblue'))
    drop_area.bind("<Leave>", lambda e: drop_area.config(bg='lightgray'))


def browse_file():
    try:
        file_path = filedialog.askopenfilename()
        if file_path:
            print("选择的文件名称: " + file_path)
        else:
            print("未选择文件")
    except Exception as e:
        print("文件选择时出现错误: " + str(e))
        print("文件选择时出现错误:", e)


# 使用 tkinterdnd2 的 Tk 类代替 tkinter 的 Tk 类
root = tkinterdnd2.Tk()
root.title("文件拖放程序")


create_drop_area()

browse_button = tk.Button(root, text="选择文件", command=browse_file)
browse_button.pack(pady=10)
# 创建文本框
text_widget = tk.Text(root)
text_widget.pack(pady=20)

root.mainloop()
