# Hcal Calibrations

## Check missing IDs

Hcal calibration files should contain all IDs. To check if your calibration file has all IDs and insert a placeholder `value` for the missing IDs you can use `check_missingId.py`.
```
python3 check_missingId.py  mips/v1_0_0/mip_calib_phase3_run287_adcsum_1stpedexcl_pass1_v0.csv --value -9999.0
```