<!-- lang-bar -->
[English](README.md) · [Português (Brasil)](README.pt-BR.md) · **Español** · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [العربية](README.ar.md)

> Traducido de `README.md` v1.1.0 (2026-11-25). Traducción asistida por máquina; se agradecen las revisiones de hablantes nativos. La versión en inglés es la canónica.

# The Traveler's Watch (El Reloj del Viajero)

[![Version](https://img.shields.io/badge/version-v1.1.0-blue)](CHANGELOG.md)
[![License: MIT (code) + CC BY 4.0 (docs)](https://img.shields.io/badge/license-MIT%20%2B%20CC%20BY%204.0-green)](LICENSE-docs)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24543183.svg)](https://doi.org/10.5281/zenodo.24543183)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-8A2BE2)](https://agentskills.io/)

**Evaluación, análisis de metodología y vigilancia de la deriva de contexto para proyectos con Claude.**
Fija el rumbo de tu proyecto una vez, recibe un aviso de una línea cada vez que el trabajo se desvíe
de él y cambia de rumbo solo a propósito, con cada cambio confirmado por el jefe de proyecto y
registrado.

> Un viajero cruza una niebla espesa con un reloj roto. Cada vez que lo mira al mediodía, se atrasa
> diez minutos, así que sigue recorriendo el mismo tramo, convencido de que avanza.
> — [lee el cuento completo](docs/tale.md)

Los proyectos largos hechos con modelos de lenguaje fallan de la misma manera: las suposiciones
iniciales se endurecen, el contexto se pierde en resúmenes y un modelo que tomó un giro equivocado
vuelve a él una y otra vez ([por qué ocurre](docs/methods.md)). The Traveler's Watch le da a tu
proyecto un reloj en el que puedes confiar.

## Cómo funciona

| Comando | Qué hace |
|---|---|
| **`/checkwatch`** | **Sin bitácora:** primero lee la documentación y el historial del propio proyecto, luego acuerda contigo el *rumbo* (Alcance, Estándar, Contexto, Restricciones, Problema, Herramientas), mueve los elementos mal ubicados, te pide resolver o aceptar cada contradicción con la evidencia y escribe `.watch/WATCH.md`. **Con bitácora:** hace un punto de control sobre el trabajo *y* sobre el propio rumbo e informa **En el camino / Desviándose / Fuera del camino / Rumbo en duda**, con evidencias. |
| **vigía** *(automático)* | En cada prompt, un hook de Claude Code le recuerda el rumbo a Claude. Si tu petición se desvía, Claude lo dice en una línea, sugiere `/fixwatch` y continúa con la tarea. También avisa, una vez por sesión, cuando toca un punto de control, y se pausa mientras el rumbo está *en revisión*. |
| **`/fixwatch`** | Propone un cambio de rumbo como un diff antes/después, muestra qué más afecta, espera la confirmación del jefe de proyecto y solo entonces actualiza el rumbo y **añade** una entrada al Registro de ruta (*Path log*). Claude puede proponer, incluso cuando malinterpretó el contexto; solo el jefe de proyecto confirma. |
| **`/configwatch`** | Muestra el estado del vigía y define cada cuánto pide un punto de control: cada *N* commits o *M* sesiones (por defecto 3 o 2), o desactivado. |

### Anclado en evidencias

Un rumbo puede ser coherente consigo mismo y aun así estar equivocado sobre el proyecto. Desde la v1.1.0, el reloj se ajusta con la evidencia del propio proyecto, un punto de control temprano detecta los errores pronto y el vigía se pausa mientras el rumbo está en revisión ([por qué](docs/benchmarks/2026-11-25-best-vs-worst.md)).

### El rumbo

| Sección | Responde a esto |
|---|---|
| **Alcance** (*Scope*) | ¿Qué parte del proyecto guía este rumbo, y cuál no? |
| **Estándar** (*Standard*) | ¿Contra qué se evaluará el trabajo? Un **preset de lente**, una **rúbrica de texto libre** o un **estándar externo con nombre**, siempre verificado en pertinencia, evaluabilidad, coherencia, alcance, derechos y ética. |
| **Contexto** (*Context*) | ¿Dónde vive este trabajo? Campo, partes interesadas, estado actual, **obras de referencia**. |
| **Restricciones** (*Constraints*) | ¿Qué te limita? Plazo, presupuesto, personas, tecnología obligatoria, regulación. |
| **Problema** (*Problem*) | ¿Qué falla hoy (**problema original**) y cómo se ve "terminado" (**objetivo final**)? |
| **Herramientas** (*Tools*) | ¿Qué vas a usar, y por qué cada una encaja con el contexto y las restricciones? |

### Lentes

Las lentes adaptan las preguntas y los criterios por defecto a un campo.
Incluidas: [Gestión de Proyectos](skills/checkwatch/references/lenses/project-management.md) (por defecto) ·
[Investigación](skills/checkwatch/references/lenses/research.md) ·
[Software](skills/checkwatch/references/lenses/software.md) ·
[Ciencia de Datos](skills/checkwatch/references/lenses/data-science.md).
Para añadir la tuya, consulta [CONTRIBUTING.md](CONTRIBUTING.md#adding-a-lens).

## Instalación

**Como plugin de Claude Code** (skills + hook del vigía):

```text
/plugin marketplace add Icharu/travelerswatch
/plugin install travelerswatch@travelerswatch
```

Los comandos quedan con espacio de nombres: `/travelerswatch:checkwatch`, `/travelerswatch:fixwatch`, `/travelerswatch:configwatch`.

**Solo las skills** (Claude Code o cualquier agente que lea [Agent Skills](https://agentskills.io/); sin hook):

```bash
git clone https://github.com/Icharu/travelerswatch
cp -r travelerswatch/skills/checkwatch travelerswatch/skills/fixwatch travelerswatch/skills/configwatch ~/.claude/skills/
```

Los comandos son entonces `/checkwatch`, `/fixwatch` y `/configwatch`. Sin el hook, ejecuta `/checkwatch` al inicio
de cada sesión de trabajo.

**Probar en local sin instalar:** `claude --plugin-dir ./travelerswatch`

**Desactivar el vigía temporalmente:** `export TRAVELERSWATCH_DISABLE=1`

## Ejemplo rápido

```text
Tú:     /checkwatch
Claude: Aún no hay bitácora. Primero, el Estándar: ¿preset de lente, tu propia rúbrica o un estándar con nombre?
Tú:     Lente de GP. Contexto: solo tenemos dos personas a media jornada. Problema: crear una app de recogida.
Claude: "Solo dos personas a media jornada" es una limitación, así que va en Restricciones.
        "Crear una app de recogida" es una solución. ¿Qué problema hay detrás y cómo se ve "terminado"?
…
Tú:     Añadamos una app gamificada para toda la ciudad.
Claude: ⚠️ Vigía: se desvía del Problema (dos distritos piloto) y de las Restricciones (presupuesto de 20 mil).
        ¿Continuar o /fixwatch?
```

Sesión completa (en inglés): [examples/pm-walkthrough.md](examples/pm-walkthrough.md).

## Estructura del repositorio

```text
.claude-plugin/        manifiestos del plugin y del marketplace
skills/checkwatch/     SKILL.md · references/ (estándares, secciones, relaciones, lentes) · assets/WATCH.md · evals/
skills/fixwatch/       SKILL.md · evals/
skills/configwatch/    SKILL.md · evals/
hooks/                 hooks.json · watchman.sh (bash + awk, sin otras dependencias)
tests/                 watchman.test.sh
docs/                  cuento · conceptos · métodos (literatura) · adr/
examples/              sesión de GP comentada
```

Ejecutar las pruebas: `bash tests/watchman.test.sh` · medir el hook: `python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir>`

## Documentación

- [Conceptos](docs/concepts.md): skills, el rumbo, veredictos, quién decide
- [Métodos](docs/methods.md): la investigación detrás de cada decisión de diseño
- [ADR 0001](docs/adr/0001-hook-for-per-prompt-watch.md) · [ADR 0002](docs/adr/0002-committed-logbook.md) · [ADR 0003](docs/adr/0003-evidence-grounded-bearing.md)
- [Benchmark: mejor vs peor caso](docs/benchmarks/2026-11-25-best-vs-worst.md): lo que la v1.0.0 no detectó, lo que corrigió la v1.1.0, tiempo del hook por prompt
- [Changelog](CHANGELOG.md)

*(La documentación detallada está en inglés.)*

## Contribuir

Las contribuciones son bienvenidas, sobre todo **nuevas lentes** para otros campos, traducciones
revisadas por hablantes nativos y nuevos casos de evaluación. Lee [CONTRIBUTING.md](CONTRIBUTING.md)
antes de abrir un pull request.

## Seguridad

**No reportes vulnerabilidades en issues públicas.** Usa el
[reporte privado de vulnerabilidades](https://github.com/Icharu/travelerswatch/security/advisories/new)
de GitHub (pestaña **Security**, luego **Report a vulnerability**). Los tiempos de respuesta son de
mejor esfuerzo y dependen de la severidad. Consulta [SECURITY.md](SECURITY.md) para el alcance, la
tabla de respuestas y qué hacer mientras esperas.

## Cita

Si usas The Traveler's Watch en investigación o docencia, por favor cítalo. El botón
**"Cite this repository"** de GitHub lee [CITATION.cff](CITATION.cff). DOIs de Zenodo: todas las versiones [10.5281/zenodo.24543183](https://doi.org/10.5281/zenodo.24543183) (cita este, salvo que
necesites una versión concreta) · v1.1.0 [10.5281/zenodo.24543326](https://doi.org/10.5281/zenodo.24543326) · v1.0.0 [10.5281/zenodo.24543184](https://doi.org/10.5281/zenodo.24543184).

## Licencia

© 2026 Icaro de Jesus Silva. El **código** (`hooks/`, `tests/` y todos los archivos `.sh`, `.py`, `.json`, `.yml`, `.cff`) está bajo la licencia [MIT](LICENSE). La **documentación y el texto de las skills** (todos los archivos Markdown, incluidos `skills/**/*.md`, `docs/`, `examples/` y los READMEs) están bajo la licencia [CC BY 4.0](LICENSE-docs): reutiliza y adapta libremente, con atribución. La versión v1.0.0 sigue íntegramente bajo MIT. El cuento en [docs/tale.md](docs/tale.md) es una
reescritura original; la cita de Isaías 21:11 es de dominio público.

## Lecturas recomendadas

- Laban et al. (2025), [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120)
- Dongre et al. (2025), [*Drift No More? Context Equilibria in Multi-Turn LLM Interactions*](https://arxiv.org/abs/2510.07777)
- Liu et al. (2024), [*Lost in the Middle: How Language Models Use Long Contexts*](https://doi.org/10.1162/tacl_a_00638)
- Komal et al. (2020), [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098)
- Anthropic (2025), [*Equipping agents for the real world with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- Lista comentada completa: [docs/methods.md](docs/methods.md)
