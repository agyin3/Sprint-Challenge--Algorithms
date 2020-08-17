class SortingRobot:
    def __init__(self, l):
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        return self._position < len(self._list) - 1

    def can_move_left(self):
        return self._position > 0

    def move_right(self):
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        self._light = "ON"
    def set_light_off(self):
        self._light = "OFF"
    def light_is_on(self):
        return self._light == "ON"

    def r_position(self):
        '''
        Returns the robot's position
        '''
        return self._position

    def list_length(self):
        '''
        Returns the robot's list's length
        '''
        return len(self._list)

    def sort(self):
        '''
        LIGHT "ON" -> robot carrying item
        LIGHT "OFF" -> robot not carrying item  
        '''    
        if self.light_is_on() is False:
            
            # Index len(self._list) - 1
            if self.can_move_right() is False:
                '''
                If robot reaches the end of the list 
                while not carrying an item, then the 
                list is sorted
                '''
                return self._list
            
            else:
                '''
                Swap items and turn the light on to in
                indicate the robot is carrying an item
                The robot is using None as a partition
                so everything to the left of None is sorted
                '''
                self.swap_item()
                self.set_light_on()
                return self.sort()
                
                
        else:    

                # Able to move right
                while self.can_move_right():
                    '''
                    Robot will move right and compare items

                    ** Can move right **
                    Robot's item is smaller -> swap items
                    Robot's item larger -> continue forward

                    ** Can't move right **
                    Robot's item smaller -> will move left
                    Robot's items larger -> swap items
                    '''

                    self.move_right()
                        
                    if self.compare_item() < 0:
                        if self.can_move_right():
                            self.swap_item()
                        
                    elif self.compare_item() > 0:
                        if self.can_move_right() is False:
                            self.swap_item()

                while self.can_move_left():
                    '''
                    Robot will move left and compare items
                    until it reaches a None. If position of None
                    is equal to or greater then len(self._list)
                    list will be sorted

                    *** None position < len(self._list) ***
                    Robot's item smaller -> continue forward
                    Robot's item larger -> swap items
                    None comparison -> swap items, turn light off, move right, recursive call self.sort

                    *** None position >= len(self._list) ***
                    Robot's item smaller -> continue forward
                    Robot's item larger -> swap items
                    None comparison -> swap items, return list
                    '''
                    self.move_left()
                    
                    if self.compare_item() is None:
                        if self.r_position() <= (self.list_length() // 2):
                            self.swap_item()
                            self.set_light_off()
                            self.move_right()
                            return self.sort()

                        else:
                            self.swap_item()
                            return self._list

                    elif self.compare_item() >= 0:
                        self.swap_item()
                   
        return self._list
        
if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    large_list = [1, -38, -95, 4, 23, -73, -65, -36, 85, 2, 58, -26, -55, 96, 55, -76, 64, 45, 69, 36, 69, 47, 29, -47, 13, 89, -57, -88, -87, 54, 60, 56, -98, -78, 59, 93, -41, -74, 73, -35, -23, -79, -35, 46, -18, -18, 37, -64, 14, -57, -2, 15, -85, 45, -73, -2, 79, -87, -100, 21, -51, 22, 26, -59, 81, 59, -24, 24, -81, 43, 61, 52, 38, -88, -95, 87, -57, -37, -65, -47, -3, 21, -77, 98, 25, 1, -36, 39, 78, 47, -35, -40, -69, -81, 11, -47, 21, 25, -53, -31]

    import random
    random_list = [random.randint(0, 100) for i in range(0, 100)]

    robot = SortingRobot(l)
    robot2 = SortingRobot(large_list)
    robot3 = SortingRobot(random_list)

    # robot.sort()
    # print(robot._list)
    # robot2.sort()
    # print(robot2._list)
    robot3.sort()
    print(robot3._list)