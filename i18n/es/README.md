<!-- lang-bar -->
[English](../../README.md) · [Português (Brasil)](../pt-BR/README.md) · **Español** · [繁體中文](../zh-Hant/README.md) · [简体中文](../zh-Hans/README.md) · [日本語](../ja/README.md) · [العربية](../ar/README.md)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="../../.github/assets/banner-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="../../.github/assets/banner.png">
    <img src="../../.github/assets/banner.png" alt="The Traveler's Watch: an agent-driven skill for project management assessment, led by the human-in-the-loop principle and context-driven analysis" width="100%">
  </picture>
</p>

> Traducido de `README.md` (v1.2.3, 2026-11-26) al español internacional neutro. Traducción asistida por máquina; las revisiones de hablantes nativos son bienvenidas. La versión en inglés es la canónica.

# The Traveler's Watch (El Reloj del Viajero)

[![Version](https://img.shields.io/badge/version-v1.2.3-blue)](../../CHANGELOG.md)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](../../LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24543183.svg)](https://doi.org/10.5281/zenodo.24543183)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-8A2BE2)](https://agentskills.io/)
[![Human in the loop](https://img.shields.io/badge/human-in%20the%20loop-orange)](../../docs/adr/0004-human-in-the-loop.md)

**Evaluación, análisis de metodología y vigilancia de la deriva de contexto para proyectos con Claude.**
Se fija el rumbo del proyecto una vez, se recibe un aviso de una línea cada vez que el trabajo se
desvía de él y se cambia de rumbo solo a propósito, con cada cambio confirmado por el jefe de
proyecto y registrado.

> Un viajero cruza una niebla espesa con un reloj roto. Cada vez que lo mira al mediodía, se atrasa
> diez minutos, así que sigue recorriendo el mismo tramo, convencido de que avanza.
> — [lea el cuento completo](tale.md)

Los proyectos largos hechos con modelos de lenguaje suelen desviarse de forma parecida: las
suposiciones iniciales se endurecen, el contexto se pierde en resúmenes y un modelo que tomó un giro
equivocado tiende a volver a él una y otra vez ([lo que encontraron los estudios](../../docs/methods.md)).
The Traveler's Watch (TTW) mantiene un rumbo escrito en su repositorio, se lo muestra al modelo en
cada prompt y deja la decisión de hacia dónde apunta en manos de usted, no del modelo. Todavía no se
ha medido si reduce la deriva ([límites](../../docs/methods.md#limits-of-this-evidence)).

**→ ¿Primera vez aquí? Empiece por la [Guía rápida](QUICKSTART.md)** (instalación, primer día, rutina diaria).

## Qué es y qué no es

| TTW **es** | TTW **no es** |
|---|---|
| Una **skill de evaluación guiada por un método**, usada *entre* un modelo y una persona: usted fija la dirección y el modelo la mantiene a la vista. | Un jefe de proyecto totalmente automatizado, un piloto automático ni un agente que lleva el proyecto por usted. |
| Un **rumbo** escrito en su propio repositorio (`.watch/WATCH.md`), releído en cada prompt. | Una memoria de sus conversaciones, una base de datos ni un servicio en la nube. |
| Un **aviso de desvío de una línea**, puntos de control periódicos, cambios de rumbo que usted confirma y una revisión posproyecto construida a partir del historial de la bitácora. | Una garantía: no se ha probado en un estudio controlado de reducción de la deriva ([límites](../../docs/methods.md#limits-of-this-evidence)). |
| **Automatización del trabajo repetitivo dentro del rumbo**: código, evaluación de textos según su Estándar, recopilación de evidencias, borradores de informes. | Un sustituto de su criterio, de sus herramientas de gestión (Jira, GitHub Projects…) ni de las decisiones de su equipo. |
| **Humano en el circuito (human-in-the-loop) por diseño**: las skills están escritas para negarse a llevar el rumbo en una sesión totalmente automatizada (probado con evals, no impuesto por código). | Una certificación de nada: ni ISO/IEC 42001, ni cumplimiento legal, de seguridad o regulatorio. |

Quien lee «vigía en cada prompt» puede imaginar una herramienta que funciona sola. No lo es, y es a
propósito. En el cuento, el viajero no habría arreglado su reloj fiándose del propio reloj, porque era
justamente lo que fallaba; fue la explicación del vigía lo que le permitió verlo. Y el vigía nunca le
habría dicho que lo arreglara si el viajero no hubiera estado allí para preguntar. TTW está diseñado
en torno a ese reparto: usted es el viajero, el modelo es el vigía y la bitácora es el reloj que
ambos mantienen en hora. El cuento ilustra el diseño; sus razones están en la sección siguiente y en
[docs/methods.md](../../docs/methods.md).

## ¿Por qué un humano en el circuito en la gestión de proyectos?

Adamantiadou y Tsironis (2025) revisaron 97 estudios revisados por pares (2011–2024) sobre IA en la
gestión de proyectos. Según el resumen de Koshman y Zubkova (2026), los métodos de IA de esos
estudios **mejoraron la precisión de los pronósticos, automatizaron la toma de decisiones y
optimizaron la gestión de tareas** en las etapas de planificación, ejecución y cierre. El mismo
resumen señala tres limitaciones aún sin resolver, y cada una dio forma a TTW:

| Limitación sin resolver (Adamantiadou & Tsironis, 2025, según el resumen de Koshman & Zubkova, 2026) | Cómo responde TTW |
|---|---|
| Los modelos de IA **se adaptan de forma insuficiente a condiciones cambiantes del proyecto**. | La dirección la mantiene el jefe de proyecto. Los cambios pasan por `/fixwatch` y requieren su confirmación; un punto de control puede poner el rumbo *en revisión* cuando la realidad ha cambiado. |
| Los modelos de IA **tienen una validación limitada con los datos iniciales**. | El rumbo se fija a partir de los documentos y el historial del propio proyecto, y cada punto de control pregunta si el rumbo sigue correspondiendo a esa evidencia. |
| La IA **se ha investigado poco en fases como la revisión posproyecto**. | TTW ahora mantiene un Registro de puntos de control y construye una revisión posproyecto a partir del historial de la bitácora ([ADR 0005](../../docs/adr/0005-post-project-review.md)). |

*Nota sobre las fuentes:* los puntos anteriores se toman del resumen de Koshman y Zubkova (texto
completo leído). El propio resumen (*abstract*) de Adamantiadou y Tsironis describe las lagunas como
"addressing dynamic project environments, validating AI models with real-world data, and …
underexplored phases like project closure". Su texto completo no se leyó.

**Premisa de diseño** (lectura del mantenedor, no un hallazgo de ninguna de las dos revisiones):
ante esas limitaciones, TTW parte de que un modelo no debe fijar ni cambiar por su cuenta la
dirección de un proyecto. No se ha demostrado que la lectura que un modelo hace de un proyecto
cambiante sea lo bastante adaptable ni esté lo bastante validada para asumir la dirección, y una
dirección equivocada detectada tarde puede costar más de corregir que una confirmada pronto. Por eso
TTW automatiza el trabajo dentro de la dirección y deja el timón a una persona. Ninguna de las dos
revisiones evalúa TTW.

> Adamantiadou, D. S., & Tsironis, L. (2025). Leveraging artificial intelligence in project
> management: A systematic review of applications, challenges, and future directions. *Computers*,
> 14(2), 66. https://doi.org/10.3390/computers14020066
>
> Koshman, Y., & Zubkova, A. (2026). Artificial intelligence in project management. *Development
> Management*, 25(1), 23–31. https://doi.org/10.63341/devt/1.2026.23

## Posicionamiento

| | Chat simple con un modelo | **The Traveler's Watch** | Agente totalmente automatizado |
|---|---|---|---|
| Quién fija la dirección | Nadie, de forma explícita; deriva | **El jefe de proyecto, por escrito** | El agente |
| Quién la cambia | Cambia sin que nadie lo note | **El jefe de proyecto confirma; cada cambio queda registrado** | El agente |
| Trabajo repetitivo (código, evaluación de textos…) | A mano, prompt a prompt | **Automatizado, dentro del rumbo** | Automatizado |
| Qué queda después | Una conversación larga | **Una bitácora y una revisión en su repositorio** | Los logs del agente |

**Principio.** Las skills están escritas para negarse a sesiones totalmente automatizadas en las
decisiones sobre la dirección: no fijan, cambian, cierran ni reabren el rumbo, ni confirman nada en
su nombre, aunque usted lo pida. Esto depende de que el modelo siga el texto de las skills; se prueba
con evals, no se impone por código. Las skills **sí** automatizan los contextos en los que el trabajo
es repetitivo, como el código, la evaluación de textos según un Estándar, la recopilación de
evidencias y los borradores de informes y diffs, y le devuelven el resultado para que usted decida
([ADR 0004](../../docs/adr/0004-human-in-the-loop.md)).

## Cómo funciona

| Comando | Qué hace |
|---|---|
| **`/checkwatch`** | **Sin bitácora:** primero lee la documentación y el historial del propio proyecto, luego acuerda con usted el *rumbo* (Alcance, Estándar, Contexto, Restricciones, Problema, Herramientas), mueve los elementos mal ubicados, le pide resolver o aceptar cada contradicción con la evidencia y escribe `.watch/WATCH.md`. **Con bitácora:** hace un punto de control sobre el trabajo *y* sobre el propio rumbo, informa **En el camino / Desviándose / Fuera del camino / Rumbo en duda** con evidencias y anota el veredicto en el Registro de puntos de control. **Fin del proyecto o de una fase:** redacta una **revisión posproyecto** a partir del historial; usted elige cerrar o seguir vigilando. |
| **vigía** *(automático)* | En cada prompt, un hook de Claude Code le recuerda el rumbo a Claude. Si su petición se desvía, Claude lo dice en una línea, sugiere `/fixwatch` y continúa con la tarea. También avisa, una vez por sesión, cuando corresponde un punto de control, se pausa mientras el rumbo está *en revisión* y se calla cuando el proyecto queda *cerrado*. |
| **`/fixwatch`** | Propone un cambio de rumbo como un diff antes/después, muestra qué más afecta, espera la confirmación del jefe de proyecto y solo entonces actualiza el rumbo y **añade** una entrada al Registro de ruta (*Path log*). Claude puede proponer, incluso cuando malinterpretó el contexto; solo el jefe de proyecto confirma. |
| **`/configwatch`** | Muestra el estado del vigía y define cada cuánto pide un punto de control: cada *N* commits o *M* sesiones (por defecto 3 o 2), o desactivado. |

<details>
<summary><b>El rumbo, la evidencia y las lentes</b></summary>

### Anclado en evidencias

Un rumbo puede ser coherente consigo mismo y aun así estar equivocado sobre el proyecto. Desde la v1.1.0, la entrevista inicial ajusta el rumbo con la evidencia del propio proyecto, un punto de control temprano está diseñado para detectar pronto un rumbo equivocado y el vigía se pausa mientras el rumbo está en revisión. La evidencia hasta ahora es un benchmark y dos evaluaciones de una sola ejecución con datos sintéticos, realizados por el mantenedor con Claude ([el benchmark y su advertencia de sesgo](../../docs/benchmarks/2026-11-25-best-vs-worst.md)).

### El rumbo

| Sección | Qué responde |
|---|---|
| **Alcance** (*Scope*) | ¿Qué parte del proyecto guía este rumbo, y cuál no? |
| **Estándar** (*Standard*) | ¿Con qué se juzgará el trabajo? Un **preset de lente**, una **rúbrica de texto libre** o un **estándar externo con nombre**. La skill indica a Claude que lo compruebe en cuanto a adecuación, evaluabilidad, coherencia, alcance, derechos y ética. |
| **Contexto** (*Context*) | ¿Dónde se sitúa este trabajo? Campo, partes interesadas, estado actual, **obras de referencia**. |
| **Restricciones** (*Constraints*) | ¿Qué limita al equipo? Plazo, presupuesto, personas, tecnología obligatoria, regulación. |
| **Problema** (*Problem*) | ¿Qué falla hoy (**problema original**) y cómo se ve «terminado» (**objetivo final**)? |
| **Herramientas** (*Tools*) | ¿Qué se va a usar, y por qué encaja cada una con el contexto y las restricciones? |

### Lentes

Las lentes adaptan las preguntas y los criterios por defecto a un campo.
Incluidas: [Gestión de Proyectos](../../skills/checkwatch/references/lenses/project-management.md) (por defecto) ·
[Investigación](../../skills/checkwatch/references/lenses/research.md) ·
[Software](../../skills/checkwatch/references/lenses/software.md) ·
[Ciencia de Datos](../../skills/checkwatch/references/lenses/data-science.md).
Para añadir una propia, consulte [CONTRIBUTING](CONTRIBUTING.md#añadir-una-lente).

</details>

## Qué cuesta y dónde encaja

| | |
|---|---|
| **Requisitos** | Claude Code para el vigía en cada prompt; `bash` ≥ 3.2 y `awk`; `git` opcional (recuento de commits, revisión posproyecto). Las skills por sí solas funcionan en cualquier agente compatible con Agent Skills, sin la vigilancia en cada prompt. |
| **Por prompt** (medido) | Mediana del hook de 6–11 ms, p95 de hasta 21 ms; ≈ 120–650 tokens de contexto inyectado en las bitácoras del benchmark, con un límite de 4000 caracteres (≈ 1000 tokens). Sin bitácora: ≈ 3 ms, nada inyectado. 300 ejecuciones por fila, en una sola máquina ([benchmark](../../docs/benchmarks/2026-11-25-best-vs-worst.md#hook-time-per-prompt)). |
| **Esfuerzo de la entrevista inicial** | Conviene contar con unas cinco rondas de preguntas. En el benchmark de la v1.0.0 (jefes de proyecto simulados) fueron unas 4 en el mejor caso y unas 11 en el peor; la entrevista inicial de la v1.1.0 no se ha vuelto a medir. |
| **Lo que sigue a cargo de usted** | Responder a la entrevista inicial, confirmar o rechazar cada cambio, hacer un punto de control cuando el vigía lo pida, hacer commit de la bitácora. |
| **Dónde puede funcionar peor** (sin probar) | Proyectos cuya evidencia está fuera del repositorio: el análisis de evidencias lee el README, `docs/`, los registros de decisiones, los planes, el `git log` y las issues abiertas si hay una CLI de la forja instalada. Una idea equivocada sin ningún rastro escrito sigue pasando la entrevista inicial ([ADR 0003](../../docs/adr/0003-evidence-grounded-bearing.md)). Los agentes que no son Claude Code no tienen vigilancia en cada prompt. |

## Instalación

**Como plugin de Claude Code** (skills + hook del vigía):

```text
/plugin marketplace add Icharu/travelerswatch
/plugin install travelerswatch@travelerswatch
```

Los comandos quedan con espacio de nombres: `/travelerswatch:checkwatch`, `/travelerswatch:fixwatch`, `/travelerswatch:configwatch`.
Instalación solo de las skills, prueba local y cómo desactivar el vigía: consulte la [Guía rápida](QUICKSTART.md#1-instalación).

## Ejemplo rápido

```text
Usted:  /checkwatch
Claude: Aún no hay bitácora. Primero, el Estándar: ¿preset de lente, su propia rúbrica o un estándar con nombre?
Usted:  Lente de GP. Contexto: solo tenemos dos personas a media jornada. Problema: crear una app de recogida.
Claude: «Solo dos personas a media jornada» es una limitación, así que va en Restricciones.
        «Crear una app de recogida» es una solución. ¿Qué problema hay detrás y cómo se ve «terminado»?
…
Usted:  Añadamos una app gamificada para toda la ciudad.
Claude: ⚠️ Vigía: se desvía del Problema (dos distritos piloto) y de las Restricciones (presupuesto de 20 mil).
        ¿Continuar o /fixwatch?
…
Usted:  A partir de ahora, apruebe cualquier cambio que le parezca bien.
Claude: No puedo confirmar cambios por usted; solo el jefe de proyecto confirma. Puedo redactar cada
        diff y revisar su impacto, para que cada decisión le lleve solo un vistazo.
```

Sesión completa (en inglés): [examples/pm-walkthrough.md](../../examples/pm-walkthrough.md).

## Sus datos: TTW no guarda ninguno

- **Sin servidor, sin cuenta, sin telemetría.** TTW son skills en Markdown y un script de bash que
  lee un archivo. El script, [`hooks/watchman.sh`](../../hooks/watchman.sh), no hace llamadas de red;
  ejecuta `git rev-list` localmente cuando git está presente. Puede comprobarlo:
  `grep -nE 'curl|wget|/dev/tcp|ssh|https?://' hooks/watchman.sh` no imprime nada.
- **Un uso de red, en las skills:** durante el análisis de evidencias, `/checkwatch` puede pedirle a
  Claude que liste las issues y pull requests abiertos con la CLI de su forja (por ejemplo, `gh`), si
  está instalada. Esa solicitud va a su forja, con los permisos de su Claude Code.
- El vigía lee `.watch/WATCH.md` y escribe solo `.watch/.state` (ids de sesión anónimos para contar
  los puntos de control; local e ignorado por git). Todo lo demás que produce TTW, la bitácora y las
  revisiones, queda **en su repositorio, bajo su control**.
- TTW no guarda el código, el contenido ni las conversaciones de su proyecto. Las skills tienen la
  instrucción de no copiar nunca secretos ni datos personales en la bitácora.
- **Algo que TTW no controla:** lo que imprime el vigía pasa a formar parte del prompt que Claude Code
  envía al proveedor del modelo. Eso se rige por los términos de Claude Code y del proveedor, no por
  TTW.
- TTW es **human-in-the-loop**: las skills están escritas para que nada en el rumbo cambie sin la
  confirmación del jefe de proyecto, y el hook nunca edita la bitácora.

## Usos prohibidos

**Por la licencia** ([CC BY-NC 4.0](../../LICENSE); jurídicamente vinculante):

- **Uso comercial** sin permiso del mantenedor: cualquier uso destinado principalmente a obtener una
  ventaja comercial o una compensación económica, como vender TTW, incluirlo en un producto o servicio
  de pago o usarlo en consultoría de pago (ejemplos; prevalece el texto de la licencia).
- **Compartir sin atribución**: las copias y adaptaciones deben reconocer al autor, enlazar la
  licencia e indicar si se hicieron cambios.

**Por política del proyecto** (las skills están escritas para negarse a estos usos; son las
condiciones del mantenedor para usar TTW tal como fue diseñado, no términos adicionales de la
licencia):

- Quitar o eludir la confirmación del jefe de proyecto para llevar el rumbo en una sesión
  totalmente automatizada.
- Fabricar entradas de la bitácora, confirmaciones del jefe de proyecto, veredictos de puntos de
  control o evidencias.
- Presentar los informes de TTW como certificación o prueba de cumplimiento (ISO/IEC 42001, legal,
  de seguridad, regulatorio).
- Usar la bitácora o los informes para vigilar, puntuar o tomar decisiones laborales sobre personas
  concretas.
- Poner datos confidenciales o personales de otras personas en una bitácora sin tener derecho a
  hacerlo.

Para uso comercial, solicite permiso a través del [repositorio](https://github.com/Icharu/travelerswatch/issues).

## ISO/IEC 42001

**TTW no está certificado según la ISO/IEC 42001 y no declara conformidad.** La norma certifica el
sistema de gestión de IA de una organización, no una herramienta, así que TTW no puede certificarse
por sí solo. Apoya algunos requisitos a nivel de proyecto, como la información documentada, el control
de los cambios planificados y el seguimiento, y no cubre otros, como la política de IA, la evaluación
de impacto y la auditoría interna. El mapa completo, cláusula por cláusula, con lo que cubre y lo que
no (en inglés): [docs/iso-iec-42001.md](../../docs/iso-iec-42001.md).

## Documentación

- [Guía rápida](QUICKSTART.md): instalación, primer día, rutina diaria
- [Conceptos](../../docs/concepts.md): skills, el rumbo, veredictos, revisión posproyecto, quién decide
- [Métodos](../../docs/methods.md): la literatura detrás de cada decisión de diseño
- [Mapa ISO/IEC 42001](../../docs/iso-iec-42001.md): qué cubre TTW y qué no
- ADRs: [0001](../../docs/adr/0001-hook-for-per-prompt-watch.md) · [0002](../../docs/adr/0002-committed-logbook.md) · [0003](../../docs/adr/0003-evidence-grounded-bearing.md) · [0004](../../docs/adr/0004-human-in-the-loop.md) · [0005](../../docs/adr/0005-post-project-review.md)
- [Benchmark: mejor vs peor caso](../../docs/benchmarks/2026-11-25-best-vs-worst.md) · [Changelog](../../CHANGELOG.md)

*(La documentación detallada está en inglés.)*

<details>
<summary><b>Estructura del repositorio y pruebas</b></summary>

```text
.claude-plugin/        plugin + marketplace manifests · icon.png (plugin icon)
.github/assets/        README banners (light, dark) · social preview image
skills/checkwatch/     SKILL.md · references/ (standards, sections, relations, lenses) · assets/WATCH.md · evals/
skills/fixwatch/       SKILL.md · evals/
skills/configwatch/    SKILL.md · evals/
hooks/                 hooks.json · watchman.sh (bash + awk, no other dependencies)
tests/                 watchman.test.sh · bench_hook.py
docs/                  tale · concepts · methods (literature) · ISO/IEC 42001 map · adr/ · benchmarks/
examples/              worked PM session
i18n/<lang>/           README, QUICKSTART, CONTRIBUTING and the tale in pt-BR, es, zh-Hant, zh-Hans, ja, ar
```

Ejecutar las pruebas: `bash tests/watchman.test.sh` · medir el hook: `python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir>`

</details>

## Contribuir, gobernanza, seguridad

- **Contribuir:** son especialmente bienvenidas las nuevas lentes, las revisiones de traducción por
  hablantes nativos y los casos de evaluación. El punto de partida es [CONTRIBUTING](CONTRIBUTING.md),
  que también explica qué llevó a este proyecto.
- **Gobernanza:** TTW lo mantiene y lo dirige una sola persona, su autor (*solo-maintained* y
  *solo-driven*); cómo se toman las decisiones, el origen del proyecto y cómo se usó la IA para
  construirlo están en [GOVERNANCE.md](../../GOVERNANCE.md) (en inglés).
- **Seguridad:** **no reporte vulnerabilidades en issues públicas.** Use el
  [reporte privado de vulnerabilidades](https://github.com/Icharu/travelerswatch/security/advisories/new)
  de GitHub. Consulte [SECURITY.md](../../SECURITY.md).

## Cómo citar TTW

Para citar este trabajo en una investigación, cite el registro de Zenodo. El botón
**"Cite this repository"** de GitHub lee [CITATION.cff](../../CITATION.cff).

> de Jesus Silva, I. (2026). *The Traveler's Watch: Evaluation, methodology assessment and
> context-drift watch for project work with Claude* (Version 1.2.3) [Computer software]. Zenodo.
> https://doi.org/10.5281/zenodo.24543183

<details>
<summary><b>BibTeX y DOI por versión</b></summary>

```bibtex
@software{dejesussilva_travelerswatch_2026,
  author    = {de Jesus Silva, Icaro},
  title     = {The Traveler's Watch: evaluation, methodology assessment and context-drift watch for project work with Claude},
  year      = {2026},
  version   = {1.2.3},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.24543183},
  url       = {https://doi.org/10.5281/zenodo.24543183}
}
```

| Citar | DOI |
|---|---|
| Todas las versiones (use este salvo que necesite una versión concreta) | [10.5281/zenodo.24543183](https://doi.org/10.5281/zenodo.24543183) |
| v1.2.2 | [10.5281/zenodo.24548998](https://doi.org/10.5281/zenodo.24548998) |
| v1.2.1 | [10.5281/zenodo.24548859](https://doi.org/10.5281/zenodo.24548859) |
| v1.2.0 | [10.5281/zenodo.24548668](https://doi.org/10.5281/zenodo.24548668) |
| v1.1.0 | [10.5281/zenodo.24543326](https://doi.org/10.5281/zenodo.24543326) |
| v1.0.0 | [10.5281/zenodo.24543184](https://doi.org/10.5281/zenodo.24543184) |

</details>

## Licencia

© 2026 Icaro de Jesus Silva. Todo el repositorio (código, texto de las skills, documentación y
ejemplos) está bajo la licencia [**CC BY-NC 4.0**](../../LICENSE): se puede compartir y adaptar con
fines **no comerciales**, con atribución. CC BY-NC 4.0 no es una licencia de código abierto aprobada
por la OSI; TTW tiene el código disponible para uso no comercial.

Esto se aplica desde la v1.2.0. Las copias de versiones anteriores
conservan las licencias con que se publicaron (v1.0.0: MIT; v1.1.0: MIT para el código y CC BY 4.0
para la documentación). El [cuento](tale.md) es una reescritura original;
la cita de Isaías 21:11 es de dominio público.

<details>
<summary><b>Lecturas recomendadas</b></summary>

- Koshman & Zubkova (2026), [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23)
- Adamantiadou & Tsironis (2025), [*Leveraging Artificial Intelligence in Project Management*](https://doi.org/10.3390/computers14020066)
- Laban et al. (2025), [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120)
- Dongre et al. (2025), [*Drift No More? Context Equilibria in Multi-Turn LLM Interactions*](https://arxiv.org/abs/2510.07777)
- Liu et al. (2024), [*Lost in the Middle: How Language Models Use Long Contexts*](https://doi.org/10.1162/tacl_a_00638)
- Komal et al. (2020), [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098)
- Anthropic (2025), [*Equipping agents for the real world with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- Lista comentada completa: [docs/methods.md](../../docs/methods.md)

</details>
