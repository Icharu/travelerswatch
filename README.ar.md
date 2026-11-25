<!-- lang-bar -->
[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · **العربية**

<div dir="rtl">

> مترجم عن `README.md` الإصدار v1.1.0 (2026-11-25). ترجمة بمساعدة الآلة؛ نرحّب بمراجعة المتحدثين الأصليين. النسخة الإنجليزية هي المرجع المعتمد.

# The Traveler's Watch (ساعة المسافر)

[![Version](https://img.shields.io/badge/version-v1.1.0-blue)](CHANGELOG.md)
[![License: MIT (code) + CC BY 4.0 (docs)](https://img.shields.io/badge/license-MIT%20%2B%20CC%20BY%204.0-green)](LICENSE-docs)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24543183.svg)](https://doi.org/10.5281/zenodo.24543183)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-8A2BE2)](https://agentskills.io/)

**تقييم، ومراجعة للمنهجية، ومراقبة لانحراف السياق في المشاريع التي تُنجَز مع Claude.**
حدِّد مسار مشروعك مرة واحدة، واحصل على تنبيه من سطر واحد كلما انحرف العمل عنه، ولا تغيّر الاتجاه إلا عن قصد، على أن يؤكد مدير المشروع كل تغيير ويُسجَّل.

> مسافرٌ يعبر ضبابًا كثيفًا بساعةٍ معطلة. كلما نظر إليها عند الظهيرة رجعت عشر دقائق، فظلّ يقطع المسافة نفسها مرة بعد مرة، وهو واثق أنه يتقدّم.
> — [اقرأ الحكاية كاملة](docs/tale.md)

تفشل المشاريع الطويلة التي تُنجَز بالنماذج اللغوية بالطريقة نفسها: تترسّخ الافتراضات المبكرة، ويضيع السياق في التلخيص، والنموذج الذي سلك منعطفًا خاطئًا يظل يعود إليه ([لماذا يحدث ذلك](docs/methods.md)). تمنح The Traveler's Watch مشروعك ساعةً يمكنك الوثوق بها.

## كيف تعمل

| الأمر | ماذا يفعل |
|---|---|
| **`/checkwatch`** | **عند عدم وجود سجل:** يقرأ أولًا وثائق المشروع نفسه وتاريخه، ثم يتفق معك على *المسار* (النطاق، المعيار، السياق، القيود، المشكلة، الأدوات)، وينقل البنود الموضوعة في غير مكانها، ويطلب منك حلّ كل تناقض مع الأدلة أو قبوله صراحةً، ثم يكتب `.watch/WATCH.md`. **عند وجود السجل:** يُجري نقطة تفتيش على العمل *وعلى* المسار نفسه، ويُبلغ بالحالة **على المسار / ينحرف / خارج المسار / المسار موضع شك** مع الأدلة. |
| **الحارس** *(تلقائي)* | مع كل طلب، يذكّر hook في Claude Code الـ Claude بالمسار. إذا انحرف طلبك، يقول Claude ذلك في سطر واحد ويقترح `/fixwatch`، ثم يتابع المهمة. وينبّه مرة واحدة في كل جلسة عندما تحين نقطة تفتيش، ويتوقف مؤقتًا ما دام المسار *قيد المراجعة*. |
| **`/fixwatch`** | يقترح تغيير المسار في صورة فرق «قبل/بعد»، ويبيّن ما يتأثر به أيضًا، وينتظر تأكيد مدير المشروع، ثم يحدّث المسار و**يضيف** قيدًا جديدًا إلى سجل الطريق (*Path log*). يمكن لـ Claude أن يقترح، حتى عندما يكون قد أساء فهم السياق؛ لكن مدير المشروع وحده يؤكد. |
| **`/configwatch`** | يعرض حالة الحارس ويحدّد عدد مرات طلب نقطة تفتيش: كل *N* من الإيداعات (commits) أو *M* من الجلسات (الافتراضي 3 أو 2)، أو إيقافها. |

### مستند إلى الأدلة

قد يكون المسار متّسقًا مع نفسه ومع ذلك مخطئًا بشأن المشروع. منذ الإصدار v1.1.0 تُضبط الساعة على أدلة المشروع نفسه، وتكشف نقطة تفتيش مبكرة الأخطاء سريعًا، ويتوقف الحارس مؤقتًا ما دام المسار قيد المراجعة ([لماذا](docs/benchmarks/2026-11-25-best-vs-worst.md)).

### المسار

| القسم | أجب عن هذا |
|---|---|
| **النطاق** (*Scope*) | أيّ جزء من المشروع يوجّهه هذا المسار، وأيّ جزء لا؟ |
| **المعيار** (*Standard*) | على أي أساس سيُقيَّم العمل؟ **عدسة جاهزة**، أو **معايير تقييم مكتوبة بحرية**، أو **معيار خارجي مسمّى**؛ ويُفحص دائمًا من حيث الملاءمة وقابلية التقييم والاتساق والنطاق والحقوق والأخلاقيات. |
| **السياق** (*Context*) | أين يقع هذا العمل؟ المجال، وأصحاب المصلحة، والوضع الحالي، و**الأعمال المرجعية**. |
| **القيود** (*Constraints*) | ما الذي يحدّك؟ الوقت، والميزانية، والأفراد، والتقنيات المفروضة، والأنظمة. |
| **المشكلة** (*Problem*) | ما الخلل اليوم (**المشكلة الأصلية**)، وكيف يبدو «الإنجاز» (**الهدف النهائي**)؟ |
| **الأدوات** (*Tools*) | ماذا ستستخدم، ولماذا تناسب كل أداة السياقَ والقيود؟ |

### العدسات

تكيّف العدسات الأسئلة والمعايير الافتراضية مع مجال معيّن.
المضمَّنة: [إدارة المشاريع](skills/checkwatch/references/lenses/project-management.md) (افتراضية) ·
[البحث العلمي](skills/checkwatch/references/lenses/research.md) ·
[البرمجيات](skills/checkwatch/references/lenses/software.md) ·
[علم البيانات](skills/checkwatch/references/lenses/data-science.md).
لإضافة عدستك، راجع [CONTRIBUTING.md](CONTRIBUTING.md#adding-a-lens).

## التثبيت

**كإضافة (plugin) في Claude Code** (المهارات + hook الحارس):

</div>

```text
/plugin marketplace add Icharu/travelerswatch
/plugin install travelerswatch@travelerswatch
```

<div dir="rtl">

تصبح الأوامر ضمن نطاق اسم: `/travelerswatch:checkwatch` و`/travelerswatch:fixwatch` و`/travelerswatch:configwatch`.

**المهارات فقط** (Claude Code أو أي وكيل يقرأ [Agent Skills](https://agentskills.io/)؛ بدون hook):

</div>

```bash
git clone https://github.com/Icharu/travelerswatch
cp -r travelerswatch/skills/checkwatch travelerswatch/skills/fixwatch travelerswatch/skills/configwatch ~/.claude/skills/
```

<div dir="rtl">

تصبح الأوامر `/checkwatch` و`/fixwatch` و`/configwatch`. بدون الـ hook، شغّل `/checkwatch` في بداية كل جلسة عمل.

**للتجربة محليًا دون تثبيت:** `claude --plugin-dir ./travelerswatch`

**لإيقاف الحارس مؤقتًا:** `export TRAVELERSWATCH_DISABLE=1`

## مثال سريع

</div>

```text
أنت:    /checkwatch
Claude: لا يوجد سجل بعد. أولًا المعيار: عدسة جاهزة، أم معاييرك الخاصة، أم معيار مسمّى؟
أنت:    عدسة إدارة المشاريع. السياق: لدينا موظفان فقط بدوام جزئي. المشكلة: بناء تطبيق للجمع.
Claude: «موظفان فقط بدوام جزئي» قيدٌ، لذا مكانه في القيود.
        «بناء تطبيق للجمع» حلّ. ما المشكلة التي وراءه، وكيف يبدو «الإنجاز»؟
…
أنت:    لنُضِف تطبيقًا بأسلوب الألعاب للمدينة كلها.
Claude: ⚠️ الحارس: ينحرف عن المشكلة (حيّان تجريبيان) وعن القيود (ميزانية 20 ألفًا).
        هل نتابع، أم /fixwatch؟
```

<div dir="rtl">

الجلسة كاملة (بالإنجليزية): [examples/pm-walkthrough.md](examples/pm-walkthrough.md).

## بنية المستودع

</div>

```text
.claude-plugin/        plugin + marketplace manifests
skills/checkwatch/     SKILL.md · references/ (standards, sections, relations, lenses) · assets/WATCH.md · evals/
skills/fixwatch/       SKILL.md · evals/
skills/configwatch/    SKILL.md · evals/
hooks/                 hooks.json · watchman.sh (bash + awk only)
tests/                 watchman.test.sh
docs/                  tale · concepts · methods · adr/
examples/              worked PM session
```

<div dir="rtl">

تشغيل الاختبارات: `bash tests/watchman.test.sh` · قياس زمن الـ hook: `python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir>`

## التوثيق

- [المفاهيم](docs/concepts.md): المهارات، والمسار، والأحكام، ومن يقرّر
- [المنهجية](docs/methods.md): الأبحاث وراء كل قرار تصميمي
- [ADR 0001](docs/adr/0001-hook-for-per-prompt-watch.md) · [ADR 0002](docs/adr/0002-committed-logbook.md) · [ADR 0003](docs/adr/0003-evidence-grounded-bearing.md)
- [قياس الأداء: أفضل وأسوأ حالة](docs/benchmarks/2026-11-25-best-vs-worst.md): ما فات الإصدار v1.0.0، وما أصلحه v1.1.0، وزمن الـ hook لكل طلب
- [سجل التغييرات](CHANGELOG.md)

(التوثيق المفصّل باللغة الإنجليزية.)

## المساهمة

المساهمات مرحَّب بها، ولا سيما **العدسات الجديدة** لمجالات أخرى، ومراجعة الترجمات من قِبل متحدثين أصليين، وحالات تقييم جديدة. اقرأ [CONTRIBUTING.md](CONTRIBUTING.md) قبل فتح طلب سحب (pull request).

## الأمان

**لا تُبلّغ عن الثغرات في issues عامة.** استخدم [الإبلاغ الخاص عن الثغرات](https://github.com/Icharu/travelerswatch/security/advisories/new) في GitHub (تبويب **Security** ثم **Report a vulnerability**). أوقات الاستجابة بأفضل جهد ممكن وتعتمد على درجة الخطورة. راجع [SECURITY.md](SECURITY.md) لمعرفة النطاق وجدول الاستجابة وما يمكنك فعله أثناء الانتظار.

## الاستشهاد

إذا استخدمت The Traveler's Watch في البحث أو التدريس، يُرجى الاستشهاد به. يقرأ زر **"Cite this repository"** في GitHub الملف [CITATION.cff](CITATION.cff). معرّفات DOI في Zenodo: جميع الإصدارات [10.5281/zenodo.24543183](https://doi.org/10.5281/zenodo.24543183) (استشهد به ما لم تحتج إلى إصدار بعينه) · v1.1.0 [10.5281/zenodo.24543326](https://doi.org/10.5281/zenodo.24543326) · v1.0.0 [10.5281/zenodo.24543184](https://doi.org/10.5281/zenodo.24543184).

## الترخيص

© 2026 Icaro de Jesus Silva. **الشيفرة** (`hooks/` و`tests/` وجميع ملفات `.sh` و`.py` و`.json` و`.yml` و`.cff`) مرخّصة بموجب [MIT](LICENSE). أما **التوثيق ونصوص المهارات** (جميع ملفات Markdown، بما فيها `skills/**/*.md` و`docs/` و`examples/` وملفات README) فمرخّصة بموجب [CC BY 4.0](LICENSE-docs): يمكنك إعادة استخدامها وتعديلها بحرية مع نسبة العمل إلى صاحبه. يبقى الإصدار v1.0.0 مرخّصًا بالكامل بموجب MIT. الحكاية في [docs/tale.md](docs/tale.md) إعادة سرد أصلية؛ والاقتباس من سفر إشعياء 21:11 في الملك العام.

## قراءات إضافية

</div>

- Laban et al. (2025), [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120)
- Dongre et al. (2025), [*Drift No More? Context Equilibria in Multi-Turn LLM Interactions*](https://arxiv.org/abs/2510.07777)
- Liu et al. (2024), [*Lost in the Middle: How Language Models Use Long Contexts*](https://doi.org/10.1162/tacl_a_00638)
- Komal et al. (2020), [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098)
- Anthropic (2025), [*Equipping agents for the real world with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

<div dir="rtl">

- القائمة المشروحة كاملة: [docs/methods.md](docs/methods.md)

</div>
