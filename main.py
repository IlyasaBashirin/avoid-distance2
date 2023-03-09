Distance = 0
basic.show_icon(IconNames.CHESSBOARD)

def on_forever():
    global Distance
    Distance = Tinybit.Ultrasonic_Car()
    if Distance < 30:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_BACK, 100)
        basic.pause(100)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINRIGHT, 125)
        basic.pause(100)
    else:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 235)
        Tinybit.RGB_Car_Big(Tinybit.enColor.CYAN)
basic.forever(on_forever)
