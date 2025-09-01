salaries = []

def create_salary(salary):
      global salaries
      salaries.append(salary)


def read_all():
      return salaries

def read_by_salary(salary): # return first occurance index range(stp) | range(start, end) | range(start, stop, step)
      for I in range(len(salaries)): #len(salaries)=5, I=0,1,2,3,4
            if salaries [I] == salary:
             return I
      return -1
            
def update(old_salary, new_salary):
     global salaries
     index = read_by_salary(old_salary)
     salaries[index] = new_salary

def delete_by_salary(salary):
     global salaries
     index = read_by_salary(salary) #index of 2000 is 0
     salaries.pop(index)
