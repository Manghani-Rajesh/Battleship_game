#################################################################################
# Problem: BattleShip Game
# Author: Rajesh Manghani
#################################################################################

import sys
class Battleship:
    def __init__(self, size_of_ships, number_of_battleship, missile_dimension1,
        missile_dimension2, firing_player1, firing_player2):
        self.size_of_ships = size_of_ships
        self.number_of_battleship = number_of_battleship
        self.missile_dimension1 = missile_dimension1
        self.missile_dimension2 = missile_dimension2
        self.firing_player1 = firing_player1
        self.firing_player2 = firing_player2
        self.ship_types = {'Q':2, 'P':1}
        self.ship_player1 = []
        self.ship_player2 =[]
        self.create_ship()
        self.firing_positions_p1 = self.get_firing_positions(self.firing_player1)
        self.firing_positions_p2 = self.get_firing_positions(self.firing_player2) 
        self.fire_player1()     
    
    #This method will use for setting up the ship
    def create_ship(self,):
            list_ships = self.size_of_ships.strip().split(' ')
            if len(list_ships)==2 and list_ships[1].isalpha():
                x_coordinate =  int(list_ships[0])
                y_coordinate =  self.convert_to_ascii(list_ships[1])
                self.ship_player1 = [[0 for x_c in range(x_coordinate)] for y_c in range(y_coordinate)]
                self.ship_player2 = [[0 for x_c in range(x_coordinate)] for y_c in range(y_coordinate)]
                self.set_missile(self.missile_dimension1)
                self.set_missile(self.missile_dimension2)
            else:
                print 'please check input of size ships ',self.size_of_ships
                exit()

    #This method will use for converting ascii value to character
    def convert_to_char(self, ascii):
        return chr(65+ascii)
        
    #This method will use for converting character to ascii value
    def convert_to_ascii(self, char):
        return ord(char) - 64
    
    #This will get the players attacking position   
    def get_firing_positions(self, firing_player):
            firing_player = firing_player.strip().split()
            firing_positions = []
            for positions in firing_player:
                if positions[0].isalpha():
                    x,y = self.convert_to_ascii(positions[0]) - 1, int(positions[1]) - 1
                    firing_positions.append([x,y])
                else:
                    print 'please check input of firing position of ',firing_player
                    exit()
            return firing_positions

    #set the missile for each player
    def set_missile(self, missile_dimension1):
        missile_dimension = missile_dimension1.strip().split(' ')
        type_of_ship = missile_dimension[0]
        width_of_ship = int(missile_dimension[1])
        height_of_ship = int(missile_dimension[2])
        p1_dimension = missile_dimension[3]
        p2_dimension = missile_dimension[4]
        if p1_dimension[0].isalpha() and p2_dimension[0].isalpha():
            p1_dimension_h, p1_dimension_w = self.convert_to_ascii(p1_dimension[0])-2, int(p1_dimension[1]) - 2
            p2_dimension_h, p2_dimension_w = self.convert_to_ascii(p2_dimension[0])-2, int(p2_dimension[1]) - 2
            for height in range(height_of_ship):
                p1_dimension_h = p1_dimension_h + 1
                p2_dimension_h = p2_dimension_h + 1
                for width in range(width_of_ship):
                    p1_dimension_w = p1_dimension_w + 1
                    p2_dimension_w = p2_dimension_w + 1
                    self.ship_player1[p1_dimension_h][p1_dimension_w] = self.ship_types[type_of_ship]
                    self.ship_player2[p2_dimension_h][p2_dimension_w] = self.ship_types[type_of_ship]
        else:
            print 'please check input of dimension ',missile_dimension1
            exit()

    #this will missile fire by player 1
    def fire_player1(self,):
        if self.firing_positions_p1:
            x,y = self.firing_positions_p1[0]
            if self.ship_player2[x][y] != 0:
                self.ship_player2[x][y] = self.ship_player2[x][y] - 1
                self.firing_positions_p1.pop(0)
                print 'Player-1 fires a missile with target '+self.convert_to_char(x)+str(y+1)+' which got hit'
                if all(all(item == 0 for item in items) for items in self.ship_player2):
                    print 'Player-1 won the battle'
                    return
                self.fire_player1()
            else:
                self.firing_positions_p1.pop(0)
                print 'Player-1 fires a missile with target '+self.convert_to_char(x)+str(y+1)+' which got miss'
                self.fire_player2()
        else:
            print 'Player-1 has no more missiles left to launch'
            self.fire_player2()

    #This will missile fire by player 2
    def fire_player2(self,):
        if self.firing_positions_p1 or self.firing_positions_p2:
            if self.firing_positions_p2:
                x,y = self.firing_positions_p2[0]
                if self.ship_player1[x][y] != 0:
                    self.ship_player1[x][y] = self.ship_player1[x][y] - 1
                    self.firing_positions_p2.pop(0)
                    print 'Player-2 fires a missile with target '+self.convert_to_char(x)+str(y+1)+' which got hit'
                    if all(all(item == 0 for item in items) for items in self.ship_player1):
                        print 'Player-2 won the battle'
                        return
                    self.fire_player2()
                else:
                    self.firing_positions_p2.pop(0)
                    print 'Player-2 fires a missile with target '+self.convert_to_char(x)+str(y+1)+' which got miss'
                    self.fire_player1()
            else:
                print 'Player-2 has no more missiles left to launch'
                self.fire_player1()
        else:
            print 'Game has drawn'
def main():
    #get input from sample.txt file.
    if len(sys.argv) < 2:
        print 'please provide input file'
        return
    file_name = sys.argv[1]
    with open(file_name) as sample_file:
        input_data = sample_file.readlines()
    try:
        size_of_ships = input_data[0]
        number_of_battleship = input_data[1]
        missile_dimension1 = input_data[2]
        missile_dimension2 = input_data[3]
        firing_player1 = input_data[4]
        firing_player2 = input_data[5]
    except:
        print 'Input should have 6 lines ',len(input_data), 'Given'
        return
    Battleship(size_of_ships, number_of_battleship, missile_dimension1, 
        missile_dimension2, firing_player1, firing_player2)

if __name__ == '__main__':
    main()