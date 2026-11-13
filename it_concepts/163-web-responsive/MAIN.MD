# OMQ - EAL299 - R.409 - Nr.163 WEB 9 - RESPONSIVE - HANDY + PC!

## OMQ ist Responsive! OMQ ist EAL299! Webseite auf PC = Breit! Schön! Gleiche Webseite auf Handy = Zerschossen! Winzig! Man muss scrollen! Schrecklich! Responsive = Webseite passt sich an! PC = Nebeneinander! Handy = Untereinander! Automatisch! Eine Seite! Alle Geräte!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Responsive!

| Gerät | Breite | Layout |
| --- | --- | --- |
| PC! | > 800px! | Nebeneinander! |
| Handy! | < 600px! | Untereinander! |

### Responsive-Regel!

**@media (max-width: 600px) { ... } = Wenn Handy, mach das!**


```html
<!-- responsive.html - OMQ Web Responsive -->
<!DOCTYPE html>
<html>
<head><meta name='viewport' content='width=device-width, initial-scale=1'><style>.box { display: flex; gap: 10px; } .karte { background: lightgreen; padding: 20px; flex: 1; } @media (max-width: 600px) { .box { flex-direction: column; } .karte { background: lightpink; } }</style></head>
<body>
<h1>Zieh mich klein!</h1>
<p>PC = Grün nebeneinander! Handy = Rosa untereinander!</p>
<div class='box'><div class='karte'>Karte 1</div><div class='karte'>Karte 2</div><div class='karte'>Karte 3</div></div>
</body>
</html>
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL299 R.409 - Nr.163

