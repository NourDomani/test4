def on_button_pressed_a():
    if input.temperature() > 29:
        basic.show_leds("""
            # # # # #
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            """)
    else:
        basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_icon(IconNames.SMALL_HEART)
basic.forever(on_forever)
