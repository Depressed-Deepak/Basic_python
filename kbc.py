question = [
    ["Which 2 members of the Fellowship are cousins?","Aaragon & Elrond","Legolas & Gladerial","Gloen & Smeagol","Merry & Pippin",4],
    ["What is Gimli father name?","Aaragon","Legolas","Gloen","Galdalf",3],
    ["What creature is Golum?","Elf","Hobbit","Goblin","Orc",3],
    ['Where is Legolas from?','Isengard','Mirkwood','Edoras','Rivendell',2],
    ['What do the Elfs call Gandald?','Icanus','Mithrandir','Olorin','Tharkun',2],
    ['What\'s the name of Frodo\'s sword, given to him by Bilbo?','Orcrist','Anduril','Sting','Glamdring',3],
    ['What colour does Sting turn when Orcs are nearby?','Orange','Purple','Red','Blue',4]
]

levels = [
    1000,2000,3000,50000,10000,20000,400000
]


for i in range (0, len(question)):
    print(f"\n{question[i][0]}")
    print(f"a.{question[i][1]}       b.{question[i][2]}")
    print(f"c.{question[i][3]}       d.{question[i][4]}")
    selected = input('Select one option: ').strip().lower()
    if(selected == 'a' ):
        selected = 1
    elif(selected == 'b' ):
        selected = 2
    elif(selected == 'c' ):
        selected = 3
    elif(selected == 'd' ):
        selected = 4
    else:
        print('Select a valid option')
        break     
    
    if selected != question[i][5]:
        print('Incorrect answer')
        if i>0:
            print(f"Congraluation you have won {levels[i-1]}")
            break
        else:
            print(f"Sorry, Better luck next time")
            break
    else:
        print('Correct Answer')
        print(f"Congratulation, you have won {levels[i]}")