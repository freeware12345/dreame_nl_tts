# Dreame NL TTS — Dutch Voice Packages for Dreame Vacuum Cleaners

I have created 2 voice packages using Microsoft Azure TTS for Dreame vacuums: **Fenna** and **Maarten** (native Dutch voices).

**Compatibility and info:**

* **Supported devices:** Likely works on all **Dreame**, **Mova**, and **Truver** robot vacuums. (Note: The wording is optimized for rotary mop pads; models with roller mops might have slight terminology discrepancies, but functionality remains unaffected.)
* **Tested on:** Dreame L50s Pro Ultra.
* **Translation:** Since the original English package was incomplete for newer models, the missing parts were translated from the original Chinese voice package using auditory AI translation. Minor errors may occur, but functionality remains clear.

---

## Voice Package Data

- **fenna\_dreame\_nl\_voice** (Microsoft TTS - nl-NL-FennaNeural):

  - URL: `https://raw.githubusercontent.com/freeware12345/dreame_nl_tts/main/dreame_voicepack_nl/fenna_dreame_nl_voice`
  - MD5 hash: *(generated after workflow run)*
  - File size: *(generated after workflow run)*

- **maarten\_dreame\_nl\_voice** (Microsoft TTS - nl-NL-MaartenNeural):

  - URL: `https://raw.githubusercontent.com/freeware12345/dreame_nl_tts/main/dreame_voicepack_nl/maarten_dreame_nl_voice`
  - MD5 hash: *(generated after workflow run)*
  - File size: *(generated after workflow run)*

---

## Installation Guide

### 1. HomeAssistant (Dreame Vacuum Integration)

Run the following command under Developer Tools / Services (example for Fenna):

```yaml
service: dreame_vacuum.vacuum_install_voice_pack
data:
  url: https://raw.githubusercontent.com/freeware12345/dreame_nl_tts/main/dreame_voicepack_nl/fenna_dreame_nl_voice
  lang_id: nl
  md5: "<md5-hash>"
  size: <file-size-in-bytes>
target:
  entity_id: vacuum.dreamebot_<<<entity_id>>>
```

### 2. Valetudo

Go to `Robot Settings` → `Misc Settings`.
In the `Voice packs` section, enter the following (example for Fenna):

* **URL:** `https://raw.githubusercontent.com/freeware12345/dreame_nl_tts/main/dreame_voicepack_nl/fenna_dreame_nl_voice`
* **Language Code:** `nl`
* **Hash:** `<md5-hash>`
* **File size:** `<file-size-in-bytes>`

Then click the `Set Voice Pack` button.

---

## Creating Your Own TTS Voice

If you want to customize a voice or a sound is missing, you can generate your own package using the included CSV, PHP, and Python scripts. You do not need this if you are satisfied with the pre-made voice packages!

1. **API key:** You need a Microsoft Azure Speech API key. Save it as the secret `AZURE_SPEECH_KEY` in your GitHub repository settings.
2. **Required programs:** (automatically installed via the GitHub Actions workflow)
   * PHP 8.1
   * Vorbis-tools (`oggenc`)
   * FFmpeg
   * Python 3
3. **Usage via GitHub Actions:**
   * Go to **Actions → Create Voice Package → Run workflow**
   * Choose a voice (Fenna or Maarten)
   * After completion, the `.tar.gz` file is available as a downloadable artifact, with the MD5 hash and file size printed in the workflow logs.
4. **Manual usage (local):**
   * `python ttscreate.py Fenna --convert` — Generates WAV files from CSV → normalizes → converts to OGG → copies non-TTS sounds → cleans up placeholders → creates `.tar.gz` → outputs MD5 and size info.
   * `php bing_hu_voice.php "text" filename Fenna` — Generates a single WAV file for corrections.
   * `python convert.py Fenna` — Converts WAV to OGG if the conversion was skipped previously.
