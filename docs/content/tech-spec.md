(tech-spec)=
# Technical Specification

## Basic Composition

The **us4R-lite™** device (with probe adapter)
- PCIe, Model: RL-2024-PCIe:
  - 1x PCIe host adapter card
  - 4x PCIe cable
  - 1x power adapter AC/DC
- Thunderbolt, Model: RL_2020:
  - 1x Thunderbolt cable
-   (optional) ultrasound probe
-   (optional) PC system controller with GPU cards
-   User Manual (on-line)

## Technical data and Detailed specification

:::{list-table} 
:widths: 15 35
:align: left
* - **Transmit**
  - 
* - Number of channels
  - 256
* - Transmit frequency
  - 1MHz to 20MHz (Model: RL-2020); 1MHz to 30MHz (Model: RL-2024-PCIe)
* - Tx time delay resolution
  - up to 7 .7 ns (depends on the system clock)
* - Programmable TX voltage
  - up to 180Vpp (±90V) 
* - TX pulsers levels
  - 3 (Model: R), 3/5 (Model: R-2023 - depends on configuration)
* - Per-channel programmable
  - center frequency, pulse length, polarity and delay
* - TX function
  - Possibility of generating pseudo-arbitrary transmit waveforms
* - Pulse repetition frequency
  - up to 20 kHz (depends on the other parameters and loading conditions)
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
  - 14-bit @ 65MSPS  /  16-bit @ 120MSPS
* - Raw data buffer
  - up to 128MB per channel
* - **External synchronization**
  - 
* - Output for synchronization (TRIG OUT)
  - digital, LVTTV 3.3V, 50$\Omega$ output impedance
* - Input for synchronization (TRIG IN)
  - digital, LVTTV 3.3V, HiZ input impedance
* - Reference clock output (CLK OUT)
  - digital, LVTTV 3.3V, 50$\Omega$ output impedance
* - Output for synchronization (CLK IN)
  - digital, LVTTV 3.3V, HiZ input impedance
* - **Ultrasound probes**
  - 
* - Ultrasound probe connectors
  -  1x connectors (linear/phase/convex/RCA)
* - Supported probes
  -
    - 2D probes (linear/phase/convex): up to 256-elem (depending on the probe adapter and the probe)
    - 3D probes (RCA) -- offered by us4us / produced by Vermon
* - **Interface (Model: RL-PCIe-2024)**
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
* - Power connection
  - pluggable
* - External AC/DC power supply*
  - 
    - INPUT: 120V,60Hz / 230V,50Hz ±10%
    - OUTPUT: 19VDC, 4.74A
    - The us4R-liteTM must be supplied from the source that meets IEC Class II and NEC Class 2 power supply requirements.
    - Dedicated FSP090-RBCM1 power supply is delivered with the device
* - Max power consumption
  - 90W
* - **Physical / Environmental**
  - 
* - System size (DxWxH)
  -  260 x 200 × 83 [mm] *high without probe adapter; total high may slightly differ depending on the Probe Adapter used: +27mm (EPA), +39mm (PAU), +26mm (VPA)*
* - System weight
  - ~2.8 kg
* - Ingress protection
  - IP2x
* - Position
  - vertical
* - Mobility
  - portable
* - Environmental conditions
  - 
    - Application: laboratory 
    - up to 2000 m
    - pollution degree II

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
  - e.g. Dolphinics PXH832
* - Accessories
  - e.g. LCD monitor with DP input, USB keyboard and mouse
:::


(tech-spec/limitations)=
## Current system limitations

Here is a list current system limitations:

- SWE (Shear-Wave Elastography) functions are limited and available only to approved early-adopters.
- The system provides only pre-beamformed RF or I/Q data. It does not perform image reconstruction in particular. The signal processing should be handled by a dedicated processing hardware, e.g. GPU. We provide ready to use examples e.g. for the B-mode image reconstruction on the NVIDIA GPU. 
- The ability to achieve a stable, selected PRF depends on the chosen communication interface between the host PC and the ultrasound system. For a custom solution, it is the user's responsibility to ensure that the selected communication interface with the host PC and the signal processing setup satisfies requirements for the selected PRF.

The above limitations may be removed in future versions of the system software/firmware.
