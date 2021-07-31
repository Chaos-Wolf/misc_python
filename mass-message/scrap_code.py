import os.path
import oauth2client
from oauth2client import client,tools,file

SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Send Email'
def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-email-send.json')
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
def login_2():  
	print('Enter the gmailid and password')
	gmailId = input(">")
	passWord = input(">")
	try:
		driver = webdriver.Chrome(ChromeDriverManager().install())
		driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
		'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
		'&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
		driver.implicitly_wait(15)

		loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
		loginBox.send_keys(gmailId)

		nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
		nextButton[0].click()

		passWordBox = driver.find_element_by_xpath(
			'//*[@id ="password"]/div[1]/div / div[1]/input')
		passWordBox.send_keys(passWord)

		nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
		nextButton[0].click()

		print('Login Successful...!!')
	except:
		print('Login Failed')


def login():
	SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
	
	creds = None
	if os.path.exists('token.json'):
		creds = Credentials.from_authorized_user_file('token.json', SCOPES)
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
		with open('token.json','w') as token:
			token.write(creds.to_json())
	service = build('gmail','v1',credentials=creds)
	results = service.users().labels().list(userId='me').execute()
	labels = results.get('labels',[])
	if not labels:
		print('no labels found')
	else:
		print('labels:')
		for label in labels:
			print(label['name'])
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
