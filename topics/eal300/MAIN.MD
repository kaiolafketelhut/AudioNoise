# OMQ - EAL300 - R.410 - Nr.164 WEB 10 - PROJEKT - DEINE EIGENE WEBSEITE!

## OMQ ist PROJEKT! OMQ ist EAL300! 300 Lektionen! Du kannst jetzt: HTML + CSS + JS + DOM + Formular + Flexbox + Fetch + LocalStorage + Responsive! Jetzt: ALLES ZUSAMMEN! Eine echte Webseite! Mit allem! Das ist dein Meisterstück!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Was drin ist!

| Teil | Aus Lektion |
| --- | --- |
| HTML! | EAL291! |
| CSS + Flexbox! | EAL292 + EAL296! |
| DOM + JS! | EAL293 + EAL294! |
| Formular! | EAL295! |
| Fetch Witz! | EAL297! |
| LocalStorage! | EAL298! |
| Responsive! | EAL299! |

### Projekt-Regel!

**Eine Datei = Alles! HTML + CSS + JS zusammen = Echte Webseite!**


```html
<!-- meine-seite.html - OMQ MEISTERSTÜCK -->
<!DOCTYPE html>
<html>
<head><meta name='viewport' content='width=device-width, initial-scale=1'><style>body{font-family:sans-serif;text-align:center}.box{display:flex;gap:10px;justify-content:center}.karte{background:lightblue;padding:20px;border-radius:10px;flex:1}@media(max-width:600px){.box{flex-direction:column}.karte{background:lightpink}}</style></head>
<body>
<h1 id='titel'>Hallo! Ich bin Kai!</h1>
<p>Name: <input id='name' type='text'> <button onclick='speichern()'>Merken!</button></p>
<p id='gruss'></p>
<div class='box'><div class='karte'>HTML - Knochen!</div><div class='karte'>CSS - Haut!</div><div class='karte'>JS - Muskeln!</div></div>
<p><button onclick='holWitz()'>Neuer Witz aus Internet!</button></p><p id='witz'></p>
<script>
let alt=localStorage.getItem('name'); if(alt){document.getElementById('gruss').innerText='Hallo zurück, '+alt+'!';}
function speichern(){let n=document.getElementById('name').value; localStorage.setItem('name',n); document.getElementById('gruss').innerText='Gespeichert, '+n+'!';}
async function holWitz(){let a=await fetch('https://api.chucknorris.io/jokes/random'); let d=await a.json(); document.getElementById('witz').innerText=d.value;}
</script>
</body>
</html>
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL300 R.410 - Nr.164

