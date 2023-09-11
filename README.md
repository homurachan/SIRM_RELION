# SIRM_RELION
Depository of the SIRM_RELION, a modification of RELION 3.1.2 implemented with SIRM algorithm.

Installation is the same as conventional RELION.

# Update 07/25/2023
Fix SIRM and MWTCF option in GUI of 3D auto-refine remained deactivate when triggered continue run.

# Usage

# 1. Using SIRM in 3D auto-refine

We added two options in "Optimisation" dialog.

![alt text](https://github.com/homurachan/SIRM_RELION/blob/main/Pictures/Pic1.png?raw=true)

The first one is "Do SIRM correction". If set to True, SIRM will be triggered during auto-refine.

Th second one is "Do MWTCF". If set to True, instead of using the whole Fourier space ( < resolution) to calculate FSC, the directions where the number of particles filled in are less than a given threshold will be discarded. This option improves the reported resolution and helps converge a refine. You may think this also enhance model-bias. It is. Nevertheless, when considering perferred-orientation, the resolution between directions where many particles are filled and others where only very few particles are filled is very diversed. The FSC we computed would be smaller than its true value in good directions, thus hindering accurate estimation of SNR in good directions.

Let's see all options in detail.

![alt text](https://github.com/homurachan/SIRM_RELION/blob/main/Pictures/Pic2.png?raw=true)
