import wx
from ftplib import FTP
import os

class FTPFileListFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self,None, title=title, size=(1000, 500))
        
        self.panel = wx.Panel(self)

        font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)


        self.list_ctrl = wx.ListCtrl(self.panel, style=wx.LC_REPORT)
        self.list_ctrl.InsertColumn(0, 'File Name', width=500)

        self.list_ctrl.GetColumn(0).SetFont(font)




        self.download_button = wx.Button(self.panel, label='Download Selected', size=(150, -1))
        self.download_button.Bind(wx.EVT_BUTTON, self.on_download)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.download_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.panel.SetSizer(sizer)
        self.load_ftp_files()

        self.Centre()
        self.Show()

    def load_ftp_files(self):
        ftp_host = 'ftp.axonet-emsys.com'
        ftp_user = 'submeter@axonet-emsys.com'
        ftp_password = 'submeter1234!@#$'
        ftp_directory = 'Onkar_Test'
        #ftp_directory = 'Elcom PCBA Report'

        with FTP(host=ftp_host, user=ftp_user, passwd=ftp_password) as ftp:
            ftp.cwd(ftp_directory)
            files = []
            ftp.dir(files.append)

            for line in files:
                parts = line.split()
                if len(parts) > 8 and parts[-1].endswith('.pdf'):
                    file_name = parts[-1]
                    font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
                    self.list_ctrl.SetFont(font)

                    index = self.list_ctrl.InsertItem(self.list_ctrl.GetItemCount(), file_name)
                    self.list_ctrl.SetItemFont(index, font)
                    

    def on_download(self, event):
        selected_index = self.list_ctrl.GetFirstSelected()
        if selected_index != -1:
            file_name = self.list_ctrl.GetItemText(selected_index)
            self.download_file(file_name)

    def download_file(self, file_name):
        ftp_host = 'ftp.axonet-emsys.com'
        ftp_user = 'submeter@axonet-emsys.com'
        ftp_password = 'submeter1234!@#$'
        ftp_directory = 'Onkar_Test'
        local_directory = r'C:\Users\msi\Desktop\Tkinter\Wx\ftp'

        with FTP(host=ftp_host, user=ftp_user, passwd=ftp_password) as ftp:
            ftp.cwd(ftp_directory)

            local_file_path = os.path.join(local_directory, file_name)
            with open(local_file_path, 'wb') as local_file:
                ftp.retrbinary(f'RETR {file_name}', local_file.write)

            wx.MessageBox(f'Downloaded: {file_name}', 'Download Complete', wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App(False)
    frame = FTPFileListFrame(None, 'FTP File List')
    app.MainLoop()
