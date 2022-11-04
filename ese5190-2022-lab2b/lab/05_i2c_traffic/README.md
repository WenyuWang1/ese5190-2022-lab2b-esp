# I2C on Oscilloscope
To check the I2C pins' waveforms on the oscilloscope, we use our Lab 1 firefly code to generate ADPS9960 I2C traffic and display it on a lab oscilloscope to confirm that the I2C communication is active (taking place) between the QT Py (KB2040 and sensor (APDS-9960). This can be done by flashinging the 'firefly' code on to the QT Py, which in ture is connected to the sensor (APDS-9960). In this lab, we connect the first probe to SCL (CLK or clock) while the associated black wire to ground of the microcontroller. Similarly, the second probe is connected to SDA while the associated black wire to ground.

## Circuit Setup

![confi](https://user-images.githubusercontent.com/113371324/200063827-37c6f682-93bc-4c75-bea5-8db3a01acfae.jpg)

## Resulting waveform
![1](https://user-images.githubusercontent.com/113371324/200064097-499057a3-510d-4f92-be52-026371e8bdde.jpg)

![2](https://user-images.githubusercontent.com/113371324/200064108-e133a4a0-7c59-4602-81c6-622c28f040cd.jpg)


