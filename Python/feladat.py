import random
vege = False
while not vege:
    print("\n--- Számkitalálós Játék ---")
    print("1. FreePlay")
    print("2. Level 1")
    print("3. Level 2")
    print("4. Level 3")
    print("5. Kilépés")
    valasztas = input("Válassz egy opciot (1,2,3,4 és 5): ")

    if valasztas == "1":
        freeplay = random.randint(1,100)
        gameon = True
        ossztipp = 0
        while gameon:
            ok = True
            while ok:
                tipp = input("Add meg a tipped a számhoz 1 és 100 között: ")
                if not tipp.isdigit():
                    print("Nem számot adtál meg!")
                else:
                    jotipp = (int)(tipp)
                    if jotipp > 100 or jotipp < 1:
                        print("Nem a jó intervallumban adtál meg adatot!")
                    else:
                        ok = False
            if freeplay > jotipp:
                print("Nagyobb számra gondoltam!")
                ossztipp += 1
                print()
            elif freeplay < jotipp:
                print("Kisebb számra gondoltam!")
                ossztipp += 1
                print()
            else:
                ossztipp += 1
                print(f"Gratulálok eltaláltad!! És összesen ez {ossztipp} probálkozásból sikerült ! ! !")
                gameon = False
    
    elif valasztas == "2":
        level1 = random.randint(1,10)
        tippek = 3
        gameon = True
        while gameon:
            if tippek == 0:
                print("Sajnálom elfogyott a tipp")
                gameon = False
            else:
                print(f"{tippek} Tipped maradt")
                ok = True
                while ok:
                    tipp = input("Add meg a tipped a számhoz 1 és 10 között: ")
                    if not tipp.isdigit():
                        print("Nem számot adtál meg!")
                    else:
                        jotipp = (int)(tipp)
                        if jotipp > 10 or jotipp < 1:
                            print("Nem a jó intervallumban adtál meg adatot!")
                        else:
                            ok = False
                if level1 > jotipp:
                    print("Nagyobb számra gondoltam!")
                    tippek = tippek - 1
                    print()
                elif level1 < jotipp:
                    print("Kisebb számra gondoltam!")
                    tippek = tippek - 1
                    print()
                else:
                    print()
                    tippek = tippek - 1
                    print(f"Gratulálok eltaláltad!! És {tippek} Tipped maradt")
                    gameon = False

    elif valasztas == "3":
        level2 = random.randint(30,50)
        tippek = 5
        gameon = True
        while gameon:
            if tippek == 0:
                print("Sajnálom elfogyott a tipp")
                gameon = False
            else:
                print(f"{tippek} Tipped maradt")
                ok = True
                while ok:
                    tipp = input("Add meg a tipped a számhoz 30 és 50 között: ")
                    if not tipp.isdigit():
                        print("Nem számot adtál meg!")
                    else:
                        jotipp = (int)(tipp)
                        if jotipp > 50 or jotipp < 30:
                            print("Nem a jó intervallumban adtál meg adatot!")
                        else:
                            ok = False
                if level2 > jotipp:
                    print("Nagyobb számra gondoltam!")
                    tippek = tippek - 1
                    print()
                elif level2 < jotipp:
                    print("Kisebb számra gondoltam!")
                    tippek = tippek - 1
                    print()
                else:
                    print()
                    tippek = tippek - 1
                    print(f"Gratulálok eltaláltad!! És {tippek} Tipped maradt")
                    gameon = False

    elif valasztas == "4":
        level3 = random.randint(1,100)
        tippek = 8
        gameon = True
        while gameon:
            if tippek == 0:
                print("Sajnálom elfogyott a tipp")
                gameon = False
            else:
                print(f"{tippek} Tipped maradt")
                ok = True
                while ok:
                    tipp = input("Add meg a tipped a számhoz 1 és 10 között: ")
                    if not tipp.isdigit():
                        print("Nem számot adtál meg!")
                    else:
                        jotipp = (int)(tipp)
                        if jotipp > 100 or jotipp < 1:
                            print("Nem a jó intervallumban adtál meg adatot!")
                        else:
                            ok = False
                if level3 > jotipp:
                    print("Nagyobb számra gondoltam!")
                    tippek = tippek - 1
                    print()
                elif level3 < jotipp:
                    print("Kisebb számra gondoltam!")
                    tippek = tippek - 1
                    print()
                else:
                    print()
                    tippek = tippek - 1
                    print(f"Gratulálok eltaláltad!! És {tippek} Tipped maradt")
                    gameon = False

    elif valasztas == "5":
        print()
        print("Kilépés...")
        vege = True

    else:
        print("Nem jól adtad meg az adatot!")