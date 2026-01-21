# Write your solution here
# If you use the classes made in the previous exercise, copy them here
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


class OrderApp():

    def __init__(self):
        self.__orders = OrderBook()
    def __helpers(self):
        print('commands:\n0 exit\n1 add order\n2 list finished tasks' \
        '\n3 list unfinished tasks\n4 mark task as finished' \
        '\n5 programmers\n6 status of programmer')

    def __add_order(self):
        desc = input('description:')
        if type(desc) == str:
            try:
                name, workload = input('programmer and workload estimate:').split()
                workload = int(workload)
                self.__orders.add_order(desc, name, workload)
                print('added!')
                return
            except:
                print('erroneous input')
        print('erroneous input')

    def __finished_tasks(self):
        tasks = self.__orders.finished_orders()
        if len(tasks) == 0:
            print('no finished tasks')
            return
        for task in tasks:
            print(task)
    def __unfinished_tasks(self):
        tasks = self.__orders.unfinished_orders()
        if len(tasks) == 0:
            print('no unfinished tasks')
            return
        for task in tasks:
            print(task)

    def __mark_finished(self):
        id = input('id: ')
        try:
            id = int(id)
            self.__orders.mark_finished(id)
            print('marked as finished')
        except:
            print('erroneous input')

    def __programmers(self):
        programmers = self.__orders.programmers()
        if programmers:
            for name in programmers:
                print(name) 
    
    def __status(self):
        try:
            name = input('programmer: ')
            fin, unfin, fin_work, unfin_work = self.__orders.status_of_programmer(name)
            print(f'tasks: finished {fin} not finished {unfin}, hours: done {fin_work} scheduled {unfin_work}')
        except:
            print('erroneous input')

    def run(self):
        self.__helpers()
        while True:
            command = int(input('command: '))
            if command == 0:
                break
            elif command == 1:
                self.__add_order()
            elif command == 2:
                self.__finished_tasks()
            elif command == 3:
                self.__unfinished_tasks()
            elif command == 4:
                self.__mark_finished()
            elif command == 5:
                self.__programmers()
            elif command == 6:
                self.__status()
            else:
                self.__helpers()
    
        
def main():
    app = OrderApp()
    app.run()
    
main()