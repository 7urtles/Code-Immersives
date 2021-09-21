# Check for the greatest of 3 numbers
# Write a Program to imitate a traffic light.
#   Submit on Populi

from os import system, name
from time import sleep
import random

# B. Write a program to imitate a Traffic Light. _(Think about the information you need to generate to make your program mimic the real world.

class Traffic_Light():

    def __init__(self,timer):
        self.status = {'green':False, 'yellow':False, 'red':True}
        self.color = 'green'
        self.car_approaching = False
        self.spawn_taken = False
        self.timer = {'on':True, 'time':timer}


class Traffic_Light_Manager():
    
    
    # Set light True/False values according to the 'color' value
    def light_updater(traffic_light):
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
        if traffic_light.timer['time'] < -40:
            traffic_light.timer['time'] = 40
            traffic_light.timer['on'] = True
            traffic_light.color = "green"

        for i in traffic_light.status:
            if i == traffic_light.color:
                traffic_light.status[i] = True
            else:
                traffic_light.status[i] = False
        return(traffic_light)


class Car():

    def __init__(self,id,direction):
        self.id = id
        self.distance_from_light = 20
        if direction == "eastbound":
            self.distance_from_light = 19
        self.waiting = True
        self.driving = False
        self.in_spawn = True
        self.room_ahead = False



class Car_Manager():
    # Makes a new car and gives it a unique id
    def car_creator(self,list_of_cars, traffic_light, direction):

        # Random chance of spawing car
        x = random.randint(0,3)
        if x == 1:
            # Car_Manager().car_creator(self.traffic[direction], self.traffic_lights[direction])

            # If there are 3 or less cars in the lane, and no car in the spawn position
            if len(list_of_cars) < 10 and traffic_light.spawn_taken == False:

                # Assign the id
                if list_of_cars != {}:
                    for car in list_of_cars:
                        car_id = list_of_cars[car].id + 1  
                
                else:
                    car_id = 0

                # Construct the car
                new_car = Car(car_id, direction)

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

            if list_of_cars[car].distance_from_light > 0 or list_of_cars[car].distance_from_light < 0:
                list_of_cars[car].driving = True

            try:
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
    def car_despawner(self,list_of_cars):

        # Build a list of existing car IDs
        list_of_car_ids = []
        for car in list_of_cars:
            list_of_car_ids.append(list_of_cars[car].id)
        # print(list_of_car_ids)
        # print(list_of_cars)

        # Look up car whos iD is in the list, and check it's movement.
        for id in list_of_car_ids:
            # De-Spawn it if it has traveled a certain distance
            if list_of_cars[id].distance_from_light <= -20:
                # print('DELETED CAR: ',list_of_cars[id])
                list_of_cars.pop(id)

class Lane():
    def __init__(self):
        self.lane_data = {}

    def run(self, list_of_cars, heading):
        self.lane_data = {}
        road_ascii = ''
        # print('the',list_of_cars)
        try:
            if heading == 'westbound':
                for i in range(20, -20, -1):
                    self.lane_data[i] = False
            if heading == 'eastbound':
                for i in range(-20, 20):
                    self.lane_data[i] = False
        except:
            pass
        

        for car in list_of_cars:
           self.lane_data[list_of_cars[car].distance_from_light] = True 

        # Check the road position values and give an ascii 'car' if it is True
        # print(self.lane_data)
        for i in self.lane_data:
            if self.lane_data[i] == True:
                road_space_ascii = '[]'
            else:
                road_space_ascii = '__'
            road_ascii += road_space_ascii
        
        return(road_ascii, self.lane_data)


'''
___
o-o>  

'''


# Operates the run time and intersection environment
class World_Handler():
    def __init__(self):
        
        westbound_traffic_light = Traffic_Light(10)
        eastbound_traffic_light = Traffic_Light(25)
        self.traffic_lights = {'westbound':westbound_traffic_light, 'eastbound':eastbound_traffic_light}

        # Construct Traffic Lights and Cars
        self.westbound_cars = {}
        self.eastbound_cars = {}
        self.traffic = {'westbound': self.westbound_cars, 'eastbound': self.eastbound_cars}


        self.westbound_lane = {}
        self.eastbound_lane = {}
        self.lanes = {'westbound':self.westbound_lane,'eastbound':self.eastbound_lane}
        while True:
            self.clear()

            for direction in self.traffic:
                heading = direction
                print(direction)
               
                # Retrieve data about the road
                self.lanes[direction] = Lane().run(self.traffic[direction],heading)

                print('{}        {} Light: {}\n'.format(self.lanes[direction][0],heading, self.traffic_lights[heading].color.upper()))
                
                # Call to have chance of spawing car
                Car_Manager().car_creator(self.traffic[direction], self.traffic_lights[direction],direction)

                # Update the car positions
                Car_Manager().move_cars(self.traffic[direction], self.traffic_lights[direction], self.traffic[direction])

                # If there are cars on the road check if they need to be removed
                if self.traffic[direction] != {}:
                    Car_Manager().car_despawner(self.traffic[direction])    
                
                # Update Traffic light timers and data
                self.traffic_lights[direction] = Traffic_Light_Manager.light_updater(self.traffic_lights[direction])

            sleep(.25)

    
    # define our clear function
    def clear(self):
    
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
World_Handler()


