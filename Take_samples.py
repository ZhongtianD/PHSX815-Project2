import sys
import numpy as np


sys.path.append(".")
from Random import Gaussian2

#main function 
if __name__ == "__main__":

    # default seed
    seed = 2048
    
    # default deviation of the distribution of the sample
    sigma = 1

    # default mean of the distribution of mean
    mu0 = 0
    
    # default deviation of the distribution of mean
    sigma0 = 0.3
    

    # default number of samples (per experiment)
    Nsample = 10

    # default number of experiments
    Nexp = 1

    # output file defaults
    doOutputFile = False

    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -seed [number] seed for random number generation")
        print ("   -sigma [number] standard deviation for the gaussian distribution of the sample")
        print ("   -mu0 [number] mean for the gaussian distribution of the mean")
        print ("   -sigma0 [number] standard deviation for the gaussian distribution of the mean")
        print ("   -Nsample [number] number of samples for each experiment")
        print ("   -Nexp [number] number of experiments")
        print ("   -output [.npy file] output file saved in the .npy format")
        print
        sys.exit(1)
    
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-mu0' in sys.argv:
        p = sys.argv.index('-mu0')
        mu0 = float(sys.argv[p+1])
    if '-sigma' in sys.argv:
        p = sys.argv.index('-sigma')
        ptemp = float(sys.argv[p+1])
        if ptemp > 0 :
            sigma = ptemp
    if '-sigma0' in sys.argv:
        p = sys.argv.index('-sigma0')
        ptemp = float(sys.argv[p+1])
        if ptemp > 0 :
            sigma0 = ptemp
    if '-Nsample' in sys.argv:
        p = sys.argv.index('-Nsample')
        Ns = int(sys.argv[p+1])
        if Ns > 0:
            Nsample = Ns
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # Initialze an object of the Gaussian class
    G = Gaussian2(seed = seed, sigma = sigma, mu0 = mu0 ,sigma0 = sigma0)

    if doOutputFile:
        S = np.zeros((Nexp,Nsample))
        #Generate samples
        for e in range(Nexp):
            x = np.random.rand()
            #Generate samples with a random starting point
            S[e] = G.Sample([mu0, mu0+x*sigma ],Nsample)
        np.save(OutputFileName, S)
   
