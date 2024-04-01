# Technical specification

## Technical data

-   Ultrasound frequencies up to 20 MHz (Model: R-2021) or up to 30MHz (Model: R-2023);
-   Mains power supply 120V,60Hz / 230V,50Hz ±10%
-   Power consumption (average) 70W
-   Power consumption (max) 90W (max power of the us4R-lite power supply)
-   Product Dimensions (DxWxH) [mm]: 264 x 445 × 154\* mm

> *\*high without probe adapter; total high may slightly differ
> depending on the installed Probe Adapter: +37mm (EPA),
> +50mm (PAU), +38mm (VPA)*

-   Weight 10.5 kg

## Basic Composition

-   the **us4R-lite™** device (with probe adapter)
-   for PCIe model:
  -   1x PCIe host adapter card
  -   4x PCIe cable
  -   1x power adapter AC/DC
-   for Thunderbolt model:
  -   1x Thunderbolt cable
-   (optional) ultrasound probe
-   (optional) PC system controller with GPU cards
-   User Manual (on-line)

## Detailed specification

:::{list-table} 
:widths: 15 35
:align: left
* - **Transmit**
  - 
* - Number of channels
  - 256
* - Transmit frequency
  - up to 20MHz (Model: R-2021); up to 30MHz (Model: R-2023)
* - Tx time delay resolution
  - up to 5 ns (depends on the system clock)
* - Programmable TX voltage
  - up to 180Vpp (±90V) 
* - TX pulsers levels
  - 3 (Model: R-2021), 3/5 (Model: R-2023 - depends on configuration)
* - Per-channel programmable
  - center frequency, pulse width (pulse duty cycle), pulse length, polarity and delay
* - Pulse repetition frequency
  - up to 100 kHz
* - **Receive**
  - 
* - Number of channels
  - 64
* - Frequency range
  - up to 50MHz
* - Programmable anti-aliasing filter (cutoff)
  - 10, 15, 20, 30, 35, 50 MHz 
* - Amplifier gain
  - 
    - LNA with programmable gain: 24, 18, 12 
    - Voltage-Controlled Attenuator: 40dB 
    - Programmable Gain Amplifier: 24, 30 dB 
    - Total signal chain gain: 54 dB (max) 
    - TGC update rate 1MHz
* - Data sampling
  - 14-bit @ 65MSPS
* - Raw data buffer
  - up to 128MB per channel
* - **External synchronization**
  - 
* - Output for synchronization
  - digital, LVTTV 3.3V, 50$\Omega$ output impedance
* - Input for synchronization
  - digital, LVTTV 3.3V, 50$\Omega$ input impedance
* - Reference clock output
  - digital, LVTTV 3.3V, 50$\Omega$ output impedance
* - Output for synchronization
  - digital, LVTTV 3.3V, 50$\Omega$ input impedance
* - **Ultrasound probes**
  - 
* - Ultrasound probe connectors
  -  1x connectors (linear/phase/convex/RCA)
* - Supported probes
  -
    - 2D probes (linear/phase/convex): up to 256-elem (depending on the probe adapter and the probe)
    - 3D probes (RCA) -- offered by us4us / produced by Vermon
* - **Interface**
  - 
* - Data streaming interface
  - 2x PCIe gen3 x4
* - Raw data real-time streaming data rate (wire speed)
  - 6 GB/s 
* - Streaming method
  - PCIe Direct Memory Access
* - **Software**
  - 
* - Low-level API
  - C++ (currently RF data acquisition only); Python; Matlab® 
* - **Power supply**
  - 
* - Mains power
  - 120V,60Hz / 230V,50Hz ±10%
* - Average power usage
  - 300W
* - External dimensions (DxWxH) [mm]
  -  264 x 445 × 154 mm *high without probe adapter; total high may slightly differ depending on the Probe Adapter used: +31mm (MAT2372), +37mm (EPA), +50mm (PAU), +38mm (VPA)*
* - Weight
  - 10.5 kg
* - **Requirements**
  - 
* - PC host
  - e.g. Lenovo Thinkstation P620
* - CPU
  - e.g. AMD Ryzen Threadripper PRO
* - Memory -- RAM
  - e.g. 32 GB
* - Storage
  - e.g. 1TB NVMe PCIe
* - Operating system
  - Microsoft Windows 10 Pro (64-bit) / Linux Ubuntu 20.04 or newer
* - GPU (optional)
  - e.g. High-performance NVidia GPU with GPU-Direct support
* - PCIe adapter card
  - e.g. Dolphinics PXH832 or MXH (depends on configuration)
* - Accessories
  - e.g. LCD monitor with DP input, USB keyboard and mouse
:::
