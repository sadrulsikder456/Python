def add_cream(func):
    def wrapper():
        print("Adding cream...")
        func()
        print("Cream added.")
    return wrapper
@add_cream
def make_coffee():
    print("Brewing a cup of coffee..." )
@add_cream
def make_cake():
    print("Baking a delicious cake..." )

make_cake()
make_coffee()