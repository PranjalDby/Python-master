from __future__ import print_function
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import base64
from email import encoders
from email.message import EmailMessage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os.path
from mimetypes import guess_type as guess_mime_type
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from typing import Any, Optional
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
        
        else:
            print('Send Complete')

        return service
    
    def build_filePart(self,file,message):

        content_type,encoding = guess_mime_type(file,False)

        if(content_type is None or encoding is not None):
            content_type = 'application/octet-stream'

        mtype,subtype = content_type.split('/',1)

        print(f'File Selected = ......... {content_type}.{encoding}')
        if mtype == "text":
            with open(file,'rb') as fp:
                self.msg_ = MIMEText(fp.read().decode(),_subtype=subtype)

        elif mtype == "image":
         
            with open(file,'rb') as fp:
                self.msg_ = MIMEImage(fp.read(),_subtype = subtype)


        elif mtype == "audio":

            with open(file,'rb') as fp:
                self.msg_ = MIMEAudio(fp.read(),_subtype=subtype)

        else:
            with open(file, "rb") as fp:
                self.msg_ = MIMEBase(mtype, subtype)
                self.msg_.set_payload(fp.read())

        self.msg_.add_header('Content-Disposition',"attachment ",filename=os.path.basename(file))
        message.attach(self.msg_)
    
    def FileAttach(self,message):
        # attachment_data = None
        if len(self.attachmentFiles) == 1:
            message =  self.build_filePart(self.attachmentFiles[0],message=message)
            print("Single file Clicked")
                    
        elif len(self.attachmentFiles) > 1:
            for f in self.attachmentFiles:
                self.build_filePart(f,message)

    # def create_draft(self,des:str,service:Any):
    #     message = EmailMessage()
    #     message.set_content('This is Automated Draft')
    #     message['To'] = des
    #     message['from'] = 'pranjalorg11@gmail.com'
    #     message['subject'] = 'Automated draft'
    #     # Encoded message

    #     try:
    #         encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    #         create_message = {"message":{"raw":encoded_message}}
    #         draft = (
    #             service.users()
    #             .drafts()
    #             .create(userId = "me",body = create_message)
    #             .execute()
    #         )
    #         print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

    #     except HttpError as error:
    #         print('Http Error')
    #         draft = None

    #     return draft
    
    def createMessage(self,des:list[str],message:str,subject:str,Attachment:bool,attachment:Optional[list[str] | None]):

        self.attachmentFiles = attachment
        try:
            #headers
            multiple_users = ""
            if len(des)> 1:
                multiple_users = ",".join(des)
            
            else:
                multiple_users = des[0]
        
            if not Attachment:
                message_obj = MIMEText(message,"plain")
                message_obj['To'] = multiple_users
                message_obj['From'] = "pranjalorg11@gmail.com"
                message_obj['Subject'] = subject
            else:
                message_obj = MIMEMultipart()
                message_obj['To'] = multiple_users
                message_obj['From'] = "pranjalorg11@gmail.com"
                message_obj['Subject'] = subject
                message_obj.attach(MIMEText(message))

                if self.attachmentFiles != None:
                    self.FileAttach(message_obj)

        except TimeoutError as e:
            print('Timeout')


        return {
            "raw":base64.urlsafe_b64encode(message_obj.as_bytes()).decode()
        }

    def sendMessage(self,destination,body,attachments = [],addAttachment=False,subject:str="noreply"):
        service = self.gmail_auth()
        try:
            return service.users().messages().send(
                userId = "me",
                body = self.createMessage(destination,body,subject,addAttachment,attachments)
            ).execute()    
        except HttpError as e:
            print('HTTP ERROR')

        except TimeoutError as e2:
            print('Timeout Error..')




                            


