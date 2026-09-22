# KLM SRAM Expansion — Service Task

Belle II KLM service work · Instrumentation Development Lab, University of Hawai'i at Mānoa

## Overview

The KLM scintillator readout currently shares a single SRAM between the Bus A and
Bus B firmware modules through the SCROD FPGA. During multi-strip hits, pedestal
fetching becomes the rate-limiting step in waveform processing. This project adds
a second SRAM on an auxiliary daughtercard so each bus has its own memory path,
along with the power-distribution hardware needed to supply it.

Three boards make up the system:

| Board | Function |
| --- | --- |
| **Aux SRAM daughtercard** | Mounts to the spare 80-pin mezzanine connector on the scintillator motherboard; carries the second SRAM and a local 3.3 V regulator |
| **RTM +5 V board** | Rear transition module; taps +5 V from the crate backplane, fuses it, and feeds the wiring harness |
| **2-pole fanout board** | Splits the 12 AWG trunk into 22 AWG drops, one per SRAM card |

**Board design credit:** all three boards were designed by Chris Ketter (UH Mānoa),
with contributions from Horacio Ledesma. My role is prototype testing and design
finalization.

## Scope of this qualification task

Testing and validation:

- Test the prototype SRAM expansion board on the UH KLM testbench
- Test the associated RTM and power-distribution boards
- Verify electrical connections and power delivery across the full chain
- Confirm correct operation with the dedicated SRAM firmware

Finalization:

- Feed prototype results back into the board designs
- Help finalize assembly procedures ahead of the production run

Superseded board revisions are kept under [`Archive/`](Archive/) (see its README); current files are in `Finalized-Boards/`.

## Deliverable

- Finalized board designs
- Production of the boards
- Installation of the boards

## After the qualification task

Continued contribution to board production, testing, and installation as part of
ongoing KLM service work.
