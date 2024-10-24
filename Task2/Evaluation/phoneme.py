# Example phoneme ground truth and hypothesis
ground_truth_phonemes = "AA B IH K"  # Ground truth phonemes (use phonetic transcription)
hypothesis_phonemes = "AA B IH K"

# Calculate phoneme accuracy
correct_phonemes = sum(1 for g, h in zip(ground_truth_phonemes.split(), hypothesis_phonemes.split()) if g == h)
total_phonemes = len(ground_truth_phonemes.split())

phoneme_accuracy = correct_phonemes / total_phonemes * 100
print(f"Phoneme Accuracy: {phoneme_accuracy:.2f}%")
