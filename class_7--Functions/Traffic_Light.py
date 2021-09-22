# B. Write a program to imitate a Traffic Light. _(Think about the information you need to generate to make your program mimic the real world.

from os import system, name
from time import sleep
import random



#---------[WORLD SETTINGS]----------------------------------------------------------------------------
run_speed = .04             # Under .03 can be unstable [.01-.1]                Default:  .1
number_of_roads = 4         # Supports 1-4 roads two lane roads                 Default:   2
road_length = 60            # The length of the road [20-80] recommended        Default:  20
intersection_width = 20     # Gap between streen lights [0-10]                  Default:   4
max_number_cars = 60        # Max number of cars in a lane at one time          Default:  15
spawn_rate = 40             # Car span rate [1-50]                              Default:  40
light_length = 300          # How long the light takes to turn colors           Default:  35
traffic_light_timer = 200   # Starting seed for initial traffic light timer     Default:  200
syncronize_lights = True
#-----------------------------------------------------------------------------------------------------



# Operates the runtime and road environment
class World_Handler():
    def __init__(self,run_speed,max_number_cars,spawn_rate,road_size,traffic_light_timer,syncronize_lights,intersection_width,number_of_roads):
        
        # Initialize runtime settings
        self.world = {}
        self.settings = {}
        self.run_speed = run_speed
        self.max_number_cars = max_number_cars
        self.spawn_rate = spawn_rate 
        self.road_size = road_size 
        self.traffic_light_timer = traffic_light_timer 
        self.light_length = light_length
        self.syncronized_lights = syncronize_lights
        self.intersection_width = intersection_width
        self.number_of_roads = number_of_roads

        # Initialize Traffic Lights
        self.westbound_traffic_light = Traffic_Light(self.traffic_light_timer)
        self.eastbound_traffic_light = Traffic_Light(self.traffic_light_timer)
        self.northbound_traffic_light = Traffic_Light(self.traffic_light_timer)
        self.southound_traffic_light = Traffic_Light(self.traffic_light_timer)
        self.westbound1_traffic_light = Traffic_Light(self.traffic_light_timer)
        self.eastbound1_traffic_light = Traffic_Light(self.traffic_light_timer)
        self.northbound1_traffic_light = Traffic_Light(self.traffic_light_timer)
        self.southound1_traffic_light = Traffic_Light(self.traffic_light_timer)

        # Dictionary Containing all Traffic Light objects
        self.traffic_lights = {'eastbound':self.westbound_traffic_light, 'westbound':self.eastbound_traffic_light,'northbound':self.northbound_traffic_light, 'southbound':self.southound_traffic_light,
        'eastbound1':self.westbound1_traffic_light, 'westbound1':self.eastbound1_traffic_light,'northbound1':self.northbound1_traffic_light, 'southbound1':self.southound1_traffic_light}
        # If Lights are not set to synced, assign their timers random values
        for light in self.traffic_lights:
            if self.syncronized_lights == False:
                self.traffic_lights[light] = Traffic_Light(random.randint(-self.traffic_light_timer,self.traffic_light_timer))

        # Construct Traffic and Cars
        self.westbound_cars = {}
        self.eastbound_cars = {}
        self.northbound_cars = {}
        self.southbound_cars = {}
        self.westbound1_cars = {}
        self.eastbound1_cars = {}
        self.northbound1_cars = {}
        self.southbound1_cars = {}
        # Dictionary Containing all car objects
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
        # Dictionary Containing all lane objects
        self.lanes = {'eastbound':self.westbound_lane,'westbound':self.eastbound_lane, 'northbound':self.northbound_lane,'southbound':self.southbound_lane,
        'eastbound1':self.westbound1_lane,'westbound1':self.eastbound1_lane, 'northbound1':self.northbound1_lane,'southbound1':self.southbound1_lane}




        ''' THE LANE BULLDOZER NEEDS TO BE MOVED TO ITS OWN CLASS/FUNCTION '''
        # -------Removes lanes from self.traffic in order to meet user specified amount of roads--------
        # Turns the road count into a lane counter
        total_lanes = self.number_of_roads * 2

        # Build list of all the lanes
        lane_list = []
        for i in self.traffic:
            lane_list.append(i)

        # Remove all unwanted lanes from the program
        while len(lane_list) > total_lanes:
            self.traffic.pop(lane_list[-1])
            lane_list.pop()       
        ''' END OF LANE BULLDOZER '''


        self.settings = {'Speed':run_speed, 'Roads':number_of_roads, 'Cars':max_number_cars, 'spawn_rate':spawn_rate, 
        'road_size':road_length, 'Synced Traffic':syncronize_lights, 'Intersection size':intersection_width, 
        'traffic_light_timer':traffic_light_timer, 'light_length':light_length}

        # WOLRD OBJECT containing all data about the world
        self.world = {'settings':self.settings, 'cars':self.traffic, 'traffic_lights':self.traffic_lights, 'lanes':self.lanes}

        # MAIN LOOP
        while True:
            self.clear()
            # Updating every direction of traffic
            for direction in self.world['cars']:               
                # Initialize the Lane
                self.world['lanes'][direction] = Lane().run(self.world, direction)

                # CALL THE DISPLAY HANDLER HERE
                Display_Handler().display_road(self.world, direction)

                # Call to have chance of spawing car
                self.world = Car_Manager().spawn(self.world, direction)
                # Update the car positions
                self.world = Car_Manager().move_cars(self.world, direction)
                # Destroy cars that have left the road
                self.world = Car_Manager().kill(self.world, direction)    

                # Update Traffic light timers and data
                self.world = Traffic_Light_Manager.light_updater(self.world, direction)
            
            # Drawing World Data box  
            print("    ","----[WORLD SETTINGS]----")
            for i in self.world['settings']:
                # print("   ",f' {i}:[{self.world}]')
                pass
            print("    ","------------------------")
            
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
    def light_updater(world, direction):
        light_length = world['settings']['light_length']
        # Decrement time until light changes
        world['traffic_lights'][direction].timer['time'] -= 1
        # If the timer is on and not has time on it make the light green
        if world['traffic_lights'][direction].timer['on'] == True and world['traffic_lights'][direction].timer['time'] > 0:
            world['traffic_lights'][direction].color = 'green'
        # Otherwise red
        else:
            world['traffic_lights'][direction].timer['on'] = False
            world['traffic_lights'][direction].color = 'red'
        # If the time reaches its negative value, make it green again and reset the timer
        if world['traffic_lights'][direction].timer['time'] < -light_length:
            if syncronize_lights == True:
                world['traffic_lights'][direction].timer['time'] = light_length
            else:
                world['traffic_lights'][direction].timer['time'] = light_length + random.randint(-20,20)
            world['traffic_lights'][direction].timer['on'] = True
            world['traffic_lights'][direction].color = "green"

        for i in world['traffic_lights'][direction].status:
            if i == world['traffic_lights'][direction].color:
                world['traffic_lights'][direction].status[i] = True
            else:
                world['traffic_lights'][direction].status[i] = False
        return(world)






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
    def spawn(self, world, direction):

        # Random chance of spawing car
        x = random.randint(world['settings']['spawn_rate'],50)
        if x == world['settings']['spawn_rate']:
            # If there are 3 or less cars in the lane, and no car in the spawn position
            if len(world['cars'][direction]) < world['settings']['Cars'] and world['traffic_lights'][direction].spawn_taken == False:
                # Assign the id
                if world['cars'][direction] != {}:
                    for car in world['cars'][direction]:
                        car_id = world['cars'][direction][car].id + 1  
                else:
                    car_id = 0
                # Construct the car
                new_car = Car(car_id, direction, world['settings']['road_size'])

                # Add it to the list of cars
                world['cars'][direction][new_car.id] = new_car

                # Mark that traffic lights spawn to filled
                world['traffic_lights'][direction].spawn_taken = True
        return world


    # Controlling car movement by reducing their distance to the light by 1 if they are moving
    def move_cars(self, world, direction):
        # print(traffic_light.status)
        for car in world['cars'][direction]:
            # If light is green, drive
            if world['traffic_lights'][direction].status['green'] == True:
                world['cars'][direction][car].driving = True
            # Otherwise stop
            else:
                world['cars'][direction][car].driving = False
            # Keep driving if not close to the intersection, or already through it
            if world['cars'][direction][car].distance_from_light > intersection_width or world['cars'][direction][car].distance_from_light < intersection_width:
                world['cars'][direction][car].driving = True

            try:
                # If there is a car in the space ahead stop and wait until it has moved to drive again
                if world['cars'][direction][car].distance_from_light - world['cars'][direction][car-1].distance_from_light <= 1:
                    world['cars'][direction][car].driving = False
                    world['cars'][direction][car].waiting = True
                    continue
            except:
                pass
            # Skip turn if waiting and prepare to drive
            if world['cars'][direction][car].waiting == True:
                world['cars'][direction][car].waiting = False
                continue
            # If the car is in drive, move it by one space
            if world['cars'][direction][car].driving == True:
                world['cars'][direction][car].distance_from_light -= 1

                # If the car was in spawn, mark lane spawn position as now open
                if world['cars'][direction][car].in_spawn == True:
                    world['cars'][direction][car].in_spawn = False  
                    world['traffic_lights'][direction].spawn_taken = False 
        return(world)

    # Despawing cars after the leave the map
    def kill(self,world, direction):
        road_length = world['settings']['road_size']
        # Build a list of existing car IDs
        list_of_car_ids = []
        for car in world['cars'][direction]:
            list_of_car_ids.append(world['cars'][direction][car].id)

        # Look up car whos iD is in the list, and check it's movement.
        for id in list_of_car_ids:
            # De-Spawn it if it has traveled a certain distance
            if world['cars'][direction][id].distance_from_light <= -road_length:
                # print('DELETED CAR: ',list_of_cars[id])
                world['cars'][direction].pop(id)
        return world




