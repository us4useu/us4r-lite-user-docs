# First Use

:::{CAUTION}
Never unplug the probe from the device during transmission!
This can result in damage to the transmission unit of the us4R-lite™.
:::

Before first use of the **us4R-lite™**, you must ensure that:

-   the device has been set up according to Manufacturer guidelines
    found in section {numref}`Section %s <set-up/System setup>`,
-   proper probe adapter has been installed,
-   an external host PC and monitor have been connected to the **us4R-lite™**.

Step-by-step instruction:

1.  Connect the supplied power adapter to the **us4R-lite™** (DC jack) and to the mains (the power cable).
2.  Now, turn on the device by clicking the ON/OFF button.
3.  Connect the ultrasound probe.
4.  Turn on the host PC

    a.  Before login check the color of the LEDs on the back of the PC
        -- all 2 LED indicators (from the top and/or bottom card)
        should light up GREEN, see {numref}`pcie-cables-1234`.

```{figure} img/pcie-cables-1234.jpeg
:name: pcie-cables-1234
:alt: The PCIe card interface.

The host PC: the PCIe card interface with 2 connected PCIe cables and the PCIe links LEDs.
```

>IMPORTANT NOTE: If any of the LED indicators light up ORANGE, please reboot the PC. Keep rebooting until all LEDs are green.

5.  Log in to the host PC (in the case where us4us provides the host PC) using the following login and password:

    `user: us4us`
    
    `password: us4us`

6.  Make sure to check that the device and its software is starting
    correctly. If any errors are signaled by the device or messages
    displayed on screen, proceed according to instructions.

7.  Install the ARRUS package according to instructions available
    [here](https://us4useu.github.io/arrus-toolkit/content/installation/index.html#python) (if it is not already installed).

8.  Follow the instruction on how to run "plane wave imaging" example script available [here](https://us4useu.github.io/arrus-toolkit/content/installation/index.html#python). Please remember to use the provided configuration file.

9.  Once the test is over, close the image window.

10. The host PC can now be turned off by shutting down the Windows
    system as normal.

11. Turn off the **us4R-lite™** by pressing the ON/OFF button.

12. After 5 seconds turn off the Power Switch.

