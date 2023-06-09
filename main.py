
def on_gesture_screen_up():
    basic.show_icon(IconNames.TARGET)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_gesture_shake():
    basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_left():
    basic.show_icon(IconNames.SQUARE)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)
