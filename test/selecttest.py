import tkinter as tk

import tkinterdnd2

from entity.Opeate import processes, mould_parts, operate_types
from util import TimeUtil, MouldSerialParseUtil

# 复选框的变量列表
mould_part_check_vars = []
process_check_vars = []

mould_serial = None
version_id = 3


def show_selected():
    process_selected_items = []
    mould_part_selected_items = []

    for i, var in enumerate(mould_part_check_vars):
        if var.get() == 1:
            mould_part_selected_items.append(mould_parts[i])

    for i, var in enumerate(process_check_vars):
        if var.get() == 1:
            process_selected_items.append(processes[i])

    date = TimeUtil.get_today()
    result_text = f"{mould_serial}-{date}-{operate_type.get()}"
    if len(mould_part_selected_items) != 0:
        result_text = f"{result_text}-{', '.join(mould_part_selected_items)}"
    if len(process_selected_items) != 0:
        result_text = f"{result_text}-{', '.join(process_selected_items)}"
    result_text = f"{result_text}-{version_id}"
    result_label.config(text=result_text)
    custom_process.delete(0, tk.END)  # 清空输入框
    custom_process.insert(0, result_text)  # 向输入框插入文本


# 创建主窗口
root = tkinterdnd2.Tk()
root.title("Checkbox Example")

def drop(event):
    global mould_serial
    try:
        file_path = event.data
        print("拖放的文件名称: " + file_path)
        mould_serial = MouldSerialParseUtil.parse_file_path(file_path)
        show_selected()
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

create_drop_area()

operate_type_checkbox_frame = tk.Frame(root)
operate_type_checkbox_frame.pack(side=tk.TOP, pady=10)
# 创建一个 StringVar 来存储单选框的选择
operate_type = tk.StringVar()
operate_type.set(operate_types[0])  # 设置默认选中的选项

for i in range(len(operate_types)):
    radio = tk.Radiobutton(operate_type_checkbox_frame, text=operate_types[i], variable=operate_type,
                           value=operate_types[i],command=show_selected)
    radio.pack(side=tk.LEFT)

mould_part_checkbox_frame = tk.Frame(root)
mould_part_checkbox_frame.pack(side=tk.TOP, pady=10)

for i in range(len(mould_parts)):
    var = tk.IntVar()
    mould_part_check_vars.append(var)
    checkbox = tk.Checkbutton(mould_part_checkbox_frame, text=mould_parts[i], variable=var,command=show_selected)
    checkbox.pack(side=tk.LEFT)

process_checkbox_frame = tk.Frame(root)
process_checkbox_frame.pack(side=tk.TOP, pady=10)

for i in range(len(processes)):
    var = tk.IntVar()
    process_check_vars.append(var)
    checkbox = tk.Checkbutton(process_checkbox_frame, text=processes[i], variable=var,command=show_selected)
    checkbox.pack(side=tk.LEFT)

# 创建一个水平布局管理器
row1_frame = tk.Frame(root)
row1_frame.pack(side=tk.TOP, pady=10)
tk.Label(row1_frame, text="自定义加工工艺：").pack(side=tk.LEFT, padx=(10, 5))
custom_process = tk.Entry(row1_frame, width=80)
custom_process.pack(side=tk.LEFT, padx=(0, 10), expand=True)

# 创建一个新的框架来放置按钮，确保按钮另起一行
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, pady=10)

# 显示选中结果的标签
result_label = tk.Label(root, text="最终文件名：")
result_label.pack()


# 运行主循环
root.mainloop()
