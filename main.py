#!/usr/bin/python3
import sys, requests, re

if len(sys.argv) == 3:
   print("\nMade by https://github.com/antonchu2006")
else:
    print("\n[!] USAGE: python3" + sys.argv[0] + " <username> <passwd>")
    sys.exit(1)
 

def checker(username, password):

    ## Obtener el PHPSESSID

    url1 = "https://escolarosaliadecastro.clickedu.eu/students/la_meva_classe.php"
    r1 = str(requests.get(url1).cookies)
    PHPSESSID = re.search(r"PHPSESSID=\w*", r1).group().split("=")[1]

    ## Hacer la POST request

    url2 = "https://escolarosaliadecastro.clickedu.eu/user.php?action=doLogin"
    cookies = { "cookiescheck": "true", "PHPSESSID": PHPSESSID }
    post_data = { "username": username, "password": password, "button": "Inicia" }

    r2 = requests.post(url2, cookies=cookies, data=post_data).text
    
    if(re.search(r"window.location.href='students/index.php';", r2)):
        return True
    else:
        return False

print(checker(str(sys.argv[1]), str(sys.argv[2])))

