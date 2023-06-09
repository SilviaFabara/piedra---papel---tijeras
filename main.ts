input.onGesture(Gesture.ScreenUp, function () {
    basic.showIcon(IconNames.Target)
})
input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.Scissors)
})
input.onGesture(Gesture.TiltLeft, function () {
    basic.showIcon(IconNames.Square)
})
