# OMQ - EAL293 - R.403 - Nr.157 WEB 3 - JAVASCRIPT - LEBENDIG MACHEN!

## OMQ ist JavaScript! OMQ ist EAL293! HTML = Skelett! CSS = Kleidung! JavaScript = Muskeln! Gehirn! Ohne JS = Webseite ist tot! Statisch! Mit JS = Klick! Zähler! Rechner! Spiel! JS macht Webseite LEBENDIG! Button drücken -> Etwas passiert! Das ist JS!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Web-Trio!

| | Was? | Vergleich! |
| --- | --- | --- |
| HTML! | Inhalt! | Skelett! |
| CSS! | Aussehen! | Kleidung! |
| JavaScript! | Aktion! | Muskeln! Gehirn! |

### JS-Regel!

**Klick -> Funktion -> Änderung!**

Button onclick = Wenn geklickt, mach das!


```html
<!-- lebendig.html - OMQ Web JavaScript -->
<!DOCTYPE html>
<html>
<head><style>button { background: green; color: white; padding: 15px; font-size: 20px; }</style></head>
<body>
<h1 id='titel'>Klick den Button!</h1>
<p>Zähler: <span id='zahl'>0</span></p>
<button onclick='klick()'>Klick mich!</button>
<script>
let z = 0;
function klick() { z = z + 1; document.getElementById('zahl').innerText = z; document.getElementById('titel').innerText = 'Geklickt ' + z + ' Mal!'; }
</script>
</body>
</html>
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL293 R.403 - Nr.157

