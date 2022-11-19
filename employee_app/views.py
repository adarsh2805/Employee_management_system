from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Employee,Role,Department

# Create your views here.
def index(request):
    return render(request,'index.html')




def view_employee(request):
    det=Employee.objects.all()
    context={
        'det':det
    }
    return render(request,'view.html',context)





def add_employee(request):
    dept_det=Department.objects.all()
    role_det=Role.objects.all()
        
    context={
            'dept_det': dept_det,
             'role_det': role_det

        }
    try:    
        if request.method=="POST":
            print('post')
            temp_firstname=request.POST['firstname']
            temp_lastname=request.POST['lastname']
            temp_salary=request.POST['salary']
            temp_bonus=request.POST['bonus']
            temp_phone=request.POST['phone']

            temp_role=request.POST['role']

            temp_dapt=request.POST['dept']
            temp_location=request.POST['location']
            temp_hire_date=request.POST['hire_date']
            print(temp_firstname,temp_lastname,temp_salary,temp_bonus,temp_phone,temp_role,temp_dapt,temp_location,temp_hire_date)
           
    
            empsave=Employee(firstname= temp_firstname,lastname=temp_lastname,salary= temp_salary,
                         bonus=temp_bonus,
                         phone=temp_phone,
                         role_id=temp_role,
                         dapt_id=temp_dapt,
                        location=temp_location,
                       hire_date=temp_hire_date)

            empsave.save()
            return redirect('/')
          
    except:
        return render(request,'add.html',context)
   
    else:   
             return render(request,'add.html',context)



def remove_employee(request):

    det=Employee.objects.all()
    context={
        'emp_det':det
    }
    if request.method=="POST":
        try:
            eid=request.POST['emp_det']
            a=Employee.objects.get(id=eid)
            a.delete()
            return redirect('/')
        except:
            return render(request,'remove.html',context)
    else:
        return render(request,'remove.html',context)
    




def filter_employee(request):

    det=Employee.objects.all()
    context={
        'emp_det':det
    }
    if request.method=="POST":
      try:  
        eid=request.POST['dis_det']
        a=Employee.objects.get(id=eid)
        display={
            'dis':a,
            'emp_det':det
        }
        return render(request,'filter.html',display)
      except:
        return render(request,'filter.html',context)


    else:
        return render(request,'filter.html',context)
