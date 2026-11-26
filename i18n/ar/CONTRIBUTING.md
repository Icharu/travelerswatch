<!-- lang-bar -->
[English](../../CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [繁體中文](../zh-Hant/CONTRIBUTING.md) · [简体中文](../zh-Hans/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · **العربية**

<div dir="rtl">

> مترجم عن `CONTRIBUTING.md` (Unreleased، 2026-11-25). ترجمة بمساعدة الآلة؛ النسخة الإنجليزية هي المرجع المعتمد.

# المساهمة في The Traveler's Watch

شكرًا لمساعدتك في إبقاء المسافرين على طريقهم. نرحّب بالمساهمات مهما كان حجمها.

## ما الذي أدّى إلى هذا المشروع

تشجّع TTW المستخدمين والمساهمين على فهم ما أدّى إليها قبل تعديلها. يستند التصميم إلى نحو **خمس سنوات من الأبحاث (2021–2026)** حول كيفية انحراف النماذج اللغوية في الأعمال الطويلة، وكيف يغيّر الذكاء الاصطناعي إدارة المشاريع، إضافةً إلى دراسة سابقة عن تضخّم النطاق (*scope creep*).

البحث في كيفية عمل الذكاء الاصطناعي واستخدامه في العالم الحديث **متعدد التخصصات** بطبيعته (Koshman & Zubkova, 2026)، ولذلك نرحّب بالمساهمات من أي مجال. وتحدّد مراجعتان موقع TTW في هذا البحث:

- **ما يُحسنه الذكاء الاصطناعي بالفعل في إدارة المشاريع.** وجد Adamantiadou وTsironis ‏(2025) أن تعلّم الآلة والتعلّم العميق والنماذج الهجينة وسّعت كثيرًا قدرات إدارة المشاريع، فحسّنت **تقدير التكاليف، والتنبؤ بالجداول الزمنية، وتحليل المخاطر**. وتأخذ TTW ذلك بجدية: فهي تؤتمت العمل المتكرر داخل المسار.
  *ملاحظة شفافية: نستشهد بهذه النتيجة كما وردت في Koshman & Zubkova ‏(2026)؛ وقد تحققنا من بيانات المقال الأصلي عبر معرّف DOI الخاص به.*
- **ما لم يُحلّ بعد.** راجع Koshman وZubkova ‏(2026) سبعًا وتسعين منشورًا، ووجدا أن نماذج الذكاء الاصطناعي ضعيفة التكيّف مع تغيّر ظروف المشروع، ونادرًا ما يُتحقَّق منها مقابل البيانات الأولية، وقليلة الدراسة في مراحل مثل مراجعة ما بعد المشروع. وقد بُنيت TTW حول هذه الفجوات: يحتفظ مدير المشروع بالاتجاه، ويُطابَق المسار مع الأدلة، ويدعم السجل مراجعة ما بعد المشروع.

| السنة | المرجع | لماذا يهمّ هنا |
|---|---|---|
| 2020 | Komal et al., [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098) | التغيير غير المصرّح به يضرّ بالمشاريع ← يُؤكَّد كل تغيير في المسار ويُسجَّل |
| 2024 | Liu et al., [*Lost in the Middle*](https://doi.org/10.1162/tacl_a_00638) | تستفيد النماذج أكثر من طرفَي السياق الطويل ← مسار قصير بجوار كل طلب |
| 2024 | [*A Survey on LLM-as-a-Judge*](https://arxiv.org/abs/2411.15594) | تحتاج النماذج المُحكِّمة إلى معايير صريحة ← يُحدَّد المعيار قبل أي حكم |
| 2025 | Laban et al., [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120) | تسلك النماذج منعطفات خاطئة ولا تتعافى ← يُحدَّد المسار منذ البداية |
| 2025 | Dongre et al., [*Drift No More?*](https://arxiv.org/abs/2510.07777) | التذكيرات تقلّل الانحراف ← الحارس مع كل طلب |
| 2025 | Adamantiadou & Tsironis, [*Leveraging AI in Project Management*](https://doi.org/10.3390/computers14020066) | يحسّن الذكاء الاصطناعي التقدير والتنبؤ وتحليل المخاطر ← أتمتة العمل المتكرر |
| 2026 | Koshman & Zubkova, [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23) | التكيّف والتحقق ومراجعة ما بعد المشروع لم تُحلّ ← الإنسان في الحلقة |

القائمة المشروحة كاملة، مع الأثر التصميمي لكل مصدر، في [docs/methods.md](../../docs/methods.md) (بالإنجليزية). وكيف بدأ المشروع ومن يقرّر، في [GOVERNANCE.md](../../GOVERNANCE.md).

</div>

<details>
<summary><b>References</b></summary>

- Adamantiadou, D. S., & Tsironis, L. (2025). Leveraging artificial intelligence in project
  management: A systematic review of applications, challenges, and future directions. *Computers*,
  14(2), 66. https://doi.org/10.3390/computers14020066
- Koshman, Y., & Zubkova, A. (2026). Artificial intelligence in project management. *Development
  Management*, 25(1), 23–31. https://doi.org/10.63341/devt/1.2026.23
- [docs/methods.md](../../docs/methods.md)

</details>

<div dir="rtl">

## طرق المساهمة

| المساهمة | المكان |
|---|---|
| **عدسة** لمجال جديد (مثل الفعاليات، والبناء، والبرامج غير الربحية، وتصميم المنتجات) | `skills/checkwatch/references/lenses/` |
| **مراجعة ترجمة** من متحدث أصلي | `i18n/<lang>/` (README وQUICKSTART وCONTRIBUTING) |
| **حالة تقييم** جديدة (طلب مع السلوك المتوقع) | `skills/<skill>/evals/evals.json` |
| **بلاغ عن خطأ** أو فكرة | [Issues](https://github.com/Icharu/travelerswatch/issues). استخدم القوالب. |
| **مشكلة أمنية** | **ليس** في issues. راجع [SECURITY.md](../../SECURITY.md). |

## إضافة عدسة

1. انسخ عدسة موجودة (مثل `project-management.md`) إلى `lenses/<field>.md`.
2. احتفظ بالعناوين الأربعة نفسها كي تستخدم المهارة أي عدسة بالطريقة ذاتها:
   - **How the sections read in this field**: جدول يعيد صياغة السياق والقيود والمشكلة والأدوات
   - **Default criteria**: من 4 إلى 8 معايير *قابلة للملاحظة* (راجع `references/standards.md`)
   - **Drift signals**: كيف يبدو الخروج عن الطريق في هذا المجال
   - **Typical tools**
3. اكتب المعايير **بكلماتك الخاصة**. لا تلصق نصوصًا من معايير مدفوعة أو محمية بحقوق النشر؛ اذكرها بالاسم وأشر إلى أقسامها فقط.
4. أضف العدسة إلى القائمة في `skills/checkwatch/SKILL.md` (الخطوة A1) وإلى قسم *Lenses* في README.
5. أضف حالة تقييم واحدة على الأقل في `skills/checkwatch/evals/evals.json` تستخدم العدسة.

## تعديل المهارات

- اجعل كل `SKILL.md` قصيرًا وموجّهًا نحو القرارات؛ وضع التفاصيل في `references/`.
- لا تُضعف القواعد الأساسية ([GOVERNANCE.md](../../GOVERNANCE.md#how-decisions-are-made)): **مدير المشروع وحده يؤكد** تغيير المسار أو الإغلاق أو قبول التناقض؛ **Path log وسجل نقاط التفتيش يقبلان الإضافة فقط**؛ **لا جلسات مؤتمتة بالكامل** للمسار ([ADR 0004](../../docs/adr/0004-human-in-the-loop.md))؛ **لا بيانات تُحفظ** خارج مستودع المستخدم.
- استخدم فقط الـ frontmatter القياسي لـ Agent Skills ‏(`name` و`description` و`license` و`metadata`) لتظل المهارات قابلة للنقل.
- اشرح تغييرات السلوك في ADR ضمن `docs/adr/` عندما تغيّر قرارًا تصميميًا.

## تعديل الـ hook

- bash فقط (الإصدار 3.2 أو أحدث، من أجل macOS) وawk؛ وgit اختياري. فضّل الأوامر المدمجة في bash على العمليات الإضافية؛ ويُحلَّل السجل بمرور واحد لـ `awk`.
- يجب أن ينتهي دائمًا بالرمز 0، وأن يصمت عند غياب السجل أو عندما يكون المسار `closed`، وأن يحدّ من حجم المخرجات، وألا يجري اتصالات شبكية، وألا يكتب شيئًا سوى `.watch/.state`.
- **اكتب الاختبار الفاشل أولًا** في `tests/watchman.test.sh`، ثم اجعله ينجح، وقِس الزمن لكل طلب قبل التعديل وبعده:

</div>

```bash
bash tests/watchman.test.sh
python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir> [...]
```

<div dir="rtl">

## تعديل صيغة السجل

يحلّل الـ hook تسميات دقيقة: `## Status`، و`- **Bearing:**` ‏(`confirmed` / `under review …` / `closed …`)، و`- **Checkpoint cadence:**` ‏(`every N commits or M sessions` / `off`)، و`- **Last checkpoint:** <date> @ <sha>`، و`**Boundary notes:**`، وأسطر Relations التي تحتوي على "accepted"، والعنوان `## Path log`. أما `## Checkpoint log` فتقرؤه المهارات فقط. لا تغيّر هذه التسميات إلا مع الـ hook والقالب (`skills/checkwatch/assets/WATCH.md`) والمهارات والاختبارات معًا.

## الترجمات

الملفات الإنجليزية في الجذر (`README.md` و`QUICKSTART.md` و`CONTRIBUTING.md`) هي المرجع المعتمد. وتُجمَّع الترجمات حسب اللغة في `i18n/<lang>/` كي يبقى الجذر مرتّبًا. عندما تغيّر ملفًا إنجليزيًا، اذكر في طلب السحب أي الترجمات أصبحت قديمة. أيها المترجمون: أبقوا شريط اللغات، والروابط (نسبةً إلى `i18n/<lang>/`، مثل `../../docs/tale.md`)، والشارات، والأوامر، وكتل شيفرة shell كما هي (يمكن ترجمة الحوار في *مثال سريع*). حدّثوا ملاحظة «مترجم عن» في أعلى الملف. العربية: أبقوا النص داخل `<div dir="rtl">` وكتل الشيفرة خارجه.

## طلبات السحب (Pull requests)

1. أنشئ نسخة (fork)، ثم فرعًا: `feat/<thing>` أو `fix/<thing>` أو `docs/<thing>` أو `lens/<field>`.
2. اجعل كل طلب سحب مركّزًا على تغيير واحد.
3. شغّل `bash tests/watchman.test.sh` و`claude plugin validate .` إن كان لديك Claude Code.
4. أضف بندًا تحت **Unreleased** في [CHANGELOG.md](../../CHANGELOG.md).
5. استخدم رسائل [Conventional Commits](https://www.conventionalcommits.org/) ‏(`feat:` و`fix:` و`docs:`).

بمساهمتك، توافق على أن مساهماتك مرخّصة بالشروط نفسها التي يخضع لها باقي المستودع: [CC BY-NC 4.0](../../LICENSE).

</div>
