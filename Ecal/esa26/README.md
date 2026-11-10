# ECal, ESA 2026 cosmic stand

Conditions for ECal layers 2 and 3 of the ESA 2026 cosmic stand, loaded in
ldmx-sw by `LDMX.Ecal.esa26_conditions.esa26_recon_conditions()`. Cell IDs
follow `EcalDetectorMap.esa26()`.

## pedestals

EcalReconConditions tables (`DetID,ADC_PEDESTAL,ADC_GAIN,TOT_PEDESTAL,TOT_GAIN`).

- `v1_0_0/pedestals_20261103.csv`: ADC pedestal per cell from the 03-Nov-26
  100 V calibration sets, default gains (0.3125 fC/ADC). Valid from run 230
  (first run of 03-Nov) onward.
