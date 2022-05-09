# conditions-data
Data tables of run conditions for LDMX.

## Organization
Each LDMX subsystem has its own subdirectory within this repository that it can manage.
Generally, the subdirectories within a subsystem are the different conditions to be loaded and each condition has its own version controlled index files.
Each of these index files then contain a list of which data files should be used for specific run intervals (or "Intervals of Validity" -- IOV).
The location of the actual data files containing the condition values is up to the condition. Generally, they should be kept within that condition's directory to avoid confusion. An example structure is given in the `Hcal/ADC_PEDESTAL` condition below.
```
- conditions-data/
  - Hcal/
    - ADC_PEDESTAL/
      - index-v1_0_0.csv
      - index-v1_0_1.csv
      - data/
        - v1_0_0/
          - run-200-237.csv
          - run-238-300.csv
          - <other runs>
        - v1_0_1/
          - run-200-237.csv -> ../v1.0.0/run-200-237.csv #doesn't change so symlink to previous version
          - run-238-300.csv # updated from previous version
          - <other runs>
    - ADC_GAIN/
      - index-v1_0_0.csv
  - TrigScint/
    - PEDESTAL/
      - index-v1_0_0.csv
    - GAIN/
      - index-v1_0_0.csv
```
In the conditions system in ldmx-sw, the root directory of this repository (e.g. `file:///home/tom/conditions-data/`) is referred to as the "base URL" for the conditions system. This allows ldmx-sw to be "pointed" at a variety of different methods of distributing this conditions data (local copy on a laptop, a shared copy on a cluster, or even available via HTTP).
**Remember**: When running ldmx-sw with the container, it can only "see" files within directories that are mounted to it. If the copy of the conditions data you are using is not being downloaded via HTTP or already within the LDMX_BASE directory, you will need to mount it with `ldmx mount`.

## Index File
Each condition requires a index file to assign IOVs to values for that condition.
These index files are CSV files and have the following columns.
- `URL` : full path to CSV file with condition values (use the syntax `${LDMX_CONDITION_BASEURL}` so that the "base URL" is inherited
  - The full path _must_ be specified in a URL syntax (use `file://` for files locally on your computer) so that users developing the conditions table can specify tables outside of the base URL if need be.
- `FIRST_RUN`: integer value of first run number for which these values are valid (_inclusive_)
- `LAST_RUN`: integer value of last run number for which these values are valid (_inclusive_)
- `RUNTYPE`: string value of either `MC` or `DATA` to signal that these values are valid for either MC samples or real data samples
