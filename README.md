# KLM SRAM Expansion — Qualification Task

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
| **Aux SRAM daughtercard** (`IDL_25_007`) | Mounts to the spare 80-pin mezzanine connector on the scintillator motherboard; carries the second SRAM and a local 3.3 V regulator |
| **RTM +5 V board** | Rear transition module; taps +5 V from the crate backplane, fuses it, and feeds the wiring harness |
| **2-pole fanout board** | Splits the 12 AWG trunk into 22 AWG drops, one per SRAM card |

**Board design credit:** all three boards were designed by Chris Ketter (UH Mānoa),
with contributions from Horacio Ledesma. My role is prototype testing and design
finalization, not original design.

## Scope of this qualification task

Testing and validation:

- Test the prototype SRAM expansion board on the UH KLM testbench
- Test the associated RTM and power-distribution boards
- Verify electrical connections and power delivery across the full chain
- Confirm correct operation with the dedicated SRAM firmware
  (`feature/SRAM_upgrade`)

Finalization:

- Feed prototype results back into the board designs
- Help finalize assembly procedures ahead of the production run

## Deliverable

A short technical note covering:

1. Test results
2. Remaining risks
3. Recommendations for moving the boards into production

## After the qualification task

Continued contribution to board production, testing, and installation as part of
ongoing KLM service work.

## Related repositories

- `klm-sram-exp` — KiCad projects for all three boards
- `klm_scrod`, branch `feature/SRAM_upgrade` — SCROD firmware

## Note on KiCad versions

The board files were created in **KiCad 9** (format `20241229`). Opening and saving
them in KiCad 10 upgrades the format irreversibly and prevents KiCad 9 users from
opening them. Use KiCad 9.0.x unless the change has been coordinated with the
original designer.
