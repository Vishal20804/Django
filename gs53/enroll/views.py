from django.shortcuts import render

# Create your views here.
def home(request,check):
    print(check)
    return render(request,'enroll/home.html')


# def show_details(request,my_id):
#     print(my_id)
#     return render(request,'enroll/show.html',{'my_id':my_id})


def show_details(request,my_id,check):
    print(check)
    if my_id==1:
        student={'my_id':my_id,'name':'Kisan'}
    if my_id==2:
        student={'my_id':my_id,'name':'Manvi'}
    if my_id==3:
        student={'my_id':my_id,'name':'Jiya'}
    return render(request,'enroll/show.html',student)

def show_subdetails(request,my_id,my_subid):
    print(my_id)
    if my_id==1 and my_subid==1:
        student={'my_id':my_id,'name':'Kumar','info':'kumar is my son'}
    if my_id==2 and my_subid==2:
        student={'my_id':my_id,'name':'Mahak','info':'mahak is asha`s sister  ' }
    if my_id==3 and my_subid==3:
        student={'my_id':my_id,'name':'junaid','info':'junaid is good guy'}
    return render(request,'enroll/show.html',student)