<?php
if ($argc < 4) exit(1);

$szoveg = $argv[1];
$mentes = $argv[2];
$hang   = $argv[3];

$dir      = strtolower($hang);
$filePath = $dir . "/" . $mentes . ".wav";

if (file_exists($filePath)) {
    exit(0);
}

if (!is_dir($dir)) {
    mkdir($dir, 0777, true);
}

$apiKey    = getenv('AZURE_SPEECH_KEY');
$region    = 'northeurope';
$voiceName = ($hang === 'Maarten') ? 'nl-NL-MaartenNeural' : 'nl-NL-FennaNeural';

$cleanText = htmlspecialchars($szoveg, ENT_XML1, 'UTF-8');
$ssml = "<speak version='1.0' xml:lang='nl-NL'>"
      . "<voice xml:lang='nl-NL' name='" . $voiceName . "'>"
      . "<lang xml:lang='nl-NL'>" . $cleanText . "</lang>"
      . "</voice></speak>";

$endpoint = "https://" . $region . ".tts.speech.microsoft.com/cognitiveservices/v1";

$ch = curl_init($endpoint);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $ssml);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/ssml+xml; charset=utf-8",
    "X-Microsoft-OutputFormat: riff-16khz-16bit-mono-pcm",
    "Ocp-Apim-Subscription-Key: " . $apiKey,
    "User-Agent: TTSPHP"
]);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$result    = curl_exec($ch);
$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($http_code === 200 && $result) {
    file_put_contents($filePath, $result);
    // Wacht 3,5 seconden om de Azure F0-limiet (20 req/min) te respecteren
    usleep(3500000);
} else {
    fwrite(STDERR, "Fout HTTP $http_code voor: $szoveg\n");
    sleep(4);
    exit(1);
}
