import numpy as np
import matplotlib.pyplot as plt

def plot_audio_embeddings(scores, embeddings, spectrogram, waveform, class_names, patch_window_seconds, patch_hop_seconds):
    scores = scores.numpy()
    spectrogram = spectrogram.numpy()
    
    # Visualize the results.
    plt.figure(figsize=(10, 8))

    # Plot the waveform.
    plt.subplot(3, 1, 1)
    plt.plot(waveform)
    plt.xlim([0, len(waveform)])
    
    # Plot the log-mel spectrogram (returned by the model).
    plt.subplot(3, 1, 2)
    plt.imshow(spectrogram.T, aspect='auto', interpolation='nearest', origin='lower')

    # Plot and label the model output scores for the top-scoring classes.
    mean_scores = np.mean(scores, axis=0)
    top_N = 10
    top_class_indices = np.argsort(mean_scores)[::-1][:top_N]
    plt.subplot(3, 1, 3)
    plt.imshow(scores[:, top_class_indices].T, aspect='auto', interpolation='nearest', cmap='gray_r')
    
    # Compensate for the PATCH_WINDOW_SECONDS (0.96 s) context window to align with spectrogram.
    patch_padding = (patch_window_seconds / 2) / patch_hop_seconds
    plt.xlim([-patch_padding, scores.shape[0] + patch_padding])
    
    # Label the top_N classes.
    yticks = range(0, top_N, 1)
    plt.yticks(yticks, [class_names[top_class_indices[x]] for x in yticks])
    _ = plt.ylim(-0.5 + np.array([top_N, 0]))