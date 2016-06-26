# electrobrain
A python script to creatively illuminate "LED copper wire" lights using the Raspberry Pi's PWM GPIO pins. (As the Pi will live inside a head-shaped glass jar, it got the name "electrobrain")
Quick and crappy video may be available [here] (https://www.facebook.com/mmdc.net/videos/979343528845213/) but I'm not sure if my Facebook settings will allow you to see it.
[image](electrobrain.jpeg)
I'm starting out with a script by Alex Eames (http://RasPi.tv) that I found for working with PWM on the Raspberry Pi
	see: http://RasPi.tv/2013/how-to-use-soft-pwm-in-rpi-gpio-pt-2-led-dimming-and-motor-speed-control 
The script is a simple way to incrementally dim and brighten an LED that's attached to (and powered by)the Pi's PWM-capable GPIO pins.

The original demo I saw used a simple LED, but I recently happened upon some "[LED Copper Wire](http://www.ebay.com/itm/Warm-White-Battery-Powered-100LEDs-Copper-Wire-Xmas-Party-String-Fairy-Light-10M-/141768650258?hash=item210211ee12:g:K68AAOSwQPlV7khq)" strings in a shop and bought them on impulse, knowing I might do something cool with them.  They're made from a pair of very thin strands of varnished wire with tiny surface-mount LEDs attached every few inches, with a blob of some sort of resin covering each LED, which both protects the LED and acts like a diffuser. The strings can be cut to desired lengths.

Strobing the LED strands has a very pleasing effect. The wires have just a bit of stiffness, so they are easy to form and keep their shape a bit.

The glass head we are using is the kind commonly used as a hat stand or for sunglasses.  A quick eBay search:
http://www.ebay.com/sch/i.html?_odkw=hollow+glass+head&_osacat=0&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xhollow+glass+mannequin+head.TRS0&_nkw=hollow+glass+mannequin+head&_sacat=0

The goal of this project is to combine several strands of lights to make a passive informational display. So far, I've gotten it to watch system load and have the lights go nuts when the load gets high.