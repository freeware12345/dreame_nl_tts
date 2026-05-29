
## English

I have created 4 voice packages using Microsoft Azure TTS for Dreame vacuums. Two of these are **Tamás** and **Noémi** (native Hungarian voices), while **Ryan** and **Jenny** are Multilingual voices that also support Hungarian. The multilingual voices have a unique charm, but they are quite good.

**Compatibility and Info:**

  * **Supported Devices:** Likely works on all **Dreame**, as well as **Mova** and **Truver** robot vacuums. (Note: The wording is optimized for rotary mop pads; models with roller mops might have slight terminology discrepancies, but functionality remains unaffected.)
  * **Tested on:** Dreame X50 Ultra Complete and L10 Prime.
  * **Translation:** Since the original English package was incomplete for newer models, the missing parts were translated from the original Chinese voice package using auditory AI translation. Therefore, minor errors may occur, but the functionality remains clear.

### Voice Package Data (Updated):

  - **tamas\_dreame\_hu\_voice** (Microsoft TTS - hu-HU-TamasNeural):

      - URL: `https://raw.githubusercontent.com/v1k70rk4/dreame_hu_tts/main/dreame_voicepack_hu/tamas_dreame_hu_voice`
      - MD5 hash: `c11b64d9d473d7c0404836822e6f3d74`
      - File size: `13320907` bytes

  - **noemi\_dreame\_hu\_voice** (Microsoft TTS - hu-HU-NoemiNeural):

      - URL: `https://raw.githubusercontent.com/v1k70rk4/dreame_hu_tts/main/dreame_voicepack_hu/noemi_dreame_hu_voice`
      - MD5 hash: `2f69f5bd66fd7199353169efaf05ed92`
      - File size: `15148480` bytes

  - **ryan\_dreame\_hu\_voice** (Microsoft TTS - en-US-RyanMultilingualNeural):

      - URL: `https://raw.githubusercontent.com/v1k70rk4/dreame_hu_tts/main/dreame_voicepack_hu/ryan_dreame_hu_voice`
      - MD5 hash: `f7b0b17793f4a50e9cecfd73ca9beaf3`
      - File size: `13500677` bytes

  - **jenny\_dreame\_hu\_voice** (Microsoft TTS - en-US-JennyMultilingualV2Neural):

      - URL: `https://raw.githubusercontent.com/v1k70rk4/dreame_hu_tts/main/dreame_voicepack_hu/jenny_dreame_hu_voice`
      - MD5 hash: `f2855619fcf421dc08f163d29737e665`
      - File size: `13528449` bytes

### Installation Guide:

#### 1\. HomeAssistant (Dreame Vacuum Integration)

Run the following command under Developer Tools / Services (example for Noémi voice):

```yaml
service: dreame_vacuum.vacuum_install_voice_pack
data:
  url: >-
    [https://raw.githubusercontent.com/v1k70rk4/dreame_hu_tts/main/dreame_voicepack_hu/noemi_dreame_hu_voice](https://raw.githubusercontent.com/v1k70rk4/dreame_hu_tts/main/dreame_voicepack_hu/noemi_dreame_hu_voice)
  lang_id: hu
  md5: "2f69f5bd66fd7199353169efaf05ed92"
  size: 15148480
target:
  entity_id: vacuum.dreamebot_<<<entity_id>>>
```

#### 2\. Valetudo

Go to `Robot Settings` -\> `Misc Settings`.
In the `Voice packs` section, enter the following (example for Noémi voice):

  * **URL:** `https://raw.githubusercontent.com/v1k70rk4/dreame_hu_tts/main/dreame_voicepack_hu/noemi_dreame_hu_voice`
  * **Language Code:** `hu`
  * **Hash:** `2f69f5bd66fd7199353169efaf05ed92`
  * **File size:** `15148480`
    Then click the `Set Voice Pack` button.

### Creating Your Own TTS Voice:

If any sound is missing, you can create your own using the attached CSV, along with the PHP and Python scripts. You do not need this part if you are satisfied with the pre-made voice packages\!

1.  **API Key:** You need a Microsoft Azure Speech (Bing TTS) API key, which must be entered in line 12 of the `bing_hu_voice.php` file.
2.  **Required Programs:** (Instructions above are for Windows, but Linux users can install via repo).
      * PHP 7/8 (add to PATH)
      * Vorbis-tools (add `oggenc.exe` to PATH)
      * FFmpeg
      * Python 3.11
3.  **Usage:**
      * `ttscreate.py VOICE --convert` : Generates WAVs from CSV -\> Normalizes -\> Converts to OGG -\> Copies non-TTS sounds -\> Cleans up placeholders -\> Creates .tar.gz -\> Generates MD5 and size info.
      * `bing_hu_voice.php "text" filename VOICE` : Generates a single WAV file for corrections.
      * `convert.py VOICE` : Converts WAV to OGG if skipped previously.

<!-- end list -->

```
```
