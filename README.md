# Communication with Shimano batteries to enable their free use

The Shimano BT-E60xx batteries use an UART protocol between the battery and the motor controller or the charger. I made this tool to listen to it, record it, and be able to play it back and so enable the charging and discharging of these batteries without origial Shimano equipment.

The surely compatible batteries:
* BT-E6000
* BT-E6001
* BT-E6010

I strongly suspect that the BT-E80xx series is also compatible, but I didn't test due to lack of connector.
* BT-E8010
* BT-E8014
* BT-E8016
* BT-E8035
* BT-E8036

I suspect the compatibility because they can be charged with the same chargers.

The repo contains a recorded communication set already, so you can use it with batteries even if you do not have a bike to record from.

## How to set up on a Raspberry Pi
Connect the UART and run the python script. When the script starts running, the LEDs come on on the battery, and the power connectors are now enabled both for charging and discharging.

I used this to measure the capacity of used batteries with a battery tester, and also to charge the batteries with a desktop power supply. I 3D printed a custom connector as seen on the photos, I'll publish that too shortly.

*Please note that batteries are dangerous and you play at your own risk.*

![pins](https://github.com/user-attachments/assets/fafd0416-462b-4f29-a352-17530809f230)
![IMG_2281](https://github.com/user-attachments/assets/16cef52e-e884-42de-8016-8ee6cbbb2f04)
