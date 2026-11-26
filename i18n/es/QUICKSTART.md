<!-- lang-bar -->
[English](../../QUICKSTART.md) · [Português (Brasil)](../pt-BR/QUICKSTART.md) · **Español** · [繁體中文](../zh-Hant/QUICKSTART.md) · [简体中文](../zh-Hans/QUICKSTART.md) · [日本語](../ja/QUICKSTART.md) · [العربية](../ar/QUICKSTART.md)

> Traducido de `QUICKSTART.md` (v1.2.3, 2026-11-26) al español internacional neutro. Traducción asistida por máquina; la versión en inglés es la canónica.

# Guía rápida

Cómo instalar The Traveler's Watch (TTW), fijar el rumbo del proyecto el primer día y usarlo cada
día a partir de entonces. Volver al [README](README.md).

**TTW se guía día a día (daily-led).** Usted dirige el trabajo de cada día. El vigía mantiene el
rumbo a la vista en cada prompt y la bitácora guarda el historial, así que cada día empieza desde
donde el proyecto está realmente, no desde lo que el modelo recuerda.

## 1. Instalación

Elija una opción.

| Opción | Comandos | Qué se obtiene |
|---|---|---|
| **Plugin de Claude Code** (recomendado) | `/plugin marketplace add Icharu/travelerswatch`<br>`/plugin install travelerswatch@travelerswatch` | Skills + el vigía automático. Comandos: `/travelerswatch:checkwatch`, `/travelerswatch:fixwatch`, `/travelerswatch:configwatch` |
| **Solo las skills** (Claude Code o cualquier agente de [Agent Skills](https://agentskills.io/)) | `git clone https://github.com/Icharu/travelerswatch`<br>`cp -r travelerswatch/skills/checkwatch travelerswatch/skills/fixwatch travelerswatch/skills/configwatch ~/.claude/skills/` | Skills, sin vigía. Comandos: `/checkwatch`, `/fixwatch`, `/configwatch`. Ejecute `/checkwatch` a mano al inicio de cada sesión. |
| **Probar sin instalar** | `claude --plugin-dir ./travelerswatch` | Todo, solo en esta sesión |

Requisitos: Claude Code para el vigía; `bash` y `awk` (macOS y Linux ya los incluyen); `git` es
opcional, pero habilita el recuento de commits y la revisión posproyecto completa.

## 2. Primer día: fijar el rumbo

1. Abra Claude Code en la carpeta raíz del proyecto.
2. Ejecute **`/checkwatch`**. Responda en una línea: qué es el proyecto y qué parte guía este rumbo.
3. Claude lee el README, `docs/` y el historial reciente de git, y muestra una **tarjeta de
   evidencias** y **borradores** de cada sección. Usted los corrige; Claude pregunta por huecos,
   elementos mal ubicados y cualquier punto donde sus respuestas contradigan la evidencia. Conviene
   contar con unas cinco rondas; en el benchmark de la v1.0.0 fueron unas 4 en el mejor caso y unas
   11 en el peor.
4. Confirme el rumbo. Claude escribe `.watch/WATCH.md` y añade `.watch/.state` a `.gitignore`.
5. **Haga commit de la bitácora**: `git add .watch/WATCH.md .gitignore && git commit -m "watch: bearing set"`.

A partir de aquí, las skills están escritas para que nada en el rumbo cambie sin su confirmación.

## 3. Cada día

| Cuándo | Qué hace usted | Qué hace TTW |
|---|---|---|
| **Al empezar el día** | Abra Claude Code y trabaje como siempre. | El vigía relee `.watch/WATCH.md` en su primer prompt; los cambios confirmados el día anterior ya están vigentes. |
| **Durante el trabajo** | Pida lo que necesite: código, revisiones, borradores. | El trabajo repetitivo se hace dentro del rumbo. Si una petición se desvía, Claude lo dice en **una línea** y sigue. |
| **Aparece un aviso de desvío** | Decida: ¿fue un rodeo o el camino está cambiando de verdad? | Rodeo: continúe sin más. Cambio real: ejecute **`/fixwatch`**, revise el diff y su impacto, y confirme o cancele. |
| **«Corresponde un punto de control»** | Ejecute **`/checkwatch`** cuando tenga un momento. | Informa *En el camino / Desviándose / Fuera del camino / Rumbo en duda* con evidencias y añade una línea al Registro de puntos de control. |
| **Al terminar el día** | Haga commit de `.watch/WATCH.md` junto con su trabajo si cambió. | Nada más. TTW no guarda datos fuera de su repositorio. |
| **Al final de una fase o del proyecto** | Dígale a Claude: «la fase termina, hagamos la revisión posproyecto». | Redacta una revisión a partir del Registro de puntos de control, el Path log y el historial de git. Usted elige **revisar y cerrar** o **solo revisar**. |

### Qué sabe TTW, y cuándo

TTW sigue los cambios diarios del proyecto a través de la bitácora y de git, no vigilando sus
archivos. Con precisión:

| Momento | Qué se lee | Qué **no** se lee |
|---|---|---|
| **Cada prompt** (vigía) | El rumbo y el Status en `.watch/WATCH.md`; el número de commits y sesiones desde el último punto de control. | Su código, diffs u otros archivos. |
| **Punto de control** (`/checkwatch`) | La conversación, el `git log` desde el último punto de control, los archivos modificados, los documentos listados en *Evidence scanned*; las issues y pull requests abiertos a través de la CLI de su forja (p. ej., `gh`), si está instalada. | Nada fuera de la carpeta del proyecto está en la lista de lectura de la skill. |
| **Revisión posproyecto** | La bitácora completa (Registro de puntos de control + Path log) y el historial de git de `.watch/WATCH.md`. | Nada fuera de la carpeta del proyecto. |

## 4. Comandos de un vistazo

| Comando | Sirve para |
|---|---|
| `/checkwatch` | Fijar el rumbo (la primera vez) · hacer un punto de control · hacer una revisión posproyecto |
| `/fixwatch` | Cambiar de rumbo a propósito · cerrar una revisión · reabrir un proyecto cerrado |
| `/configwatch` | Ver el estado · fijar la frecuencia de los puntos de control: inicial `every 3 commits or 2 sessions` (por defecto), estable `every 10 commits or 5 sessions`, personalizada u `off` |

## 5. Lo que TTW no hará por usted

Las skills están escritas para no confirmar un cambio, no aceptar una contradicción ni cerrar el
proyecto en su nombre, aunque usted lo pida (probado con evals, no impuesto por código). Redactarán
el diff, revisarán el impacto y reunirán la evidencia para que cada decisión le lleve solo un
vistazo. Es a propósito: consulte [Qué es y qué no es](README.md#qué-es-y-qué-no-es).

## 6. Desactivar o pausar

- En esta terminal: `export TRAVELERSWATCH_DISABLE=1`
- De forma permanente: `/plugin` → travelerswatch → disable (las skills siguen funcionando a mano).
- Menos recordatorios de punto de control: `/configwatch` → estable u `off`.

## Siguientes pasos

[Conceptos](../../docs/concepts.md) · [Ejemplo completo](../../examples/pm-walkthrough.md) ·
[Métodos](../../docs/methods.md) · [Contribuir](CONTRIBUTING.md)
