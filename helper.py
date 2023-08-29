# initial commit from local

import numpy as np

tarray = np.array([1, 1, 2, 2, 3, 3]) #test array
tblock_size = 2
thop = 1 # test hop
tfs = 1 # test sampling frequency

def block_audio(x, block_size, hop_size, fs):
    # blocking function
    # x = input signal vector
    # fs = sampling frequency
    # returns a matrix xb (dim: NumOfBlocks by blockSize)
    #         a vector timeInSec (dim: NumOfBlocks) - start time of each block


    numSamples = int(len(x)) # total number of samples
    NumOfBlocks = int(numSamples / hop_size - 1)

    xb = np.empty((NumOfBlocks, int(block_size)))
    section = np.empty((1, block_size))

    for i in range(0, int(NumOfBlocks)-1):
        print(section)
        section = x[(i*block_size):(i*block_size + block_size)]
        print(section)
        xb[i:block_size] = section
        #xb = np.append(xb, section)
        

    return xb
    # return  timeInSec


def comp_acf(input_vector, is_normalized):
    # autocorrelation function
    # returns r - non-redundant (right) park of result r
    # boolean is_normalized



    return r


def get_f0_from_acf(r, fs):
    # computes fundamental frequency
    # r = output of comp_acf()
    # fs = sampling frequency
    # returns f0 - fundamental frequency of that block in Hz


    return f0

def track_pitch_acf(x, block_size, hop_size, fs):
    # calls block_audio(), comp_acf(), get_f0_from_acf()
    # returns f0
    #         timeInSec

    return f0
    return timeinSec


if __name__ == "__main__":

    xb = block_audio(tarray, tblock_size, thop, tfs)
    print(xb)