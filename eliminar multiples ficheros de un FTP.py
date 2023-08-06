from ftplib import FTP

host = input('host: ')
port = input('port: ')
user = input('user: ')
passwd = input('pass: ')
path = input('path: ')
filesToDelete = input('introduce los nombres de los ficheros a eliminar separados por ";" : ')
arrayFilesToDelete = filesToDelete.split(";")

ftp = FTP()
ftp.connect(host, int(port))
ftp.login(user, passwd)
ftp.cwd(path)
ftp.dir()

for i in range(len(arrayFilesToDelete)):
    ftp.delete(arrayFilesToDelete[i])
    print('fichero eliminado: ', arrayFilesToDelete[i])

ftp.quit()