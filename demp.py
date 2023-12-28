from ftplib import FTP, all_errors
import os,stat

with FTP(host='ftp.axonet-emsys.com', user='submeter@axonet-emsys.com', passwd='submeter1234!@#$') as ftp:
    ftp.cwd('Onkar_Test')
    files = []
    ftp.dir(files.append)  
    for f in files:
        #print(f)
        if f.endswith('.pdf'):
            print(f)
            #os.chmod(f,stat.S_IRWXU | stat.S_IRWXG |stat.S_IRWXO )
            with open(f, 'w') as local_file:
     
                response = ftp.retrbinary(f'RETR {f}', local_file.write)

                if response.startswith('226'):  
                     print('Transfer complete')
                else:
                    print('Error transferring. Local file may be incomplete or corrupt.')
    

    ftp.quit()
