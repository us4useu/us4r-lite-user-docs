(hardware/general)=
# Hardware Description

(system-overview)=
## System Overview

The us4R-lite™ system is an ultrasound research device designed for transmission and acquisition of ultrasound signals using connected piezoceramic probes/transducers.

**The us4R-lite™ is a peripheral device, so in addition to an ultrasound probe, it always requires an external Host PC to work.**

The us4R-lite™ is connected using a Thunderbolt-3 ({numref}`peripheral-notebook`) or PCIe cable ({numref}`peripheral-desktop`) to a PC/notebook running ARRUS™ SDK. 
An open-source ARRUS™ SDK (Software Development Kit) is provided to be installed and run on the host PC to execute User’s applications/scripting for device configuration, data acquisition, and custom processing.

```{figure} img/peripheral-notebook.png
:name: peripheral-notebook
Peripheral mode with external Host PC connected through Thunderbolt, us4R-lite™, Model: RL-2020 <span style="color:red">(EOL)</span>
```
```{figure} img/peripheral-desktop.png
:name: peripheral-desktop
Peripheral mode with external Host PC connected through PCIe, us4R-lite™, Model: RL-2021
```

(hardware/versions)=
## Hardware Models
The table below summarizes all hardware models of the us4R-lite™:

:::{list-table} us4R-lite™ Hardware Models
:header-rows: 1

*   - Model
    - Options
    - External Interface
*   - RL_2020
         <span style="color:red">(EOL)</span>
    - +GPU (NO LONGER SUPPORTED)
    - Thunderbolt-3
*   - RL_2021
        (OBSOLETE)
    - none
    - PCIe (2x gen3 4-lanes)
*   - RL-2024-PCIe
    - +HF
    - PCIe (2x gen3 4-lanes)
:::

(hardware/probe-adapters)=
## Ultrasound Probe Adapters

Us4R-lite™ research system features changeable ultrasound probe adapter.
Currently, we offer the following adapters:

:::{list-table} Probe adapters 
   :widths: 20 20 50 20 20
   :header-rows: 1

*   - Connector <br>
        Type
    - Name
    - Rev
    - Supported Probes
    - List of tested probes
*   - QLC-260
    - EPA
    - 3.0
    - ESAOTE compatible <br>
    _up to 192-element probes <br>
    (linear/array/convex)_
    - 
        - SL1543 linear-array
        - AL2442 linear-array
        - SP2430 phased-array
        - AC2541 convex-array
*   - DL1-156
    - PAU
    - 1.0
    - ULTRASONIX compatible <br>
    _[up to 128-element probes (linear/array/convex)]_
    - 
        - L14-5/38 linear-array
        - L9-4/38 linear-array
*   - DL5-260
    - VPA
    - 1.0
    - ATL / Philips compatible <br>
    _[up to 128-element probes (linear/array/convex)]_<br>
    _in-probe MUX is not supported!_
    - 
        - L7-4/38 linear-array
        - C5-2 convex-array
*   - DLP-408
    - DLPx
    - 2.0
    - GE compatible <br>
    RCA compatible <br>
    _[up to 256-element probes (linear/array/convex/row-column)]_
    - 
        - GE..LLL
        - RCA..LLL

:::


If you cannot find the adapter that suits your application, it is possible to order a custom probe adapter from the us4us®. Please contact us at <support@us4us.eu> to discuss the options.


:::{Note}
The system is supplied with one selected probe adapter. 
Additional adapters can be purchased separately.
:::

(inputs-outputs)=
## Inputs and outputs

The **us4R-lite™** is equipped with:

-   a single probe connector,
-   2x PCIe ports (see {numref}`us4r-lite-pcie-back-rl-2024`) or Thunderbolt-3 port ,
-   2x digital inputs (TRIG-IN, CLK-IN),
-   2x digital outputs (TRIG-OUT, CLK-OUT),
-   1x DC power input.

```{figure} img/us4r-lite-pcie-back-rl-2024.jpg
:name: us4r-lite-pcie-back-rl-2024
:alt: Back-side of the us4R-lite™ device with PCIe interface. 
:width: 60 %
Back-side of the us4R-lite™, Model: RL-2024-PCIe device with PCIe interface.
```

**PLEASE NOTE:** External devices should be connected via cables no longer than 3m.

(hardware/power-switch)=
## Power adapter and ON/OFF button

The power adapter connection is shown in the picture below ({numref}`us4r-lite-pcie-power-rl-2024`).

```{figure} img/us4r-lite-pcie-power-rl-2024.jpg
:name: us4r-lite-pcie-power-rl-2024
:alt: The us4R-lite™, model RL-2024-PCIe DC power connector and ON/OFF button.
:width: 60 %
The us4R-lite™, model RL-2024-PCIe DC power connector and ON/OFF button.
```

