class Fish:
    def swim(self):
        print("Swimming under water")
    
    def breath(self):
        print("Breathing under water")
        
    def eat(self):
        print("Eating sea plants")
        
class Shark(Fish):
    def kill(self):
        print("Killing other fishes")
    
    def eat(self):
        super().eat()
        print("Eating killed fishes")
        
class WhiteShark(Shark):
    def jump(self):
        print("Jumps outside water")
        
class Hunter():
    def hunt(self):
        print("Hunt other fishes")
        
    def eat(self):
        print("Eating hunted fishes")
        
class Wheal(Fish, Hunter):
    def sleep(self):
        print("sleeping under the water")
        
koi = Fish()
koi.swim()
koi.breath()
koi.eat()

bs = Shark()
bs.kill()
bs.swim()
bs.breath()
bs.eat()

ws = WhiteShark()
ws.swim()
ws.breath()
ws.kill()
ws.eat()
ws.jump()

wl = Wheal()
wl.swim()
wl.hunt()
wl.eat()
