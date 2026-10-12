[CmdletBinding()]
param(
    [switch]$PrintOnly,
    [string]$Name = '',
    [ValidateSet(1,2)][int]$SpriteVersion = 2
)
$ErrorActionPreference = 'Stop'
if ([string]::IsNullOrWhiteSpace($Name)) {
    $Name = [Uri]::UnescapeDataString('%E9%9B%AA%E4%BC%9E')
}
$imageFile = if ($SpriteVersion -eq 2) { 'xuesan.png' } else { 'xuesan-v1.png' }
$imageUrl = 'https://raw.githubusercontent.com/WMXhy/The-desk-favorite-of-Chat-GPT/main/assets/' + $imageFile
$description = 'Black-and-red hair, white horns, an ice-blue kimono, and a little red parasol.'
$installUri = 'codex://pets/install?name=' + [Uri]::EscapeDataString($Name) +
    '&imageUrl=' + [Uri]::EscapeDataString($imageUrl) +
    '&description=' + [Uri]::EscapeDataString($description) +
    '&spriteVersionNumber=' + $SpriteVersion
if ($PrintOnly) {
    Write-Output $installUri
    exit 0
}
Write-Host 'Opening the desktop app pet-import flow. Complete the import and select the pet in the app.'
Start-Process -FilePath $installUri
