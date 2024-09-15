# EV-DataLogger

This project is part of an effort by the University of Portland's EV Club to use a Raspberry PI 5 as a fully functioning datalogger and display driver for an electric go-kart.

To fufill this goal, this project must accomplish the following:
 - Utilize a CANOpen library in conjunction with a Waveshare CAN HAT adapter for the PI to communicate with the SEVCON and BMS systems
 - Record live data from both the BMS and SEVCON into non-volatile memory.
 - Sort and appropriately display live data to an HDMI display in an easy to read format.

Long-term goal(s):
 - Manage I/O from driver and change corresponding settings via CAN network.