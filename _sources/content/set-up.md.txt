# Unboxing and setting-up the device

The device is delivered to the user pre-assembled and boxed.

The user must connect the components and perform a setup before the
first use (see: {numref}`Section %s <set-up/System setup>`.). The unboxing of the device should
be performed with utmost care.


:::{Caution}
If the device was placed in an environment with climatic conditions that sharply diverge from normal office conditions, it should undergo a process of acclimatization before the first use. This comprises of leaving the device out of the transport packaging for a minimum of 12 hours.
:::

The packaging should include:

-   **us4R™** device (with probe adapter) -- 1 pcs.;
-   PCIe cables -- 4 or 8 pcs.;
-   PCIe adapter card -- 1 or 2 pcs.;
-   mains power cable -- 1 pcs.;
-   PCIe cable ferrites -- 8 or 16 pcs.;
-   (optional) PC system controller -- 1 pcs.;
-   (optional) ultrasound probe(s).

In case of any missing items, the Customer is advised to contact the
Manufacturer.

Before the first use, it is necessary to ensure that the room has ample
space, stable ground and 120/230VAC mains power source with a protective
bonding.

The device should be placed to facilitate a safe operation: the power
cables must be neither strained nor hanging too loose in a manner that
may lead to tripping, wrenching out of cables or otherwise damaging them
through breaking or cutting.

Procedures using the **us4R™** should not be performed if the device is
in proximity to another working ultrasound device. Ultrasound probes can
cause interference, resulting in a falsification of the image.

A proper operation of the device is described in the next chapters of
this manual.

:::{Caution}
The power cable should be plugged into the 120V,60Hz or 230V,50Hz mains power supply with a protective bonding.
:::
## Power supply connection

:::{Caution}
The 120/230VAC power socket used to power the us4R™ must be equipped with a protective earth wire. It is imperative to ensure that the electrical system provides the fire protection required for the class I devices.
:::

A loss of mains power during operation will result in an immediate shutdown of the device. The us4R™ will enter standby mode
once the mains power is restored. ON/OFF button must be pressed to power the us4R™ back on. After power on the host PC must 
be restarted to restore the communication with the system.

:::{Caution}
To shut down the us4R™ in case of malfunction, remove the mains power cable from the electrical socket. The electrical sockets should be situated in proximity to the device and be easily accessible.
:::

(set-up/system-setup)=
(set-up/probe-adapters)=
## Probe Adapters

Several adapters are available for use with the **us4R™** system. Please
consult the list of adapters as shown below:

:::{list-table} Probe adapters 
:widths: 15 20 30
:header-rows: 1

*   - Options \*
    - Probes compatibility
    - Probe adapters
*   - 128 RX (4xus4OEM) 
    - up to 128-element probes (linear/array/convex) 
    - 
        - PAU (Ultrasonix Probe Adapter)
        - VPA (ATL/Philips Probe Adapter)
        - Custom Probe Adapter (on request)
*   - 192 RX (6xus4OEM) 
    - up to 192-element probes (linear/array/convex) 
    - 
        - EPA (Ultrasonix Probe Adapter)\**
        - PAU (Ultrasonix Probe Adapter)\**
        - VPA (ATL/Philips Probe Adapter)\**
        - Custom Probe Adapter (on request)
*   - 256 RX (8xus4OEM) 
    - up to 256-element probes (linear/array/convex) and up to 1024-element matrix-array probes
    - 
        - EPA (Ultrasonix Probe Adapter)
        - PAU (Ultrasonix Probe Adapter)
        - VPA (ATL/Philips Probe Adapter)
        - 2D MATRIX 2372 Vermon probe
        - Custom Probe Adapter (on request)
:::


*\* Switching between 4x, 6x and 8x us4OEM module options can be done by
the Manufacturer only.*

*\*\* Not easily interchangeable! If you plan to use probes above 128
elements from various manufacturers (e.g. Esaote and Philips probes) please contact us4us to find the best
solution for you.*

If you cannot find the adapter that suits your application, it is
possible to order a custom probe adapter from the us4us®. Please contact
us at <support@us4us.eu> to discuss the options.

(set-up/system-setup)=
(set-up/System setup)=
## System setup

The **us4R™** should be positioned so that operation is safe --- i.e. on
a stable, flat surface in a place with no risk of spillage on the device
and away from the sources of interference and radiation. To limit unintentional radiation from the device, ferrites for PCIe cables should be mounted on each cable, on both sides of the PCIe cable and as close to the connectors as possible. The external
power supply and/or power strip should be placed nearby the device. 

For more details
see section: {numref}`Section %s <hardware/general>`.

The heat is dissipating by the **us4R™**  system during normal work
conditions and may slightly increase the temperature of the device
surroundings. The ventilation holes on each side of the device must
remain uncovered to ensure free flow of air. Covering the ventilation
holes risks overheating, shutting down or damaging the **us4R™.** The
power and probe cables must not be strained or hang too loosely in a
manner that may lead to tripping, mechanical damage, wrenching the
cables out of the socket and/or damaging them through breaking or
cutting. The audio frequency noise is coming from the fans and sometimes
from the HV power supply during transmit during normal work conditions.

Please consult the Manufacturer guidelines in section {numref}`Section %s <manufacturer-guidelines>`.

## Firmware and software

For the firmware update and software installation, follow the instructions available
[here](https://us4useu.github.io/arrus-toolkit/content/installation/index.html).

Links to the ARRUS™ SDK package documentation are available
[here](https://github.com/us4useu/arrus).



