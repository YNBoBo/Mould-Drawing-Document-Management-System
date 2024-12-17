import tkinter as tk


def update_text():
    selected_items = []
    if checkbox1_var.get():
        selected_items.append(checkbox1_text.get())
    if checkbox2_var.get():
        selected_items.append(checkbox2_text.get())
    if radiobutton1_var.get():
        selected_items.append(radiobutton1_text.get())
    if radiobutton2_var.get():
        selected_items.append(radiobutton2_text.get())
    text_label.config(text=", ".join(selected_items))


# 创建主窗口
root = tk.Tk()
root.title("选择器")

# 创建变量存储复选框和单选框的状态
checkbox1_var = tk.IntVar()
checkbox2_var = tk.IntVar()
radiobutton1_var = tk.IntVar()
radiobutton2_var = tk.IntVar()

# 创建复选框
checkbox1_text = tk.StringVar()
checkbox1_text.set("选项 1")
checkbox1 = tk.Checkbutton(root, textvariable=checkbox1_text, variable=checkbox1_var, command=update_text)
checkbox1.pack()

checkbox2_text = tk.StringVar()
checkbox2_text.set("选项 2")
checkbox2 = tk.Checkbutton(root, textvariable=checkbox2_text, variable=checkbox2_var, command=update_text)
checkbox2.pack()

# 创建单选框
radiobutton1_text = tk.StringVar()
radiobutton1_text.set("单选 1")
radiobutton1 = tk.Radiobutton(root, textvariable=radiobutton1_text, variable=radiobutton1_var, value=1, command=update_text)
radiobutton1.pack()

radiobutton2_text = tk.StringVar()
radiobutton2_text.set("单选 2")
radiobutton2 = tk.Radiobutton(root, textvariable=radiobutton2_text, variable=radiobutton2_var, value=2, command=update_text)
radiobutton2.pack()

# 创建文本标签
text_label = tk.Label(root, text="")
text_label.pack()

# 运行主循环
root.mainloop()