import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import math

# Distance from nut to bridge in %.
scale_length = 100
# Number of frets to show.
frets = np.arange(1, 25)
# Harmonics to show nodes of.
harmonics = [2, 3, 4, 5, 6, 7, 8, 9]

def main():
  plt.rc('font', size=10)
  plt.rc('font', family="monospace")

  _, ax = plt.subplots(figsize=(18, 2.8), layout="constrained")

  # Figure styling.
  ax.axhline(1, alpha=0.25, color="blue", linewidth=0.5)
  ax.axhline(0, alpha=0.25, color="blue", linewidth=0.5)
  ax.set_xlim([0, scale_length])
  ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
  ax.set_ylim([-0.5, 1.5])
  ax.set_xlabel("Distance from nut to bridge (%)")
  ax.get_yaxis().set_visible(False)
  bbox_style = dict(facecolor='white', edgecolor='none', boxstyle='round, pad=0.1')

  # Reverse harmonics as multiples are drawn on top of eachother.
  for harmonic in reversed(harmonics):
    for numerator in range(1, harmonic):
      distance = scale_length * numerator / harmonic
      numSemitones = freqRatioToSemitones(harmonic)
      # Calculate cent offset from nearest equally tempered note.
      numCents = 100 * (numSemitones - round(numSemitones))
      roundedNumCents = round(numCents)

      ax.plot(distance, 0, color="black", marker="|", ms=1000, alpha=0.3, markeredgewidth=0.5)
      ax.text(distance, 0, rf"${harmonic}f_0$", horizontalalignment="center", verticalalignment="bottom", bbox=bbox_style)
      ax.text(distance, 0, rf"${roundedNumCents:+}$", horizontalalignment="center", verticalalignment="top", bbox=bbox_style)

  # Mark frets with a single dot.
  marked_frets = [3, 5, 7, 9, 15, 17, 19, 21]
  # Mark octaves with two dots.
  marked_octaves = [12, 24]

  for fret in frets:
    # Use equal temperament for fret spacing calculations.
    distance = scale_length - scale_length / 2 ** (fret / 12)
    
    ax.plot(distance, 1, color="black", marker="|", ms=50, markeredgewidth=0.5)
    ax.text(distance, 1, f"{fret}", horizontalalignment="center", verticalalignment="center", bbox=bbox_style)

    if fret in marked_frets:
      ax.text(distance, 0.5, f"●", horizontalalignment="center", verticalalignment="center")

    if fret in marked_octaves:
      ax.text(distance, 0.5, f"●●", horizontalalignment="center", verticalalignment="center")

  plt.title("Fretboard locations of first 9 flageolets with cents detune from nearest note")
  plt.savefig("flageolets.png", bbox_inches="tight", dpi=200)
  plt.show()

def freqRatioToSemitones(freqRatio):
  """Convert a frequency ratio to tonal distance in semitones."""
  numSemitones = 12 * math.log(freqRatio, 2)

  return numSemitones

if __name__ == "__main__":
  main()
