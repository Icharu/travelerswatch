<!-- lang-bar -->
[English](../../CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [繁體中文](../zh-Hant/CONTRIBUTING.md) · [简体中文](../zh-Hans/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · **العربية**

<div dir="rtl">

> مترجم عن `CONTRIBUTING.md` (v1.2.3، 2026-11-26). ترجمة بمساعدة الآلة؛ النسخة الإنجليزية هي المرجع المعتمد.

# المساهمة في The Traveler's Watch

شكرًا لمساعدتك في إبقاء المسافرين على طريقهم. نرحّب بالمساهمات مهما كان حجمها.

## ما الذي أدّى إلى هذا المشروع

تشجّع TTW المستخدمين والمساهمين على فهم ما أدّى إليها قبل تعديلها. يستند التصميم إلى أدبيات نُشرت بين 2020 و2026: دراسات عن كيفية انحراف النماذج اللغوية في الأعمال الطويلة، ومراجعات عن كيفية تغيير الذكاء الاصطناعي لإدارة المشاريع، ودراسة عن تضخّم النطاق (*scope creep*).

يصف Koshman وZubkova ‏(2026) البحث في كيفية عمل الذكاء الاصطناعي واستخدامه في العالم الحديث بأنه **متعدد التخصصات** بطبيعته، ولذلك نرحّب بالمساهمات من أي مجال. وتحدّد مراجعتان موقع TTW في هذا البحث:

- **ما يُحسنه الذكاء الاصطناعي بالفعل في إدارة المشاريع.** راجع Adamantiadou وTsironis ‏(2025) ‏97 دراسة محكّمة (2011–2024). ووفقًا لملخّصهما، أظهر تعلّم الآلة والتعلّم العميق والنماذج الهجينة إمكانات لتحسين إدارة المشاريع، ولا سيما في **تقدير التكاليف، والتنبؤ بالمدد، وتقييم المخاطر**. وتأخذ TTW ذلك بجدية: فهي تؤتمت العمل المتكرر داخل المسار.
- **ما لم يُحلّ بعد.** وفقًا لما لخّصه Koshman وZubkova ‏(2026)، تشير المراجعة نفسها إلى أن نماذج الذكاء الاصطناعي غير كافية التكيّف مع تغيّر ظروف المشروع، وأن التحقق منها مقابل البيانات الأولية محدود، وأنها قليلة البحث في مراحل مثل مراجعة ما بعد المشروع. وقد بُنيت TTW حول هذه الفجوات: يحتفظ مدير المشروع بالاتجاه، ويُطابَق المسار مع الأدلة، ويدعم السجل مراجعة ما بعد المشروع.

*ملاحظة عن المصادر (ما الذي قُرئ):* Koshman & Zubkova ‏(2026): النص الكامل. Adamantiadou & Tsironis ‏(2025): قُرئت من خلال ملخّص Koshman & Zubkova، ومن خلال الملخّص (*abstract*) والبيانات الببليوغرافية في سجل DOI الخاص بها؛ ولم يُقرأ النص الكامل. كانت النسخ السابقة من هذا الملف تنسب مراجعة الـ 97 منشورًا إلى Koshman & Zubkova؛ وكان ذلك خطأً في النسبة، صُحّح في الإصدار v1.2.3.

| السنة | المرجع | لماذا يهمّ هنا |
|---|---|---|
| 2020 | Komal et al., [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098) | التغيير غير المصرّح به يضرّ بالمشاريع ← يُؤكَّد كل تغيير في المسار ويُسجَّل |
| 2024 | Liu et al., [*Lost in the Middle*](https://doi.org/10.1162/tacl_a_00638) | تستفيد النماذج أكثر من طرفَي السياق الطويل ← مسار قصير بجوار كل طلب |
| 2024 | [*A Survey on LLM-as-a-Judge*](https://arxiv.org/abs/2411.15594) | تحتاج النماذج المُحكِّمة إلى معايير صريحة ← يُحدَّد المعيار قبل أي حكم |
| 2025 | Laban et al., [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120) | تسلك النماذج منعطفات خاطئة ولا تتعافى ← يُحدَّد المسار منذ البداية |
| 2025 | Dongre et al., [*Drift No More?*](https://arxiv.org/abs/2510.07777) | التذكيرات تقلّل الانحراف ← الحارس مع كل طلب |
| 2025 | Adamantiadou & Tsironis, [*Leveraging AI in Project Management*](https://doi.org/10.3390/computers14020066) | مراجعة لـ 97 دراسة: يُظهر الذكاء الاصطناعي إمكانات في التقدير والتنبؤ والمخاطر؛ والتكيّف والتحقق والمراحل المتأخرة لم تُحلّ ← أتمتة العمل المتكرر، مع إبقاء الإنسان في الحلقة |
| 2026 | Koshman & Zubkova, [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23) | مراجعة لـ 21 منشورًا (2021–2025) ولأدوات الذكاء الاصطناعي؛ تلخّص مراجعة الـ 97 دراسة؛ منظور متعدد التخصصات ← الإنسان في الحلقة، والمساهمات من أي مجال |

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
| **مراجعة ترجمة** من متحدث أصلي | `i18n/<lang>/` (README وQUICKSTART وCONTRIBUTING وtale) |
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

الملفات الإنجليزية في الجذر (`README.md` و`QUICKSTART.md` و`CONTRIBUTING.md`) هي المرجع المعتمد. وتُجمَّع الترجمات حسب اللغة في `i18n/<lang>/` كي يبقى الجذر مرتّبًا. عندما تغيّر ملفًا إنجليزيًا، اذكر في طلب السحب أي الترجمات أصبحت قديمة. أيها المترجمون: أبقوا شريط اللغات، والروابط (نسبةً إلى `i18n/<lang>/`، مثل `../../docs/methods.md`)، والشارات، والأوامر، وكتل شيفرة shell كما هي (يمكن ترجمة الحوار في *مثال سريع*). حدّثوا ملاحظة «مترجم عن» في أعلى الملف. العربية: أبقوا النص داخل `<div dir="rtl">` وكتل الشيفرة خارجه.

**حافظوا على نوع الادعاء.** كل جملة عن TTW إما *نية تصميم* («صُمّمت لـ»، «توجّه المهارةُ Claude إلى»)، أو *آلية* («يفعل الـ hook كذا»، ويمكن التحقق منها في ملف)، أو *نتيجة* («في <الاختبار>، <الرقم>»). ويجب أن تحافظ الترجمة على النوع نفسه: راجعوا الفعل لا الاسم وحده. أبقوا المصادر والأرقام كما في النسخة الإنجليزية، واتركوا الاستشهادات بصيغة المؤلف–السنة والعناوين الأصلية دون ترجمة، ولا تضيفوا ادعاءات أو مصادر محلية. تستخدم الإسبانية الإسبانيةَ الدولية المحايدة (*se* غير الشخصية أو *usted*). وتُوطَّن zh-Hans وzh-Hant كلٌّ على حدة، ولا تُحوَّل إحداهما إلى الأخرى حرفًا بحرف.

</div>

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

<div dir="rtl">

هذا المسرد بمساعدة الآلة؛ ونرحّب بتصحيحات المتحدثين الأصليين.

## طلبات السحب (Pull requests)

1. أنشئ نسخة (fork)، ثم فرعًا: `feat/<thing>` أو `fix/<thing>` أو `docs/<thing>` أو `lens/<field>`.
2. اجعل كل طلب سحب مركّزًا على تغيير واحد.
3. شغّل `bash tests/watchman.test.sh` و`claude plugin validate .` إن كان لديك Claude Code.
4. أضف بندًا تحت **Unreleased** في [CHANGELOG.md](../../CHANGELOG.md).
5. استخدم رسائل [Conventional Commits](https://www.conventionalcommits.org/) ‏(`feat:` و`fix:` و`docs:`).

بمساهمتك، توافق على أن مساهماتك مرخّصة بالشروط نفسها التي يخضع لها باقي المستودع: [CC BY-NC 4.0](../../LICENSE).

</div>
