import random
import time
DISTANCE = 20
RACERS = 5
players = [DISTANCE for x in range(RACERS)]
clearConsole = lambda: print('\n' * 50)

def main():
    fin = []
    while(not all(x == 0 for x in players)):
        clearConsole()
        for i in range(len(players)):
            if(random.randint(0,3)== 0 and players[i]>0):
                players[i]-=1
                if players[i] == 0:
                    fin.append(i)

        for i in range(len(fin)):
            print(f"Player {fin[i]+1} has finished")


        for i in range(len(players)):
            print(str(i+1)+"-"*(DISTANCE-players[i])+" "*(players[i])+"|")
        print()
        time.sleep(0.5)

if __name__ == "__main__":
    main()