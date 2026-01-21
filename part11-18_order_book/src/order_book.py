# Write your solution here:
class Task:

    id_counter = 0

    def __init__(self, desc: str, name: str, hour: int):
        Task.id_counter += 1
        self.__id = Task.id_counter
        self.__description = desc
        self.__programmer = name
        self.__workload = hour
        self.__isfinished = False

    @property
    def id(self):
        return self.__id
    @property
    def description(self):
        return self.__description
    @property
    def programmer(self):
        return self.__programmer
    @property
    def workload(self):
        return self.__workload

    def is_finished(self):
        return self.__isfinished
    
    def mark_finished(self):
        self.__isfinished = True

    def __str__(self):
        return f'{self.__id}: {self.__description} ({self.__workload} hours), programmer {self.__programmer} {'FINISHED' if self.__isfinished else 'NOT FINISHED'}'



class OrderBook:
    def __init__(self):
        self.__orders = []

    def add_order(self, description, programmer, workload):
        self.__orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return [order for order in self.__orders]
    
    def programmers(self):
        return list(set([order.programmer for order in self.__orders]))
    
    def mark_finished(self, id: int):
        for order in self.__orders:
            if order.id == id:
                order.mark_finished()
                return 
        raise ValueError

    def finished_orders(self):
        return [order for order in self.__orders if order.is_finished()]
    def unfinished_orders(self):
        return [order for order in self.__orders if not order.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        for order in self.__orders:
            if order.programmer == programmer:
                finished_list = [task for task in self.finished_orders() if task.programmer == programmer]
                unfinished_list = [task for task in self.unfinished_orders() if task.programmer == programmer]
                return (len(finished_list), len(unfinished_list), sum([task.workload for task in finished_list]), sum([task.workload for task in unfinished_list]))
        raise ValueError        
