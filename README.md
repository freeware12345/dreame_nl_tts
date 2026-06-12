Dreame NL TTS — Dutch Voice Packages for Dreame Vacuum Cleaners

This repository provides a ready-to-use Dutch voice package for Dreame robot vacuum cleaners, generated using Microsoft Azure TTS. The voice used is Fenna (nl-NL-FennaNeural), a native Dutch voice.

Compatibility and info:


Supported devices: Likely works on all Dreame, Mova, and Truver robot vacuums. (Note: The wording is optimized for rotary mop pads; models with roller mops might have slight terminology discrepancies, but functionality remains unaffected.)
Tested on: Dreame L50s Pro Ultra.
Translation: Since the original English package was incomplete for newer models, the missing parts were translated from the original Chinese voice package using auditory AI translation. Minor errors may occur, but functionality remains clear.



Voice Package Data


fenna_dreame_nl_voice (Microsoft TTS - nl-NL-FennaNeural):

URL: https://raw.githubusercontent.com/freeware12345/dreame_nl_tts/main/dreame_voicepack_nl.tar.gz
MD5 hash: d959396effaa3803636428e3bf260fbe
File size: 12667045 bytes






Installation Guide

1. HomeAssistant (Dreame Vacuum Integration)

Go to Developer Tools → Actions, and run the following:

yamlaction: dreame_vacuum.vacuum_install_voice_pack
data:
  url: https://raw.githubusercontent.com/freeware12345/dreame_nl_tts/main/dreame_voicepack_nl.tar.gz
  lang_id: nl
  md5: d959396effaa3803636428e3bf260fbe
  size: 12667045
target:
  entity_id: vacuum.your_vacuum_entity_id

Replace vacuum.your_vacuum_entity_id with your actual entity ID. You can find it under Developer Tools → States by searching for vacuum.

2. Valetudo

Go to Robot Settings → Misc Settings.
In the Voice packs section, enter the following:


URL: https://raw.githubusercontent.com/freeware12345/dreame_nl_tts/main/dreame_voicepack_nl.tar.gz
Language Code: nl
Hash: d959396effaa3803636428e3bf260fbe
File size: 12667045


Then click the Set Voice Pack button.


Creating Your Own TTS Voice

If you want to customize a voice or a sound is missing, you can generate your own package using the included CSV, PHP, and Python scripts. You do not need this if you are satisfied with the pre-made voice package!


API key: You need a Microsoft Azure Speech API key. Save it as the secret AZURE_SPEECH_KEY in your GitHub repository settings.
Required programs: (automatically installed via the GitHub Actions workflow)

PHP 8.1
Vorbis-tools (oggenc)
FFmpeg
Python 3



Usage via GitHub Actions:

Fork this repository
Add your AZURE_SPEECH_KEY as a secret under Settings → Secrets and variables → Actions
Go to Actions → Create Voice Package → Run workflow
Choose a voice (Fenna or Maarten)
After completion, the .tar.gz file is available as a downloadable artifact, with the MD5 hash and file size printed in the workflow logs.



Manual usage (local):

python ttscreate.py Fenna --convert — Generates WAV files from CSV → normalizes → converts to OGG → copies non-TTS sounds → cleans up placeholders → creates .tar.gz → outputs MD5 and size info.
php bing_hu_voice.php "text" filename Fenna — Generates a single WAV file for corrections.
python convert.py Fenna — Converts WAV to OGG if the conversion was skipped previously.
