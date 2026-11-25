# The Traveler's Watch

*An original retelling, written for this project.*

A traveler set out across a valley that the fog had swallowed whole. He could not see the road, so
he trusted the one thing he carried that did not depend on sight: his pocket watch. He had reckoned
the journey in hours — walk until noon, turn east at the stone bridge, reach the town by dusk.

At what the watch called noon he stopped, pressed the crown with his right index finger, and read
the hands. Twelve. He turned east. He walked. Some while later he checked again — and the watch read
ten minutes to twelve. He frowned, assumed he had misread it, and walked on until it said twelve
again. He turned east once more.

He did not know the watch was broken. Every time he pressed it at noon, it slipped back ten minutes.
So every time he checked, he went back over ground he had already walked, quite sure he was moving
forward. The fog hid the stone bridge he kept passing. He was tired by evening and no closer to the
town, and he could not say where he had lost the day.

On the town wall a watchman stood his post through the night. Travelers below called up to him the
old question — *"Watchman, what of the night?"* — and he answered with what he could actually see:
where the road ran, how far it was to dawn. He did not guess and he did not flatter. When the road
changed, he said so, and he said why.

The traveler's trouble was not the fog. Fog is normal; every long road has some. His trouble was a
reference he could not trust, consulted at the very moment he most needed it, rewinding without
warning — and nobody standing watch to tell him he had seen that bridge before.

---

## Why this is a skill

Long projects worked through with language models drift in much the same way. Early assumptions
harden, part of the conversation is summarized away, and a model that took a wrong turn keeps
returning to it while every individual step feels like progress. The Traveler's Watch gives the
project two things the traveler lacked:

| In the tale | In the skill |
|---|---|
| A watch you can trust | The **bearing** in `.watch/WATCH.md` — written down, committed, not rewound by context loss |
| The watchman's honest report | The **watchman hook** — on every prompt, one line if the work has drifted |
| Turning east on purpose | **`/fixwatch`** — a course change that is chosen, confirmed by the PM, and logged |
| Knowing the road before setting out | **`/checkwatch`** — Standard, Context, Constraints, Problem and Tools agreed before walking |

The line *"Watchman, what of the night?"* is from Isaiah 21:11 (public domain).
