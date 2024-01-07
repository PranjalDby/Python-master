from __future__ import print_function
import base64
from email import encoders
from email.message import EmailMessage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os.path
import google.auth
from mimetypes import guess_type as guess_mime_type
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import zipfile
from typing import Any
SCOPES = ["https://mail.google.com/"]



class GmailMain:
    creds  = None
    attachmentFiles:list[str] = []
    msg_ = None
    def __init__(self,choose_secret:str) -> None:
        self.choose_secret = choose_secret

    def gmail_auth(self)->Any:

        if self.creds == None:
            service = None
        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json',SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(request=Request())
            else:
                if self.choose_secret != None:
                    try:
                        flow = InstalledAppFlow.from_client_secrets_file(
                                self.choose_secret,
                                SCOPES
                            )
                        self.creds = flow.run_local_server(port=0)
                    
                    except Exception as e:
                        print("Some Error at line 46")
                
                else:
                    print("No client_secret found...")

            with open('token.json','w+') as token:
                token.write(self.creds.to_json())
        try:
            # calling the api
            service = build(
                    'gmail',
                    'v1',
                    credentials=self.creds,
                    cache_discovery=False,
                )
        except HttpError as e:
            print(e)

        return service
    
    def build_filePart(self,file,message):

        _mtype,sub = guess_mime_type(file,False)

        if(_mtype is not None or sub is None):
            _mtype = "application/octet-stream"

        mtype,subs = _mtype.split('/')
        print(mtype)
        if mtype == "text":
            with open(file,'rb'):
                self.msg_ = MIMEText("r",_subtype = subs)

        elif mtype == "image":
            with open(file, "rb"):
                self.msg_ = MIMEImage("r", _subtype=subs)
        elif mtype == "audio":
            with open(file, "rb"):
                self.msg_ = MIMEAudio("r", _subtype=subs)
        else:
            with open(file, "rb") as fp:
                self.msg_ = MIMEBase(mtype, subs)
                self.msg_.set_payload(fp.read())

        filename = os.path.basename(file)
        self.msg_.add_header('Content-Disposition',"attachment",filename = filename)
        encoders.encode_base64(self.msg_)
        message.attach(self.msg_)

        return message
    
    def FileAttach(self,message):
        # attachment_data = None
        if len(self.attachmentFiles) == 1:
            message =  self.build_filePart(self.attachmentFiles[0],message=message)
            print("Single file Clicked")
                    
        elif len(self.attachmentFiles) > 1:
            curr = ""
            for files in self.attachmentFiles:
                message = self.build_filePart(files,message)
                print("Multiple file is")

        
        return base64.urlsafe_b64encode(message.as_bytes()).decode()

    def create_draft(self,des:str,service:Any):
        message = EmailMessage()
        message.set_content('This is Automated Draft')
        message['To'] = des
        message['from'] = 'pranjalorg11@gmail.com'
        message['subject'] = 'Automated draft'
        # Encoded message

        try:
            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            create_message = {"message":{"raw":encoded_message}}
            draft = (
                service.users()
                .drafts()
                .create(userId = "me",body = create_message)
                .execute()
            )
            print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

        except HttpError as error:
            print('Http Error')
            draft = None

        return draft
    
    def createMessage(self,des:list[str],message:str,subject:str,Attachment:bool):
        send_message = None
        create_message  = ''
        try:
            service = self.gmail_auth()
            message_obj =  MIMEMultipart()
            isEncoded = None
            #headers
            multiple_users = ""
            if len(des)> 1:
                multiple_users = ",".join(des)
            
            else:
                multiple_users = des[0]
            
            text = MIMEText(message,"plain")
            message_obj['To'] = multiple_users
            message_obj['From'] = "Enter Appl"
            message_obj['Subject'] = subject
            message_obj.attach(text)
            if Attachment:
                if self.attachmentFiles != None:
                    isEncoded = self.FileAttach(message_obj)
                    create_message = {
                        "raw":isEncoded
                    }

            else:
                isEncoded = base64.urlsafe_b64encode(message_obj.as_bytes()).decode()
                create_message = {
                    "raw":isEncoded
                }
            
            print("is Encoded = ",isEncoded)
            send_message = (
                service.users()
                .messages()
                .send(userId = "me",body = create_message)
                .execute()
            )

        except HttpError as e:
            print(e)
            send_message = None
    
        return send_message


                            


