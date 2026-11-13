# OMQ - EAL294 - R.404 - Nr.158 WEB 4 - DOM - DER BAUM!

## OMQ ist DOM! OMQ ist EAL294! DOM = Document Object Model! Browser macht aus HTML einen Baum! Wurzel = html! Äste = head, body! Blätter = h1, p, button! JavaScript greift in den Baum! Findet Blatt! Ändert Blatt! So funktioniert alles! Kein DOM = Kein JS!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### DOM-Baum!

| | |
| --- | --- |
| html | Wurzel! |
| head + body | Äste! |
| h1, p, button | Blätter! |

### DOM-Regel!

**document.getElementById('...') = Finde Blatt mit ID!**

**.innerText = Text ändern! .style.color = Farbe ändern!**


```html
<!-- baum.html - OMQ Web DOM -->
<!DOCTYPE html>
<html>
<body>
<h1 id='titel'>Ich bin ein Blatt!</h1>
<p id='text'>Finde mich!</p>
<button onclick='aendern()'>Baum ändern!</button>
<script>
function aendern() { document.getElementById('titel').innerText = 'Ich wurde geändert!'; document.getElementById('titel').style.color = 'red'; document.getElementById('text').innerText = 'DOM = Baum! JS ändert den Baum!'; }
</script>
</body>
</html>
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL294 R.404 - Nr.158

