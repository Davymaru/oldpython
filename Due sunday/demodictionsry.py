def main():
    emoji={"Snake":"🐍", "gator":"🐊","fish":"🐠", "bird":"🦜", "Guitar":"🎸"}


    print(emoji)
    print(emoji["Snake"])
    animal = emoji.get("gator")
    print(animal)


    print(emoji.keys())




    print('/n/n')
    print(emoji.values())

    print('\n\n')
    print(emoji.items())

    if "Guitar" in emoji:
        print(emoji["Guitar"])

    emoji["Guitar"] ="🪕"
    print(emoji)

    
    emoji.update({"bird": "🐧"})

    emoji.pop("fish")
    print(emoji)

    del emoji["bird"]
    print(emoji)

    for x in emoji:
        print(x)

main()
