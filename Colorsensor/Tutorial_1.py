from ev3robot import *

robot = LegoRobot()

#redefine black color cube
ColorSensor.colorCubes[0]=[0,20,0,20,0,10]

#redefine blue color cube
ColorSensor.colorCubes[4]=[10,20,10,15,15,20]

#redefine green color cube
ColorSensor.colorCubes[2]=[35,40,45,53,10,17]

#redefine yellow color cube
ColorSensor.colorCubes[3]=[85,95,60,73,5,15]

#redefine red color cube
ColorSensor.colorCubes[4]=[40,100,5,25,5,25]

#redefine white color cube
ColorSensor.colorCubes[5]=[90,105,60,80,60,75]

#black[0],blue[1],green[2],yellow[3],red[4],white[5]

fs = ColorSensor(SensorPort.S3)
robot.addPart(fs)

for i in range(6):
    print ColorSensor.colorCubes[i]

while not robot.isEscapeHit():
    c = fs.getColor()
    colorName = fs.getColorStr()
    
    print c.getRed(), c.getGreen(), c.getBlue(),colorName
    
    robot.drawString(colorName,0,0)
    Tools.delay(300)
    

robot.exit()