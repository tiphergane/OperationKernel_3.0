#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import binascii
import hashlib
import json
import random

sbox = [225, 215, 45, 11, 70, 238, 109, 46, 159, 235, 57, 173, 90, 53, 85, 114, 245, 40, 78, 2, 71, 229, 199, 201, 58, 42, 177, 76, 210, 246, 12, 27, 26, 208, 243, 73, 92, 200, 206, 102, 217, 207, 17, 14, 147, 101, 170, 32, 10, 255, 80, 82, 24, 61, 95, 43, 124, 122, 216, 115, 205, 218, 75, 227, 239, 175, 152, 113, 74, 224, 248, 194, 97, 155, 91, 125, 249, 3, 25, 51, 103, 213, 204, 104, 63, 244, 145, 44, 160, 106, 21, 94, 222, 48, 121, 165, 171, 202, 31, 203, 29, 230, 156, 240, 168, 34, 129, 182, 234, 185, 241, 123, 33, 163, 15, 9, 0, 99, 7, 178, 49, 186, 154, 126, 148, 141, 130, 250,
        67, 41, 232, 195, 52, 56, 118, 105, 22, 242, 184, 226, 64, 254, 162, 191, 66, 138, 20, 132, 72, 39, 221, 146, 161, 237, 86, 153, 166, 5, 120, 54, 81, 38, 77, 47, 19, 189, 4, 36, 128, 50, 111, 180, 1, 140, 13, 149, 172, 107, 181, 100, 169, 187, 83, 117, 192, 143, 139, 197, 190, 219, 136, 212, 251, 228, 231, 62, 179, 8, 60, 79, 84, 211, 144, 18, 188, 89, 35, 28, 158, 96, 30, 174, 151, 23, 112, 116, 87, 253, 127, 65, 133, 236, 220, 247, 252, 157, 55, 193, 209, 137, 196, 164, 233, 167, 16, 134, 69, 59, 98, 68, 135, 198, 223, 88, 150, 6, 142, 93, 131, 119, 108, 214, 176, 110, 183, 37]
pbox = [2, 5, 7, 4, 1, 0, 3, 6]


class Encryptor(object):
    def __init__(self, passphrase):
        self.key = passphrase.encode()

    def generateKey(self, passphrase):
        self.key = hashlib.sha256(bytes(passphrase)).digest()[:6]
        return self.key

    def xor(self, a, b):
        res = []
        #print("a ",a)
        #print("b ",b)
        for ac, bc in zip(a, b):
            #print("zip =",zip(a, b))
            #print("ac =", ac)
            #print("bc =", bc)
            res.append(ac ^ bc)
            #print("res ",res)
        #print("res final ",res)
        return res

    def encryptBlock(self, block, passListLine):
        passListLine = str(passListLine)
        passListLine = passListLine.encode()
        key = list(self.generateKey(passListLine[:-1]))
        l = list(block[:8])
        r = list(block[8:])
        for iround in range(6):
            keybyte = key.pop()
            for isubround in range(4):
                f = []
                for i in range(8):
                    f.append(sbox[l[i] ^ keybyte])
                    keybyte = (keybyte + 1) % 256
                f = [f[pbox[i]] for i in range(8)]
                l, r = self.xor(r, f), l

        return bytes(l+r)

    def decrypt(self, ciphertext, passphrase):
        ctr = 0xD84230190F7E28377D72291D3E396A2A

        print("La valeur initiale ctr équivaut à: ", ctr)

        rockyou = open("/opt/SecLists/Passwords/rockyou.txt", 'rb')

        i = 0
        notFind = True
        while notFind:
            rockyouline = rockyou.readline()

            try:
                rockyouline = rockyouline.decode()
            except:
                pass

            encryptedBlock = self.encryptBlock(
                ctr.to_bytes(16, 'big'), rockyouline)
            encryptedLine = bytes(self.xor(ciphertext, encryptedBlock)).hex()

            if str(encryptedLine)[:8] == "504b0304":
                print(encryptedLine)
                notFind = False
                print(i, rockyouline)
            else:
                # print(i)
                i += 1
                if i == 14344395:
                    break


ciphertext = open("./original_CONFIDENTIEL.xslx.enc", 'rb')
ctr = ciphertext.read(16)
finalCipertext = ciphertext.read(16)
Encryptor("").decrypt(finalCipertext, "")
