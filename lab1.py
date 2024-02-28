import ev3dev2.motor as motor
import time
motor_a = motor.LargeMotor(motor.OUTPUT_B)
voltages = [100, 80, 60, 40, 20, -20, -40, -60, -80]
for vol in voltages:
        timeStart = time.time()
        startPos = motor_a.position
        name = "newdata" + str(vol) + ".csv"
        file = open(name,'w')
        while (True):
            currentTime = time.time() - timeStart
            motor_pose = motor_a.position
            motor_vel = motor_a.speed
            motor_a.run_direct(duty_cycle_sp = vol)
            file.write(str(currentTime) + "," + str(motor_pose) + "," + str(motor_vel) + "\n")
            if currentTime > 1:
                motor_a.run_direct(duty_cycle_sp = 0)
                time.sleep(3)
                break