import numpy as np

# Simulated MOS scores from native speakers
native_speaker_scores = [4.5, 4.2, 4.8, 4.6, 4.3]  # Replace with actual ratings collected

# Calculate average MOS score
average_mos_score = np.mean(native_speaker_scores)
print(f"Mean Opinion Score (MOS): {average_mos_score:.2f}")
