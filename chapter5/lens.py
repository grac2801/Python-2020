
#Date: Nov 21, 2020
#ogracias
#Current Module: chapter5.lens
#AP Computer Science Principles

#imports




#functions
def lens(light, temperature):
    if(light < 0.01) or (temperature > 0.0):
        if not((light < 0.01) and (temperature > 0.0)):
            turn_camera_on()

def turn_camera_on():
    print('camera is on')

if __name__ == "__main__":
    lens(0.01, 5)
    
