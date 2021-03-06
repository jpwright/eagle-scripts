eagle-scripts
=============

Collection of Python scripts to automate tasks in Cadsoft Eagle.

All scripts require an input file which contains pin and pad assignments. An example from the Xilinx Spartan-6 datasheet:

<code>0 IO_L1P_HSWAPEN_0 C4 TL<br /> 0 IO_L1N_VREF_0 A4 TL<br /> 0 IO_L2P_0 B5 TL<br /> 0 IO_L2N_0 A5 TL<br /> 0 IO_L3P_0 D5 TL<br /> ...</code>

All values should be separated by spaces. The first column is unused. The second column should contain the pin name. The third column should contain the pad name. All other columns are unused.

### pinCreator.py

Creates an Eagle command line script at out.txt to create pins in symbol view.

Usage: <code>python pinCreator.py pinlist.txt</code>

### pinConnector.py

Creates an Eagle command line script at out-pads.txt to connect pins to pads in device view.

Usage: <code>python pinConnector.py pinlist.txt</code>
