# B. Write a program to imitate a Traffic Light. _(Think about the information you need to generate to make your program mimic the real world.

from os import system, name
from time import sleep
import random


#---------[WORLD SETTINGS]----------------------------------------------------------------------------
run_speed = .1              # Under .03 can be unstable [.01-.1]                Default: .1
road_size = 30              # The lenght of the road [10-50] Recommended        Default:  20
intersection_width = 12      # Gap between streen lights [0-10]                  Default:   4
max_number_cars = 15        # Max number of cars in a lane at one time          Default:  15
spawn_rate = 40             # Car span rate [1-50]                              Default:  40
light_length = 100          # How long the light takes to turn colors           Default:  35
traffic_light_timer = 40    # Starting seed for initial traffic light timer     Default:  25
syncronize_lights = False
#-----------------------------------------------------------------------------------------------------



# Operates the runtime and road environment
class World_Handler():
    def __init__(self,run_speed,max_number_cars,spawn_rate,road_size,traffic_light_timer,syncronize_lights,intersection_width):
        # Initialize runtime settings
        self.run_speed = run_speed
        self.max_number_cars = max_number_cars
        self.spawn_rate = spawn_rate 
        self.road_size = road_size 
        self.traffic_light_timer = traffic_light_timer 
        self.light_length = light_length
        self.syncronized_lights = syncronize_lights
        self.intersection_width = intersection_width

        # Initialize Traffic Lights
        if self.syncronized_lights == True:
            westbound_traffic_light = Traffic_Light(self.traffic_light_timer)
            eastbound_traffic_light = Traffic_Light(self.traffic_light_timer)
            northbound_traffic_light = Traffic_Light(self.traffic_light_timer)
            southound_traffic_light = Traffic_Light(self.traffic_light_timer)
            westbound1_traffic_light = Traffic_Light(self.traffic_light_timer)
            eastbound1_traffic_light = Traffic_Light(self.traffic_light_timer)
            northbound1_traffic_light = Traffic_Light(self.traffic_light_timer)
            southound1_traffic_light = Traffic_Light(self.traffic_light_timer)
        else:
            westbound_traffic_light = Traffic_Light(random.randint(-self.traffic_light_timer,self.traffic_light_timer))
            eastbound_traffic_light = Traffic_Light(random.randint(-self.traffic_light_timer,self.traffic_light_timer))
            northbound_traffic_light = Traffic_Light(random.randint(-self.traffic_light_timer,self.traffic_light_timer))
            southound_traffic_light = Traffic_Light(random.randint(-self.traffic_light_timer,self.traffic_light_timer))
            westbound1_traffic_light = Traffic_Light(random.randint(-self.traffic_light_timer,self.traffic_light_timer))
            eastbound1_traffic_light = Traffic_Light(random.randint(-self.traffic_light_timer,self.traffic_light_timer))
            northbound1_traffic_light = Traffic_Light(random.randint(-self.traffic_light_timer,self.traffic_light_timer))
            southound1_traffic_light = Traffic_Light(random.randint(-self.traffic_light_timer,self.traffic_light_timer))

        self.traffic_lights = {'eastbound':westbound_traffic_light, 'westbound':eastbound_traffic_light,'northbound':northbound_traffic_light, 'southbound':southound_traffic_light,
        'eastbound1':westbound1_traffic_light, 'westbound1':eastbound1_traffic_light,'northbound1':northbound1_traffic_light, 'southbound1':southound1_traffic_light}

        # Construct Traffic and Cars
        self.westbound_cars = {}
        self.eastbound_cars = {}
        self.northbound_cars = {}
        self.southbound_cars = {}
        self.westbound1_cars = {}
        self.eastbound1_cars = {}
        self.northbound1_cars = {}
        self.southbound1_cars = {}
        self.traffic = {'northbound': self.northbound_cars, 'northbound1': self.northbound1_cars, 'southbound': self.southbound_cars, 'southbound1': self.southbound1_cars,
        'eastbound': self.westbound_cars, 'eastbound1': self.westbound1_cars, 'westbound': self.eastbound_cars, 'westbound1': self.eastbound1_cars}

        # Construct Traffic Lanes
        self.westbound_lane = {}
        self.eastbound_lane = {}
        self.northbound_lane = {}
        self.southbound_lane = {}
        self.westbound1_lane = {}
        self.eastbound1_lane = {}
        self.northbound1_lane = {}
        self.southbound1_lane = {}
        self.lanes = {'eastbound':self.westbound_lane,'westbound':self.eastbound_lane, 'northbound':self.northbound_lane,'southbound':self.southbound_lane,
        'eastbound1':self.westbound1_lane,'westbound1':self.eastbound1_lane, 'northbound1':self.northbound1_lane,'southbound1':self.southbound1_lane}
        
        while True:
            self.clear()
            # Updating every direction of traffic
            for direction in self.traffic:
                heading = direction
               
                # Initialize the Lane
                self.lanes[direction] = Lane().run(self.traffic[direction], heading, self.road_size)

                # Draw Road Imagery
                if 'eastbound' == heading or 'northbound' == heading:
                    # Top edge of ASCII road
                    # print('====' * self.road_size)
                    
                    print('__' * self.road_size)
                if 'eastbound' in heading or 'northbound' in heading:
                    # Traffic Light Position
                    print(' ' * (self.road_size - 1 - self.intersection_width),'|{}|/'.format(self.traffic_lights[direction].color.upper()))

                if 'westbound' in heading or 'southbound' in heading:
                    print(' ' * (self.road_size - 2 + self.intersection_width),'\|{}|'.format(self.traffic_lights[direction].color.upper()))

                # Draw Cars and Lane Description
                print('{}|        {}: {}'.format(self.lanes[direction][0],heading.capitalize(), self.traffic_lights[heading].color.upper()))

                # Draw center line
                if '1' not in heading:
                    print('- ' * self.road_size)
                
                if heading == 'southbound1' or heading == 'westbound1':
                    print('77' * self.road_size)
                    print('\n\n')
                
                if heading == 'eastbound1' or heading == 'northbound1':
                    print('77' * self.road_size)
                    print('  ' * self.road_size)
                    print('__' * self.road_size)
             
                # Call to have chance of spawing car
                Car_Manager().car_creator(self.traffic[direction], self.traffic_lights[direction],
                direction, self.max_number_cars,self.spawn_rate,self.road_size)

                # Update the car positions
                Car_Manager().move_cars(self.traffic[direction], self.traffic_lights[direction], self.traffic[direction])

                # Destroy cars that have left the road
                if self.traffic[direction] != {}:
                    Car_Manager().car_despawner(self.traffic[direction],self.road_size)    

                # Update Traffic light timers and data
                self.traffic_lights[direction] = Traffic_Light_Manager.light_updater(self.traffic_lights[direction], self.light_length)
            sleep(self.run_speed)

    # clear function
    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')







