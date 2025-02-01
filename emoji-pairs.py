o = open("emoji-pairs.txt","w+")
f = open("emoji.txt","r")
for e in f:
    e = e.strip()
    try:
        o.write(f"{e} {chr(ord(e) ^ 0x20)}\n")
    except TypeError as err:
        if str(err)[0:49] != "ord() expected a character, but string of length ":
            raise TypeError(err)

collected = "🔦😀😂😭😎📺🦤🏇🫃"
for e in collected:
    print(f"{e} ↷ {chr(ord(e) ^ 0x20)}")
