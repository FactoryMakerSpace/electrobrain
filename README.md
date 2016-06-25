# electrobrain
A python script to creatively illuminate "LED copper wire" lights using the Raspberry Pi's PWM GPIO pins. (As the Pi will live inside a head-shaped glass jar, it got the name "electrobrain")

I'm starting out with a script by Alex Eames (http://RasPi.tv) that I found for working with PWM on the Raspberry Pi
	see: http://RasPi.tv/2013/how-to-use-soft-pwm-in-rpi-gpio-pt-2-led-dimming-and-motor-speed-control 
The script is a simple way to incrementally dim and brighten an LED that's attached to (and powered by)the Pi's PWM-capable GPIO pins.

The original demo I saw used a simple LED, but I recently happened upon some "LED Copper Wire" strings in a shop and bought them on impulse, knowing I could do something cool with them.  They're made from a pair of very thin strands of varnished wire with tiny surface-mount LEDs attached ecery few inches, with a blob od some sort of resin covering each LED, which both protects the LED and acts like a diffuser. The strings can be cut to desired lengths.

Strobing the LED strands has a very pleasing effect. The wires have just a bit of stiffness, so they are easy to form and keep their shape a bit.

The glass head we are using is the kind commonly used as a hat stand or for sunglasses.  A quick eBay search:
http://www.ebay.com/sch/i.html?_odkw=hollow+glass+head&_osacat=0&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xhollow+glass+mannequin+head.TRS0&_nkw=hollow+glass+mannequin+head&_sacat=0

The goal of this project is to combine several strands of lights to make a passive informational display.