class Lane():
    def __init__(self):
        self.lane_data = {}

    def run(self, world, direction):
        road_length = world['settings']['road_size']
        self.lane_data = {}
        road_ascii = ''
        road_space_ascii = '  '
        # print('the',list_of_cars)

        # Fill the lane with empty positions
        try:
            if 'eastbound' in direction or 'northbound' in direction:
                for i in range(road_length, -road_length, -1):
                    self.lane_data[i] = False
            if 'westbound' in direction or 'southbound' in direction:
                for i in range(-road_length, road_length):
                    self.lane_data[i] = False
        except:
            pass
        
        # Populate the lane with cars
        for car in world['cars'][direction]:
           self.lane_data[world['cars'][direction][car].distance_from_light] = True 
        
        # Check the road position values and assign ASCII 'car' if occupied
        for i in self.lane_data:
            if self.lane_data[i] == True:
                road_space_ascii = 'O'
            else:
                if '1' in direction or '1' in direction:
                    road_space_ascii = '_'
                else:
                    road_space_ascii = ' '
            road_ascii += road_space_ascii
        return(road_ascii, self.lane_data)





class Display_Handler():
    # Gets passed the highway information to construct the ASCII
    def display_road(self, world, direction):
        road_size = world['settings']['road_size']
        color = world['traffic_lights'][direction].color
        # Road 1 upper edge 
        if 'eastbound' == direction or 'northbound' == direction:
            print(' '+'__' * road_size + '__')
        # Road 1 Traffic Light
        if 'eastbound' in direction or 'northbound' in direction:
            if color == 'green':
                print(' ]'+' ' * (road_size - 3 - intersection_width),'|{}|/{}['.format(color.upper(),(road_size+intersection_width-6)*' '))
            else:
                print(' ]'+' ' * (road_size - 3 - intersection_width),'|{}|/{}['.format(color.upper(),(road_size+intersection_width-4)*' '))
       
        # Road 2 upper edge 
        if 'westbound' == direction or 'southbound' == direction:
                print(' '+'__' * road_size + '__')
        # Road 2 Traffic Light
        if 'westbound' in direction or 'southbound' in direction:
            if color == 'green':
                print(' ]'+' ' * (road_size - 4 + intersection_width),'\|{}|{}['.format(color.upper(),(road_size-intersection_width-5)*' '))
            else:
                print(' ]'+' ' * (road_size - 4 + intersection_width),'\|{}|{}['.format(color.upper(),(road_size-intersection_width-3)*' '))
            
            
        # Draw Cars and Lane Description
        print(' ]{}[        {}: {}'.format(world['lanes'][direction][0],direction.capitalize(), color.upper()))

        # Dashed lane divider
        if '1' not in direction:
            print(' :'+' -' * road_size+':')
        
        #  Top road barriers and spacing per highway
        if direction == 'eastbound1' or direction == 'northbound1':
            print(' 77'+'77' * road_size)
            print('','  ' * road_size)
            

        # Bottom road barries per highway
        if direction == 'southbound1' or direction == 'westbound1':
            print(' 77'+'77' * road_size)
            print('\n\n')


# STARTS THE APP using specified settings (at top of file)
World_Handler(run_speed,max_number_cars,spawn_rate,road_length,traffic_light_timer,syncronize_lights,intersection_width,number_of_roads)