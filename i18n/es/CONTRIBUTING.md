<!-- lang-bar -->
[English](../../CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · **Español** · [繁體中文](../zh-Hant/CONTRIBUTING.md) · [简体中文](../zh-Hans/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

> Traducido de `CONTRIBUTING.md` (v1.2.2, 2026-11-26). Traducción asistida por máquina; la versión en inglés es la canónica.

# Contribuir a The Traveler's Watch

Gracias por ayudar a mantener a los viajeros en su camino. Las contribuciones de cualquier tamaño son bienvenidas.

## Qué llevó a este proyecto

TTW anima a usuarios y contribuidores a entender qué lo originó antes de modificarlo. El diseño se
apoya en unos **cinco años de investigación (2021–2026)** sobre cómo se desvían los modelos de
lenguaje en trabajos largos y sobre cómo la IA está cambiando la gestión de proyectos, además de un
estudio anterior sobre la ampliación descontrolada del alcance (*scope creep*).

La investigación sobre el funcionamiento y el uso de la IA en el mundo moderno es de naturaleza
**interdisciplinaria** (Koshman & Zubkova, 2026), así que son bienvenidas contribuciones de cualquier
campo. Dos revisiones sitúan a TTW dentro de esa investigación:

- **Lo que la IA ya hace bien en la gestión de proyectos.** Adamantiadou y Tsironis (2025) concluyeron
  que el aprendizaje automático, el aprendizaje profundo y los modelos híbridos han ampliado
  significativamente lo que la gestión de proyectos puede hacer, mejorando la **estimación de costes,
  la previsión de plazos y el análisis de riesgos**. TTW se lo toma en serio: automatiza el trabajo
  repetitivo dentro del rumbo.
  *Nota de transparencia: citamos este hallazgo tal como lo recogen Koshman & Zubkova (2026); hemos
  comprobado los datos del artículo original a través de su DOI.*
- **Lo que sigue sin resolverse.** Koshman y Zubkova (2026) revisaron 97 publicaciones y concluyeron
  que los modelos de IA se adaptan mal a condiciones cambiantes del proyecto, rara vez se validan con
  los datos iniciales y se han estudiado poco en fases como la revisión posproyecto. TTW se construyó
  en torno a esas lagunas: el jefe de proyecto mantiene la dirección, el rumbo se contrasta con la
  evidencia y la bitácora permite una revisión posproyecto.

| Año | Referencia | Por qué importa aquí |
|---|---|---|
| 2020 | Komal et al., [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098) | Los cambios no autorizados perjudican los proyectos → cada cambio de rumbo se confirma y se registra |
| 2024 | Liu et al., [*Lost in the Middle*](https://doi.org/10.1162/tacl_a_00638) | Los modelos aprovechan mejor los extremos de un contexto largo → un rumbo breve junto a cada prompt |
| 2024 | [*A Survey on LLM-as-a-Judge*](https://arxiv.org/abs/2411.15594) | Los LLM jueces necesitan criterios explícitos → el Estándar se fija antes de cualquier veredicto |
| 2025 | Laban et al., [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120) | Los modelos toman giros equivocados y no se recuperan → el rumbo se fija al principio |
| 2025 | Dongre et al., [*Drift No More?*](https://arxiv.org/abs/2510.07777) | Los recordatorios reducen la deriva → el vigía en cada prompt |
| 2025 | Adamantiadou & Tsironis, [*Leveraging AI in Project Management*](https://doi.org/10.3390/computers14020066) | La IA mejora estimaciones, previsiones y análisis de riesgos → automatizar el trabajo repetitivo |
| 2026 | Koshman & Zubkova, [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23) | Adaptabilidad, validación y revisión posproyecto siguen sin resolverse → humano en el circuito |

La lista comentada completa, con la consecuencia de diseño de cada fuente, está en
[docs/methods.md](../../docs/methods.md) (en inglés). Cómo empezó el proyecto y quién decide está en
[GOVERNANCE.md](../../GOVERNANCE.md).

<details>
<summary><b>Referencias completas</b></summary>

- Adamantiadou, D. S., & Tsironis, L. (2025). Leveraging artificial intelligence in project
  management: A systematic review of applications, challenges, and future directions. *Computers*,
  14(2), 66. https://doi.org/10.3390/computers14020066
- Koshman, Y., & Zubkova, A. (2026). Artificial intelligence in project management. *Development
  Management*, 25(1), 23–31. https://doi.org/10.63341/devt/1.2026.23
- Otras fuentes: [docs/methods.md](../../docs/methods.md).

</details>

## Formas de contribuir

| Contribución | Dónde |
|---|---|
| Una **lente** para un nuevo campo (p. ej., eventos, construcción, programas sin ánimo de lucro, diseño de producto) | `skills/checkwatch/references/lenses/` |
| Una **revisión de traducción** por un hablante nativo | `i18n/<lang>/` (README, QUICKSTART, CONTRIBUTING, tale) |
| Un nuevo **caso de evaluación** (un prompt y el comportamiento esperado) | `skills/<skill>/evals/evals.json` |
| Un **informe de error** o una idea | [Issues](https://github.com/Icharu/travelerswatch/issues). Usa las plantillas. |
| Un **problema de seguridad** | **No** en issues. Consulta [SECURITY.md](../../SECURITY.md). |

## Añadir una lente

1. Copia una lente existente (p. ej., `project-management.md`) a `lenses/<campo>.md`.
2. Mantén los mismos cuatro encabezados para que la skill pueda usar cualquier lente de la misma forma:
   - **How the sections read in this field**: una tabla que reformula Contexto, Restricciones, Problema, Herramientas
   - **Default criteria**: de 4 a 8 criterios *observables* (consulta `references/standards.md`)
   - **Drift signals**: cómo se ve salirse del camino en este campo
   - **Typical tools**
3. Escribe los criterios **con tus propias palabras**. No pegues texto de normas de pago o protegidas
   por derechos de autor; nómbralas y haz referencia solo a sus secciones.
4. Añade la lente a la lista de `skills/checkwatch/SKILL.md` (paso A1) y a la sección *Lenses* del README.
5. Añade al menos un caso de evaluación en `skills/checkwatch/evals/evals.json` que use la lente.

## Cambiar las skills

- Mantén cada `SKILL.md` breve y orientado a decisiones; pon el detalle en `references/`.
- No debilites las reglas centrales ([GOVERNANCE.md](../../GOVERNANCE.md#how-decisions-are-made)):
  **solo el jefe de proyecto confirma** un cambio de rumbo, un cierre o una contradicción aceptada;
  **el Path log y el Registro de puntos de control solo admiten añadidos**; **ninguna sesión totalmente
  automatizada** para el rumbo ([ADR 0004](../../docs/adr/0004-human-in-the-loop.md)); **ningún dato
  guardado** fuera del repositorio del usuario.
- Usa solo el frontmatter estándar de Agent Skills (`name`, `description`, `license`, `metadata`) para
  que las skills sigan siendo portables.
- Explica los cambios de comportamiento en un ADR en `docs/adr/` cuando cambien una decisión de diseño.

## Cambiar el hook

- Solo bash (≥ 3.2, por macOS) y awk; git es opcional. Prefiere los built-ins de bash a procesos
  adicionales; la bitácora se analiza en una sola pasada de `awk`.
- Siempre debe salir con 0, quedarse en silencio sin bitácora o con el rumbo `closed`, limitar la
  salida, no hacer llamadas de red y no escribir nada salvo `.watch/.state`.
- **Escribe primero la prueba que falla** en `tests/watchman.test.sh`, luego haz que pase, y mide el
  tiempo por prompt antes y después:

  ```bash
  bash tests/watchman.test.sh
  python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir> [...]
  ```

## Cambiar el formato de la bitácora

El hook analiza etiquetas exactas: `## Status`, `- **Bearing:**` (`confirmed` / `under review …` /
`closed …`), `- **Checkpoint cadence:**` (`every N commits or M sessions` / `off`),
`- **Last checkpoint:** <date> @ <sha>`, `**Boundary notes:**`, las líneas de Relations que contienen
"accepted" y el encabezado `## Path log`. `## Checkpoint log` solo lo leen las skills. Cámbialas solo
junto con el hook, la plantilla (`skills/checkwatch/assets/WATCH.md`), las skills y las pruebas.

## Traducciones

Los archivos en inglés de la raíz (`README.md`, `QUICKSTART.md`, `CONTRIBUTING.md`) son los canónicos.
Las traducciones se agrupan por idioma en `i18n/<lang>/`, para que la raíz no se sature. Cuando cambies
un archivo en inglés, indica en el pull request qué traducciones han quedado desactualizadas.
Traductores: mantened idénticos la barra de idiomas, los enlaces (relativos a `i18n/<lang>/`, p. ej.,
`../../docs/methods.md`), las insignias, los comandos y los bloques de código de shell (el diálogo del
*Ejemplo rápido* puede traducirse). Actualizad la nota `Traducido de` al principio del archivo. Árabe:
mantened el texto dentro de `<div dir="rtl">` y los bloques de código fuera.

## Pull requests

1. Haz un fork y crea una rama: `feat/<algo>`, `fix/<algo>`, `docs/<algo>` o `lens/<campo>`.
2. Mantén cada pull request centrado en un solo cambio.
3. Ejecuta `bash tests/watchman.test.sh` y `claude plugin validate .` si tienes Claude Code.
4. Añade una entrada en **Unreleased** en [CHANGELOG.md](../../CHANGELOG.md).
5. Usa mensajes de [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`).

Al contribuir, aceptas que tus contribuciones se licencian en los mismos términos que el resto del
repositorio: [CC BY-NC 4.0](../../LICENSE).
