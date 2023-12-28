import wx
from ftplib import FTP
import os


ftp_host = 'ftp.axonet-emsys.com'
ftp_user = 'submeter@axonet-emsys.com'
ftp_password = 'submeter1234!@#$'
ftp_directory = 'Onkar_Test'
local_directory = r'C:\Users\msi\Desktop\Tkinter\Wx\ftp'

class demo(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title="demo",size=(500,500))

        self.panel=wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(240, 240, 240))

        self.Show()


    
    def show():
        with FTP(host=ftp_host, user=ftp_user, passwd=ftp_password) as ftp:
            ftp.cwd(ftp_directory)
            files = []
            ftp.dir(files.append)
            for f in files:
                print(f)


    def Download():
        with FTP(host=ftp_host, user=ftp_user, passwd=ftp_password) as ftp:
            ftp.cwd(ftp_directory)
            files = []
            ftp.dir(files.append)

            for line in files:
                # Split the line into parts based on spaces
                parts = line.split()
                if len(parts) > 8 and parts[-1].endswith('.pdf'):
                    file_name = parts[-1]
                    local_file_path = os.path.join(local_directory, file_name)

                with open(local_file_path, 'wb') as local_file:
                    # Retrieve the file in binary mode
                    ftp.retrbinary(f'RETR {file_name}', local_file.write)



if __name__ == "__main__":
    app = wx.App(False)
    frame = demo()
    app.MainLoop()
