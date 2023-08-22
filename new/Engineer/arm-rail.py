def release():
    servo_ctrl.set_angle(2, 90, wait_for_complete=True)
    servo_ctrl.set_angle(3, -60, wait_for_complete=True)
    time.sleep(0.5)


def get_top():
    chassis_ctrl.set_pwm_value(rm_define.pwm1, 9.8)
    chassis_ctrl.set_pwm_value(rm_define.pwm2, 5.2)
    servo_ctrl.set_angle(3, -60, wait_for_complete=True)
    servo_ctrl.recenter(2, wait_for_complete=True)
    time.sleep(1)

    servo_ctrl.recenter(3, wait_for_complete=True)
    time.sleep(0.5)

    servo_ctrl.set_angle(2, -45, wait_for_complete=True)
    time.sleep(0.5)

    chassis_ctrl.set_pwm_value(rm_define.pwm1, 8.6)
    chassis_ctrl.set_pwm_value(rm_define.pwm2, 6.4)
    time.sleep(0.2)

def start():
    chassis_ctrl.set_pwm_value(rm_define.pwm_all, 7.5)
    servo_ctrl.recenter(1, wait_for_complete=True)
    servo_ctrl.recenter(3, wait_for_complete=True)
    servo_ctrl.set_angle(2, 70, wait_for_complete=True)
    time.sleep(0.5)

    get_top()

    release()

    servo_ctrl.set_speed(1, -240)
    servo_ctrl.set_angle(2, 45, wait_for_complete=False)
    servo_ctrl.recenter(3, wait_for_complete=False)
    time.sleep(2.5)
    servo_ctrl.recenter(1, wait_for_complete=False)
    servo_ctrl.set_angle(1, -15, wait_for_complete=True)

    get_top()

    servo_ctrl.set_speed(1, 240)
    servo_ctrl.set_angle(2, 45, wait_for_complete=False)
    servo_ctrl.recenter(3, wait_for_complete=False)
    time.sleep(2.5)
    servo_ctrl.recenter(1, wait_for_complete=False)

    release()

    servo_ctrl.set_speed(1, 240)
    servo_ctrl.set_angle(2, 45, wait_for_complete=False)
    servo_ctrl.recenter(3, wait_for_complete=False)
    time.sleep(2.5)
    servo_ctrl.recenter(1, wait_for_complete=True)
    servo_ctrl.set_angle(1, 15, wait_for_complete=True)
    time.sleep(0.3)

    get_top()

    servo_ctrl.set_speed(1, -240)
    servo_ctrl.set_angle(2, 45, wait_for_complete=False)
    servo_ctrl.recenter(3, wait_for_complete=False)
    time.sleep(2.5)
    servo_ctrl.recenter(1, wait_for_complete=True)

    release()

    time.sleep(5)
