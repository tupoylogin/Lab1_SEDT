from abc import ABCMeta, abstractmethod
import numpy as np
import collections
import json
import random
import string

class BaseWorker(metaclass=ABCMeta):
    """
        класс базового рабочего
    """
    def __init__(self, first_name=None, last_name=None, salary=None):
        self._name = first_name
        self._lname = last_name
        self._salary= salary
        self._id = ''.join(random.choice(string.digits) for i in range(4))

    def to_dict(self):
        dict = {}
        dict['id']=self._id
        dict["first_name"]=self.name
        dict["last_name"]=self.lname
        dict["salary"]=self.salary
        return dict

    def stringify(self):
        return str(self.to_dict()).replace("\'","\"")

    @property
    def name(self):
        return self._name

    @property
    def lname(self):
        return self._lname

    @property
    def salary(self):
        return self._salary

    @name.setter
    def name(self,first_name):
        if isinstance(first_name,str):
            self._name = first_name
        else: raise TypeError("First Name should be string")

    @lname.setter
    def lname(self,last_name):
        if isinstance(last_name,str):
            self._lname = last_name
        else: raise TypeError("Last Name should be string")

    @salary.setter
    @abstractmethod
    def salary(self, value):
        pass

    @staticmethod
    def check_json(json_field):
        keys = list(set([k.lower() for k in json_field.keys()]))
        print(keys)
        return set(keys)==set(["id","first_name", "last_name", "salary"])

    def from_json(self,json_dict):
        if self.check_json(json_dict):
            dict_copy = {k.lower():v for k,v in json_dict.items()}
            self._id=dict_copy["id"]
            self.name = dict_copy["first_name"]
            self.lname = dict_copy["last_name"]
            self.salary  = dict_copy["salary"]
        else: raise ValueError("Incorrect JSON dictionary")


class FixedPaid(BaseWorker):
    """
        класс рабочего с фиксированной з/п
    """

    def __init__(self, first_name = "John", last_name = "Doe", salary = None):
        super(FixedPaid,self).__init__()
        self.name=first_name
        self.lname=last_name
        self.salary=salary

    @property
    def name(self):
        return super(FixedPaid,self).name

    @name.setter
    def name(self,value):
        super(FixedPaid,self.__class__).name.fset(self,value)

    @property
    def lname(self):
        return super(FixedPaid,self).lname

    @lname.setter
    def lname(self,value):
        super(FixedPaid,self.__class__).lname.fset(self,value)

    @property
    def salary(self):
        #print(super(FixedPaid,self).salary)
        return super(FixedPaid,self).salary

    @salary.setter
    def salary(self, value=100):
        if value is None:
            raise ValueError("None is not allowed")
        else: 
            if not isinstance(value, (int,float)):
                raise TypeError ("Salary cannot be non-numeric")
            else:
                if (value<=0): raise ValueError("Cannot assign negative value to salary")
                else: self._salary=value


class HourlyPaid(BaseWorker):
    """
        класс рабочего с почасовой оплатой
    """
    def __init__(self, first_name = 'John', last_name = 'Doe', salary = None):
        super(HourlyPaid,self).__init__()
        self.name=first_name
        self.lname=last_name
        self.salary=salary

    @property
    def name(self):
        return super(HourlyPaid,self).name

    @name.setter
    def name(self,value):
        super(HourlyPaid,self.__class__).name.fset(self,value)

    @property
    def lname(self):
        return super(HourlyPaid,self).lname

    @lname.setter
    def lname(self,value):
        super(HourlyPaid,self.__class__).lname.fset(self,value)

    @property
    def salary(self):
        return super(HourlyPaid,self).salary

    @salary.setter
    def salary(self,value=3,hpd=8,k=20.8):
        if value is None:
            raise ValueError("None is not allowed")
        else: 
            if not isinstance(value, (int,float)):
                raise TypeError ("Salary cannot be non-numeric")
            else:
                if (value<=0): raise ValueError("Cannot assign negative value to salary")
                else: self._salary=k*value*hpd

def read_file(filename):
    if filename:
        with open(filename,"r") as fp:
            data = json.load(fp)
            workers_arr = []
            for item in data:
                workers_arr.append(FixedPaid().from_json(item))
    else: raise FileNotFoundError
    return workers_arr

def write_file(filename,data):
    with open(filename,"w+") as fp:
        for item in data:
            fp.write(json.dumps(data, indent=4))



# генерация семплов
names = ["John", "Adam", "Joe", "Andy", "Daniel", "Michael", "Jack"]
lnames = ["Smith", "King", "Johnson", "Lloyd", "Herring", "Goodfellow", "Black", "White"]
hsalaries = np.linspace(5,20,100)
fsalaries = np.random.randint(400,4000,100)
type_of_work = ['HourlyPaid','FixedPaid']
range_w = 150
wrkrs = []



for j in range(range_w):
    worker = np.random.choice(type_of_work)
    name = np.random.choice(names)
    lname = np.random.choice(lnames)
    if worker == type_of_work[0]:
        wrkrs.append(HourlyPaid(first_name=name,last_name=lname,salary=float(np.round(np.random.choice(hsalaries),2))))
    else: wrkrs.append(FixedPaid(first_name=name,last_name=lname,salary=int(np.random.choice(fsalaries))))

# ... и сортировка
workers = [i.to_dict() for i in wrkrs]
workers = sorted(workers,key=lambda k: (-k['salary'],k['first_name'].lower()))

print([workers[i]['first_name'] for i in range(5)])
print([workers[i]['id'] for i in range(-3,0)])

filename = 'task2.json'
write_file(filename,workers)




