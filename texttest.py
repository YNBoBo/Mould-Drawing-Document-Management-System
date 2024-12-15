import tkinter as tk


def show_text():
    input_text = entry.get()  # 获取输入框中的文本
    text_widget.insert(tk.END, input_text + '\n')  # 在文本框中插入输入的文本并换行


root = tk.Tk()
root.title("输入输出程序")


# 创建输入框
entry = tk.Entry(root)
entry.pack(pady=10)


# 创建按钮，点击按钮调用 show_text 函数
button = tk.Button(root, text="显示文本", command=show_text)
button.pack(pady=10)


# 创建文本框
text_widget = tk.Text(root)
text_widget.pack(pady=10)


root.mainloop()