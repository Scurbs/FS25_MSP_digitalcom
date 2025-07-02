import numpy as np
import matplotlib.pyplot as plt


def add_awgn_noise(signal, snr_db):
    """Add AWGN noise to a real-valued signal."""
    snr_linear = 10**(snr_db / 10)
    power_signal = np.mean(signal**2)
    power_noise = power_signal / snr_linear
    noise = np.sqrt(power_noise) * np.random.normal(0, 1, len(signal))
    return signal + noise

def plot_eye(signal, sps=1, span=2, offset=0,title="Eye Diagram"):
    """
    Zeichnet ein Eye-Diagramm für das gegebene Signal.
    
    Parameters:
    - signal: 1D-Array mit Samples
    - sps: Samples pro Symbol
    - span: Anzahl Symbole pro Segment (z.B. 2)
    - offset: Startoffset (in Samples)
    """
    num_segments = len(signal) // (sps * span)
    plt.figure()
    for i in range(num_segments):
        start = i * sps
        end = start + span * sps
        if end + offset <= len(signal):
            segment = signal[start + offset:end + offset]
            plt.plot(segment, color='blue', alpha=0.2)
    plt.title(title)
    plt.grid(True)
    plt.show()
    