# sylomer_bearers
Tool for faster designing of vibration insulation solutions

# Why it has been created?

In the position of acoustic engineer at Acoustic Group Ukraine, one of my routine tasks was a selection of vibration isolation supports depending on the size and mass of the source of vibration (HVAC units or similar equipment) and the working frequency of its engine. I decided to collect open-source data on the physical properties of vibration insulation materials and implement local building design rules to significantly decrease the selection time of the best possible configuration of vibration insulation materials under the source of vibration. 

# Description 

## Step 1. Design limits

The user has to check building design rules (allowed distance between bearings, maximum possible numbers of bearers), acoustic limits (maximum and minimum allowed power of bearers under the load), and take into the account list of available Sylomer marks that he has at the warehouse and define a list of possible cutting step size of the vibration insulation material.

## Step 2. Input data

The user has to prepare an Excel file with the next data for each source of vibration:

- name of the source of vibration and its mass in kg
- length, width, and height of the concrete basement under the source of vibration in mm
- mass of the concrete basement
- the ratio of concrete basement mass and mass of the source of vibration
- the load on Sylomer bearings as a sum of the mass of the concrete basement and the mass of the source of vibration
- the possible height of the Sylomer bearers in mm (separated by a comma if it is needed)

After the execution of the [run.py](https://github.com/MykhailoYar/sylomer_bearings/blob/main/run.py) script and selection of the Excel input data file user can see the name and dimensions of the source of vibration and a table of possible configurations of vibration insulation materials under the source of vibration and concrete basement that fulfill the design limits. 

The configuration table is sorted by the efficiency and the price of the vibration insulation decisions. The user has to select the best option and check the resonance frequency of the system through special software provided by Getzner.  

Based on this data, the user paste the number of the selected configuration into the terminal.
