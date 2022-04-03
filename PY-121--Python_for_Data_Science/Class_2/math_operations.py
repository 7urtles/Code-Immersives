class Operations:

    def find_mean(self, input_list:list)->float:
        """Returns mean given a list of integers"""
        mean = sum(input_list) / len(input_list)
        return mean

    def find_median(self, scores:list)->float:
        """Returns median given a list of integers"""
        num_items = len(scores)
        # if amount of numbers in list is even
        if num_items%2 == 0: 
            # add 1 to half the amount of numbers and grab th indes
            median = scores[num_items % 2 + 1]
        else:
            median = scores[num_items % 2] + scores[num_items % 2 +1] / 2
        return float(median)

    def find_mode(self, input_list:list)->list:
        """returns modes as a list of floats, takes list of numbers as input"""
        most_occuring = [0.0]
        for number in input_list:
            # if the number is already in the mode
            if number in most_occuring:
                # skip iteration
                continue
            # number of time current iteration appears in provided list
            occurances = input_list.count(number)
            # if number is new highest mode
            if occurances > input_list.count(most_occuring[-1]):
                # it is the new mode
                most_occuring = [float(number)]
            # if it appears same amount of times as current mode
            elif occurances == input_list.count(most_occuring[-1]):
                # then there are multiple modes so add it to the list of modes
                most_occuring.append(float(number))
        return most_occuring
    
    def find_variance(self, input_list:list)->float:
        '''Returns variance as a float provided a list of numbers'''
        return (sum([(number-sum(input_list)/len(input_list))**2 for number in input_list]) / (len(input_list)-1))
        
    def find_stdDev(self, input_list:list)->float:
        '''Returns standard deviation as a float provided a list of numbers'''
        return (sum([(number-sum(input_list)/len(input_list))**2 for number in input_list]) / (len(input_list)-1))**.5

    def find_STD(self, numbers:list, factor:int)->list:
        '''Returns a range of numbers as a list. List consits of the average of the data set added to the standard deviation multiplied by a specified factor (integer)'''
        # mean of the set
        numbers_mean = sum(numbers)/len(numbers)
        #Standard Deviation is square root of: sum the squares of the data set, divided by the sets length adjusted by -1
        numbers_stdDev = (sum([(number-numbers_mean)**2 for number in numbers])/(len(numbers)-1))**.5
        print(numbers_stdDev)
        # STD is applying multiples of the standard deviation to the mean
        STD = sorted([(numbers_mean + numbers_stdDev * num) for num in range(-factor,factor+1)])
        return STD

    def covariance(self, collection1:list, collection2:list)->float:
        avg1 = self.find_mean(collection1)
        avg2 = self.find_mean(collection2)
        diff1 = [temp-avg1 for temp in collection1]
        diff2 = [cream-avg2 for cream in collection2]
        multis = [diff1[n]*diff2[n] for n in range(len(collection1))]
        sum_multis = sum(multis)
        divided = sum_multis/(len(multis)-1)
        return divided

    def find_correlation(self, collection1:list, collection2:list) -> float:
        cov = self.covariance(collection1, collection2)
        # correlation = covariance / (standard_deviation_list1 * standard_deviation_list2)
        return (cov / (self.find_stdDev(collection1) * self.find_stdDev(collection2)))