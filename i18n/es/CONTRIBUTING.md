<!-- lang-bar -->
[English](../../CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · **Español** · [繁體中文](../zh-Hant/CONTRIBUTING.md) · [简体中文](../zh-Hans/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

> Traducido de `CONTRIBUTING.md` (v1.2.3, 2026-11-26) al español internacional neutro. Traducción asistida por máquina; la versión en inglés es la canónica.

# Contribuir a The Traveler's Watch

Gracias por ayudar a mantener a los viajeros en su camino. Las contribuciones de cualquier tamaño son bienvenidas.

## Qué llevó a este proyecto

TTW anima a usuarios y contribuidores a entender qué lo originó antes de modificarlo. El diseño se
basa en literatura publicada entre 2020 y 2026: estudios sobre cómo se desvían los modelos de
lenguaje en trabajos largos, revisiones sobre cómo la IA está cambiando la gestión de proyectos y un
estudio sobre la ampliación descontrolada del alcance (*scope creep*).

Koshman y Zubkova (2026) describen la investigación sobre el funcionamiento y el uso de la IA en el
mundo moderno como de naturaleza **interdisciplinaria**, así que son bienvenidas contribuciones de
cualquier campo. Dos revisiones sitúan a TTW dentro de esa investigación:

- **Lo que la IA ya hace bien en la gestión de proyectos.** Adamantiadou y Tsironis (2025) revisaron
  97 estudios revisados por pares (2011–2024). Según su resumen (*abstract*), el aprendizaje
  automático, el aprendizaje profundo y los modelos híbridos han mostrado potencial para mejorar la
  gestión de proyectos, sobre todo en la **estimación de costos, la previsión de duración y la
  evaluación de riesgos**. TTW lo toma en serio: automatiza el trabajo repetitivo dentro del rumbo.
- **Lo que sigue sin resolverse.** La misma revisión, según el resumen de Koshman y Zubkova (2026),
  señala que los modelos de IA se adaptan de forma insuficiente a condiciones cambiantes del
  proyecto, tienen una validación limitada con los datos iniciales y se han investigado poco en fases
  como la revisión posproyecto. TTW se construyó en torno a esas lagunas: el jefe de proyecto mantiene
  la dirección, el rumbo se contrasta con la evidencia y la bitácora permite una revisión posproyecto.

*Nota sobre las fuentes (qué se leyó):* Koshman & Zubkova (2026): texto completo. Adamantiadou &
Tsironis (2025): leído a través del resumen de Koshman & Zubkova y del resumen (*abstract*) y los
metadatos bibliográficos de su registro DOI; el texto completo no se leyó. Las versiones anteriores
de este archivo atribuían la revisión de 97 publicaciones a Koshman & Zubkova; fue un error de
atribución, corregido en la v1.2.3.

| Año | Referencia | Por qué importa aquí |
|---|---|---|
| 2020 | Komal et al., [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098) | Los cambios no autorizados perjudican los proyectos → cada cambio de rumbo se confirma y se registra |
| 2024 | Liu et al., [*Lost in the Middle*](https://doi.org/10.1162/tacl_a_00638) | Los modelos aprovechan mejor los extremos de un contexto largo → un rumbo breve junto a cada prompt |
| 2024 | [*A Survey on LLM-as-a-Judge*](https://arxiv.org/abs/2411.15594) | Los LLM jueces necesitan criterios explícitos → el Estándar se fija antes de cualquier veredicto |
| 2025 | Laban et al., [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120) | Los modelos toman giros equivocados y no se recuperan → el rumbo se fija al principio |
| 2025 | Dongre et al., [*Drift No More?*](https://arxiv.org/abs/2510.07777) | Los recordatorios reducen la deriva → el vigía en cada prompt |
| 2025 | Adamantiadou & Tsironis, [*Leveraging AI in Project Management*](https://doi.org/10.3390/computers14020066) | Revisión de 97 estudios: la IA muestra potencial en estimación, previsión y riesgos; adaptabilidad, validación y fases finales sin resolver → automatizar el trabajo repetitivo, mantener a un humano en el circuito |
| 2026 | Koshman & Zubkova, [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23) | Revisión de 21 publicaciones (2021–2025) y de herramientas de IA; resume la revisión de 97 estudios; enfoque interdisciplinario → humano en el circuito, contribuciones de cualquier campo |

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
| Una **lente** para un nuevo campo (p. ej., eventos, construcción, programas sin fines de lucro, diseño de producto) | `skills/checkwatch/references/lenses/` |
| Una **revisión de traducción** por un hablante nativo | `i18n/<lang>/` (README, QUICKSTART, CONTRIBUTING, tale) |
| Un nuevo **caso de evaluación** (un prompt y el comportamiento esperado) | `skills/<skill>/evals/evals.json` |
| Un **informe de error** o una idea | [Issues](https://github.com/Icharu/travelerswatch/issues). Use las plantillas. |
| Un **problema de seguridad** | **No** en issues. Consulte [SECURITY.md](../../SECURITY.md). |

## Añadir una lente

1. Copie una lente existente (p. ej., `project-management.md`) a `lenses/<campo>.md`.
2. Mantenga los mismos cuatro encabezados para que la skill pueda usar cualquier lente de la misma forma:
   - **How the sections read in this field**: una tabla que reformula Contexto, Restricciones, Problema, Herramientas
   - **Default criteria**: de 4 a 8 criterios *observables* (consulte `references/standards.md`)
   - **Drift signals**: cómo se ve salirse del camino en este campo
   - **Typical tools**
3. Escriba los criterios **con sus propias palabras**. No pegue texto de normas de pago o protegidas
   por derechos de autor; nómbrelas y haga referencia solo a sus secciones.
4. Añada la lente a la lista de `skills/checkwatch/SKILL.md` (paso A1) y a la sección *Lenses* del README.
5. Añada al menos un caso de evaluación en `skills/checkwatch/evals/evals.json` que use la lente.

## Cambiar las skills

- Mantenga cada `SKILL.md` breve y orientado a decisiones; ponga el detalle en `references/`.
- No debilite las reglas centrales ([GOVERNANCE.md](../../GOVERNANCE.md#how-decisions-are-made)):
  **solo el jefe de proyecto confirma** un cambio de rumbo, un cierre o una contradicción aceptada;
  **el Path log y el Registro de puntos de control solo admiten añadidos**; **ninguna sesión totalmente
  automatizada** para el rumbo ([ADR 0004](../../docs/adr/0004-human-in-the-loop.md)); **ningún dato
  guardado** fuera del repositorio del usuario.
- Use solo el frontmatter estándar de Agent Skills (`name`, `description`, `license`, `metadata`) para
  que las skills sigan siendo portables.
- Explique los cambios de comportamiento en un ADR en `docs/adr/` cuando cambien una decisión de diseño.

## Cambiar el hook

- Solo bash (≥ 3.2, por macOS) y awk; git es opcional. Prefiera los built-ins de bash a procesos
  adicionales; la bitácora se analiza en una sola pasada de `awk`.
- Siempre debe salir con 0, quedarse en silencio sin bitácora o con el rumbo `closed`, limitar la
  salida, no hacer llamadas de red y no escribir nada salvo `.watch/.state`.
- **Escriba primero la prueba que falla** en `tests/watchman.test.sh`, luego haga que pase, y mida el
  tiempo por prompt antes y después:

  ```bash
  bash tests/watchman.test.sh
  python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir> [...]
  ```

## Cambiar el formato de la bitácora

El hook analiza etiquetas exactas: `## Status`, `- **Bearing:**` (`confirmed` / `under review …` /
`closed …`), `- **Checkpoint cadence:**` (`every N commits or M sessions` / `off`),
`- **Last checkpoint:** <date> @ <sha>`, `**Boundary notes:**`, las líneas de Relations que contienen
"accepted" y el encabezado `## Path log`. `## Checkpoint log` solo lo leen las skills. Cámbielas solo
junto con el hook, la plantilla (`skills/checkwatch/assets/WATCH.md`), las skills y las pruebas.

## Traducciones

Los archivos en inglés de la raíz (`README.md`, `QUICKSTART.md`, `CONTRIBUTING.md`) son los canónicos.
Las traducciones se agrupan por idioma en `i18n/<lang>/`, para que la raíz no se sature. Al cambiar
un archivo en inglés, indique en el pull request qué traducciones han quedado desactualizadas.
Traductores: mantengan idénticos la barra de idiomas, los enlaces (relativos a `i18n/<lang>/`, p. ej.,
`../../docs/methods.md`), las insignias, los comandos y los bloques de código de shell (el diálogo del
*Ejemplo rápido* puede traducirse). Actualicen la nota `Traducido de` al principio del archivo. Árabe:
mantengan el texto dentro de `<div dir="rtl">` y los bloques de código fuera.

**Mantengan el tipo de afirmación.** Cada frase sobre TTW es una *intención de diseño* («está
diseñado para», «la skill indica a Claude que»), un *mecanismo* («el hook hace X», comprobable en un
archivo) o un *resultado* («en la prueba <X>, <número>»). La traducción debe conservar el mismo tipo:
revisen el verbo, no solo el sustantivo. Mantengan las mismas fuentes y los mismos números que en
inglés, dejen sin traducir las citas autor–año y los títulos originales, y no añadan afirmaciones ni
fuentes locales. El español usa español internacional neutro (*se* impersonal o *usted*). zh-Hans y
zh-Hant se localizan por separado, nunca se convierten carácter por carácter.

| English | pt-BR | es | zh-Hans | zh-Hant | ja | ar |
|---|---|---|---|---|---|---|
| is designed to | foi projetado para | está diseñado para | 旨在 | 旨在 | 〜を目的として設計されている | صُمّم لـ |
| the skill instructs Claude to | a skill instrui o Claude a | la skill indica a Claude que | 技能指示 Claude | 技能指示 Claude | スキルは Claude に〜するよう指示する | توجّه المهارةُ Claude إلى |
| tested by evals, not enforced by code | testado por evals, não imposto por código | probado con evals, no impuesto por código | 由评测检验，而非由代码强制 | 由評測檢驗，而非由程式碼強制 | eval で検証されており、コードで強制されてはいない | تُختبَر بالتقييمات ولا تفرضها الشيفرة |
| may / can | pode | puede | 可能 | 可能 | 〜可能性がある | قد |
| according to | segundo | según | 据 | 據 | 〜によれば | وفقًا لـ |
| as summarized by | conforme resumido por | según el resumen de | 据…的综述 | 據…的回顧 | 〜の要約による | كما لخّصه |
| design premise | premissa de projeto | premisa de diseño | 设计前提 | 設計前提 | 設計上の前提 | فرضية التصميم |
| guarantees | *avoid*: foi projetado para | *avoid*: está diseñado para | *avoid*: 旨在 | *avoid*: 旨在 | *avoid*: 〜設計されている | *avoid*: صُمّم لـ |
| always (rules only) | sempre | siempre | 始终 | 始終 | 必ず | دائمًا |
| significant (statistical only) | significativo | significativo | 显著 | 顯著 | 有意 | دالّ إحصائيًا |
| substantial (non-statistical) | substancial | sustancial | 较大 | 較大 | 大きな | كبير |
| evidence | evidência | evidencia | 证据 | 證據 | 根拠 | الأدلة |
| indicates (not "proves") | indica | indica | 表明 | 顯示 | 示唆する | تشير إلى |
| efficient | eficiente | eficiente | 高效 | 高效 | 効率的 | ذو كفاءة |
| effective | eficaz | eficaz | 有效 | 有效 | 効果的 | فعّال |
| drift | desvio | desvío | 漂移 | 偏移 | ずれ | الانحراف |
| bearing | rumo | rumbo | 航向 | 航向 | 針路 | المسار |
| human in the loop | humano no circuito | humano en el circuito | 人在回路中 | 人在迴路中 | ヒューマン・イン・ザ・ループ | الإنسان ضمن الحلقة |

El glosario está asistido por máquina; las correcciones de hablantes nativos son bienvenidas.

## Pull requests

1. Haga un fork y cree una rama: `feat/<algo>`, `fix/<algo>`, `docs/<algo>` o `lens/<campo>`.
2. Mantenga cada pull request centrado en un solo cambio.
3. Ejecute `bash tests/watchman.test.sh` y `claude plugin validate .` si tiene Claude Code.
4. Añada una entrada en **Unreleased** en [CHANGELOG.md](../../CHANGELOG.md).
5. Use mensajes de [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`).

Al contribuir, usted acepta que sus contribuciones se licencian en los mismos términos que el resto
del repositorio: [CC BY-NC 4.0](../../LICENSE).
