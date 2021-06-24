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
	email_tools.email_send(From_Email.get(), Subject_Email.get(), Email_Txt.get("1.0","end-1c"), BCC_Email.get())
def email_send(From,Subject,BCC):
	yag = yagmail.SMTP(From)
	yag.send(subject=Subject,contents="this is a test",bcc=BCC)
	
