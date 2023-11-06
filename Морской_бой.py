import sys
from random import randint

# Класс для распределения кораблей
class Ship:
    def __init__(self,field,choose_position):
        self.ship = "■"
        self.field = field
        self.position = choose_position
    def getship(self):
        if self.position=="11" or self.position=="21" or self.position=="31" or self.position=="41" or self.position=="51" or self.position=="61":
            self.field = self.field[:4]+self.ship+self.field[5:]
            return self.field
        elif self.position=="12" or self.position=="22" or self.position=="32" or self.position=="42" or self.position=="52" or self.position=="62":
            self.field = self.field[:8]+self.ship+self.field[9:]
            return self.field
        elif self.position=="13" or self.position=="23" or self.position=="33" or self.position=="43" or self.position=="53" or self.position=="63":
            self.field = self.field[:12]+self.ship+self.field[13:]
            return self.field
        elif self.position=="14" or self.position=="24" or self.position=="34" or self.position=="44" or self.position=="54" or self.position=="64":
            self.field = self.field[:16]+self.ship+self.field[17:]
            return self.field
        elif self.position=="15" or self.position=="25" or self.position=="35" or self.position=="45" or self.position=="55" or self.position=="65":
            self.field = self.field[:20]+self.ship+self.field[21:]
            return self.field
        elif self.position=="16" or self.position=="26" or self.position=="36" or self.position=="46" or self.position=="56" or self.position=="66":
            self.field = self.field[:24]+self.ship+self.field[25:]
            return self.field

# Класс для игрока
class Player:
    def __init__(self,desk,list_1):
        self.desk = desk
        self.list = list_1
    def getpositions(self):
        self.desk_1 = positions_of_user(self.desk, self.list)
        return self.desk_1

# Класс для AI
class AI:
    def __init__(self,desk,list_1):
        self.desk = desk
        self.list = list_1
    def getpositions(self):
        self.desk_1 = positions_of_AI(self.desk, self.list)
        return self.desk_1

