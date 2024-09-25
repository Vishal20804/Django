from django.shortcuts import HttpResponse
class BroMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time bro initialization")

    def __call__(self,request):
        print("This is bro before view")

        response=self.get_response(request)
        print("This is bro after view")

        return response            
    

class FatherMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time father initialization")


    def __call__(self,request):
        print("This is father before view")

      #  return HttpResponse("Nikal lo")
# if want to braek or want to return the response from father and not send response further then we can use remove above comment
        response=self.get_response(request)
        print("This is father after view")

        return response            
    

class MaaMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time maa initialization")

    def __call__(self,request):
        print("This is maa before view")

        response=self.get_response(request)
        print("This is maa after view")

        return response            