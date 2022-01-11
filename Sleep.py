from tkinter import *
from tkinter import messagebox


def main_timer(time_label, S):

	def time():

		if Timer:

			global S

			time_label.config(text = "Таймер: " + format(S))

			time_label.after(1000, time) 

			if S == 0:
				root.destroy()
				# Выключение PC
				import os
				os.system('shutdown -s')
			else:
				S -= 1

	time()    


def Start():

	global Timer, S

	nums = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}
	Error = False

	if len(часы.get()) != 0:
		for i in list(часы.get()):
			if i not in nums:
				messagebox.showerror("Ошибка", message = f'Неизвестный символ: "{i}"')
				Error = True
				break

	if not Error:
		if len(минуты.get()) != 0:
			for i in list(минуты.get()):
				if i not in nums:
					messagebox.showerror("Ошибка", message = f'Неизвестный символ: "{i}"')
					Error = True
					break

	if not Error:
		temp_m = float(минуты.get()) * 60 if len(минуты.get()) > 0 else 0
		temp_h = float(часы.get()) * 3600 if len(часы.get()) > 0 else 0

		S = temp_m + temp_h

		del temp_h, temp_m


		if S == 0:
			Error = True
			messagebox.showwarning("Таймер не задан", message = "Введите время")

	if not Error:
		if S <= 360000 and S >= 30:
			label_H.destroy()
			label_M.destroy()
			Ent_H.destroy()
			Ent_M.destroy()
			start_button.destroy()
			message_button.destroy()

			time_label = Label(text = format(S), fg = "#eee", bg = "#333", font = "Arial 17")

			time_label.grid(row = 0, column = 0, sticky = "w")

			root.config(bg = "#333")

			# Запуск таймера
			Timer = True
			main_timer(time_label, S)

		elif S < 30:
			messagebox.showwarning("Ограничение", message = "Минимум 30 секунд")
		else:
			messagebox.showwarning("Ограничение",message = "Максимум 100 часов")

def format(Sec):
	return (str(int(Sec // 3600)) + "ч :" if int(Sec // 3600) != 0 else "") + str(int(Sec % 3600 // 60)) + "м :" + str(int(Sec % 3600 % 60)) + "с"

def info():
	messagebox.showinfo(title = "Внимание", message = "1) Запускать от имени администратора.\n2) Windows может перевести ваш компьютер в спящий режим. Смотреть: Панель управления -> Электропитание -> Настройка схемы электропитания -> Переводить компьютер в спящий режим (Никогда)")



root = Tk()
root.title("Sleep")


root.resizable(width=False, height=False)
root.attributes('-toolwindow', True)

минуты = StringVar()
часы = StringVar()


label_H = Label(text = "Введите часы      :") 
label_M = Label(text = "Введите минуты :")

label_H.grid(row = 0, column = 0, sticky = "w")
label_M.grid(row = 1, column = 0, sticky = "w")

Ent_H = Entry(textvariable = часы)
Ent_M = Entry(textvariable = минуты)

Ent_H.focus_set()


Ent_H.grid(row = 0,column = 1, padx = 5, pady = 5)
Ent_M.grid(row = 1,column = 1, padx = 5, pady = 5)


message_button = Button(text = "?", command = info)
message_button.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")

start_button = Button(text = "Запустить таймер", command = Start)
start_button.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "e")

S = 0 # Общие секунды
Timer = False

root.mainloop()