class Traffic_Light():
    def __init__(self,timer):
        self.status = {'green':False, 'yellow':False, 'red':True}
        self.color = 'green'
        self.spawn_taken = False
        self.timer = {'on':True, 'time':timer}

class Traffic_Light_Manager():
    # Set light True/False values according to the 'color' value
    def light_updater(traffic_light, light_length):
        traffic_light.timer['time'] -= 1
        # print(traffic_light.timer['time'])

        # If the timer is on and not has time on it make the light green
        if traffic_light.timer['on'] == True and traffic_light.timer['time'] > 0:
            traffic_light.color = 'green'
        # Otherwise red
        else:
            traffic_light.timer['on'] = False
            traffic_light.color = 'red'
        # If the time reaches its negative value, make it green again and reset the timer
        if traffic_light.timer['time'] < -light_length:
            if syncronize_lights == True:
                traffic_light.timer['time'] = light_length
            else:
                traffic_light.timer['time'] = light_length + random.randint(-20,20)

            traffic_light.timer['on'] = True
            traffic_light.color = "green"

        for i in traffic_light.status:
            if i == traffic_light.color:
                traffic_light.status[i] = True
            else:
                traffic_light.status[i] = False
        return(traffic_light)






class Car():
    def __init__(self,id,direction,road_position):
        self.id = id
        self.distance_from_light = road_position
        if 'westbound' in direction or 'southbound' in direction:
            self.distance_from_light -= 1
        self.waiting = True
        self.driving = False
        self.in_spawn = True
        self.room_ahead = False

