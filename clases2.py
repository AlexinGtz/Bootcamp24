class Car:
    def __init__(self, brand, model, year, acceleration, gas_efficiency = 7, speed = 0, gas_tank = 50):
        self.brand = brand
        self.model = model
        self.year = year
        self.acceleration = acceleration
        self.speed = speed
        self.gas_tank = gas_tank
        self.gas_efficiency = gas_efficiency
        self.time_spent = 0
    
    def accelerate(self, time = 0):
        print(f'Run ruuuuun {self.model}')
        future_speed = self.acceleration * time
        gas_consumption = self.calculate_gas_consumption(future_speed, time)
        if(self.gas_tank <= 0):
            print(f'Ya no tienes gasolina Krnal coche:{self.model}')
            return
        elif(gas_consumption > self.gas_tank):
            print(f'Te vas a acabar la gas si aceleras coche:{self.model}')
            return
        self.time_spent += time
        self.speed += future_speed
        self.gas_tank -= gas_consumption

    def break_car(self, time = 0):
        if(self.speed == 0):
            print(f'No puedes frenar coche:{self.model}')
            return
        print(f'Run ruuuuun {self.model}')
        self.time_spent += time
        self.speed -= self.acceleration * time

    def calculate_traveled_distance(self):
        return self.speed * self.time_spent
    
    def calculate_future_distance(self, speed, time):
        return speed * time
    
    def calculate_gas_consumption(self, speed, time):
        distance = self.calculate_future_distance(speed, time)
        gas_consumption = distance / self.gas_efficiency
        return gas_consumption
    
    def remaining_gas(self):
        return self.gas_tank
        
        
mustang = Car('Ford', 'mustang', '2020', 15)
focus = Car('Ford', 'focus', '2022', 8)

focus.accelerate(5)
mustang.accelerate(5)

print(focus.speed)
print(mustang.speed)

focus.break_car(2)
mustang.break_car(2)

print(mustang.speed)
print(focus.speed)

focus_distance = focus.calculate_traveled_distance()
mustang_distance = mustang.calculate_traveled_distance()

print(mustang_distance)
print(focus_distance)

print(mustang.remaining_gas())
print(focus.remaining_gas())

focus.accelerate(2)
mustang.accelerate(2)

print(focus.speed)
print(mustang.speed)

focus.break_car(1)
mustang.break_car(1)

print(focus.speed)
print(mustang.speed)

print(mustang.remaining_gas())
print(focus.remaining_gas())

print(focus.calculate_traveled_distance())
print(mustang.calculate_traveled_distance())