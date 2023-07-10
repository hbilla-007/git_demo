work_hours=[('billa',6670),('venky',347),('siva',346)]
def myfunc(work_hours):
    employee_hours=0
    employee_name=''
    for employee,hours in (work_hours):
        if hours>employee_hours:
            employee_hours=hours
            employee_name=employee
        else:
            pass
    return(employee_name,employee_hours)
print(myfunc(work_hours))