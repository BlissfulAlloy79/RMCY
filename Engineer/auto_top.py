def grip_top():
    servo_ctrl.set_angle(3, 15, wait_for_complete=False)
    servo_ctrl.set_angle(2, -90, wait_for_complete=True)
    time.sleep(0.5)


def grip_pre_top():
    servo_ctrl.set_angle(3, -60, wait_for_complete=True)
    servo_ctrl.set_angle(2, -10, wait_for_complete=True)
    time.sleep(0.2)
    servo_ctrl.set_angle(1, -10, wait_for_complete=True)
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


def debug():
    servo_ctrl.recenter(1, wait_for_complete=True)
    servo_ctrl.recenter(2, wait_for_complete=True)
    servo_ctrl.recenter(3, wait_for_complete=True)
    servo_ctrl.set_angle(3, -90, wait_for_complete=True)
    time.sleep(1)


def get_top():
    grip_rest()

    grip_pre_top()
    grip_top()

    grip_drop()

    grip_rest()


def move_to_ammo():
    chassis_ctrl.set_trans_speed(1.7)
    chassis_ctrl.move_with_distance(0, 1)
    chassis_ctrl.move_with_time(180, 0.1)
    chassis_ctrl.move_with_distance(-90, 1.4)
    chassis_ctrl.move_with_distance(0, 0.4)
    chassis_ctrl.move_with_distance(-50, 2.5)

    chassis_ctrl.set_trans_speed(0.3)
    chassis_ctrl.move_with_time(0, 0.5)
    chassis_ctrl.move_with_time(-90, 0.5)

    chassis_ctrl.set_trans_speed(0.2)
    chassis_ctrl.move_with_time(0, 1.2)
    chassis_ctrl.move_with_time(-80, 1.2)
    chassis_ctrl.move_with_time(0, 1.2)


def start():
    # debug()
    grip_rest()

    move_to_ammo()
    get_top()

    chassis_ctrl.set_trans_speed(0.2)
    chassis_ctrl.move_with_distance(70, 0.4)

    get_top()

    chassis_ctrl.set_trans_speed(0.2)
    chassis_ctrl.move_with_distance(70, 0.4)

    get_top()
