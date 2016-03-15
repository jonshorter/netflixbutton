# netflixbutton
Use raspberry pi 2 as a VPN client gateway, with connect switch and status LED
(A raspberry pi 2 can manage just enough throughput for streaming - the speed constraint is the processing power required for the encryption/decryption)

## Software Requirements

Configure openVPN first, using this guide...
https://gist.github.com/superjamie/ac55b6d2c080582a3e64

## Hardware Requirements

Connect an LED (remember to use an appropriate resistor and observer correct polarity) between pins 17 and GND
Connect a momentary push-switch between pins 18 and GND
