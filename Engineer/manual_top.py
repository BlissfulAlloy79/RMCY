def grip_pre_top():
    servo_ctrl.set_angle(3, -60, wait_for_complete=True)
    servo_ctrl.set_angle(2, -10, wait_for_complete=True)
    time.sleep(0.2)
    servo_ctrl.set_angle(1, -10, wait_for_complete=True)
    time.sleep(0.5)


def grip_top():
    servo_ctrl.set_angle(3, 15, wait_for_complete=False)
    servo_ctrl.set_angle(2, -90, wait_for_complete=True)
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
    grip_rest()

    grip_pre_top()

    grip_top()
    grip_drop()

    grip_rest()

