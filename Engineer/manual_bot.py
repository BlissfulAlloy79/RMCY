def grip_bot():
    servo_ctrl.set_angle(2, 10, wait_for_complete=False)
    servo_ctrl.set_angle(1, -85, wait_for_complete=True)
    servo_ctrl.set_angle(3, 20, wait_for_complete=True)
    servo_ctrl.set_angle(1, -45, wait_for_complete=False)
    servo_ctrl.set_angle(2, 45, wait_for_complete=True)


def grip_pre_bot():
    servo_ctrl.set_angle(3, -60, wait_for_complete=True)
    servo_ctrl.set_angle(2, 45, wait_for_complete=True)
    servo_ctrl.set_angle(1, -45, wait_for_complete=True)
    time.sleep(0.5)


def grip_drop():
    servo_ctrl.set_angle(1, 20, wait_for_complete=False)
    servo_ctrl.set_angle(2, 115, wait_for_complete=True)
    servo_ctrl.set_angle(3, -60, wait_for_complete=True)
    time.sleep(0.5)


def grip_rest():
    if servo_ctrl.get_angle(1) <= 65 or not (10 >= servo_ctrl.get_angle(2) >= -10):
        servo_ctrl.recenter(1, wait_for_complete=True)
        time.sleep(0.5)
        servo_ctrl.set_angle(2, 0, wait_for_complete=True)
        servo_ctrl.set_angle(1, 75, wait_for_complete=True)
        time.sleep(0.5)


def start():
    chassis_ctrl.enable_stick_overlay()
    grip_rest()

    grip_pre_bot()
    tools.timer_ctrl(rm_define.timer_start)
    while True:
        if tools.timer_current() >= 3:
            tools.timer_ctrl(rm_define.timer_stop)
            break

    grip_bot()
    grip_drop()

    grip_rest()
