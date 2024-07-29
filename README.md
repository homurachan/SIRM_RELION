# SIRM_RELION
Depository of the SIRM_RELION, a modification of RELION 3.1.2 implemented with SIRM algorithm.

Installation is the same as conventional RELION.

If you find SIRM useful, please cite our paper:

Dongjie Zhu, Weili Cao et al., Correction of preferred orientation–induced distortion in cryo–electron microscopy maps.

Science Advances 10, eadn0092 (2024). DOI:10.1126/sciadv.adn0092

Note: Get infomred from EMDB, our EMD maps will be released on Aug 7th.

# Update 05/30/2024
Upload the English version of the usage: SIRM_usage_English.pdf

# Update 02/10/2024
Upload Validation and Mask-Picking scripts. These scripts must be used together with the SIRM v1.1 (relion-3.1.2_SIRM_v1p1.zip).

Also upload a usage PDF in Chinese: SIRM_usage_Chinese.pdf. I don't have time to translate this pdf for now. An English version will be updated soon.

Happy Chinese New Year!

# Update 07/25/2023
Fix SIRM and MWTCF option in GUI of 3D auto-refine remained deactivate when triggered continue run.

# Usage

# 1. Using SIRM in 3D auto-refine

We added two options in "Optimisation" dialog.

![alt text](https://github.com/homurachan/SIRM_RELION/blob/main/Pictures/Pic1.png?raw=true)

The first one is "Do SIRM correction". If set to True, SIRM will be triggered during auto-refine.

Th second one is "Do MWTCF". If set to True, instead of using the whole Fourier space ( < resolution) to calculate FSC, the directions where the number of particles filled in are less than a given threshold will be discarded. This option improves the reported resolution and helps converge a refine. You may think this also enhance model-bias. It is. Nevertheless, when considering preferred-orientation, the resolution between directions where many particles are filled and others where only very few particles are filled is very diverged. The FSC we computed would be smaller than its true value in good directions, thus hindering accurate estimation of SNR in good directions.

Let's see all options in detail.

![alt text](https://github.com/homurachan/SIRM_RELION/blob/main/Pictures/Pic2.png?raw=true)

The "Threshold of the SIRM SNR weight" should be set by trial-and-error. In our tests, 0.5 ~ 1.0 is a good beginning. To more accurately set this value, you can check the "debug_fsc_snr_weight.mrc" generated on the root directory of current RELION project (Where you can find directory naming Extract, Class3D, Refine...). Use software like UCSF Chimera to open it and adjust the level of map. If the blank area is a good representation of missed-orientations, you can use that.

The "Histogram threshold" should be used carefully. In most of our tests, simply using the default value 0.0 (Equivalent to Non-negativity or Shrinkwarp) is good enough. Using a histogram to determine the real space boundary is more stable than using a fixed value.

The "Iteration of SIRM" has a default value of 40. In early stage of refine where the resolution is low, it's a waste of time to run too many iterations. Higher value is only beneficial at the last two or three rounds.

The "Real space mask" should only be provided at the last couples of rounds. Otherwise it would bring significant model-bias to maps.

The "MWTCF value" should never be larger than 2.0 (unless something strange happens). In our tests, 0.1 ~ 0.2 is good enough to converge ribosome datasets. In HA datasets, we used 0.5 ~ 1.0.

# 2. Using SIRM in reconstruction.

To better utilize SIRM, we added "Reconstruction" in RELION's main GUI.

![alt text](https://github.com/homurachan/SIRM_RELION/blob/main/Pictures/Pic3.png?raw=true)

Now you can use the GUI to run reconstruction very easily.

![alt text](https://github.com/homurachan/SIRM_RELION/blob/main/Pictures/Pic4.png?raw=true)

The only difference in reconstruction step of SIRM is that you must provide additional FSC starfile.

You can use https://github.com/homurachan/SIRM_RELION/blob/main/convert_star_2_SIRM_weight.py to convert a post-process starfile to FSC starfile.

The usage is `python ./convert_star_2_SIRM_weight.py postprocess.star Weight.star`

# 3. Improving alignment using Validation and Mask-Picking.

(To be continued)