# Класс для начала игры
class start_game:
    def __init__(self,field_of_user,field_of_AI):
        self.field_of_user = field_of_user
        self.field_of_AI = field_of_AI
        self.list_user = ["11", "12", "13", "14", "15", "16", "21", "22", "23", "24", "25", "26", "31", "32", "33", "34",
                     "35", "36", "41", "42", "43", "44", "45", "46", "51", "52", "53", "54", "55", "56", "61", "62",
                     "63", "64", "65", "66"]
        self.list_AI = ["11", "12", "13", "14", "15", "16", "21", "22", "23", "24", "25", "26", "31", "32", "33", "34",
                     "35", "36", "41", "42", "43", "44", "45", "46", "51", "52", "53", "54", "55", "56", "61", "62",
                     "63", "64", "65", "66"]
        self.field_AI_without_positions = [["  | 1 | 2 | 3 | 4 | 5 | 6 |"],
["1 | О | О | О | О | О | О |"],
["2 | О | О | О | О | О | О |"],
["3 | О | О | О | О | О | О |"],
["4 | О | О | О | О | О | О |"],
["5 | О | О | О | О | О | О |"],
["6 | О | О | О | О | О | О |"]]
    def beginning_user(self):
        print("Ходит пользователь!")
        for _ in self.field_AI_without_positions:
            print(*_)
        while True:
            winner = 0
            try:
                self.pos = input(f"Введите позицию: ")
                if self.pos not in self.list_user:
                    raise IndexError("")
            except IndexError:
                print("Эта позиция находится вне координат или уже была!")
                continue
            else:
                self.list_user.remove(self.pos)
                if self.pos[0] == "1":
                    unhappy_player = Game(self.pos,*self.field_of_AI[1])
                    result = unhappy_player.check_ship()
                    self.field_of_AI[1] = [result]
                    if "■" in result:
                        self.field_AI_without_positions[1] = [result.replace("■","O")]
                    else:
                        self.field_AI_without_positions[1] = [result]

                    if self.pos in list_distance_of_AI[0]:
                         print("Корабль уничтожен!")
                         for i_1 in self.field_AI_without_positions:
                            print(*i_1)
                         list_distance_of_AI[0].remove(self.pos)
                    elif self.pos in list_distance_of_AI[1]:
                        list_distance_of_AI[1].remove(self.pos)
                        if list_distance_of_AI[1] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_AI[2]:
                        list_distance_of_AI[2].remove(self.pos)
                        if list_distance_of_AI[2] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_AI[3]:
                        list_distance_of_AI[3].remove(self.pos)
                        if list_distance_of_AI[3] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    else:
                        print("Промах!")
                        for i_1 in self.field_AI_without_positions:
                            print(*i_1)

                    for i_11 in self.field_of_AI:
                        i_str = i_11[0]
                        if "■" not in i_str:
                            winner+=1
                            if winner==7:
                                print("Пользователь победил!")
                                sys.exit()
                    self.continue_AI()
                elif self.pos[0] == "2":
                    unhappy_player = Game(self.pos, *self.field_of_AI[2])
                    result = unhappy_player.check_ship()
                    self.field_of_AI[2] = [result]
                    if "■" in result:
                        self.field_AI_without_positions[2] = [result.replace("■","O")]
                    else:
                        self.field_AI_without_positions[2] = [result]
                    if self.pos in list_distance_of_AI[0]:
                        print("Корабль уничтожен!")
                        for i_1 in self.field_AI_without_positions:
                            print(*i_1)
                        list_distance_of_AI[0].remove(self.pos)
                    elif self.pos in list_distance_of_AI[1]:
                        list_distance_of_AI[1].remove(self.pos)
                        if list_distance_of_AI[1] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_AI[2]:
                        list_distance_of_AI[2].remove(self.pos)
                        if list_distance_of_AI[2] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_AI[3]:
                        list_distance_of_AI[3].remove(self.pos)
                        if list_distance_of_AI[3] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    else:
                        print("Промах!")
                        for i_1 in self.field_AI_without_positions:
                            print(*i_1)

                    for i_21 in self.field_of_AI:
                        i_str = i_21[0]
                        if "■" not in i_str:
                            winner+=1
                            if winner==7:
                                print("Пользователь победил!")
                                sys.exit()
                    self.continue_AI()

                elif self.pos[0] == "3":
                    unhappy_player = Game(self.pos, *self.field_of_AI[3])
                    result = unhappy_player.check_ship()
                    self.field_of_AI[3] = [result]
                    if "■" in result:
                        self.field_AI_without_positions[3] = [result.replace("■","O")]
                    else:
                        self.field_AI_without_positions[3] = [result]
                    if self.pos in list_distance_of_AI[0]:
                        print("Корабль уничтожен!")
                        for i_1 in self.field_AI_without_positions:
                            print(*i_1)
                        list_distance_of_AI[0].remove(self.pos)
                    elif self.pos in list_distance_of_AI[1]:
                        list_distance_of_AI[1].remove(self.pos)
                        if list_distance_of_AI[1] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_AI[2]:
                        list_distance_of_AI[2].remove(self.pos)
                        if list_distance_of_AI[2] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_AI[3]:
                        list_distance_of_AI[3].remove(self.pos)
                        if list_distance_of_AI[3] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    else:
                        print("Промах!")
                        for i_1 in self.field_AI_without_positions:
                            print(*i_1)

                    for i_31 in self.field_of_AI:
                        i_str = i_31[0]
                        if "■" not in i_str:
                            winner+=1
                            if winner==7:
                                print("Пользователь победил!")
                                sys.exit()
                    self.continue_AI()
                elif self.pos[0] == "4":
                    unhappy_player = Game(self.pos,*self.field_of_AI[4])
                    result = unhappy_player.check_ship()
                    self.field_of_AI[4] = [result]
                    if "■" in result:
                        self.field_AI_without_positions[4] = [result.replace("■","O")]
                    else:
                        self.field_AI_without_positions[4] = [result]
                    if self.pos in list_distance_of_AI[0]:
                        print("Корабль уничтожен!")
                        for i_1 in self.field_AI_without_positions:
                            print(*i_1)
                        list_distance_of_AI[0].remove(self.pos)
                    elif self.pos in list_distance_of_AI[1]:
                        list_distance_of_AI[1].remove(self.pos)
                        if list_distance_of_AI[1] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_AI[2]:
                        list_distance_of_AI[2].remove(self.pos)
                        if list_distance_of_AI[2] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_AI[3]:
                        list_distance_of_AI[3].remove(self.pos)
                        if list_distance_of_AI[3] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    else:
                        print("Промах!")
                        for i_1 in self.field_AI_without_positions:
                            print(*i_1)

                    for i_41 in self.field_of_AI:
                        i_str = i_41[0]
                        if "■" not in i_str:
                            winner+=1
                            if winner==7:
                                print("Пользователь победил!")
                                sys.exit()
                    self.continue_AI()
                elif self.pos[0] == "5":
                    unhappy_player = Game(self.pos, *self.field_of_AI[5])
                    result = unhappy_player.check_ship()
                    self.field_of_AI[5] = [result]
                    if "■" in result:
                        self.field_AI_without_positions[5] = [result.replace("■","O")]
                    else:
                        self.field_AI_without_positions[5] = [result]
                    if self.pos in list_distance_of_AI[0]:
                        print("Корабль уничтожен!")
                        for i_1 in self.field_AI_without_positions:
                            print(*i_1)
                        list_distance_of_AI[0].remove(self.pos)
                    elif self.pos in list_distance_of_AI[1]:
                        list_distance_of_AI[1].remove(self.pos)
                        if list_distance_of_AI[1] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_AI[2]:
                        list_distance_of_AI[2].remove(self.pos)
                        if list_distance_of_AI[2] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_AI[3]:
                        list_distance_of_AI[3].remove(self.pos)
                        if list_distance_of_AI[3] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    else:
                        print("Промах!")
                        for i_1 in self.field_AI_without_positions:
                            print(*i_1)

                    for i_51 in self.field_of_AI:
                        i_str = i_51[0]
                        if "■" not in i_str:
                            winner+=1
                            if winner==7:
                                print("Пользователь победил!")
                                sys.exit()
                    self.continue_AI()
                elif self.pos[0] == "6":
                    unhappy_player = Game(self.pos, *self.field_of_AI[6])
                    result = unhappy_player.check_ship()
                    self.field_of_AI[6] = [result]
                    if "■" in result:
                        self.field_AI_without_positions[6] = [result.replace("■","O")]
                    else:
                        self.field_AI_without_positions[6] = [result]
                    if self.pos in list_distance_of_AI[0]:
                        print("Корабль уничтожен!")
                        for i_1 in self.field_AI_without_positions:
                            print(*i_1)
                        list_distance_of_AI[0].remove(self.pos)
                    elif self.pos in list_distance_of_AI[1]:
                        list_distance_of_AI[1].remove(self.pos)
                        if list_distance_of_AI[1] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_AI[2]:
                        list_distance_of_AI[2].remove(self.pos)
                        if list_distance_of_AI[2] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_AI[3]:
                        list_distance_of_AI[3].remove(self.pos)
                        if list_distance_of_AI[3] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_AI_without_positions:
                                print(*i_1)
                            continue
                    else:
                        print("Промах!")
                        for i_1 in self.field_AI_without_positions:
                            print(*i_1)

                    for i_61 in self.field_of_AI:
                        i_str = i_61[0]
                        if "■" not in i_str:
                            winner+=1
                            if winner==7:
                                print("Пользователь победил!")
                                sys.exit()
                    self.continue_AI()

    def continue_AI(self):
        print("Ходит компьютер!")
        while True:
            winner = 0
            try:
                self.pos = self.list_AI[randint(0,len(self.list_AI)-1)]
                if self.pos not in self.list_AI:
                    raise IndexError("")
            except IndexError:
                print("Эта позиция находится вне координат или уже была!")
                continue
            else:
                self.list_AI.remove(self.pos)
                if self.pos[0] == "1":
                    unhappy_AI = Game(self.pos,*self.field_of_user[1])
                    result = unhappy_AI.check_ship()
                    self.field_of_user[1] = [result]

                    if self.pos in list_distance_of_user[0]:
                        print("Корабль уничтожен!")
                        for i_1 in self.field_of_user:
                            print(*i_1)
                        list_distance_of_user[0].remove(self.pos)
                    elif self.pos in list_distance_of_user[1]:
                        list_distance_of_user[1].remove(self.pos)
                        if list_distance_of_user[1] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_user[2]:
                        list_distance_of_user[2].remove(self.pos)
                        if list_distance_of_user[2] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_user[3]:
                        list_distance_of_user[3].remove(self.pos)
                        if list_distance_of_user[3] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    else:
                        print("Промах!")
                        for i_1 in self.field_of_user:
                            print(*i_1)

                    for i_11 in self.field_of_user:
                        i_str = i_11[0]
                        if "■" not in i_str:
                            winner+=1
                            if winner==7:
                                print("ИИ победил!")
                                sys.exit()
                    self.beginning_user()

                elif self.pos[0] == "2":
                    unhappy_AI = Game(self.pos, *self.field_of_user[2])
                    result = unhappy_AI.check_ship()
                    self.field_of_user[2] = [result]

                    if self.pos in list_distance_of_user[0]:
                        print("Корабль уничтожен!")
                        for i_1 in self.field_of_user:
                            print(*i_1)
                        list_distance_of_user[0].remove(self.pos)
                    elif self.pos in list_distance_of_user[1]:
                        list_distance_of_user[1].remove(self.pos)
                        if list_distance_of_user[1] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_user[2]:
                        list_distance_of_user[2].remove(self.pos)
                        if list_distance_of_user[2] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_user[3]:
                        list_distance_of_user[3].remove(self.pos)
                        if list_distance_of_user[3] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    else:
                        print("Промах!")
                        for i_1 in self.field_of_user:
                            print(*i_1)

                    for i_21 in self.field_of_user:
                        i_str = i_21[0]
                        if "■" not in i_str:
                            winner += 1
                            if winner == 7:
                                print("ИИ победил!")
                                sys.exit()
                    self.beginning_user()
                elif self.pos[0] == "3":
                    unhappy_AI = Game(self.pos, *self.field_of_user[3])
                    result = unhappy_AI.check_ship()
                    self.field_of_user[3] = [result]

                    if self.pos in list_distance_of_user[0]:
                        print("Корабль уничтожен!")
                        for i_1 in self.field_of_user:
                            print(*i_1)
                        list_distance_of_user[0].remove(self.pos)
                    elif self.pos in list_distance_of_user[1]:
                        list_distance_of_user[1].remove(self.pos)
                        if list_distance_of_user[1] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_user[2]:
                        list_distance_of_user[2].remove(self.pos)
                        if list_distance_of_user[2] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_user[3]:
                        list_distance_of_user[3].remove(self.pos)
                        if list_distance_of_user[3] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    else:
                        print("Промах!")
                        for i_1 in self.field_of_user:
                            print(*i_1)

                    for i_31 in self.field_of_user:
                        i_str = i_31[0]
                        if "■" not in i_str:
                            winner += 1
                            if winner == 7:
                                print("ИИ победил!")
                                sys.exit()
                    self.beginning_user()
                elif self.pos[0] == "4":
                    unhappy_AI = Game(self.pos,*self.field_of_user[4])
                    result = unhappy_AI.check_ship()
                    self.field_of_user[4] = [result]

                    if self.pos in list_distance_of_user[0]:
                        print("Корабль уничтожен!")
                        for i_1 in self.field_of_user:
                            print(*i_1)
                        list_distance_of_user[0].remove(self.pos)
                    elif self.pos in list_distance_of_user[1]:
                        list_distance_of_user[1].remove(self.pos)
                        if list_distance_of_user[1] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_user[2]:
                        list_distance_of_user[2].remove(self.pos)
                        if list_distance_of_user[2] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_user[3]:
                        list_distance_of_user[3].remove(self.pos)
                        if list_distance_of_user[3] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    else:
                        print("Промах!")
                        for i_1 in self.field_of_user:
                            print(*i_1)

                    for i_41 in self.field_of_user:
                        i_str = i_41[0]
                        if "■" not in i_str:
                            winner += 1
                            if winner == 7:
                                print("ИИ победил! ")
                                sys.exit()
                    self.beginning_user()
                elif self.pos[0] == "5":
                    unhappy_AI = Game(self.pos, *self.field_of_user[5])
                    result = unhappy_AI.check_ship()
                    self.field_of_user[5] = [result]

                    if self.pos in list_distance_of_user[0]:
                        print("Корабль уничтожен!")
                        for i_1 in self.field_of_user:
                            print(*i_1)
                        list_distance_of_user[0].remove(self.pos)
                    elif self.pos in list_distance_of_user[1]:
                        list_distance_of_user[1].remove(self.pos)
                        if list_distance_of_user[1] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_user[2]:
                        list_distance_of_user[2].remove(self.pos)
                        if list_distance_of_user[2] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_user[3]:
                        list_distance_of_user[3].remove(self.pos)
                        if list_distance_of_user[3] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    else:
                        print("Промах!")
                        for i_1 in self.field_of_user:
                            print(*i_1)
                    for i_51 in self.field_of_user:
                        i_str = i_51[0]
                        if "■" not in i_str:
                            winner += 1
                            if winner == 7:
                                print("ИИ победил!")
                                sys.exit()
                    self.beginning_user()
                elif self.pos[0] == "6":
                    unhappy_AI = Game(self.pos, *self.field_of_user[6])
                    result = unhappy_AI.check_ship()
                    self.field_of_user[6] = [result]


                    if self.pos in list_distance_of_user[0]:
                        print("Корабль уничтожен!")
                        for i_1 in self.field_of_user:
                            print(*i_1)
                        list_distance_of_user[0].remove(self.pos)
                    elif self.pos in list_distance_of_user[1]:
                        list_distance_of_user[1].remove(self.pos)
                        if list_distance_of_user[1] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_user[2]:
                        list_distance_of_user[2].remove(self.pos)
                        if list_distance_of_user[2] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    elif self.pos in list_distance_of_user[3]:
                        list_distance_of_user[3].remove(self.pos)
                        if list_distance_of_user[3] == []:
                            print("Корабль уничтожен!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                        else:
                            print("Корабль повреждён!")
                            for i_1 in self.field_of_user:
                                print(*i_1)
                            continue
                    else:
                        print("Промах!")
                        for i_1 in self.field_of_user:
                            print(*i_1)

                    for i_61 in self.field_of_user:
                        i_str = i_61[0]
                        if "■" not in i_str:
                            winner += 1
                            if winner == 7:
                                print("ИИ победил!")
                                sys.exit()
                    self.beginning_user()

# Процесс игры
class Game:
    def __init__(self,pos,field):
        self.position = pos
        self.field = field
    def check_ship(self):
        if self.position == "11" or self.position == "21" or self.position == "31" or self.position == "41" or self.position == "51" or self.position == "61":
            self.position = self.field[4]
            self.position = self.Hitmark(self.position)
            self.field = self.field[:4]+self.position+self.field[5:]
            return self.field
        elif self.position == "12" or self.position == "22" or self.position == "32" or self.position == "42" or self.position == "52" or self.position == "62":
            self.position = self.field[8]
            self.position = self.Hitmark(self.position)
            self.field = self.field[:8] + self.position + self.field[9:]
            return self.field
        elif self.position == "13" or self.position == "23" or self.position == "33" or self.position == "43" or self.position == "53" or self.position == "63":
            self.position = self.field[12]
            self.position = self.Hitmark(self.position)
            self.field = self.field[:12] + self.position + self.field[13:]
            return self.field
        elif self.position == "14" or self.position == "24" or self.position == "34" or self.position == "44" or self.position == "54" or self.position == "64":
            self.position = self.field[16]
            self.position = self.Hitmark(self.position)
            self.field = self.field[:16] + self.position + self.field[17:]
            return self.field
        elif self.position == "15" or self.position == "25" or self.position == "35" or self.position == "45" or self.position == "55" or self.position == "65":
            self.position = self.field[20]
            self.position = self.Hitmark(self.position)
            self.field = self.field[:20] + self.position + self.field[21:]
            return self.field
        elif self.position == "16" or self.position == "26" or self.position == "36" or self.position == "46" or self.position == "56" or self.position == "66":
            self.position = self.field[24]
            self.position = self.Hitmark(self.position)
            self.field = self.field[:24] + self.position + self.field[25:]
            return self.field
    def Hitmark(self,pos):
        self.pos = pos
        if self.pos == "■":
            self.pos = "X"
            return self.pos
        else:
            self.pos = "T"
            return self.pos

# Функция для проверки кораблей размером в 2/3 клетки
def is_adjacent(positions):
    # Преобразуем строковые позиции в числовые координаты
    coords = [(int(pos[0]), int(pos[1])) for pos in positions]
    # Сортируем координаты по x, а затем по y
    coords.sort(key=lambda x: (x[0], x[1]))
    # Проверяем горизонтальное расположение
    horizontal = all(coords[i][0] == coords[i + 1][0] and coords[i][1] + 1 == coords[i + 1][1] for i in range(len(coords) - 1))
    # Проверяем вертикальное расположение
    vertical = all(coords[i][0] + 1 == coords[i + 1][0] and coords[i][1] == coords[i + 1][1] for i in range(len(coords) - 1))
    return horizontal or vertical

# Функции для проверки дистанции кораблей
def are_positions_distance_apart(pos1, pos2):
    row1, col1 = int(pos1[0]), int(pos1[1])
    row2, col2 = int(pos2[0]), int(pos2[1])

    row_diff = abs(row1 - row2)
    col_diff = abs(col1 - col2)

    # Если они находятся в одной и той же позиции или рядом
    if (row_diff <= 1 and col_diff <= 1):
        return False
    return True
def are_ships_distance_apart(ship_positions):
    for i in range(len(ship_positions)):
        for j in range(i+1, len(ship_positions)):
            if not are_positions_distance_apart(ship_positions[i], ship_positions[j]):
                return False
    return True


def positions_of_user(Desk, list_of_positions):
    # Поле
    Field = Desk

    # Список
    list_1 = list_of_positions

    # Отображение поля
    for i in Field:
        print(*i)

    # Переменная, в которой будет храниться список с проверяемыми позициями
    check_list = []

    # Переменная для остановки цикла (корабли размером в одну клетку)
    l = 0

    # Цикл с размещением кораблей размером в одну клетку
    while l < 4:
        choose_position = input(f"Выберите позицию для корабля на одну клетку{list_1}: ")
        if choose_position in list_1:

            # Размещение клетки
            if choose_position == "11" or choose_position == "12" or choose_position == "13" or choose_position == "14" or choose_position == "15" or choose_position == "16":
                check_list.append(choose_position)
                if l==0:
                    list_distance_of_user[0].append(choose_position)
                if len(check_list) >= 2:
                    distance = are_ships_distance_apart(check_list)
                    if not distance:
                        check_list.pop(-1)
                        print("Ошибка! Корабли должны находиться друг от друга на расстоянии минимум одной клетки!")
                        continue
                    else:
                        list_distance_of_user[0].append(choose_position)
                for k_1 in Field[1]:
                    player_1 = Ship(k_1, choose_position)
                    Field[1] = [player_1.getship()]
                    list_1.remove(choose_position)
                    for i_1 in Field:
                        print(*i_1)
                l += 1
            elif choose_position == "21" or choose_position == "22" or choose_position == "23" or choose_position == "24" or choose_position == "25" or choose_position == "26":
                check_list.append(choose_position)
                if l==0:
                    list_distance_of_user[0].append(choose_position)
                if len(check_list) >= 2:
                    distance = are_ships_distance_apart(check_list)
                    if not distance:
                        check_list.pop(-1)
                        print("Ошибка! Корабли должны находиться друг от друга на расстоянии минимум одной клетки!")
                        continue
                    else:
                        list_distance_of_user[0].append(choose_position)
                for k_2 in Field[2]:
                    player_1 = Ship(k_2, choose_position)
                    Field[2] = [player_1.getship()]
                    list_1.remove(choose_position)
                    for i_2 in Field:
                        print(*i_2)
                l += 1
            elif choose_position == "31" or choose_position == "32" or choose_position == "33" or choose_position == "34" or choose_position == "35" or choose_position == "36":
                check_list.append(choose_position)
                if l==0:
                    list_distance_of_user[0].append(choose_position)
                if len(check_list) >= 2:
                    distance = are_ships_distance_apart(check_list)
                    if not distance:
                        check_list.pop(-1)
                        print("Ошибка! Корабли должны находиться друг от друга на расстоянии минимум одной клетки!")
                        continue
                    else:
                        list_distance_of_user[0].append(choose_position)
                for k_3 in Field[3]:
                    player_1 = Ship(k_3, choose_position)
                    Field[3] = [player_1.getship()]
                    list_1.remove(choose_position)
                    for i_3 in Field:
                        print(*i_3)
                l += 1
            elif choose_position == "41" or choose_position == "42" or choose_position == "43" or choose_position == "44" or choose_position == "45" or choose_position == "46":
                check_list.append(choose_position)
                if l==0:
                    list_distance_of_user[0].append(choose_position)
                if len(check_list) >= 2:
                    distance = are_ships_distance_apart(check_list)
                    if not distance:
                        check_list.pop(-1)
                        print("Ошибка! Корабли должны находиться друг от друга на расстоянии минимум одной клетки!")
                        continue
                    else:
                        list_distance_of_user[0].append(choose_position)
                for k_4 in Field[4]:
                    player_1 = Ship(k_4, choose_position)
                    Field[4] = [player_1.getship()]
                    list_1.remove(choose_position)
                    for i_4 in Field:
                        print(*i_4)
                l += 1
            elif choose_position == "51" or choose_position == "52" or choose_position == "53" or choose_position == "54" or choose_position == "55" or choose_position == "56":
                check_list.append(choose_position)
                if l==0:
                    list_distance_of_user[0].append(choose_position)
                if len(check_list) >= 2:
                    distance = are_ships_distance_apart(check_list)
                    if not distance:
                        check_list.pop(-1)
                        print("Ошибка! Корабли должны находиться друг от друга на расстоянии минимум одной клетки!")
                        continue
                    else:
                        list_distance_of_user[0].append(choose_position)
                for k_5 in Field[5]:
                    player_1 = Ship(k_5, choose_position)
                    Field[5] = [player_1.getship()]
                    list_1.remove(choose_position)
                    for i_5 in Field:
                        print(*i_5)
                l += 1
            elif choose_position == "61" or choose_position == "62" or choose_position == "63" or choose_position == "64" or choose_position == "65" or choose_position == "66":
                check_list.append(choose_position)
                if l==0:
                    list_distance_of_user[0].append(choose_position)
                if len(check_list) >= 2:
                    distance = are_ships_distance_apart(check_list)
                    if not distance:
                        check_list.pop(-1)
                        print("Ошибка! Корабли должны находиться друг от друга на расстоянии минимум одной клетки!")
                        continue
                    else:
                        list_distance_of_user[0].append(choose_position)
                for k_6 in Field[6]:
                    player_1 = Ship(k_6, choose_position)
                    Field[6] = [player_1.getship()]
                    list_1.remove(choose_position)
                    for i_6 in Field:
                        print(*i_6)
                l += 1
        else:
            print(f"Ошибка! Введите значение из списка {list_1}")
            continue

    # Переменная для остановки цикла (корабли размером в две клетки)
    l = 0

    # Объявление списков для проверок
    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration = [*check_list]
    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration = [*check_list]
    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration = [*check_list]
    check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration = [*check_list]

    # Цикл с размещением кораблей размером в две клетки
    while l < 2:

        # Первая позиция
        choose_position_1 = input(f"Выберите 1-ую позицию для корабля на 2 клетки {list_1}: ")

        # Проверка первой позиции
        if choose_position_1 in list_1:
            if l == 0:
                check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.append(
                    choose_position_1)
                check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.append(
                    choose_position_1)
                distance = are_ships_distance_apart(
                    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration) and are_ships_distance_apart(
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration)
                if not distance:
                    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
                    print("Ошибка! Корабли должны находиться друг от друга на расстоянии минимум одной клетки!")
                    continue
                else:
                    index_of_element = list_1.index(choose_position_1)
                    list_1.remove(choose_position_1)
            else:
                check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.append(
                    choose_position_1)
                check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.append(
                    choose_position_1)
                distance = are_ships_distance_apart(
                    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration) and are_ships_distance_apart(
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration)
                if not distance:
                    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
                    print("Ошибка! Корабли должны находиться друг от друга на расстоянии минимум одной клетки!")
                    continue
                else:
                    index_of_element = list_1.index(choose_position_1)
                    list_1.remove(choose_position_1)
        else:
            print(f"Ошибка! Введите значение из списка {list_1}")
            continue

        # Вторая позиция
        choose_position_2 = input(f"Выберите 2-ую позицию для корабля на 2 клетки {list_1}: ")

        # Проверка нахождения второй позиции в списке
        if choose_position_2 in list_1:

            # Проверка второй позиции
            if l == 0:
                check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.append(
                    choose_position_2)
                check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration.append(
                    choose_position_2)
                distance = are_ships_distance_apart(
                    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration) and are_ships_distance_apart(
                    check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration)
                if not distance:
                    list_1.insert(index_of_element, choose_position_1)
                    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.pop(-1)
                    check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
                    print("Ошибка! Корабли должны находиться друг от друга на расстоянии минимум одной клетки!")
                    continue
            else:
                check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.append(
                    choose_position_2)
                check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration.append(
                    choose_position_2)
                distance = are_ships_distance_apart(
                    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration) and are_ships_distance_apart(
                    check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration)
                if not distance:
                    list_1.insert(index_of_element, choose_position_1)
                    check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
                    print("Ошибка! Корабли должны находиться друг от друга на расстоянии минимум одной клетки!")
                    continue

            # Проверка позиций на дистанцию
            checking = is_adjacent([choose_position_1, choose_position_2])
            if checking:
                if l==0:
                    list_distance_of_user[1].append(choose_position_1)
                    list_distance_of_user[1].append(choose_position_2)
                else:
                    list_distance_of_user[2].append(choose_position_1)
                    list_distance_of_user[2].append(choose_position_2)
                # Размещение первой клетки
                if choose_position_1 == "11" or choose_position_1 == "12" or choose_position_1 == "13" or choose_position_1 == "14" or choose_position_1 == "15" or choose_position_1 == "16":
                    for k_1 in Field[1]:
                        player_1 = Ship(k_1, choose_position_1)
                        Field[1] = [player_1.getship()]
                    l += 1
                elif choose_position_1 == "21" or choose_position_1 == "22" or choose_position_1 == "23" or choose_position_1 == "24" or choose_position_1 == "25" or choose_position_1 == "26":
                    for k_2 in Field[2]:
                        player_1 = Ship(k_2, choose_position_1)
                        Field[2] = [player_1.getship()]
                    l += 1
                elif choose_position_1 == "31" or choose_position_1 == "32" or choose_position_1 == "33" or choose_position_1 == "34" or choose_position_1 == "35" or choose_position_1 == "36":
                    for k_3 in Field[3]:
                        player_1 = Ship(k_3, choose_position_1)
                        Field[3] = [player_1.getship()]
                    l += 1
                elif choose_position_1 == "41" or choose_position_1 == "42" or choose_position_1 == "43" or choose_position_1 == "44" or choose_position_1 == "45" or choose_position_1 == "46":
                    for k_4 in Field[4]:
                        player_1 = Ship(k_4, choose_position_1)
                        Field[4] = [player_1.getship()]
                    l += 1
                elif choose_position_1 == "51" or choose_position_1 == "52" or choose_position_1 == "53" or choose_position_1 == "54" or choose_position_1 == "55" or choose_position_1 == "56":
                    for k_5 in Field[5]:
                        player_1 = Ship(k_5, choose_position_1)
                        Field[5] = [player_1.getship()]
                    l += 1
                elif choose_position_1 == "61" or choose_position_1 == "62" or choose_position_1 == "63" or choose_position_1 == "64" or choose_position_1 == "65" or choose_position_1 == "66":
                    for k_6 in Field[6]:
                        player_1 = Ship(k_6, choose_position_1)
                        Field[6] = [player_1.getship()]
                    l += 1

            else:
                list_1.insert(index_of_element, choose_position_1)
                if l == 0:
                    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.pop(-1)
                    check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
                else:
                    check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
                print("Ошибка! Клетки должны находиться рядом!")
                continue

        # Если вторая позиция находится вне списка
        else:
            list_1.insert(index_of_element, choose_position_1)
            if l == 0:
                check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
            else:
                check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.pop(-1)
                check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
            print(f"Ошибка! Введите значение из списка {list_1}")
            continue

        # Размещение второй клетки
        if choose_position_2 == "11" or choose_position_2 == "12" or choose_position_2 == "13" or choose_position_2 == "14" or choose_position_2 == "15" or choose_position_2 == "16":
            for k_1 in Field[1]:
                player_1 = Ship(k_1, choose_position_2)
                Field[1] = [player_1.getship()]
                list_1.remove(choose_position_2)
                for i_1 in Field:
                    print(*i_1)
        elif choose_position_2 == "21" or choose_position_2 == "22" or choose_position_2 == "23" or choose_position_2 == "24" or choose_position_2 == "25" or choose_position_2 == "26":
            for k_2 in Field[2]:
                player_1 = Ship(k_2, choose_position_2)
                Field[2] = [player_1.getship()]
                list_1.remove(choose_position_2)
                for i_2 in Field:
                    print(*i_2)
        elif choose_position_2 == "31" or choose_position_2 == "32" or choose_position_2 == "33" or choose_position_2 == "34" or choose_position_2 == "35" or choose_position_2 == "36":
            for k_3 in Field[3]:
                player_1 = Ship(k_3, choose_position_2)
                Field[3] = [player_1.getship()]
                list_1.remove(choose_position_2)
                for i_3 in Field:
                    print(*i_3)
        elif choose_position_2 == "41" or choose_position_2 == "42" or choose_position_2 == "43" or choose_position_2 == "44" or choose_position_2 == "45" or choose_position_2 == "46":
            for k_4 in Field[4]:
                player_1 = Ship(k_4, choose_position_2)
                Field[4] = [player_1.getship()]
                list_1.remove(choose_position_2)
                for i_4 in Field:
                    print(*i_4)
        elif choose_position_2 == "51" or choose_position_2 == "52" or choose_position_2 == "53" or choose_position_2 == "54" or choose_position_2 == "55" or choose_position_2 == "56":
            for k_5 in Field[5]:
                player_1 = Ship(k_5, choose_position_2)
                Field[5] = [player_1.getship()]
                list_1.remove(choose_position_2)
                for i_5 in Field:
                    print(*i_5)
        elif choose_position_2 == "61" or choose_position_2 == "62" or choose_position_2 == "63" or choose_position_2 == "64" or choose_position_2 == "65" or choose_position_2 == "66":
            for k_6 in Field[6]:
                player_1 = Ship(k_6, choose_position_2)
                Field[6] = [player_1.getship()]
                list_1.remove(choose_position_2)
                for i_6 in Field:
                    print(*i_6)

    # Переменная для остановки цикла (корабли размером в три клетки)
    l = 0

    # Создание списков для проверки
    check_list_with_first_position_1 = [
        *check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration]
    check_list_with_first_position_2 = [
        *check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration]
    check_list_with_first_position_3 = [
        *check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration]
    check_list_with_first_position_4 = [
        *check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration]

    check_list_with_second_position_1 = [
        *check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration]
    check_list_with_second_position_2 = [
        *check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration]
    check_list_with_second_position_3 = [
        *check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration]
    check_list_with_second_position_4 = [
        *check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration]

    check_list_with_third_position_1 = [
        *check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration]
    check_list_with_third_position_2 = [
        *check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration]
    check_list_with_third_position_3 = [
        *check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration]
    check_list_with_third_position_4 = [
        *check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration]

    # Цикл с размещением кораблей размером в три клетки
    while l < 1:

        # Работа с первой позицией
        choose_position__1 = input(f"Выберите 1-ую позицию для корабля на 3 клетки {list_1}: ")
        if choose_position__1 in list_1:
            check_list_with_first_position_1.append(choose_position__1)
            check_list_with_first_position_2.append(choose_position__1)
            check_list_with_first_position_3.append(choose_position__1)
            check_list_with_first_position_4.append(choose_position__1)
            distance = are_ships_distance_apart(check_list_with_first_position_1) and are_ships_distance_apart(
                check_list_with_first_position_2) and are_ships_distance_apart(
                check_list_with_first_position_3) and are_ships_distance_apart(check_list_with_first_position_4)
            if not distance:
                check_list_with_first_position_1.pop(-1)
                check_list_with_first_position_2.pop(-1)
                check_list_with_first_position_3.pop(-1)
                check_list_with_first_position_4.pop(-1)
                print("Ошибка! Корабли должны находиться друг от друга на расстоянии минимум одной клетки!")
                continue
            else:
                index_of_element_1 = list_1.index(choose_position__1)
                list_1.remove(choose_position__1)
        else:
            print(f"Ошибка! Введите значение из списка {list_1}")
            continue

        # Работа со второй позицией
        choose_position__2 = input(f"Выберите 2-ую позицию для корабля на 3 клетки {list_1}: ")
        if choose_position__2 in list_1:
            check_list_with_second_position_1.append(choose_position__2)
            check_list_with_second_position_2.append(choose_position__2)
            check_list_with_second_position_3.append(choose_position__2)
            check_list_with_second_position_4.append(choose_position__2)
            distance = are_ships_distance_apart(check_list_with_second_position_1) and are_ships_distance_apart(
                check_list_with_second_position_2) and are_ships_distance_apart(
                check_list_with_second_position_3) and are_ships_distance_apart(check_list_with_second_position_4)
            if not distance:
                list_1.insert(index_of_element_1, choose_position__1)
                check_list_with_first_position_1.pop(-1)
                check_list_with_first_position_2.pop(-1)
                check_list_with_first_position_3.pop(-1)
                check_list_with_first_position_4.pop(-1)

                check_list_with_second_position_1.pop(-1)
                check_list_with_second_position_2.pop(-1)
                check_list_with_second_position_3.pop(-1)
                check_list_with_second_position_4.pop(-1)
                print("Ошибка! Корабли должны находиться друг от друга на расстоянии минимум одной клетки!")
                continue
            else:
                index_of_element_2 = list_1.index(choose_position__2)
                list_1.remove(choose_position__2)
        else:
            list_1.insert(index_of_element_1, choose_position__1)
            check_list_with_second_position_1.pop(-1)
            check_list_with_second_position_2.pop(-1)
            check_list_with_second_position_3.pop(-1)
            check_list_with_second_position_4.pop(-1)
            print(f"Ошибка! Введите значение из списка {list_1}")
            continue

        choose_position__3 = input(f"Выберите 3-ую позицию для корабля на 3 клетки {list_1}: ")

        if choose_position__3 in list_1:

            # Работа с третьей позицией
            check_list_with_third_position_1.append(choose_position__3)
            check_list_with_third_position_2.append(choose_position__3)
            check_list_with_third_position_3.append(choose_position__3)
            check_list_with_third_position_4.append(choose_position__3)
            distance = are_ships_distance_apart(check_list_with_third_position_1) and are_ships_distance_apart(
                check_list_with_third_position_2) and are_ships_distance_apart(
                check_list_with_third_position_3) and are_ships_distance_apart(check_list_with_third_position_4)
            if not distance:
                check_list_with_first_position_1.pop(-1)
                check_list_with_first_position_2.pop(-1)
                check_list_with_first_position_3.pop(-1)
                check_list_with_first_position_4.pop(-1)

                check_list_with_second_position_1.pop(-1)
                check_list_with_second_position_2.pop(-1)
                check_list_with_second_position_3.pop(-1)
                check_list_with_second_position_4.pop(-1)

                check_list_with_third_position_1.pop(-1)
                check_list_with_third_position_2.pop(-1)
                check_list_with_third_position_3.pop(-1)
                check_list_with_third_position_4.pop(-1)

                list_1.insert(index_of_element_1, choose_position__1)
                list_1.insert(index_of_element_2, choose_position__2)
                print("Ошибка! Корабли должны находиться друг от друга на расстоянии минимум одной клетки!")
                continue

            # Проверка дистанции между клетками корабля
            checking = is_adjacent([choose_position__1, choose_position__2, choose_position__3])
            if checking:

                # Размещение первой клетки
                if choose_position__1 == "11" or choose_position__1 == "12" or choose_position__1 == "13" or choose_position__1 == "14" or choose_position__1 == "15" or choose_position__1 == "16":
                    for k_1 in Field[1]:
                        player_1 = Ship(k_1, choose_position__1)
                        Field[1] = [player_1.getship()]
                    l += 1
                elif choose_position__1 == "21" or choose_position__1 == "22" or choose_position__1 == "23" or choose_position__1 == "24" or choose_position__1 == "25" or choose_position__1 == "26":
                    for k_2 in Field[2]:
                        player_1 = Ship(k_2, choose_position__1)
                        Field[2] = [player_1.getship()]
                    l += 1
                elif choose_position__1 == "31" or choose_position__1 == "32" or choose_position__1 == "33" or choose_position__1 == "34" or choose_position__1 == "35" or choose_position__1 == "36":
                    for k_3 in Field[3]:
                        player_1 = Ship(k_3, choose_position__1)
                        Field[3] = [player_1.getship()]
                    l += 1
                elif choose_position__1 == "41" or choose_position__1 == "42" or choose_position__1 == "43" or choose_position__1 == "44" or choose_position__1 == "45" or choose_position__1 == "46":
                    for k_4 in Field[4]:
                        player_1 = Ship(k_4, choose_position__1)
                        Field[4] = [player_1.getship()]
                    l += 1
                elif choose_position__1 == "51" or choose_position__1 == "52" or choose_position__1 == "53" or choose_position__1 == "54" or choose_position__1 == "55" or choose_position__1 == "56":
                    for k_5 in Field[5]:
                        player_1 = Ship(k_5, choose_position__1)
                        Field[5] = [player_1.getship()]
                    l += 1
                elif choose_position__1 == "61" or choose_position__1 == "62" or choose_position__1 == "63" or choose_position__1 == "64" or choose_position__1 == "65" or choose_position__1 == "66":
                    for k_6 in Field[6]:
                        player_1 = Ship(k_6, choose_position__1)
                        Field[6] = [player_1.getship()]
                    l += 1
                list_distance_of_user[3].append(choose_position__1)
            else:
                check_list_with_first_position_1.pop(-1)
                check_list_with_first_position_2.pop(-1)
                check_list_with_first_position_3.pop(-1)
                check_list_with_first_position_4.pop(-1)

                check_list_with_second_position_1.pop(-1)
                check_list_with_second_position_2.pop(-1)
                check_list_with_second_position_3.pop(-1)
                check_list_with_second_position_4.pop(-1)

                check_list_with_third_position_1.pop(-1)
                check_list_with_third_position_2.pop(-1)
                check_list_with_third_position_3.pop(-1)
                check_list_with_third_position_4.pop(-1)
                list_1.insert(index_of_element_1, choose_position__1)
                list_1.insert(index_of_element_2, choose_position__2)
                print("Ошибка! Клетки должны находиться рядом!")
                continue
        else:
            check_list_with_first_position_1.pop(-1)
            check_list_with_first_position_2.pop(-1)
            check_list_with_first_position_3.pop(-1)
            check_list_with_first_position_4.pop(-1)

            check_list_with_second_position_1.pop(-1)
            check_list_with_second_position_2.pop(-1)
            check_list_with_second_position_3.pop(-1)
            check_list_with_second_position_4.pop(-1)
            list_1.insert(index_of_element_1, choose_position__1)
            list_1.insert(index_of_element_2, choose_position__2)
            print(f"Ошибка! Введите значение из списка {list_1}")
            continue

        # Размещение второй клетки
        if choose_position__2 == "11" or choose_position__2 == "12" or choose_position__2 == "13" or choose_position__2 == "14" or choose_position__2 == "15" or choose_position__2 == "16":
            for k_1 in Field[1]:
                player_1 = Ship(k_1, choose_position__2)
                Field[1] = [player_1.getship()]
        elif choose_position__2 == "21" or choose_position__2 == "22" or choose_position__2 == "23" or choose_position__2 == "24" or choose_position__2 == "25" or choose_position__2 == "26":
            for k_2 in Field[2]:
                player_1 = Ship(k_2, choose_position__2)
                Field[2] = [player_1.getship()]
        elif choose_position__2 == "31" or choose_position__2 == "32" or choose_position__2 == "33" or choose_position__2 == "34" or choose_position__2 == "35" or choose_position__2 == "36":
            for k_3 in Field[3]:
                player_1 = Ship(k_3, choose_position__2)
                Field[3] = [player_1.getship()]
        elif choose_position__2 == "41" or choose_position__2 == "42" or choose_position__2 == "43" or choose_position__2 == "44" or choose_position__2 == "45" or choose_position__2 == "46":
            for k_4 in Field[4]:
                player_1 = Ship(k_4, choose_position__2)
                Field[4] = [player_1.getship()]
        elif choose_position__2 == "51" or choose_position__2 == "52" or choose_position__2 == "53" or choose_position__2 == "54" or choose_position__2 == "55" or choose_position__2 == "56":
            for k_5 in Field[5]:
                player_1 = Ship(k_5, choose_position__2)
                Field[5] = [player_1.getship()]
        elif choose_position__2 == "61" or choose_position__2 == "62" or choose_position__2 == "63" or choose_position__2 == "64" or choose_position__2 == "65" or choose_position__2 == "66":
            for k_6 in Field[6]:
                player_1 = Ship(k_6, choose_position__2)
                Field[6] = [player_1.getship()]
        list_distance_of_user[3].append(choose_position__2)

        # Размещение третьей клетки
        if choose_position__3 == "11" or choose_position__3 == "12" or choose_position__3 == "13" or choose_position__3 == "14" or choose_position__3 == "15" or choose_position__3 == "16":
            for k_1 in Field[1]:
                player_1 = Ship(k_1, choose_position__3)
                Field[1] = [player_1.getship()]
                list_1.remove(choose_position__3)
                for i_1 in Field:
                    print(*i_1)
        elif choose_position__3 == "21" or choose_position__3 == "22" or choose_position__3 == "23" or choose_position__3 == "24" or choose_position__3 == "25" or choose_position__3 == "26":
            for k_2 in Field[2]:
                player_1 = Ship(k_2, choose_position__3)
                Field[2] = [player_1.getship()]
                list_1.remove(choose_position__3)
                for i_2 in Field:
                    print(*i_2)
        elif choose_position__3 == "31" or choose_position__3 == "32" or choose_position__3 == "33" or choose_position__3 == "34" or choose_position__3 == "35" or choose_position__3 == "36":
            for k_3 in Field[3]:
                player_1 = Ship(k_3, choose_position__3)
                Field[3] = [player_1.getship()]
                list_1.remove(choose_position__3)
                for i_3 in Field:
                    print(*i_3)
        elif choose_position__3 == "41" or choose_position__3 == "42" or choose_position__3 == "43" or choose_position__3 == "44" or choose_position__3 == "45" or choose_position__3 == "46":
            for k_4 in Field[4]:
                player_1 = Ship(k_4, choose_position__3)
                Field[4] = [player_1.getship()]
                list_1.remove(choose_position__3)
                for i_4 in Field:
                    print(*i_4)
        elif choose_position__3 == "51" or choose_position__3 == "52" or choose_position__3 == "53" or choose_position__3 == "54" or choose_position__3 == "55" or choose_position__3 == "56":
            for k_5 in Field[5]:
                player_1 = Ship(k_5, choose_position__3)
                Field[5] = [player_1.getship()]
                list_1.remove(choose_position__3)
                for i_5 in Field:
                    print(*i_5)
        elif choose_position__3 == "61" or choose_position__3 == "62" or choose_position__3 == "63" or choose_position__3 == "64" or choose_position__3 == "65" or choose_position__3 == "66":
            for k_6 in Field[6]:
                player_1 = Ship(k_6, choose_position__3)
                Field[6] = [player_1.getship()]
                list_1.remove(choose_position__3)
                for i_6 in Field:
                    print(*i_6)
        list_distance_of_user[3].append(choose_position__3)
    return Field

def positions_of_AI(Desk, list_of_positions):
    # Поле
    Field = Desk

    # Список
    list_1 = list_of_positions

    # Переменная, в которой будет храниться список с проверяемыми позициями
    check_list = []

    # Переменная для остановки цикла (корабли размером в одну клетку)
    l = 0

    # Цикл с размещением кораблей размером в одну клетку
    while l < 4:
        choose_position = list_1[randint(0,len(list_1)-1)]
        if choose_position in list_1:

            # Размещение клетки
            if choose_position == "11" or choose_position == "12" or choose_position == "13" or choose_position == "14" or choose_position == "15" or choose_position == "16":
                check_list.append(choose_position)
                if l==0:
                    list_distance_of_AI[0].append(choose_position)
                if len(check_list) >= 2:
                    distance = are_ships_distance_apart(check_list)
                    if not distance:
                        check_list.pop(-1)
                        continue
                    else:
                        list_distance_of_AI[0].append(choose_position)
                for k_1 in Field[1]:
                    player_AI = Ship(k_1, choose_position)
                    Field[1] = [player_AI.getship()]
                    list_1.remove(choose_position)
                l += 1
            elif choose_position == "21" or choose_position == "22" or choose_position == "23" or choose_position == "24" or choose_position == "25" or choose_position == "26":
                check_list.append(choose_position)
                if l==0:
                    list_distance_of_AI[0].append(choose_position)
                if len(check_list) >= 2:
                    distance = are_ships_distance_apart(check_list)
                    if not distance:
                        check_list.pop(-1)
                        continue
                    else:
                        list_distance_of_AI[0].append(choose_position)
                for k_2 in Field[2]:
                    player_AI = Ship(k_2, choose_position)
                    Field[2] = [player_AI.getship()]
                    list_1.remove(choose_position)
                l += 1
            elif choose_position == "31" or choose_position == "32" or choose_position == "33" or choose_position == "34" or choose_position == "35" or choose_position == "36":
                check_list.append(choose_position)
                if l==0:
                    list_distance_of_AI[0].append(choose_position)
                if len(check_list) >= 2:
                    distance = are_ships_distance_apart(check_list)
                    if not distance:
                        check_list.pop(-1)
                        continue
                    else:
                        list_distance_of_AI[0].append(choose_position)
                for k_3 in Field[3]:
                    player_AI = Ship(k_3, choose_position)
                    Field[3] = [player_AI.getship()]
                    list_1.remove(choose_position)
                l += 1
            elif choose_position == "41" or choose_position == "42" or choose_position == "43" or choose_position == "44" or choose_position == "45" or choose_position == "46":
                check_list.append(choose_position)
                if l==0:
                    list_distance_of_AI[0].append(choose_position)
                if len(check_list) >= 2:
                    distance = are_ships_distance_apart(check_list)
                    if not distance:
                        check_list.pop(-1)
                        continue
                    else:
                        list_distance_of_AI[0].append(choose_position)
                for k_4 in Field[4]:
                    player_AI = Ship(k_4, choose_position)
                    Field[4] = [player_AI.getship()]
                    list_1.remove(choose_position)
                l += 1
            elif choose_position == "51" or choose_position == "52" or choose_position == "53" or choose_position == "54" or choose_position == "55" or choose_position == "56":
                check_list.append(choose_position)
                if l==0:
                    list_distance_of_AI[0].append(choose_position)
                if len(check_list) >= 2:
                    distance = are_ships_distance_apart(check_list)
                    if not distance:
                        check_list.pop(-1)
                        continue
                    else:
                        list_distance_of_AI[0].append(choose_position)
                for k_5 in Field[5]:
                    player_AI = Ship(k_5, choose_position)
                    Field[5] = [player_AI.getship()]
                    list_1.remove(choose_position)
                l += 1
            elif choose_position == "61" or choose_position == "62" or choose_position == "63" or choose_position == "64" or choose_position == "65" or choose_position == "66":
                check_list.append(choose_position)
                if l==0:
                    list_distance_of_AI[0].append(choose_position)
                if len(check_list) >= 2:
                    distance = are_ships_distance_apart(check_list)
                    if not distance:
                        check_list.pop(-1)
                        continue
                    else:
                        list_distance_of_AI[0].append(choose_position)
                for k_6 in Field[6]:
                    player_AI = Ship(k_6, choose_position)
                    Field[6] = [player_AI.getship()]
                    list_1.remove(choose_position)
                l += 1
        else:
            continue

    # Переменная для остановки цикла (корабли размером в две клетки)
    l = 0

    # Объявление списков для проверок
    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration = [*check_list]
    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration = [*check_list]
    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration = [*check_list]
    check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration = [*check_list]

    # Цикл с размещением кораблей размером в две клетки
    while l < 2:

        # Первая позиция
        choose_position_1 = list_1[randint(0,len(list_1)-1)]
        # Проверка первой позиции
        if choose_position_1 in list_1:
            if l == 0:
                check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.append(
                    choose_position_1)
                check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.append(
                    choose_position_1)
                distance = are_ships_distance_apart(
                    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration) and are_ships_distance_apart(
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration)
                if not distance:
                    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
                    continue
                else:
                    index_of_element = list_1.index(choose_position_1)
                    list_1.remove(choose_position_1)
            else:
                check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.append(
                    choose_position_1)
                check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.append(
                    choose_position_1)
                distance = are_ships_distance_apart(
                    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration) and are_ships_distance_apart(
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration)
                if not distance:
                    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
                    continue
                else:
                    index_of_element = list_1.index(choose_position_1)
                    list_1.remove(choose_position_1)
        else:
            continue

        # Вторая позиция
        choose_position_2 = list_1[randint(0,len(list_1)-1)]
        # Проверка нахождения второй позиции в списке
        if choose_position_2 in list_1:

            # Проверка второй позиции
            if l == 0:
                check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.append(
                    choose_position_2)
                check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration.append(
                    choose_position_2)
                distance = are_ships_distance_apart(
                    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration) and are_ships_distance_apart(
                    check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration)
                if not distance:
                    list_1.insert(index_of_element, choose_position_1)
                    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.pop(-1)
                    check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
                    continue
            else:
                check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.append(
                    choose_position_2)
                check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration.append(
                    choose_position_2)
                distance = are_ships_distance_apart(
                    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration) and are_ships_distance_apart(
                    check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration)
                if not distance:
                    list_1.insert(index_of_element, choose_position_1)
                    check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
                    continue

            # Проверка позиций на дистанцию
            checking = is_adjacent([choose_position_1, choose_position_2])
            if checking:
                if l == 0:
                    list_distance_of_AI[1].append(choose_position_1)
                    list_distance_of_AI[1].append(choose_position_2)
                else:
                    list_distance_of_AI[2].append(choose_position_1)
                    list_distance_of_AI[2].append(choose_position_2)
                # Размещение первой клетки
                if choose_position_1 == "11" or choose_position_1 == "12" or choose_position_1 == "13" or choose_position_1 == "14" or choose_position_1 == "15" or choose_position_1 == "16":
                    for k_1 in Field[1]:
                        player_AI = Ship(k_1, choose_position_1)
                        Field[1] = [player_AI.getship()]
                    l += 1
                elif choose_position_1 == "21" or choose_position_1 == "22" or choose_position_1 == "23" or choose_position_1 == "24" or choose_position_1 == "25" or choose_position_1 == "26":
                    for k_2 in Field[2]:
                        player_AI = Ship(k_2, choose_position_1)
                        Field[2] = [player_AI.getship()]
                    l += 1
                elif choose_position_1 == "31" or choose_position_1 == "32" or choose_position_1 == "33" or choose_position_1 == "34" or choose_position_1 == "35" or choose_position_1 == "36":
                    for k_3 in Field[3]:
                        player_AI = Ship(k_3, choose_position_1)
                        Field[3] = [player_AI.getship()]
                    l += 1
                elif choose_position_1 == "41" or choose_position_1 == "42" or choose_position_1 == "43" or choose_position_1 == "44" or choose_position_1 == "45" or choose_position_1 == "46":
                    for k_4 in Field[4]:
                        player_AI = Ship(k_4, choose_position_1)
                        Field[4] = [player_AI.getship()]
                    l += 1
                elif choose_position_1 == "51" or choose_position_1 == "52" or choose_position_1 == "53" or choose_position_1 == "54" or choose_position_1 == "55" or choose_position_1 == "56":
                    for k_5 in Field[5]:
                        player_AI = Ship(k_5, choose_position_1)
                        Field[5] = [player_AI.getship()]
                    l += 1
                elif choose_position_1 == "61" or choose_position_1 == "62" or choose_position_1 == "63" or choose_position_1 == "64" or choose_position_1 == "65" or choose_position_1 == "66":
                    for k_6 in Field[6]:
                        player_AI = Ship(k_6, choose_position_1)
                        Field[6] = [player_AI.getship()]
                    l += 1

            else:
                list_1.insert(index_of_element, choose_position_1)
                if l == 0:
                    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.pop(-1)
                    check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
                else:
                    check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                    check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.pop(-1)
                    check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
                continue

        # Если вторая позиция находится вне списка
        else:
            list_1.insert(index_of_element, choose_position_1)
            if l == 0:
                check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration.pop(-1)
                check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
            else:
                check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration.pop(-1)
                check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration.pop(-1)
            continue

        # Размещение второй клетки
        if choose_position_2 == "11" or choose_position_2 == "12" or choose_position_2 == "13" or choose_position_2 == "14" or choose_position_2 == "15" or choose_position_2 == "16":
            for k_1 in Field[1]:
                player_AI = Ship(k_1, choose_position_2)
                Field[1] = [player_AI.getship()]
                list_1.remove(choose_position_2)
        elif choose_position_2 == "21" or choose_position_2 == "22" or choose_position_2 == "23" or choose_position_2 == "24" or choose_position_2 == "25" or choose_position_2 == "26":
            for k_2 in Field[2]:
                player_AI = Ship(k_2, choose_position_2)
                Field[2] = [player_AI.getship()]
                list_1.remove(choose_position_2)
        elif choose_position_2 == "31" or choose_position_2 == "32" or choose_position_2 == "33" or choose_position_2 == "34" or choose_position_2 == "35" or choose_position_2 == "36":
            for k_3 in Field[3]:
                player_AI = Ship(k_3, choose_position_2)
                Field[3] = [player_AI.getship()]
                list_1.remove(choose_position_2)
        elif choose_position_2 == "41" or choose_position_2 == "42" or choose_position_2 == "43" or choose_position_2 == "44" or choose_position_2 == "45" or choose_position_2 == "46":
            for k_4 in Field[4]:
                player_AI = Ship(k_4, choose_position_2)
                Field[4] = [player_AI.getship()]
                list_1.remove(choose_position_2)
        elif choose_position_2 == "51" or choose_position_2 == "52" or choose_position_2 == "53" or choose_position_2 == "54" or choose_position_2 == "55" or choose_position_2 == "56":
            for k_5 in Field[5]:
                player_AI = Ship(k_5, choose_position_2)
                Field[5] = [player_AI.getship()]
                list_1.remove(choose_position_2)
        elif choose_position_2 == "61" or choose_position_2 == "62" or choose_position_2 == "63" or choose_position_2 == "64" or choose_position_2 == "65" or choose_position_2 == "66":
            for k_6 in Field[6]:
                player_AI = Ship(k_6, choose_position_2)
                Field[6] = [player_AI.getship()]
                list_1.remove(choose_position_2)

    # Переменная для остановки цикла (корабли размером в три клетки)
    l = 0

    # Создание списков для проверки
    check_list_with_first_position_1 = [
        *check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration]
    check_list_with_first_position_2 = [
        *check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration]
    check_list_with_first_position_3 = [
        *check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration]
    check_list_with_first_position_4 = [
        *check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration]

    check_list_with_second_position_1 = [
        *check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration]
    check_list_with_second_position_2 = [
        *check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration]
    check_list_with_second_position_3 = [
        *check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration]
    check_list_with_second_position_4 = [
        *check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration]

    check_list_with_third_position_1 = [
        *check_list_with_first_position_in_first_itteration_and_second_position_in_second_itteration]
    check_list_with_third_position_2 = [
        *check_list_with_first_position_in_second_itteration_and_second_position_in_first_itteration]
    check_list_with_third_position_3 = [
        *check_list_with_first_position_in_first_itteration_and_first_position_in_second_itteration]
    check_list_with_third_position_4 = [
        *check_list_with_second_position_in_first_itteration_and_second_position_in_second_itteration]

    # Цикл с размещением кораблей размером в три клетки
    while l < 1:

        # Работа с первой позицией
        choose_position__1 = list_1[randint(0,len(list_1)-1)]
        if choose_position__1 in list_1:
            check_list_with_first_position_1.append(choose_position__1)
            check_list_with_first_position_2.append(choose_position__1)
            check_list_with_first_position_3.append(choose_position__1)
            check_list_with_first_position_4.append(choose_position__1)
            distance = are_ships_distance_apart(check_list_with_first_position_1) and are_ships_distance_apart(
                check_list_with_first_position_2) and are_ships_distance_apart(
                check_list_with_first_position_3) and are_ships_distance_apart(check_list_with_first_position_4)
            if not distance:
                check_list_with_first_position_1.pop(-1)
                check_list_with_first_position_2.pop(-1)
                check_list_with_first_position_3.pop(-1)
                check_list_with_first_position_4.pop(-1)
                continue
            else:
                index_of_element_1 = list_1.index(choose_position__1)
                list_1.remove(choose_position__1)
        else:
            continue

        # Работа со второй позицией
        choose_position__2 = list_1[randint(0,len(list_1)-1)]
        if choose_position__2 in list_1:
            check_list_with_second_position_1.append(choose_position__2)
            check_list_with_second_position_2.append(choose_position__2)
            check_list_with_second_position_3.append(choose_position__2)
            check_list_with_second_position_4.append(choose_position__2)
            distance = are_ships_distance_apart(check_list_with_second_position_1) and are_ships_distance_apart(
                check_list_with_second_position_2) and are_ships_distance_apart(
                check_list_with_second_position_3) and are_ships_distance_apart(check_list_with_second_position_4)
            if not distance:
                list_1.insert(index_of_element_1, choose_position__1)
                check_list_with_first_position_1.pop(-1)
                check_list_with_first_position_2.pop(-1)
                check_list_with_first_position_3.pop(-1)
                check_list_with_first_position_4.pop(-1)

                check_list_with_second_position_1.pop(-1)
                check_list_with_second_position_2.pop(-1)
                check_list_with_second_position_3.pop(-1)
                check_list_with_second_position_4.pop(-1)
                continue
            else:
                index_of_element_2 = list_1.index(choose_position__2)
                list_1.remove(choose_position__2)
        else:
            list_1.insert(index_of_element_1, choose_position__1)
            check_list_with_second_position_1.pop(-1)
            check_list_with_second_position_2.pop(-1)
            check_list_with_second_position_3.pop(-1)
            check_list_with_second_position_4.pop(-1)
            continue

        choose_position__3 = list_1[randint(0,len(list_1)-1)]
        if choose_position__3 in list_1:

            # Работа с третьей позицией
            check_list_with_third_position_1.append(choose_position__3)
            check_list_with_third_position_2.append(choose_position__3)
            check_list_with_third_position_3.append(choose_position__3)
            check_list_with_third_position_4.append(choose_position__3)
            distance = are_ships_distance_apart(check_list_with_third_position_1) and are_ships_distance_apart(
                check_list_with_third_position_2) and are_ships_distance_apart(
                check_list_with_third_position_3) and are_ships_distance_apart(check_list_with_third_position_4)
            if not distance:
                check_list_with_first_position_1.pop(-1)
                check_list_with_first_position_2.pop(-1)
                check_list_with_first_position_3.pop(-1)
                check_list_with_first_position_4.pop(-1)

                check_list_with_second_position_1.pop(-1)
                check_list_with_second_position_2.pop(-1)
                check_list_with_second_position_3.pop(-1)
                check_list_with_second_position_4.pop(-1)

                check_list_with_third_position_1.pop(-1)
                check_list_with_third_position_2.pop(-1)
                check_list_with_third_position_3.pop(-1)
                check_list_with_third_position_4.pop(-1)

                list_1.insert(index_of_element_1, choose_position__1)
                list_1.insert(index_of_element_2, choose_position__2)
                continue

            # Проверка дистанции между клетками корабля
            checking = is_adjacent([choose_position__1, choose_position__2, choose_position__3])
            if checking:

                # Размещение первой клетки
                if choose_position__1 == "11" or choose_position__1 == "12" or choose_position__1 == "13" or choose_position__1 == "14" or choose_position__1 == "15" or choose_position__1 == "16":
                    for k_1 in Field[1]:
                        player_AI = Ship(k_1, choose_position__1)
                        Field[1] = [player_AI.getship()]
                    l += 1
                elif choose_position__1 == "21" or choose_position__1 == "22" or choose_position__1 == "23" or choose_position__1 == "24" or choose_position__1 == "25" or choose_position__1 == "26":
                    for k_2 in Field[2]:
                        player_AI = Ship(k_2, choose_position__1)
                        Field[2] = [player_AI.getship()]
                    l += 1
                elif choose_position__1 == "31" or choose_position__1 == "32" or choose_position__1 == "33" or choose_position__1 == "34" or choose_position__1 == "35" or choose_position__1 == "36":
                    for k_3 in Field[3]:
                        player_AI = Ship(k_3, choose_position__1)
                        Field[3] = [player_AI.getship()]
                    l += 1
                elif choose_position__1 == "41" or choose_position__1 == "42" or choose_position__1 == "43" or choose_position__1 == "44" or choose_position__1 == "45" or choose_position__1 == "46":
                    for k_4 in Field[4]:
                        player_AI = Ship(k_4, choose_position__1)
                        Field[4] = [player_AI.getship()]
                    l += 1
                elif choose_position__1 == "51" or choose_position__1 == "52" or choose_position__1 == "53" or choose_position__1 == "54" or choose_position__1 == "55" or choose_position__1 == "56":
                    for k_5 in Field[5]:
                        player_AI = Ship(k_5, choose_position__1)
                        Field[5] = [player_AI.getship()]
                    l += 1
                elif choose_position__1 == "61" or choose_position__1 == "62" or choose_position__1 == "63" or choose_position__1 == "64" or choose_position__1 == "65" or choose_position__1 == "66":
                    for k_6 in Field[6]:
                        player_AI = Ship(k_6, choose_position__1)
                        Field[6] = [player_AI.getship()]
                    l += 1
                list_distance_of_AI[3].append(choose_position__1)
            else:
                check_list_with_first_position_1.pop(-1)
                check_list_with_first_position_2.pop(-1)
                check_list_with_first_position_3.pop(-1)
                check_list_with_first_position_4.pop(-1)

                check_list_with_second_position_1.pop(-1)
                check_list_with_second_position_2.pop(-1)
                check_list_with_second_position_3.pop(-1)
                check_list_with_second_position_4.pop(-1)

                check_list_with_third_position_1.pop(-1)
                check_list_with_third_position_2.pop(-1)
                check_list_with_third_position_3.pop(-1)
                check_list_with_third_position_4.pop(-1)
                list_1.insert(index_of_element_1, choose_position__1)
                list_1.insert(index_of_element_2, choose_position__2)
                continue
        else:
            check_list_with_first_position_1.pop(-1)
            check_list_with_first_position_2.pop(-1)
            check_list_with_first_position_3.pop(-1)
            check_list_with_first_position_4.pop(-1)

            check_list_with_second_position_1.pop(-1)
            check_list_with_second_position_2.pop(-1)
            check_list_with_second_position_3.pop(-1)
            check_list_with_second_position_4.pop(-1)
            list_1.insert(index_of_element_1, choose_position__1)
            list_1.insert(index_of_element_2, choose_position__2)
            continue

        # Размещение второй клетки
        if choose_position__2 == "11" or choose_position__2 == "12" or choose_position__2 == "13" or choose_position__2 == "14" or choose_position__2 == "15" or choose_position__2 == "16":
            for k_1 in Field[1]:
                player_AI = Ship(k_1, choose_position__2)
                Field[1] = [player_AI.getship()]
        elif choose_position__2 == "21" or choose_position__2 == "22" or choose_position__2 == "23" or choose_position__2 == "24" or choose_position__2 == "25" or choose_position__2 == "26":
            for k_2 in Field[2]:
                player_AI = Ship(k_2, choose_position__2)
                Field[2] = [player_AI.getship()]
        elif choose_position__2 == "31" or choose_position__2 == "32" or choose_position__2 == "33" or choose_position__2 == "34" or choose_position__2 == "35" or choose_position__2 == "36":
            for k_3 in Field[3]:
                player_AI = Ship(k_3, choose_position__2)
                Field[3] = [player_AI.getship()]
        elif choose_position__2 == "41" or choose_position__2 == "42" or choose_position__2 == "43" or choose_position__2 == "44" or choose_position__2 == "45" or choose_position__2 == "46":
            for k_4 in Field[4]:
                player_AI = Ship(k_4, choose_position__2)
                Field[4] = [player_AI.getship()]
        elif choose_position__2 == "51" or choose_position__2 == "52" or choose_position__2 == "53" or choose_position__2 == "54" or choose_position__2 == "55" or choose_position__2 == "56":
            for k_5 in Field[5]:
                player_AI = Ship(k_5, choose_position__2)
                Field[5] = [player_AI.getship()]
        elif choose_position__2 == "61" or choose_position__2 == "62" or choose_position__2 == "63" or choose_position__2 == "64" or choose_position__2 == "65" or choose_position__2 == "66":
            for k_6 in Field[6]:
                player_AI = Ship(k_6, choose_position__2)
                Field[6] = [player_AI.getship()]
        list_distance_of_AI[3].append(choose_position__2)

        # Размещение третьей клетки
        if choose_position__3 == "11" or choose_position__3 == "12" or choose_position__3 == "13" or choose_position__3 == "14" or choose_position__3 == "15" or choose_position__3 == "16":
            for k_1 in Field[1]:
                player_AI = Ship(k_1, choose_position__3)
                Field[1] = [player_AI.getship()]
                list_1.remove(choose_position__3)
        elif choose_position__3 == "21" or choose_position__3 == "22" or choose_position__3 == "23" or choose_position__3 == "24" or choose_position__3 == "25" or choose_position__3 == "26":
            for k_2 in Field[2]:
                player_AI = Ship(k_2, choose_position__3)
                Field[2] = [player_AI.getship()]
                list_1.remove(choose_position__3)
        elif choose_position__3 == "31" or choose_position__3 == "32" or choose_position__3 == "33" or choose_position__3 == "34" or choose_position__3 == "35" or choose_position__3 == "36":
            for k_3 in Field[3]:
                player_AI = Ship(k_3, choose_position__3)
                Field[3] = [player_AI.getship()]
                list_1.remove(choose_position__3)
        elif choose_position__3 == "41" or choose_position__3 == "42" or choose_position__3 == "43" or choose_position__3 == "44" or choose_position__3 == "45" or choose_position__3 == "46":
            for k_4 in Field[4]:
                player_AI = Ship(k_4, choose_position__3)
                Field[4] = [player_AI.getship()]
                list_1.remove(choose_position__3)
        elif choose_position__3 == "51" or choose_position__3 == "52" or choose_position__3 == "53" or choose_position__3 == "54" or choose_position__3 == "55" or choose_position__3 == "56":
            for k_5 in Field[5]:
                player_AI = Ship(k_5, choose_position__3)
                Field[5] = [player_AI.getship()]
                list_1.remove(choose_position__3)
        elif choose_position__3 == "61" or choose_position__3 == "62" or choose_position__3 == "63" or choose_position__3 == "64" or choose_position__3 == "65" or choose_position__3 == "66":
            for k_6 in Field[6]:
                player_AI = Ship(k_6, choose_position__3)
                Field[6] = [player_AI.getship()]
                list_1.remove(choose_position__3)
        list_distance_of_AI[3].append(choose_position__3)
    return Field

# Инициализация поля для пользователя
Field_for_user = [["  | 1 | 2 | 3 | 4 | 5 | 6 |"],
["1 | О | О | О | О | О | О |"],
["2 | О | О | О | О | О | О |"],
["3 | О | О | О | О | О | О |"],
["4 | О | О | О | О | О | О |"],
["5 | О | О | О | О | О | О |"],
["6 | О | О | О | О | О | О |"]]

# Инициализация поля для AI
Field_for_AI = [["  | 1 | 2 | 3 | 4 | 5 | 6 |"],
["1 | О | О | О | О | О | О |"],
["2 | О | О | О | О | О | О |"],
["3 | О | О | О | О | О | О |"],
["4 | О | О | О | О | О | О |"],
["5 | О | О | О | О | О | О |"],
["6 | О | О | О | О | О | О |"]]

# Переменная, в которой будет храниться список с позициями пользователя
list_for_user=["11","12","13","14","15","16","21","22","23","24","25","26","31","32","33","34","35","36","41","42","43","44","45","46","51","52","53","54","55","56","61","62","63","64","65","66"]

# Переменная, в которой будет храниться список с позициями AI
list_for_AI=["11","12","13","14","15","16","21","22","23","24","25","26","31","32","33","34","35","36","41","42","43","44","45","46","51","52","53","54","55","56","61","62","63","64","65","66"]

list_distance_of_user = [[],[],[],[]]
list_distance_of_AI = [[],[],[],[]]

Just_Player = Player(Field_for_user,list_for_user)

AI_player = AI(Field_for_AI,list_for_AI)

Field_for_fighting_AI = AI_player.getpositions()

Field_for_fighting_user = Just_Player.getpositions()

Start_game = start_game(Field_for_fighting_user,Field_for_fighting_AI)
Start_game.beginning_user()


