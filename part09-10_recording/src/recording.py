# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, len):
        if len<0:
            raise ValueError
        self.__length = len

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, len):
        if len<0:
            raise ValueError
        self.__length = len
        return self.__length

