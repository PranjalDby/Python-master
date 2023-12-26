from __future__ import print_function
from email import encoders
import os.path
import requests
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import zipfile
import tkinter
from tkinter.filedialog import askopenfiles
from tkinter.filedialog import askopenfilename
import asyncio
SCOPES = ['https://mail.google.com/']
our_email = 'pranjalorg11@gmail.com'
service = None
tk = tkinter.Tk()
tk.withdraw()

choose_secret = askopenfilename()

def gmail_auth():
    global service
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json',SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(request=Request())
        else:
            if choose_secret != None:
                try:
                    flow = InstalledAppFlow.from_client_secrets_file(
                            choose_secret,
                            SCOPES
                        )
                    creds = flow.run_local_server(port=5050)
                
                except Exception as e:
                    print("Some Error at line 46")
            
            else:
                print("No client_secret found...")

        with open('token.json','w+') as token:
            token.write(creds.to_json())
    try:
         # calling the api
        service = build(
                'gmail',
                'v1',
                credentials=creds,
                cache_discovery=False,
            )
    except HttpError as e:
        print(e)

    return service

# request Authenticated id 
service = gmail_auth()

async def add_attachment(message,filename):
    if type(filename) is not type(list):
        print("File selected = ",filename)
        t1 = asyncio.create_task(file_attach_helper(message,filename))
        await t1
    else:
        t2 = asyncio.create_task(file_attach_helper(message,filename))
        await t2

async def file_attach_helper(message,filename):

    if type(filename) != type(list):
        singleFileTask  = asyncio.create_task(singFileAttach(filename,message))
        await singleFileTask
    else:
        for files in filename:
            multipleFileTask  = asyncio.create_task(message_attach_multiple(files,message))
            await multipleFileTask
    

async def singFileAttach(filename,message):
    _,extension = os.path.splitext(filename)
    if extension != None:
        getMimeTypeTask = asyncio.create_task(return_guessed_mime_type(filename))
        await getMimeTypeTask
        mainType,subType = getMimeTypeTask.result()
        print(f'''
            selected file is: ==========
            maint type ={mainType} sub = {subType}
            ''')
        
        with open(filename,'rb') as openFile:
            part = MIMEBase(mainType,subType)
            part.set_payload(openFile.read())
            part.add_header('Content-Disposition',"attachments; filename= %s" % os.path.basename(str(filename)))
            encoders.encode_base64(part)
            message.attach(part)

    else:
        print("File Format is Not Supported.")

async def message_attach_multiple(filename,message):
    ext_file = {}
    extension_list = []
    count = -1
    _,extension = os.path.splitext(filename)
    if extension != None:
        extension_list.insert(count,extension)
        ext_file[extension_list[count]] = _
        task_type = asyncio.create_task(return_guessed_mime_type(filename))
        await task_type
        mt_,sub = task_type.result()
        print(f'''
                selected file is: ==========
                maint type ={mt_} sub = {sub}
                ''')
        
        if filename != None:
            with open(filename,"rb") as fp:
                part = MIMEBase(mt_,sub)
                part.set_payload(fp.read())
                part.add_header('Content-Disposition',"attachments; filename= %s" % os.path.basename(str(filename)))
                encoders.encode_base64(part)
                message.attach(part)
        else:
            print("File not found...")
    
async def return_guessed_mime_type(file_name):
    _mtype,sub = guess_mime_type(file_name,False)
    print(_mtype)
    print(sub)
    if(_mtype is not None and sub is None):
            mtype,sub = _mtype.split('/')
    else:
        f_name,ext = os.path.splitext(file_name)
        with zipfile.ZipFile(f_name+".zip",'w') as zips:
            zips.write(file_name,compress_type=zipfile.ZIP_DEFLATED)
            f_name = os.path.basename(zips.filename)
            print(f_name)
            mtype,sub = return_guessed_mime_type(f_name)


    return [mtype,sub]

