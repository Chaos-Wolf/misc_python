import tkinter as tk
import yagmail

def email_login(username):
	try: 
		test = yagmail.SMTP(username)
	except:
		print("error")
		error_window = tk.Tk()
		error_window.title("Error")
		error_label = tk.Label(error_window, text="Wrong username or password, please try again")
		error_label.grid(row=0,column=0)
		return False
	window.destroy()
def email_login_gui(user_name):
	
	return True
def email_send(To,From,Subject,Contents,CC,BCC):
	if To == "":
		To = From
	try:
		yag = yagmail.SMTP(From)
		yag.send(to=To,subject=Subject,contents=Contents,cc=CC,bcc=BCC)
		sent_window = tk.Tk()
		sent_window.title("Sent")
		sent_window.geometry('50x50')
		sent_label = tk.Label(sent_window,text="Emails Sent")
		sent_label.grid(row=0,column=0)
	except Exception as e:
		print("error")
		error_window = tk.Tk()
		error_window.title("Error")
		error_label = tk.Label(error_window, text=e)
		error_label.grid(row=0,column=0)
	
