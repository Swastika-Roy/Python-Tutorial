def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thank you")
    return mfx

@greet
def hello():
    print("Hello world")

@greet
def add(a,b):
    print(a+b)

hello()
add(3,4)


# greet(add)(1,2)