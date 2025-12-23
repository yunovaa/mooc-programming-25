# WRITE YOUR SOLUTION HERE:

class WeatherStation:

    def __init__(self, name):
        self.__name = name
        self.__obs = []

    def add_observation(self ,observation: str):
        self.__obs.append(observation)

    def latest_observation(self):
        return self.__obs[-1] if self.number_of_observations()>0 else ''
    
    def number_of_observations(self):
        return len(self.__obs)
    
    def __str__(self):
        return f'{self.__name}, {self.number_of_observations()} observations'