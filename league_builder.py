if __name__ == "__main__":

    import csv

    Sharks = []
    Dragons = []
    Raptors = []
    players = {}

    # Makes CSV iterable and divides players into even teams
    def read(filename):
        skilled = []
        unskilled = []
        unshark = []
        undragon = []
        unraptor = []
    # Take info from soccer_players.csv and make iterable
        with open('soccer_players.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(csvfile)
            for row in reader:
                players[row[0]] = int(row[1]), row[2],row[3]
    # Divide players into experienced and inexperienced
        for key,value in players.items():
            if value[1] == 'YES':
                skilled.append(key)
            else:
                unskilled.append(key)
    # Evenly divides skilled players into teams
        Sharks.extend(skilled[:3])
        for player in Sharks:
            skilled.remove(player)
        Dragons.extend(skilled[:3])
        for player in Dragons:
            skilled.remove(player)
        Raptors.extend(skilled[:3])
    # Evenly divides unskilled players into teams
        unshark.extend(unskilled[:3])
        for player in unshark:
            unskilled.remove(player)
        undragon.extend(unskilled[:3])
        for player in undragon:
            unskilled.remove(player)
        unraptor.extend(unskilled[:3])
    #Adds unskilled teams to experienced teams
        Dragons.extend(undragon)
        Sharks.extend(unshark)
        Raptors.extend(unraptor)

    #Prints team names, members, experience, and guardians to teams.txt
    def print_txt(team):
        with open('teams.txt', 'a') as file:
            if team == Dragons:
                file.write("Dagons \n\n")
            elif team == Sharks:
                file.write("\n\nSharks\n\n")
            else:
                file.write("\n\nRaptors\n\n")
            for key,value in players.items():
                if key in team:
                    file.write(key + ' , ' + value[1] + ' , ' +  value[2] + '\n')

    read('soccer_players.csv')
    #omg it worked :D

    #Generates .txt files and prints welcome letters to them.
    def create_txt(*player):
        for key,value in players.items():
            current = key
            parent = value[2]
            mykey = key.replace(' ','_')
            mykey = mykey.lower()
            thefile = mykey.lower() + ".txt"
            with open(thefile, 'w') as file:
                if current in Dragons:
                    the_team = "Dragons"
                elif current in Sharks:
                    the_team = "Sharks"
                else:
                    the_team = "Raptors"
                file.write("Dear {},\n\nCongratulations. Yous son or daughter, {}, has been placed on the {} team. The first practice will be 4/25 at 4:00AM.\n\n".format(parent, current, the_team))
                file.close()

    create_txt(players)