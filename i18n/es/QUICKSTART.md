<!-- lang-bar -->
[English](../../QUICKSTART.md) · [Português (Brasil)](../pt-BR/QUICKSTART.md) · **Español** · [繁體中文](../zh-Hant/QUICKSTART.md) · [简体中文](../zh-Hans/QUICKSTART.md) · [日本語](../ja/QUICKSTART.md) · [العربية](../ar/QUICKSTART.md)

> Traducido de `QUICKSTART.md` (v1.2.2, 2026-11-26). Traducción asistida por máquina; la versión en inglés es la canónica.

# Guía rápida

Instala The Traveler's Watch (TTW), fija el rumbo de tu proyecto el primer día y úsalo cada día a
partir de entonces. Volver al [README](README.md).

**TTW se guía día a día (daily-led).** Tú diriges el trabajo de cada día. El vigía mantiene el rumbo a
la vista en cada prompt y la bitácora guarda el historial, así que cada día empieza desde donde el
proyecto está realmente, no desde lo que el modelo recuerda.

## 1. Instalación

Elige una opción.

| Opción | Comandos | Qué obtienes |
|---|---|---|
| **Plugin de Claude Code** (recomendado) | `/plugin marketplace add Icharu/travelerswatch`<br>`/plugin install travelerswatch@travelerswatch` | Skills + el vigía automático. Comandos: `/travelerswatch:checkwatch`, `/travelerswatch:fixwatch`, `/travelerswatch:configwatch` |
| **Solo las skills** (Claude Code o cualquier agente de [Agent Skills](https://agentskills.io/)) | `git clone https://github.com/Icharu/travelerswatch`<br>`cp -r travelerswatch/skills/checkwatch travelerswatch/skills/fixwatch travelerswatch/skills/configwatch ~/.claude/skills/` | Skills, sin vigía. Comandos: `/checkwatch`, `/fixwatch`, `/configwatch`. Ejecuta `/checkwatch` a mano al inicio de cada sesión. |
| **Probar sin instalar** | `claude --plugin-dir ./travelerswatch` | Todo, solo en esta sesión |

Requisitos: Claude Code para el vigía; `bash` y `awk` (macOS y Linux ya los traen); `git` es opcional,
pero habilita el recuento de commits y la revisión posproyecto completa.

## 2. Primer día: fija el rumbo

1. Abre Claude Code en la carpeta raíz del proyecto.
2. Ejecuta **`/checkwatch`**. Responde en una línea: qué es el proyecto y qué parte guía este rumbo.
3. Claude lee tu README, `docs/` y el historial reciente de git, y muestra una **tarjeta de
   evidencias** y **borradores** de cada sección. Tú los corriges; Claude pregunta por huecos,
   elementos mal ubicados y cualquier punto donde tus respuestas contradigan la evidencia. Cuenta con
   unas cinco rondas.
4. Confirma el rumbo. Claude escribe `.watch/WATCH.md` y añade `.watch/.state` a `.gitignore`.
5. **Haz commit de la bitácora**: `git add .watch/WATCH.md .gitignore && git commit -m "watch: bearing set"`.

A partir de aquí, nada en el rumbo cambia sin tu confirmación.

## 3. Cada día

| Cuándo | Qué haces tú | Qué hace TTW |
|---|---|---|
| **Al empezar el día** | Abre Claude Code y trabaja como siempre. | El vigía relee `.watch/WATCH.md` en tu primer prompt; los cambios confirmados ayer ya están vigentes. |
| **Mientras trabajas** | Pide lo que necesites: código, revisiones, borradores. | El trabajo repetitivo se hace dentro del rumbo. Si una petición se desvía, Claude lo dice en **una línea** y sigue. |
| **Aparece un aviso de desvío** | Decide: ¿fue un rodeo o el camino está cambiando de verdad? | Rodeo: sigue sin más. Cambio real: ejecuta **`/fixwatch`**, revisa el diff y su impacto, y confirma o cancela. |
| **«Toca un punto de control»** | Ejecuta **`/checkwatch`** cuando tengas un minuto. | Informa *En el camino / Desviándose / Fuera del camino / Rumbo en duda* con evidencias y añade una línea al Registro de puntos de control. |
| **Al terminar el día** | Haz commit de `.watch/WATCH.md` junto con tu trabajo si cambió. | Nada más. TTW no guarda datos fuera de tu repositorio. |
| **Al final de una fase o del proyecto** | Dile a Claude: «la fase termina, hagamos la revisión posproyecto». | Redacta una revisión a partir del Registro de puntos de control, el Path log y el historial de git. Tú eliges **revisar y cerrar** o **solo revisar**. |

### Qué sabe TTW, y cuándo

TTW sigue los cambios diarios del proyecto a través de la bitácora y de git, no vigilando tus
archivos. Con precisión:

| Momento | Qué se lee | Qué **no** se lee |
|---|---|---|
| **Cada prompt** (vigía) | El rumbo y el Status en `.watch/WATCH.md`; el número de commits y sesiones desde el último punto de control. | Tu código, diffs u otros archivos. |
| **Punto de control** (`/checkwatch`) | La conversación, el `git log` desde el último punto de control, los archivos modificados, los documentos listados en *Evidence scanned*. | Nada fuera de la carpeta del proyecto. |
| **Revisión posproyecto** | La bitácora completa (Registro de puntos de control + Path log) y el historial de git de `.watch/WATCH.md`. | Nada fuera de la carpeta del proyecto. |

## 4. Comandos de un vistazo

| Comando | Úsalo para |
|---|---|
| `/checkwatch` | Fijar el rumbo (la primera vez) · hacer un punto de control · hacer una revisión posproyecto |
| `/fixwatch` | Cambiar de rumbo a propósito · cerrar una revisión · reabrir un proyecto cerrado |
| `/configwatch` | Ver el estado · fijar la frecuencia de los puntos de control: inicial `every 3 commits or 2 sessions` (por defecto), estable `every 10 commits or 5 sessions`, personalizada u `off` |

## 5. Lo que TTW no hará por ti

TTW no confirmará un cambio, no aceptará una contradicción ni cerrará el proyecto en tu nombre, aunque
se lo pidas. Redactará el diff, revisará el impacto y reunirá la evidencia para que cada decisión te
lleve solo un vistazo. Es a propósito: consulta [Qué es y qué no es](README.md#qué-es-y-qué-no-es).

## 6. Desactivar o pausar

- En esta terminal: `export TRAVELERSWATCH_DISABLE=1`
- Para siempre: `/plugin` → travelerswatch → disable (las skills siguen funcionando a mano).
- Menos recordatorios de punto de control: `/configwatch` → estable u `off`.

## Siguientes pasos

[Conceptos](../../docs/concepts.md) · [Ejemplo completo](../../examples/pm-walkthrough.md) ·
[Métodos](../../docs/methods.md) · [Contribuir](CONTRIBUTING.md)