__sameAttachment = False
message = MIMEMultipart()
async def create_body(message_entry,destination,subject,no_usr):
    global __sameAttachment
    attachment  = 'no'
    if not __sameAttachment:
        attachment = str(input('Do you Want to Add Attachemnt: yes or no: ').lower())

    if __sameAttachment == False and attachment == 'yes':
        if no_usr > 1:
            is_same = str(input('Do you Want to send this attachments to all users[yes][no]: ')).lower()
            __sameAttachment = True if is_same == 'yes' else False

    if(attachment == 'yes'):
        if  message.get_filename() == None:
            print(message.get_filename())
            t3 = asyncio.create_task(prepareMessage(message,message_entry,destination,subject))
            await t3
            no_usr -=1

    elif attachment == 'no':
        message['To'] = destination
        message['From'] = 'pranjalorg11@gmail.com'
        message['Subject'] = subject

    return {
        'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()
    }

async def prepareMessage(message,message_entry,destination,subject):
    message.attach(MIMEText(message_entry))
    message['To'] = destination
    message['From'] = 'pranjalorg11@gmail.com'
    message['Subject'] = subject or "Auto-Generated"
    if int(input("want to select multiple files: 1 - YES: ")) == 1:
        files = askopenfiles('r')
        str1 = []
        for i in files:
            str1.append(i.name)
        for i in str1:
            t2 =  asyncio.create_task(add_attachment(message,i))
            await asyncio.sleep(0.5)
        
    else:
        files  = askopenfilename()
        task  = asyncio.create_task(add_attachment(message,files))
        await asyncio.sleep(0.5)
        
# SameToAll = False
prev_mess = ""
prev_sub = ""
SameToAll = False
async def send_email(des="",no_usr=1):
    global __sameAttachment
    print('---------------------------CALLED SEND_EMAIL()-------------------------------------')
    global prev_sub,prev_mess,SameToAll,message

    if des == "":
        des = str(input('Enter the Destination: '))
    
    print("Message To :{}".format(des))
    if no_usr > 1 and not SameToAll:
        np = str(input('do you want the same message for every other people: ')).lower()
        if np == 'yes':
            SameToAll = True
            __sameAttachment = True
        else:
            SameToAll = False
            __sameAttachment = False
    
    if SameToAll and prev_mess == "" or prev_sub == "":
        mess = str(input('Enter your Message: '))
        prev_mess = mess
        sub = str(input('Enter the Subject: '))
        prev_sub = mess
        
    elif SameToAll and prev_mess != "":
        print(message.raw_items())
        mess = prev_mess
        sub = prev_sub

    else:
        message = MIMEMultipart()
        mess = str(input('Enter your Message: '))
        sub = str(input('Enter the Subject: '))

    if mess != None and des != None:
        res_task  =  asyncio.create_task(create_body(mess,des,sub,no_usr))
        await res_task
        if res_task.done():
            res = res_task.result()
        try:
            return service.users().messages().send(
            userId='me',
            body = res
            ).execute()
        
        except TimeoutError as e:
            print("Timeout...")
    else:
        raise HttpError('Http Error at Send Email')
    
def send_to_multiple():
    file_list =[]
    files = askopenfilename()
    with open(files,'r') as file:
        for lines in file.readlines():
            file_list.append(lines)

async def main():
    try:
        opt1 = int(input(
    '''\bEnter the options Showed Belowed:
        1> Send to multiple user
        2> Send to single user\n
        '''))
        if opt1 == 1:
            email_liss = []
            if len(email_liss) == 0:
                user = "".join(str(input('Enter The Email Addresses: ')))
                print(user)
                email_liss = user.split(" ")
                
            for j in email_liss:
                task1 = asyncio.create_task(send_email(j,len(email_liss)))
                await asyncio.sleep(0.43)
            
        else:
            print('-----------------------------------FOR SINGLE USER---------------------------------------')
            await send_email()
    except HttpError as e:
        print("Http Error at line 206")
    except requests.exceptions.JSONDecodeError as e2:
        print("Json File or Something..")
    
    except TypeError as e:
        print('Error')
    else:
        print("🥵 send Successfully")

if __name__ == "__main__":
    cr = asyncio.run(main=main())
