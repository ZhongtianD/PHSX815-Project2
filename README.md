# PHSX815-Project2

Take_samples.py generates samples drawn from the gaussian distribution with varying mean with the slice sampling method.

Analyze_samples.py creates a Log-likelihood plot.

Use the -h flag to see instructions on input parameters.

For example, to generate samples of mu=1, use

python Take_samples.py -mu0 0 -sigma 1 -sigma0 0.5 -seed 1010 -Nsample 10 -Nexp 1000 -output sample0.npy

To analyze simulated samples from two different hypothesis of Gaussian, use

python Analyze_samples.py -mu0_0 0 -mu0_1 2 -sigma0 1 -sigma0_0 0.5 -alpha 0.05 -input0 sample0.npy -input1 sample1.npy

It will generate a picture of loglikelihood ratio plot comparing the two hypothesis
