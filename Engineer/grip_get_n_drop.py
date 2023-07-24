def grip_top():
    servo_ctrl.set_angle(3, 20, wait_for_complete=False)
    servo_ctrl.set_angle(2, -90, wait_for_complete=True)
    time.sleep(0.5)


def grip_bot():
    servo_ctrl.set_angle(1, -85, wait_for_complete=True)
    servo_ctrl.set_angle(3, 20, wait_for_complete=True)
    servo_ctrl.set_angle(1, -45, wait_for_complete=False)
    servo_ctrl.set_angle(2, 45, wait_for_complete=True)


def grip_drop():
    servo_ctrl.set_angle(1, 20, wait_for_complete=False)
    servo_ctrl.set_angle(2, 115, wait_for_complete=True)
    servo_ctrl.set_angle(3, -60, wait_for_complete=True)
    time.sleep(0.5)


def start():
    if (0 >= servo_ctrl.get_angle(1) >= -20) and (-5 >= servo_ctrl.get_angle(2) >= -25):
        grip_top()
        # grip_bot()

    grip_drop()
