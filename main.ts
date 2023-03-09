let Distance = 0
basic.showIcon(IconNames.Chessboard)
basic.forever(function () {
    Distance = Tinybit.Ultrasonic_Car()
    if (Distance < 30) {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Back, 100)
        basic.pause(100)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinRight, 125)
        basic.pause(100)
    } else {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 235)
        Tinybit.RGB_Car_Big(Tinybit.enColor.Cyan)
    }
})
