# ECal, ESA 2026 cosmic stand

Conditions for ECal layers 0, 2 and 3 of the ESA 2026 cosmic stand, loaded in
ldmx-sw by `LDMX.Ecal.esa26_conditions.esa26_recon_conditions()`. Cell IDs
follow `EcalDetectorMap.esa26()`.

## pedestals

EcalReconConditions tables (`DetID,ADC_PEDESTAL,ADC_GAIN,TOT_PEDESTAL,TOT_GAIN`).

- `v1_0_0/pedestals_20261103.csv`: ADC pedestal per cell from the 03-Nov-26
  100 V calibration sets, default gains (0.3125 fC/ADC). Valid from run 230
  (first run of 03-Nov) onward.
- `v1_1_0/pedestals_20261103.csv`: same pedestals, ADC gain per cell from
  cosmic MIPs: `ADC_GAIN = charge_per_mip / MIP_ADC` (5.93 fC), so a MIP
  gives 1 MIP equivalent. `MIP_ADC` is the median ZS-bounded fit amplitude
  (as `EcalRecProducer.esa_cosmic_stand()`) of L2 and L3 hits within 1.3
  pitch of each other (HCal trigger, 100 V).
  - L2: runs 255, 271-273, 282, 284, 294-296, 298, 23.5 ADC, median 124 MIPs
    per cell, statistical error 2.5%.
  - L3: runs 255-284 only, 23.4 ADC, median 92 MIPs, 3.1%. From run 287 L3
    runs with ZS offset 7, which biases this fit (bounded at 5.5 ADC) up by
    about 9%; its max sample moves only 2%.
  - Gain spread between cells 8.5%; L2 stable to 1% between 30-Oct..06-Nov
    and 06..07-Nov. Measured for 250 L2 and 215 L3 cells; the 182 L2 cells
    outside the L3 shadow (and 1 L3 cell) have the layer median gain.
  - The muon angle is not corrected (the MIP grows only about 4% from 0 to
    30 degrees).
- `index_v1_3_0.csv`: adds layer 0 (ROCs 1, 2, 4, 5, 288 cells) from run 590.
  Runs 230-589 keep `v1_2_0/pedestals_20261103.csv`; from run 590
  `v1_3_0/pedestals_20261122.csv` is the same layer 2 and 3 rows plus layer
  0: ADC pedestal per channel from the 22-Nov-26 100 V calibration set (taken
  right after the pedestal leveling at 14:00), default gains (0.3125 fC/ADC).
  Runs before 590 had unleveled layer 0 pedestals and get no layer 0 rows.

## alignment

EcalAlignment tables (`DetID,DX,DY,DZ`, mm): shift of the whole ECal vs the
`ldmx-esa-cosmic26-v2` geometry, one row with the ID of `EcalID(0, 0, 0)`.
`EcalGeometryProvider` (with `alignment` set, as in `esa26_alignment()`)
builds the geometry of each run with it.

- DY = HCal y track at the hit layer minus the ldmx-sw cell center y, mean
  of the core (median +- 30 mm), single L2 or L3 hits >= 12 ADC on a good
  straight HCal y track, L2 and L3 pooled.
- `v1_0_0/alignment_20261103.csv`, runs 230-461: DY +64.8 (runs 317-426,
  run-to-run rms 0.7, 300 to 2200 hits per run).
- `v1_0_0/alignment_20261118.csv`, from run 462: DY -0.6 (runs 466-500,
  rms 0.5). The ECal moved down by 65.4 mm during 18-Nov (run 459 on 17-Nov
  is at the old place, 462 on 18-Nov at the new one; 460 and 461 have no
  HCal tracks), to within 1 mm of the CAD position.
- L2 alone needs 1.7 mm less DY than L3, in both periods; not corrected.
- DX and DZ are 0: x needs HCal x tracks, whose plane conventions are still
  provisional; z is not measured with HCal tracks.
- `index_v1_1_0.csv` (for `ldmx-esa-cosmic26-v2` without `flip_x`): same DY,
  plus DX from HCal x tracks with the corrected ESA26 HCal map, defined as DY
  (x track minus ldmx-sw cell center x, core mean). Runs 230-461: DX +33.3
  (runs 394-459, x from the planes above the ECal only); from run 462: DX
  +37.6 (runs 484-564, planes above and below). L2 and L3 agree within
  1.4 mm. DZ stays 0 (the residual vs track slope suggests about 8 mm, not
  applied).
