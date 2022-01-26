from dd_gpio import DD_GPIO, GPIO_INPUT, GPIO_OUTPUT
import time

if __name__ == '__main__':

    gpio = DD_GPIO()
    pin = GPIO_OUTPUT

    gpio.write(pin.ADC0, pin.HIGH)
    gpio.write(pin.ADC1, pin.HIGH)
    toggle = False

    while True:
        state = int(gpio.read(GPIO_INPUT.ADC5))

        if(state):
            if not (toggle): # this runs if the lights are currently green (or default state)
                gpio.write(pin.ADC0, pin.HIGH)
                gpio.write(pin.ADC1, pin.LOW)
                time.sleep(2)
                gpio.write(pin.ADC0, pin.LOW)
                gpio.write(pin.ADC1, pin.HIGH)
            
            if(toggle): # this runs if the lights are currently red
                gpio.write(pin.ADC0, pin.LOW)
                gpio.write(pin.ADC1, pin.LOW)
                time.sleep(2)
                gpio.write(pin.ADC0, pin.HIGH)
                gpio.write(pin.ADC1, pin.HIGH)
            
            toggle = not toggle

