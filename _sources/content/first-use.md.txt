# First Use

## Unboxing and setting-up the device

The device is delivered to the user pre-assembled and boxed.

The user must connect the components and perform a setup before the
first use (see: {numref}`Section %s <setup/system-setup>`.). The unboxing of the device should
be performed with utmost care.

:::{Caution}
If the device was placed in an environment with climatic conditions that sharply diverge from normal office conditions, it should undergo a process of acclimatization before the first use. This comprises of leaving the device out of the transport packaging for a minimum of 12 hours.
:::

The packaging should include:

-   **us4R-lite™** device (with a selected probe adapter) -- 1 pcs.;
-   power brick supply (AC/DC) -- 1 pcs.
-   for model with PCIe interface:
    -   PCIe host adapter card -- 1 pcs.;
    -   PCIe cables + ferrites -- 2 pcs.;
-   for model with Thunderbolt interface:
    -   Thunderbolt cable -- 1 pcs.;
-   (optional) PC system controller -- 1 pcs.;
-   (optional) ultrasound probe(s).

In case of any missing items, the Customer is advised to contact the Manufacturer.

Before the first use, it is necessary to ensure that the room has ample space, stable ground and 120/230VAC mains power source with a protective bonding.

The device should be placed to facilitate a safe operation: the power
cables must be neither strained nor hanging too loose in a manner that
may lead to tripping, wrenching out of cables or otherwise damaging them
through breaking or cutting.

Procedures using the **us4R-lite™** should not be performed if the device is in proximity to another working ultrasound device. Ultrasound probes can cause interference, resulting in a falsification of the image.

A proper operation of the device is described in the next chapters of this manual.

:::{Caution}
The power cable should be plugged into the 120V,60Hz or 230V,50Hz mains power supply with a protective bonding.
:::
## Power supply connection

<!-- :::{Caution}
The 120/230VAC power socket used to power the us4R-lite™ must be equipped with a protective earth wire. It is imperative to ensure that the electrical system provides the fire protection required for the class I devices.
::: -->

A loss of mains power during operation will result in an immediate shutdown of the device. The us4R-lite™ will enter standby mode once the mains power is restored. ON/OFF button must be pressed to power the us4R-lite™ back on. After power on the host PC must be restarted to restore the communication with the system.

:::{Caution}
To shut down the us4R-lite™ in case of malfunction, remove the mains power cable from the electrical socket. The electrical sockets should be situated in proximity to the device and be easily accessible.
:::

(set-up/system-setup)=
(set-up/probe-adapters)=
## Probe Adapters

Several adapters are available for use with the **us4R-lite™** system. Please consult the list of adapters as shown below:

:::{list-table} Probe adapters 
:widths: 15 20 30
:header-rows: 1

*   - Probes compatibility
    - Probe adapters
*   - up to 128-element probes (linear/array/convex) 
        - PAU (Ultrasonix Probe Adapter)
        - VPA (ATL/Philips Probe Adapter)
        - Custom Probe Adapter (on request)
*   - up to 192-element probes (linear/array/convex) 
        - EPA (Esaote Probe Adapter)
        - Custom Probe Adapter (on request)
*   - up to 256-element probes (linear/array/convex)
        - GE (GE Probe Adapter)
        - Custom Probe Adapter (on request)
:::

If you cannot find the adapter that suits your application, it is possible to order a custom probe adapter from the us4us®. Please contact us at <support@us4us.eu> to discuss the options.


(set-up/System setup)=
## System setup

The **us4R-lite™** should be positioned so that operation is safe --- i.e. on a stable, flat surface in a place with no risk of spillage on the device and away from the sources of interference and radiation. 
To limit unintentional radiation from the device, the provided ferrites for PCIe cables should be mounted on each cable, on both ends of the cable and as close to the connectors as possible. The external power supply and/or power strip should be placed nearby the device. 

<!-- For more details see section: {numref}`Section %s <hardware/general>`. -->

The heat is dissipating by the **us4R-lite™** system during normal work conditions and may slightly increase the temperature of the device surroundings. The ventilation holes on each side of the device must remain uncovered to ensure free flow of air. Covering the ventilation holes risks overheating, shutting down or damaging the **us4R-lite™.** The power and probe cables must not be strained or hang too loosely in a manner that may lead to tripping, mechanical damage, wrenching the cables out of the socket and/or damaging them through breaking or
cutting. The audio frequency noise is coming from the fans and sometimes
from the HV power supply during transmit during normal work conditions.

<!-- Please consult the Manufacturer guidelines in section {numref}`Section %s <manufacturer-guidelines>`. -->

## Firmware and software

For the firmware update and software installation, follow the instructions available
[here](https://us4useu.github.io/arrus-toolkit/content/installation/index.html).

Links to the ARRUS™ SDK package documentation are available
[here](https://github.com/us4useu/arrus).


(setup/system-setup)=
## System Setup

:::{CAUTION}
Never unplug the probe from the device during transmission!
This can result in damage to the transmission unit of the us4R-lite™.
:::

Before first use of the **us4R-lite™**, you must ensure that:

* the device has been set up according to Manufacturer guidelines,
* proper probe adapter has been installed,
* an external host PC have been connected to the **us4R-lite™**.

Step-by-step instruction:

1.  Connect the supplied power adapter to the **us4R-lite™** (DC jack) and to the mains (the power cable).
1.  Connect the ultrasound probe.
1.  Now, turn on the device by clicking the ON/OFF button.
1.  Turn on the host PC

    a.  Before login check the color of the LEDs on the back of the PC
        -- all 2 LED indicators (from the top and/or bottom card)
        should light up GREEN, see {numref}`pcie-cables-1234`.

```{figure} img/pcie-cables-1234.jpg
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
