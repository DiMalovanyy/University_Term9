import numpy as np
import os
import random


def create_hopfield_network(pattern_size):
    num_pixels = pattern_size[0] * pattern_size[1]
    weight_matrix = np.zeros((num_pixels, num_pixels))
    return weight_matrix


def train_hopfield_network(weight_matrix, patterns):
    num_pixels = weight_matrix.shape[0]
    num_patterns = patterns.shape[0]
    for p in range(num_patterns):
        pattern = patterns[p].flatten()
        weight_matrix += np.outer(pattern, pattern)
    weight_matrix /= num_pixels
    np.fill_diagonal(weight_matrix, 0)
    return weight_matrix


def apply_noise(pattern, noise_ratio):
    num_pixels = pattern.shape[0]
    noisy_pattern = pattern.flatten()
    num_noise_pixels = int(noise_ratio * noisy_pattern.shape[0])
    noise_indices = random.sample(range(num_pixels), num_noise_pixels)
    noisy_pattern[noise_indices] *= -1
    return noisy_pattern.reshape(pattern.shape)


def signum_activation(x):
    return np.where(x >= 0, 1, -1)


def hopfield_inference(weight_matrix, patterns):
    num_patterns = patterns.shape[0]
    outputs = []
    for p in range(num_patterns):
        pattern = patterns[p].flatten()
        output = signum_activation(weight_matrix @ pattern)
        outputs.append(output.reshape(patterns[p].shape))
    return np.array(outputs)


if __name__ == '__main__':
    img_size = (11, 9)
    data_path = './digits/'
    num_digits = 10
    digits = []
    for i in range(num_digits):
        file_path = os.path.join(data_path, f'digit_{i}.txt')
        with open(file_path, 'r') as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [list(map(int, list(line))) for line in lines]
        digit_img = np.array(lines)
        digit_img = digit_img.astype(np.single)
        digit_img = (digit_img / 255) * 2 - 1  # Normalize to [-1, 1]
        digit_img = np.where(digit_img > 0, 1, -1)  # Binarize
        digit_img = digit_img.reshape(img_size)
        digits.append(digit_img)
    digits = np.array(digits)
    
    noise_ratio = 0.3
    noisy_digit = apply_noise(digits[0], noise_ratio)
    noisy_digit = noisy_digit.reshape((1,) + img_size)
    
    hopfield_network = create_hopfield_network(img_size)
    hopfield_network = train_hopfield_network(hopfield_network, digits)
    
    noisy_digit_reconstructed = hopfield_inference(hopfield_network, noisy_digit)
    


