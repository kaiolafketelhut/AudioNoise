# OMQ - EAL295 - R.405 - Nr.159 WEB 5 - FORMULAR - EINGABEN!

## OMQ ist Formular! OMQ ist EAL295! Webseite ohne Eingabe = Plakat! Langweilig! Formular = User tippt! Name! Alter! Passwort! Button = Senden! So funktioniert Login! So funktioniert Google! So funktioniert Shop! Ohne Formular = Kein Internet wie wir es kennen!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Formular!

| Tag | Was? |
| --- | --- |
| input! | Eingabefeld! |
| type=text! | Text! |
| type=password! | Passwort - Punkte! |
| type=number! | Zahl! |
| button! | Senden! |

### Formular-Regel!

**input.value = Was User getippt hat!**


```html
<!-- formular.html - OMQ Web Formular -->
<!DOCTYPE html>
<html>
<body>
<h1>Wer bist du?</h1>
<p>Name: <input id='name' type='text' placeholder='Dein Name'></p>
<p>Alter: <input id='alter' type='number' placeholder='18'></p>
<button onclick='sagHallo()'>Senden!</button>
<p id='gruss'></p>
<script>
function sagHallo() { let n = document.getElementById('name').value; let a = document.getElementById('alter').value; document.getElementById('gruss').innerText = 'Hallo ' + n + '! Du bist ' + a + ' Jahre alt! OMQ!'; }
</script>
</body>
</html>
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL295 R.405 - Nr.159

