#! /usr/bin/env python
import argparse

from covest import config
from covest.data import load_histogram
from covest.histogram import auto_sample_hist, get_trim


def remove_noise(hist):
    total = sum(hist.values())
    hist_denoised = {k: v for k, v in hist.items() if v/total > config.NOISE_THRESHOLD}
    tail = sum(v for v in hist.values() if v/total <= config.NOISE_THRESHOLD)
    return hist_denoised, tail


def main(args):
    k, r = args.kmer_size, args.read_length
    hist_orig = load_histogram(args.input_histogram)
    hist_orig, tail = remove_noise(hist_orig)
    hist, sample_factor = auto_sample_hist(hist_orig, k, r)
    print('Suggested sf:', sample_factor)
    print('Suggested trim:', max(get_trim(hist, 6), min(50, max(hist))))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze histogram')
    parser.add_argument('input_histogram', help='Input histogram')
    parser.add_argument('-k', '--kmer-size', type=int,
                        default=config.DEFAULT_K, help='Kmer size')
    parser.add_argument('-r', '--read-length', type=int,
                        default=config.DEFAULT_READ_LENGTH, help='Read length')

    main(parser.parse_args())
