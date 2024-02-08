from PIL import Image
from UiStructure import *
from smtpBased import *
import customtkinter
def callSend(window:Skelton,smtp_instance:GmailMain):
    if window.getEmails or window.getMessages :
        print('Sending Email')
        smtp_instance.sendMessage(window.getEmails,window.getMessages,window.getFiles,window.attachmentFLag,'noreply')
        window.attachmentFLag = False


if __name__ == "__main__":
    window = Skelton()
    smtp_instance = None
    getCLientSecret = window._secretKey
    if  getCLientSecret != "":
        smtp_instance = GmailMain(window.getClientSecret)
        window.showComponents()
        sendbutton = CTkButton(master=window,width=5,text='Send',corner_radius=4,command= lambda : callSend(window,smtp_instance) if smtp_instance is not None else print('Error'))
        sendbutton.place(x = 50,y = 200)

        # window.focus_force() 
    else :
        window.destroy()

    window.mainloop()
