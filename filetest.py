import tkinter as tk
from tkinter import filedialog
import tkinterdnd2
import logging
import os

def show_text(input_text):
    logger.info("输入文本: " + input_text)
    text_widget.insert(tk.END, input_text + '\n')  # 在文本框中插入输入的文本并换行

def setup_logging():
    # 获取桌面路径
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    log_file_path = os.path.join(desktop_path, 'test_log.txt')
    # 创建一个日志记录器
    logger = logging.getLogger('FileDropLogger')
    logger.setLevel(logging.DEBUG)
    # 创建一个文件处理器
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)
    # 创建一个格式化器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    # 将处理器添加到记录器
    logger.addHandler(file_handler)
    return logger


def drop(event):
    try:
        file_path = event.data
        logger.info("拖放的文件名称: " + file_path)
        show_text(file_path)
    except Exception as e:
        logger.error("文件拖放时出现错误: " + str(e))
        print("文件拖放时出现错误:", e)


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
            logger.info("选择的文件名称: " + file_path)
            show_text(file_path)
        else:
            logger.info("未选择文件")
    except Exception as e:
        logger.error("文件选择时出现错误: " + str(e))
        print("文件选择时出现错误:", e)


# 使用 tkinterdnd2 的 Tk 类代替 tkinter 的 Tk 类
root = tkinterdnd2.Tk()
root.title("文件拖放程序")


logger = setup_logging()


create_drop_area()


browse_button = tk.Button(root, text="选择文件", command=browse_file)
browse_button.pack(pady=10)
# 创建文本框
text_widget = tk.Text(root)
text_widget.pack(pady=20)

root.mainloop()