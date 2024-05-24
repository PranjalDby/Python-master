from tkinter import PhotoImage, font
import customtkinter
from customtkinter import *
from tkinter.filedialog import askopenfilename, askopenfilenames
class Skelton(customtkinter.CTk):
    _EmailList = []
    _selectedFilesList = []
    def __init__(self):
        super().__init__('blue')
        super().title('GMAIL API')
        self.geometry("500x400")
        self.iconphoto(False,PhotoImage(file='gmailProject/UI/gmail.png'))
        self.textStatus = StringVar()
        self.textStatus.set("Open")
        self._userEmail = StringVar()
        self._messages = StringVar()
        self._secretKey = StringVar()
        self._selectedFiles = StringVar()
        self._selectedFiles.set('Add Attachment')
        self.attachmentFLag = False

    def showComponents(self):
        self.emailField = CTkEntry(self,width=90,height=50,font=('consolas', 18),placeholder_text='Email Please',placeholder_text_color='red',textvariable=self._userEmail,exportselection=True,corner_radius=2)
        self.emailField.place(y = 50,x = 6,relwidth = 1.0)
        self.emailField.bind('<Leave>',lambda _ : self.__getUserInfo())

        #Attach Button
        self.attachButton = CTkButton(self,text='Add Atttachment',textvariable=self._selectedFiles,border_spacing=2,corner_radius=5,command=lambda : self.__addFilesToList())
        self.attachButton.place(x = 50,y = 160)

        #Input Message Area
        self.inputMessageArea = CTkTextbox(self,width=260,height=200,bg_color='white',fg_color='red',font=('Comic-Sans-MS',20),exportselection=True,corner_radius=2,border_spacing=2,border_color='blue')
        self.inputMessageArea.place(x =6,anchor='se',relwidth = 1.0,relx=1.0,y = 460)
        self.inputMessageArea.bind(sequence='<Leave>',command= lambda _ : self.__getUserMessages())

    def __addFilesToList(self):
        self.attachmentFLag = True
        __files = askopenfilenames(initialdir='Downloads')
        if __files != None:
            files = __files
            for f in files:
                self._selectedFilesList.append(f)

        print(__files)
        return
    
    def __getUserMessages(self):
        if self.inputMessageArea.get("1.0",'end-1c') != "":

            self._messages.set(self.inputMessageArea.get("1.0",'end-1c'))
            print(self._messages.get())

        return

    def __getUserInfo(self):
        if self._userEmail.get() != "":
            if self._userEmail not in self._EmailList:
                self._EmailList.append(self._userEmail.get())
        
        return

    @property
    def getClientSecret(self)->str:
        self._clientSecret = askopenfilename(initialdir='Downloads')
        print(self._clientSecret)
        return self._clientSecret if self._clientSecret != "" else ""
    

    @property
    def getEmails(self)->list[str]:
        return self._EmailList if len(self._EmailList) != 0 else []
    
    @property
    def getMessages(self) -> str:

        return self._messages.get() if self._messages.get() != "" else ""
    
    @property
    def getFiles(self)->list[str]:
        return self._selectedFilesList if len(self._selectedFilesList) != 0 else []
    


    
    


    

    
    
        
        



