import RPi.GPIO as GPIO
import time
import curses
import picamera
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

camera = picamera.PiCamera()
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

GPIO.output(7, False)
GPIO.output(11, False)
GPIO.output(13, False)
GPIO.output(15, False)
camera.start_recording('robovid.h264')
try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                camera.stop_recording()
                break
            elif char == curses.KEY_UP:
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,False)
                GPIO.output(15,True)
            elif char == curses.KEY_DOWN:
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,True)
                GPIO.output(15,False)
            elif char == curses.KEY_RIGHT:
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,True)
            elif char == curses.KEY_LEFT:
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,True)
                GPIO.output(15,False)
            elif char == ord('d'):
                for i in range(0,4):
                    GPIO.output(11,True)
                    GPIO.output(15,True)
                    time.sleep(2)
                    GPIO.output(11,False)
                    GPIO.output(15,False)
                    time.sleep(0.5)
                    GPIO.output(11,True)
                    GPIO.output(13,True)
                    time.sleep(0.97)
                    GPIO.output(11,False)
                    GPIO.output(13,False)
            elif char == ord('s'):
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()