## Connecting ultrasound probes

Ultrasound probes require special care, as they can be easily damaged by any impact. The damaged transducers could have internal element short-circuits or open-circuits, both can cause malfunction or even
breakdown of the **us4R-lite™** transmit circuitry. 
**Therefore, it is vital that the probes are handled with extreme care and defective probes are never connected to the system.**

Probes should be disconnected from the device during the transport.

The ultrasound probe connector is situated on the top of the device.

```{figure} img/us4r-lite-probe-conn.jpg
:name: us4r-lite-probe-conn
:alt: Top-view of the us4R-lite™ model RL_2020 with probe connector (linear/phase/convex/RCA).
:width: 60 %
Top-view of the us4R-lite™ model RL_2020 with probe connector (linear/phase/convex/RCA).
```

A video instruction on how to change the probe adapter is available on our YouTube channel:

[![A picture containing text, electronics, display Description automatically generated](img/us4r-lite-change-adapter-video.png)](https://www.youtube.com/watch?v=v9DwhbGclBE)

**PLEASE NOTE:** Only a probe prepared and configured for use with the **us4R-lite™** can be connected to the device. For assistance, please contact the Manufacturer.

```{Caution}
Using non-compatible or broken probes can result in damage to the transmission section of the us4R-lite™!
Such damages are NOT covered under the warranty!
```
(hardware/connecting-hostPC)=
## Connecting the host PC
The **us4R-lite™** requires an external host PC (desktop / notebook) with a display to function correctly. The only way to connect the **us4R-lite™** device to the PC is through the PCIe or Thunderbolt cables (depending on the model).

So far, it is required that the host PC be equipped with an NVIDIA GPU with CUDA Toolkit installed and, for PCIe connections, an available PCIe Gen3 x8 slot to install the provided PCIe host adapter card.



### PCIe interface

(hardware/pcie-ports)=
**PCIe ports & PCIe cables** <br> 
The **us4R-lite™** models: RL_2021 and RL-2024-PCIe are equipped with 2x PCIe gen3 x4 ports on the back of the device.

The PCIe ports are intended for connecting the system to an external host PC using the provided PCIe cables ({numref}`us4r-lite-pcie-back-rl-2024+cables`). 

 ```{figure} img/us4r-lite-pcie-back-rl-2024+cables.jpg
:name: us4r-lite-pcie-back-rl-2024+cables
:width: 60 %
Back panel of the us4R-lite™ showing the PCIe connectors and properly connected cabling. 
```

When connecting the PCIe cables you should hear/feel "a click" to be
sure that the connector is latched properly ({numref}`us4r-lite-pcie-back-rl-2024+cables`).

**PCIe adapter card** <br>
The **us4R-lite™** models equiped with the PCIe interface are also provided with compatible PCIe host adapter card that should be properly installed in the host PC controller before the first use. 

The host PC must have an empty PCIe gen3 x8 slot to install the provided
PCIe host adapter card ({numref}`pcie-adapter-gen3`). 

```{figure} img/pcie-adapter-gen3.jpg
:name: pcie-adapter-gen3
:width: 60 %
Provided PCIe host adapter card for the us4R-lite-PCIe.
```

To proper install the PXH832 PCIe adapter cards follow the instructions available [here](https://www.dolphinics.com/download/PX/OPEN_DOC/PXH832_users_guide.pdf). Ensure that the DIP switch configuration shown in Table 3 of the referenced document is set to Transparent Host, Four x4 Ports (all switches in the position closer to the PCIe connector.).

**The proper order of the PCIe cables doesn't matter if you configure your DIP-Switches on the PXH832 card properly!**

To disconnect the PCIe cables pull the plastic tab at the bottom of the PCIe cable plug ({numref}`host-PC-back-rl-2024+cables`).

```{figure} img/host-PC-back-rl-2024+cables.jpg
:name: host-PC-back-rl-2024+cables
:width: 60 %
Back of the host PC with PCIe host adapter card installed and PCIe cables connected.
```

## Digital I/O ports

The **us4R-lite™** provides four digital I/O signals in the LVTTL 3.3V
standard available on the SMA-type connectors:

1.  CLOCK IN -- input of an external reference clock signal.
2.  TRIG IN -- input of an external trigger signal -- can be used to
    synchronize transmit events with other devices/systems.
3.  CLOCK OUT -- output of an internal reference clock signal.
4.  TRIG OUT -- output of an internal trigger signal -- can be used to synchronize other external devices/systems with the **us4R-lite™**.

```{figure} img/us4r-lite-pcie-back-io-rl-2024.jpg
:name: us4r-lite-pcie-back-io-rl-2024
:width: 60 %
Back panel of the us4R-lite™, model RL-2024-PCIe showing the 4x digital I/O signals
```