class Car_Manager():
    # Makes a new car and gives it a unique id
    def car_creator(self,list_of_cars, traffic_light, direction, max_number_cars,spawn_rate,road_length):

        # Random chance of spawing car
        x = random.randint(spawn_rate,50)
        if x == spawn_rate:
            # If there are 3 or less cars in the lane, and no car in the spawn position
            if len(list_of_cars) < max_number_cars and traffic_light.spawn_taken == False:
                # Assign the id
                if list_of_cars != {}:
                    for car in list_of_cars:
                        car_id = list_of_cars[car].id + 1  
                else:
                    car_id = 0
                # Construct the car
                new_car = Car(car_id, direction, road_length)

                # Add it to the list of cars
                list_of_cars[new_car.id] = new_car
                traffic_light.spawn_taken = True


    # Controlling car movement by reducing their distance to the light by 1 if they are moving
    def move_cars(self, list_of_cars, traffic_light, traffic_positions):
        # print(traffic_light.status)
        for car in list_of_cars:
            # If light is green, drive
            if traffic_light.status['green'] == True:
                list_of_cars[car].driving = True
            # Otherwise stop
            else:
                list_of_cars[car].driving = False
            # Keep driving if not close to the intersection, or already through it
            if list_of_cars[car].distance_from_light > intersection_width or list_of_cars[car].distance_from_light < intersection_width:
                list_of_cars[car].driving = True

            try:
                # If there is a car in the space ahead stop and wait until it has moved to drive again
                if traffic_positions[car].distance_from_light - traffic_positions[car-1].distance_from_light <= 1:
                    # print(list_of_cars[car])
                    list_of_cars[car].driving = False
                    list_of_cars[car].waiting = True
                    continue
            except:
                pass
            # Skip turn if waiting and prepare to drive
            if list_of_cars[car].waiting == True:
                list_of_cars[car].waiting = False
                # print(car)
                continue
            # If the car is in drive, move it by one space
            if list_of_cars[car].driving == True:
                list_of_cars[car].distance_from_light -= 1

                # If the car was in spawn, mark lane spawn position as now open
                if list_of_cars[car].in_spawn == True:
                    list_of_cars[car].in_spawn = False  
                    traffic_light.spawn_taken = False 
        return(list_of_cars)

    # Despawing cars after the leave the map
    def car_despawner(self,list_of_cars, road_length):

        # Build a list of existing car IDs
        list_of_car_ids = []
        for car in list_of_cars:
            list_of_car_ids.append(list_of_cars[car].id)

        # Look up car whos iD is in the list, and check it's movement.
        for id in list_of_car_ids:
            # De-Spawn it if it has traveled a certain distance
            if list_of_cars[id].distance_from_light <= -road_length:
                # print('DELETED CAR: ',list_of_cars[id])
                list_of_cars.pop(id)





class Lane():
    def __init__(self):
        self.lane_data = {}

    def run(self, list_of_cars, heading, road_length):
        self.lane_data = {}
        road_ascii = ''
        road_space_ascii = '  '
        # print('the',list_of_cars)

        # Fill the lane with empty positions
        try:
            if 'eastbound' in heading or 'northbound' in heading:
                for i in range(road_length, -road_length, -1):
                    self.lane_data[i] = False
            if 'westbound' in heading or 'southbound' in heading:
                for i in range(-road_length, road_length):
                    self.lane_data[i] = False
        except:
            pass
        
        # Populate the lane with cars
        for car in list_of_cars:
           self.lane_data[list_of_cars[car].distance_from_light] = True 

        # Check the road position values and assign ASCII 'car' if occupied
        for i in self.lane_data:
            if self.lane_data[i] == True:
                road_space_ascii = 'X'
            else:
                if '1' in heading or '1' in heading:
                    road_space_ascii = '_'
                else:
                    road_space_ascii = ' '
            road_ascii += road_space_ascii
        return(road_ascii, self.lane_data)



World_Handler(run_speed,max_number_cars,spawn_rate,road_size,traffic_light_timer,syncronize_lights,intersection_width)


