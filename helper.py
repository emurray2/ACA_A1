# initial commit from local

def block_audio(x, block_size, hop_size, fs):
    # blocking function
    # x = input signal vector
    # fs = sampling frequency
    # returns a matrix xb (dim: NumOfBlocks by blockSize)
    #         a vector timeInSec (dim: NumOfBlocks) - start time of each block
    #        
    # 





    # return xb
    # return  timeInSec


def comp_acf(input_vector, is_normalized):
    # autocorrelation function
    # returns r - non-redundant (right) park of result r
    # boolean is_normalized



    # return r


def get_f0_from_acf(r, fs):
    # computes fundamental frequency
    # r = output of comp_acf()
    # fs = sampling frequency
    # returns f0 - fundamental frequency of that block in Hz


    # return f0

def track_pitch_acf(x, block_size, hop_size, fs):
    # calls block_audio(), comp_acf(), get_f0_from_acf()
    # returns f0
    #         timeInSec

    # return f0
    # return timeinSec