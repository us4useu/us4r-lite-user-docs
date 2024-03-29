# Technical specification

## Technical data

-   Ultrasound frequencies up to 20 MHz (Model: R-2021) or up to 30MHz (Model: R-2023);

-   Mains power supply 120V,60Hz / 230V,50Hz ±10%

-   Power consumption (average) 300W

-   Power consumption (max) 1200W (max power of the us4R power supply)

-   Product Dimensions (DxWxH) [mm]: 264 x 445 × 154\* mm

> *\*high without probe adapter; total high may slightly differ
> depending on the Probe Adapter used: +31mm (MAT2372), +37mm (EPA),
> +50mm (PAU), +38mm (VPA)*

-   Weight 10.5 kg

## Basic Composition

-   the **us4R™** device (with probe adapter)

-   4 or 8 PCIe cable

-   1 or 2 PCIe adapter card

-   1x mains power cable

-   (optional) ultrasound probe

-   (optional) PC system controller with GPU cards

-   User Manual

## Detailed specification

:::{list-table} 
:widths: 15 35
:align: left
* - **Transmit**
  - 
* - Number of channels
  - 128‑1024 (depends on configuration)
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
  - 128‑256 (depends on configuration) 
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
  - 14-bit @ 65MSPS or 12-bit @ 80MSPS
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
  -  2 connectors of the 2D (linear/phase/convex) probe or up to 4 connectors of the 2D array probe
* - Supported probes
  -
    - 2D probes (linear/phase/convex): up to 192 el. from Esaote and up to 128 from ATL/Philips/Ultrasonix
    - Matrix-array 32x32 from Vermon (MAT2372)
    - probes with up to 1024-elements via a dedicated custom Probe Adapter.
* - **Interface**
  - 
* - Data streaming interface
  - Single/Dual PCIe gen3 x16
* - Raw data real-time streaming data rate (wire speed)
  - 1x/2x 16 GB/s 
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
