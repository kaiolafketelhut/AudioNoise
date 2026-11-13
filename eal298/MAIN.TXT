# OMQ - EAL298 - R.408 - Nr.162 WEB 8 - LOCALSTORAGE - MERKEN!

## OMQ ist LocalStorage! OMQ ist EAL298! Browser vergisst alles bei Refresh! Du tippst Name! Refresh! Weg! Schrecklich! LocalStorage = Browser merkt sich! Wie Notizbuch im Browser! Speichern! Laden! Bleibt auch nach Schließen! So funktioniert Dark Mode! So funktioniert Warenkorb!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### LocalStorage!

| Code | Was? |
| --- | --- |
| localStorage.setItem('name', 'Kai')! | Speichern! |
| localStorage.getItem('name')! | Laden! |
| localStorage.removeItem('name')! | Löschen! |

### LocalStorage-Regel!

**setItem = Speichern! getItem = Laden! Bleibt für immer - bis du löschst!**


```html
<!-- merken.html - OMQ Web LocalStorage -->
<!DOCTYPE html>
<html>
<body>
<h1>Ich merke mir dich!</h1>
<p>Name: <input id='name' type='text'></p>
<button onclick='speichern()'>Speichern!</button>
<button onclick='loeschen()'>Vergessen!</button>
<p id='gruss'></p>
<script>
let alt = localStorage.getItem('name');
if (alt) { document.getElementById('gruss').innerText = 'Hallo zurück, ' + alt + '! Ich habe dich gemerkt!'; }
function speichern() { let n = document.getElementById('name').value; localStorage.setItem('name', n); document.getElementById('gruss').innerText = 'Gespeichert! ' + n + '! Refresh mal! Ich vergesse dich nicht!'; }
function loeschen() { localStorage.removeItem('name'); document.getElementById('gruss').innerText = 'Vergessen!'; }
</script>
</body>
</html>
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL298 R.408 - Nr.162

