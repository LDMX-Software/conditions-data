# ECal, ESA 2026 cosmic stand

Conditions for ECal layers 2 and 3 of the ESA 2026 cosmic stand, loaded in
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
