# OMQ - EAL296 - R.406 - Nr.160 WEB 6 - CSS FLEXBOX - LAYOUT!

## OMQ ist Flexbox! OMQ ist EAL296! Früher: Elemente untereinander! Wie Liste! Langweilig! Flexbox: Elemente NEBENEINANDER! Wie Regale! Wie Menü! Wie Karten! Jede moderne Webseite = Flexbox! Ohne Flexbox = Kein schönes Layout!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Flexbox!

| Code | Was? |
| --- | --- |
| display: flex; | Mach Box zu Flex! |
| justify-content: center; | Mitte! |
| gap: 10px; | Abstand! |
| flex-direction: column; | Untereinander! |

### Flexbox-Regel!

**Container = display: flex! Kinder = Daneben!**


```html
<!-- flexbox.html - OMQ Web Flexbox -->
<!DOCTYPE html>
<html>
<head><style>.box { display: flex; gap: 10px; justify-content: center; } .karte { background: lightblue; padding: 20px; border-radius: 10px; font-size: 20px; }</style></head>
<body>
<h1 style='text-align:center'>Meine Karten!</h1>
<div class='box'>
<div class='karte'>Karte 1 - Katze!</div>
<div class='karte'>Karte 2 - Hund!</div>
<div class='karte'>Karte 3 - Berlin!</div>
</div>
</body>
</html>
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL296 R.406 - Nr.160

