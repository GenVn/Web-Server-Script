import os
import shutil

def mainProcess(name):
	path = os.path.join("/var/www/html",name)
	if not os.path.exists(path): 
		os.mkdir(path)
		os.system("chown -R apache:apache /var/www/html/"+name)
		os.system("chmod 755 /var/www")
		os.system("chmod 755 /var/www/html")
		print("Create domain "+name+" folder sucessfully!")
		addVitualHostSetting()
		addVitualHost(name)
	else:
		print("Domain "+name+" folder already exists!")

def addVitualHostSetting():
	string = "NameVirtualHost *:80"
	with open("/etc/httpd/conf/httpd.conf", "r+") as f:
		content = f.read()
		if not string in content:
			f.write(string)
	f.close
	print("Create VitualHost sucessfully (Default port 80)")
def addVitualHost(name):
	with open("/etc/httpd/conf.d/"+name+".conf", "w") as f:
		completeVitualHost = "<VirtualHost *:80>\n"
		completeVitualHost += "\tServerAdmin admin@"+name+"\n"
		completeVitualHost += "\tDocumentRoot /var/www/html/"+name+"\n"
		completeVitualHost += "\tServerName "+name+"\n"
		completeVitualHost += "\tServerAlias "+name+"\n"
		completeVitualHost += "</VirtualHost>\n"
		f.write(completeVitualHost)
	f.close
	print("Create VitualHost setting for "+name+" sucessfully")
def copyFolder(source,domain):
	target = "/var/www/html/"+domain
	os.system("cp "+source+"/* "+target)
	os.system("chmod +x /var/www/html/"+domain+"/index.html")
	os.system("systemctl restart httpd")
	print("Copy sucessfully")
