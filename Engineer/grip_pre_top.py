def grip_pre_top():
    servo_ctrl.set_angle(3, -60, wait_for_complete=True)
    servo_ctrl.set_angle(2, -15, wait_for_complete=True)
    servo_ctrl.set_angle(1, -10, wait_for_complete=True)
    time.sleep(0.5)


def grip_rest():
    if servo_ctrl.get_angle(1) <= 65 or (80 >= servo_ctrl.get_angle(2) >= 100):
        servo_ctrl.recenter(1, wait_for_complete=True)
        time.sleep(0.5)
        servo_ctrl.set_angle(2, 90, wait_for_complete=True)
        servo_ctrl.set_angle(1, 75, wait_for_complete=True)


def start():
    grip_rest()
    time.sleep(0.5)

    grip_pre_top()
