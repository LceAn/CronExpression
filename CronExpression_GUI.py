# -*-  coding : utf-8 -*-
# @Time : 2023/12/11 01:00
# @Autor : LceAn
# @File : CronExpression_GUI.py
# @Software : PyCharm

import tkinter as tk
from tkinter import ttk
import pyperclip

def update_cron_expression(*args):
    # 更新 Cron 表达式
    global second, minute, hour, day, month, day_of_week
    second = second_var.get()
    minute = minute_var.get()
    hour = hour_var.get()
    day = day_var.get()
    month = month_var.get()
    day_of_week = day_of_week_var.get()

    cron_expression = f"{second} {minute} {hour} {day} {month} {day_of_week}"
    cron_label.config(text=f"Cron 表达式为: {cron_expression}")

def copy_to_clipboard():
    # 复制到剪贴板
    cron_expression = cron_label.cget("text").split(": ")[1]  # 获取文本内容
    pyperclip.copy(cron_expression)

def initialize_values():
    # 初始化值
    second_var.set('*')
    minute_var.set('*')
    hour_var.set('*')
    day_var.set('*')
    month_var.set('*')
    day_of_week_var.set('*')
    cron_label.config(text="Cron 表达式为: * * * * * *")

root = tk.Tk()
root.title("Cron表达式生成器")

# 创建选择框框架
frame = ttk.Frame(root, padding="20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# 标签和选择框的样式
label_style = ttk.Style()
label_style.configure("CustomLabel.TLabel", font=('Arial', 12))
ttk.Style().configure("TCombobox", font=('Arial', 12))

# 秒
second_label = ttk.Label(frame, text="秒:", style="CustomLabel.TLabel")
second_label.grid(column=0, row=0, sticky=tk.W)
second_var = tk.StringVar(root)
second_options = list(range(60))
second_var.trace("w", update_cron_expression)
second_menu = ttk.OptionMenu(frame, second_var, *second_options)
second_menu.grid(column=1, row=0)

# 分钟
minute_label = ttk.Label(frame, text="分钟:", style="CustomLabel.TLabel")
minute_label.grid(column=0, row=1, sticky=tk.W)
minute_var = tk.StringVar(root)
minute_options = list(range(60))
minute_var.trace("w", update_cron_expression)
minute_menu = ttk.OptionMenu(frame, minute_var, *minute_options)
minute_menu.grid(column=1, row=1)

# 小时
hour_label = ttk.Label(frame, text="小时:", style="CustomLabel.TLabel")
hour_label.grid(column=0, row=2, sticky=tk.W)
hour_var = tk.StringVar(root)
hour_options = list(range(24))
hour_var.trace("w", update_cron_expression)
hour_menu = ttk.OptionMenu(frame, hour_var, *hour_options)
hour_menu.grid(column=1, row=2)

# 日期
day_label = ttk.Label(frame, text="日期:", style="CustomLabel.TLabel")
day_label.grid(column=0, row=3, sticky=tk.W)
day_var = tk.StringVar(root)
day_options = list(range(1, 32))
day_var.trace("w", update_cron_expression)
day_menu = ttk.OptionMenu(frame, day_var, *day_options)
day_menu.grid(column=1, row=3)

# 月份
month_label = ttk.Label(frame, text="月份:", style="CustomLabel.TLabel")
month_label.grid(column=0, row=4, sticky=tk.W)
month_var = tk.StringVar(root)
month_options = list(range(1, 13))
month_var.trace("w", update_cron_expression)
month_menu = ttk.OptionMenu(frame, month_var, *month_options)
month_menu.grid(column=1, row=4)

# 星期
day_of_week_label = ttk.Label(frame, text="星期:", style="CustomLabel.TLabel")
day_of_week_label.grid(column=0, row=5, sticky=tk.W)
day_of_week_var = tk.StringVar(root)
day_of_week_options = ["0", "1", "2", "3", "4", "5", "6", "7"]
day_of_week_var.trace("w", update_cron_expression)
day_of_week_menu = ttk.OptionMenu(frame, day_of_week_var, *day_of_week_options)
day_of_week_menu.grid(column=1, row=5)

# 初始化按钮
initialize_button = ttk.Button(frame, text="初始化", command=initialize_values)
initialize_button.grid(column=0, row=6, pady=20, columnspan=2)

# 复制按钮
copy_button = ttk.Button(frame, text="复制结果", command=copy_to_clipboard)
copy_button.grid(column=0, row=7, pady=10, columnspan=2)

# 显示实时更新的 Cron 表达式
cron_label = ttk.Label(frame, text="Cron 表达式为: * * * * * *", style="CustomLabel.TLabel")
cron_label.grid(column=0, row=8, columnspan=2)
cron_label.config(justify="left", wraplength=300)  # 长文本换行
cron_label.bind("<1>", lambda event: cron_label.focus_set())  # 允许标签内容被选中

# 添加归属信息
ttk.Label(frame, text="© 2023 Lcean", style="CustomLabel.TLabel").grid(column=0, row=9, columnspan=2, sticky=tk.E)

root.mainloop()
