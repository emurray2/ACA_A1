# initial commit from local
import numpy

# Combine channels to mono signal
def sum_and_scale(matrix, shape):
    channel_count = shape[0]
    audio_length = shape[1]
    added_audio = numpy.zeros((1, audio_length))

    for i in range(0, channel_count):
        added_audio += numpy.matrix[i]
    added_audio /= channel_count

# Append zeros to remaining block samples
def append_remaining_zeros(input_vector, block_size):
    remainder = input_vector % block_size
    numpy.pad(input_vector, remainder, 'constant')
    return input_vector

def block_audio(x, block_size, hop_size, fs):
    # blocking function
    # x = input signal vector
    # fs = sampling frequency
    # returns a matrix xb (dim: NumOfBlocks by blockSize)
    #         a vector timeInSec (dim: NumOfBlocks) - start time of each block
    #        
    # 
    x = sum_and_scale(x, numpy.shape(x))
    x = append_remaining_zeros(x, block_size)
    block_start = 0
    next_block_start = block_start + hop_size
    block_count = len(x) / block_size
    xb = numpy.zeros((block_count, block_size))
    timeInSec = numpy.zeros((1, block_count))

    for i in range(0, block_count):
        timeInSec[i] = block_start / fs
        xb[i] += x[block_start:next_block_start-1]
        block_start = next_block_start
        next_block_start = block_start + hop_size
    return (xb, timeInSec)

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
