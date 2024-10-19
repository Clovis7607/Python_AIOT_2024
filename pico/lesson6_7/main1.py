from machine import Pin, PWM, ADC

tools.connect()

pwm = PWM(Pin(15))
adc = ADC(Pin(26))

pwm.freq(2000)

while True:
    duty = adc.read_u16()
    pwm.duty_u16(duty)
    print(f"{duty}")



# import machine
# import utime
# 
# sensor_temp = machine.ADC(4)
# conversion_factor = 3.3 / (65535)
# 
# while True:
#     reading = sensor_temp.read_u16() * conversion_factor
# 
#     # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
#     # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.
#     temperature = 27 - (reading - 0.706)/0.001721
#     print(temperature)
#     utime.sleep(2)