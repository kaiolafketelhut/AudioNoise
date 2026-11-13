# OMQ - EAL297 - R.407 - Nr.161 WEB 7 - FETCH API - DATEN AUS INTERNET!

## OMQ ist Fetch! OMQ ist EAL297! Webseite ohne Daten = Leer! Fetch = Hol Daten aus Internet! Wie Bestellung! Du sagst: Gib mir Wetter! Gib mir Witz! Gib mir Katze! Server schickt JSON zurück! JS zeigt es an! So funktioniert jede App!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Fetch!

| Schritt | Was? |
| --- | --- |
| 1. fetch(url)! | Anfrage schicken! |
| 2. .json()! | Antwort in JSON umwandeln! |
| 3. Anzeigen! | Im DOM zeigen! |

### Fetch-Regel!

**fetch('https://...') .then(r => r.json()) .then(d => zeig(d))!**


```html
<!-- fetch.html - OMQ Web Fetch API -->
<!DOCTYPE html>
<html>
<body>
<h1>Zufalls-Witz!</h1>
<button onclick='holWitz()'>Neuer Witz!</button>
<p id='witz'>Klick den Button!</p>
<script>
async function holWitz() { document.getElementById('witz').innerText = 'Lade...'; let antwort = await fetch('https://api.chucknorris.io/jokes/random'); let daten = await antwort.json(); document.getElementById('witz').innerText = daten.value; }
</script>
</body>
</html>
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL297 R.407 - Nr.161

