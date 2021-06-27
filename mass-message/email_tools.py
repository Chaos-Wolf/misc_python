import tkinter as tk
import yagmail

"""def email_login(username, password, window):
	try: 
		test = yagmail.SMTP(username, password)
		test.send(to=username,subject="External Login",contents="You are succesfully logged in")
	except:
		print("error")
		error_window = tk.Tk()
		error_window.title("Error")
		error_label = tk.Label(error_window, text="Wrong username or password, please try again\nIf this keeps happening check your privacy settings and allow third party apps access")
		error_label.grid(row=0,column=0)
		return False
	window.destroy()
def email_login_gui(user_name):
	login_window = tk.Tk()
	login_window.title("Login")
	main_frame = tk.Frame(login_window,relief=tk.RAISED,bd=2)
	main_frame.grid(row=0,column=0)
	username_label = tk.Label(main_frame, text="Username:").grid(row=0,column=0)
	username_input = tk.Entry(main_frame)
	username_input.grid(row=0,column=1)
	password_label = tk.Label(main_frame, text="Password:").grid(row=1,column=0)
	password_input = tk.Entry(main_frame)
	password_input.grid(row=1,column=1)
	username_input.insert(tk.END,user_name)
	login_button = tk.Button(main_frame, text="Login", command=lambda: email_login(username_input.get(),password_input.get(),login_window)).grid(row=2,column=0)
	return True"""
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
	
