<!-- lang-bar -->
[English](../../docs/tale.md) · [Português (Brasil)](../pt-BR/tale.md) · **Español** · [繁體中文](../zh-Hant/tale.md) · [简体中文](../zh-Hans/tale.md) · [日本語](../ja/tale.md) · [العربية](../ar/tale.md)

> Traducido de `docs/tale.md` (v1.2.3, 2026-11-26). Traducción asistida por máquina; la versión en inglés es la canónica.

# El Reloj del Viajero

*Una reescritura original, escrita para este proyecto.*

Un viajero se adentró en un valle que la niebla se había tragado por completo. No podía ver el
camino, así que confió en lo único que llevaba consigo que no dependía de la vista: su reloj de
bolsillo. Había calculado el viaje en horas: caminar hasta el mediodía, girar al este en el puente de
piedra, llegar al pueblo al anochecer.

A lo que el reloj llamaba mediodía, se detuvo, apretó la corona con el índice derecho y leyó las
agujas. Las doce. Giró al este. Caminó. Un rato después volvió a mirar, y el reloj marcaba las doce
menos diez. Frunció el ceño, supuso que lo había leído mal y siguió andando hasta que marcó otra vez
las doce. Giró al este una vez más.

No sabía que el reloj estaba roto. Cada vez que lo apretaba a mediodía, se atrasaba diez minutos. Así
que cada vez que lo miraba, volvía a recorrer un terreno que ya había pisado, convencido de que
avanzaba. La niebla ocultaba el puente de piedra por el que pasaba una y otra vez. Al anochecer
estaba cansado y no más cerca del pueblo, y no sabía decir dónde había perdido el día.

En la muralla del pueblo, un vigía guardaba su puesto toda la noche. Los viajeros, desde abajo, le
gritaban la vieja pregunta (*«Guarda, ¿qué de la noche?»*) y él respondía con lo que de verdad
alcanzaba a ver: por dónde iba el camino, cuánto faltaba para el alba. No adivinaba ni adulaba.
Cuando el camino cambiaba, lo decía, y decía por qué.

El problema del viajero no era la niebla. La niebla es normal; todo camino largo tiene algo. Su
problema era una referencia en la que no podía confiar, consultada justo en el momento en que más la
necesitaba, que retrocedía sin avisar, y nadie de guardia que le dijera que ya había visto ese
puente antes.

Si aquella noche hubiera llegado a la muralla y hubiera gritado la vieja pregunta, el vigía le habría
dicho lo que de verdad alcanzaba a ver: que el puente por el que pasaba era uno solo, y que su reloj
se atrasaba. El viajero habría abierto la caja y lo habría arreglado. No lo habría arreglado fiándose
de lo que decía el reloj, porque lo que fallaba era precisamente el reloj. Y el vigía nunca le habría
dicho que lo arreglara si el viajero no hubiera estado allí para preguntar. Ninguno de los dos habría
podido arreglar el reloj solo.

---

## Por qué esto es una skill

Los proyectos largos hechos con modelos de lenguaje se desvían de una manera muy parecida. Las
suposiciones iniciales se endurecen, parte de la conversación se pierde en resúmenes, y un modelo que
tomó un giro equivocado vuelve a él una y otra vez mientras cada paso, por separado, parece un
avance. The Traveler's Watch le da al proyecto dos cosas que al viajero le faltaron:

| En el cuento | En la skill |
|---|---|
| El viajero que pregunta, decide y arregla el reloj | **Tú, el jefe de proyecto**: fijas el rumbo y confirmas cada cambio |
| Un reloj en el que se puede confiar | El **rumbo** en `.watch/WATCH.md`: escrito, versionado, sin retroceder cuando se pierde el contexto |
| El informe honesto del vigía | El **hook del vigía**: en cada prompt, una línea si el trabajo se ha desviado |
| Girar al este a propósito | **`/fixwatch`**: un cambio de rumbo elegido, confirmado por el jefe de proyecto y registrado |
| Conocer el camino antes de salir | **`/checkwatch`**: Estándar, Contexto, Restricciones, Problema y Herramientas acordados antes de caminar |
| Mirar atrás desde la puerta del pueblo | **Revisión posproyecto**: lo que la bitácora muestra sobre todo el viaje |

Ninguna de las dos partes funciona sola. El vigía solo puede responder a un viajero que esté allí
para preguntar, y el viajero no puede fiarse de un reloj que nadie comprueba. Por eso TTW es un método
que se usa *entre* un modelo y una persona, nunca una herramienta que recorre el camino por ti.

La frase *«Guarda, ¿qué de la noche?»* es de Isaías 21:11 (dominio público).
