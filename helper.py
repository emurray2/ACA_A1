# initial commit from local

import numpy as np

tarray = np.array([1, 1, 2, 2, 3, 3, 4]) #test array
tblock_size = 4
thop = 2 # test hop
tfs = 1 # test sampling frequency

def block_audio(x, block_size, hop_size, fs):
    # blocking function
    # x = input signal vector
    # fs = sampling frequency
    # returns a matrix xb (dim: NumOfBlocks by blockSize)
    #         a vector timeInSec (dim: NumOfBlocks) - start time of each block

    #x = append_remaining_zeros(x, block_size)
    print(x)

    numSamples = int(len(x)) # total number of samples
    NumOfBlocks = int(numSamples / hop_size - 1)

    xb = np.zeros((NumOfBlocks, int(block_size)))
    section = np.zeros((1, block_size))
    timeInSec = np.zeros(NumOfBlocks)

    j = 0 # x sample index

    for i in range(0, int(NumOfBlocks)):
        section = x[j:(j+block_size)]
        timeInSec[i] = j
        print(section.shape)
        # xb[[(i*hop_size)], :] = section[None, :]
        xb[i*hop_size, :] =section
        j += hop_size
        

    return xb, timeInSec

def append_remaining_zeros(input_vector, block_size):
    remainder = len(input_vector) % block_size
    print(np.shape(input_vector))
    print(remainder)
    input_vector = np.pad(input_vector, (0, remainder), 'constant')

    print(input_vector)
    return input_vector


def comp_acf(input_vector, is_normalized):
    # autocorrelation function
    # returns r - non-redundant (right) park of result r
    # boolean is_normalized
    

    r = np.corrcoef(input_vector, input_vector)


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

    return f0, timeInSec


if __name__ == "__main__":

    xb, timeInSec = block_audio(tarray, tblock_size, thop, tfs)
    print(xb)
    print(timeInSec)

    #r = comp_acf(tarray, False)
    #print(r)