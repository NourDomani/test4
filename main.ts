input.onButtonPressed(Button.A, function () {
    if (input.temperature() > 29) {
        basic.showLeds(`
            # # # # #
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            `)
    } else {
        basic.showNumber(input.temperature())
    }
})
basic.forever(function () {
    basic.showIcon(IconNames.SmallHeart)
})
