import tkinter as tk
import yagmail


#takes a recipient, the sender, a subject,contents, attachments and both CC and BCC and attempts to send a email
#will throw a error message if the email doesnt work. will also give a popup window if the message sent
#can also work for text messages if you add the right suffix to the end of the number in the mass text tab
def email_send(To,From,Subject,Contents,Attachments,CC,BCC):
	if To == "":
		To = From
	try:
		yag = yagmail.SMTP(From)
		yag.send(to=To,subject=Subject,contents=Contents,attachments=Attachments,cc=CC,bcc=BCC)
		sent_window = tk.Tk()
		sent_window.title("Sent")
		sent_window.geometry('200x200')
		sent_label = tk.Label(sent_window,text="Emails Sent")
		sent_label.grid(row=0,column=0)
	except Exception as e:
		print("error")
		if "Please log in via your web browser and then try again" in str(e):
			e = "Please sign into your account in your webbrowser\nThen restart this application and try again\nYou also might have to set your security settings to allow for third party apps"
		error_window = tk.Tk()
		error_window.title("Error")
		error_label = tk.Label(error_window, text=e)
		error_label.grid(row=0,column=0)
        