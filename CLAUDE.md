# CLAUDE.md — kubernetes-ct

A **content repo**, not an app. It holds the **Kubernetes** concept, authored **video-first**
for the `graphl-movie` app (sibling repo), which loads it **at runtime**. No render
engine and no scenes live here — the app fetches this repo's `manifest.json` + notebooks
+ slides over the network and renders/records them. Read alongside the workspace map in
`../CLAUDE.md`, the app contract in `../graphl-movie/CLAUDE.md`, and the sibling
video-first content repos `../docker-ct/CLAUDE.md`, `../linux-ct/CLAUDE.md`,
`../aws-ct/CLAUDE.md`, and `../apache-spark-ct/CLAUDE.md`.

This is a `-ct` (video-target) content repo. It is authored **fresh** for the video
target — the existing graphl-ux-era `../kubernetes-content` (whole-notebook, feed/canvas
era) is **reference material**, not something to copy wholesale. We refine structure for
video, not port it.

Concretely, each module's section notebooks are **split from the `../kubernetes-content`
per-module notebook** — the source of truth for the split — then refined for the video
target (trimmed to the agreed spine, `## `-per-section, images dropped). Example: module
02's sections split from `../kubernetes-content/notebooks/02-pods-labels-and-the-object-model.ipynb`.

There is **nothing to build, run, or test** here. The one executable (later) is a Colab
tool that turns `tts/` scripts into `audio/` `.wav`s.

## Working agreement

Same as the app repo: **step by step, one small slice, review gate between each.** We
settle the shape first (module spine → sections → …), then fill content deliberately. No
batch generation, no "I generated 12 files" — list files and get a yes.

## The core contract (from graphl-movie — do not break)

1. **The notebook is the single source of truth** for a section's prose and code.
   `manifest.json` only *wires* — it must never duplicate notebook content.
2. **One notebook per section** (not per module): each `.ipynb` holds exactly one `## `
   section. The section is the atomic unit across all four artifacts — `.ipynb` + `.tts`
   + `.slide` + `.wav` share the same `NN-SS-slug` stem — so a section can be authored and
   reviewed on its own. The manifest references each artifact by path; the notebook's
   single `## ` heading is the section title (mirror it in the manifest `heading`).
3. Each section is the unit the video steps through and has its own **`.ipynb`**
   (prose/code), **`.tts`** (narration script), **`.wav`** (generated audio), and — new
   for video — a **`.slide`** file (the authored right-pane bullets). Module title/lede
   lives in `README.md` + the manifest, not in the section notebooks.
4. A section's diagram images (`![]()`) are **stripped** by the app — the React Flow
   **scene** replaces them.
5. **Scenes live in the `graphl-movie` app** (`src/scenes/*`), authored with the engine's
   pattern helpers. Here you only reference a scene **by id**, plus `highlight` (node ids
   brightened in-place, the rest dimmed) and `focus` (a node id the camera frames) per
   section. Kubernetes rides a **single dense scene** — `kubernetes`, ported into
   graphl-movie from `../graphl-ux/src/scenes/kubernetes.ts`, refined for the 1920×1080
   video frame. Every module frames one band/subsystem of that one map (`k8s-*` node ids).

## Folder layout

```
kubernetes-ct/
  notebooks/   # one .ipynb per SECTION (one ## section each) — source of truth for prose/code
  tts/         # one .tts per section (plain spoken narration script)
  audio/       # one .wav per section (generated from tts/ via Colab)
  slides/      # one .slide per section (authored right-pane title + bullets)
  manifest.json  # wires sections → notebook / slide / scene / highlight / focus / audio
  scripts/     # (later) colab_generate_audio.ipynb (.tts -> .wav)
  CLAUDE.md · README.md
```

Naming: every artifact for a section shares the stem `<NN>-<SS>-<slug>`, where `NN` =
module number, `SS` = section position (so a sorted glob stays in reading order):
`notebooks/<NN>-<SS>-<slug>.ipynb`, `tts/…​.tts` → `audio/…​.wav`, `slides/…​.slide`.

The `.slide` format is a one-screen, scannable Markdown subset — **not** just title +
bullets: a `# Title`, then `## ` sub-labels, short paragraphs, fenced ` ```code``` `
blocks, and numbered / `- ` lists, each key term marked with inline **`**bold**`**
(rendered bright white, the rest a softer gray). **Keep the whole slide inside the fixed
1920×1080 frame:** the app's right pane does not scroll or auto-shrink type, so an
over-long slide clips top and bottom — trim it to fit (drop connective prose the narration
already carries) rather than expecting the engine to resize. Title may be punchier than
the notebook `## ` heading. First line is a single `#` title; `##` for sub-labels
(never `##` on line 1).

## Audio

The `.tts` scripts are **re-authored fresh** for the video target — never reuse a
graphl-ux-era `.wav`. `audio/` stays empty until the **owner** generates the `.wav`s from
`tts/` via Colab (`scripts/colab_generate_audio.ipynb`, added later); the manifest `audio`
fields are wired back in after generation. The `../kubernetes-content/CLAUDE.md` "TTS
Guidelines" still apply — write plain spoken prose, no code, no markdown; spell out
symbols and component names (`kubectl` shorthand, `etcd` → "et-see-dee", `kubelet` →
"kube-let", `-n` → "namespace flag", RBAC → "are-back", PV/PVC → "persistent volume" /
"persistent volume claim", CRI/CNI/CSI → "container runtime / network / storage
interface", etc.).

## Curriculum

The course outline (module spine + per-module sections) lives in [`README.md`](./README.md)
— the single human-facing source for structure while we plan; `manifest.json` becomes the
machine source of truth once authored. Don't duplicate the module/section list here.

**Starting point:** the 10-module beginner-to-CKA Kubernetes curriculum in
`../kubernetes-content` (source of truth for the split). The reader has finished the
`docker` concept — knows containers, images, volumes, the docker CLI, a Linux shell — but
has never touched Kubernetes. The video set keeps the 10-module spine, each normalized to
~10 tight teaching sections.

## Status

**Scaffolded + section spine settled** (10 modules × 10 = 100 sections in `README.md`,
each mapped to a real `k8s-*` scene node). Nothing authored yet (`notebooks/`, `tts/`,
`slides/` empty; `audio/` empty pending the owner's Colab run); scene not yet ported into
graphl-movie; nothing pushed. **Next:** port `../graphl-ux/src/scenes/kubernetes.ts` into
`../graphl-movie/src/scenes/kubernetes.ts` (register in `scenes/index.ts`, add the
`kubernetes` concept to `content/catalog.ts` → this repo's raw-GitHub URL, `npm run build`
green), then split section notebooks from `../kubernetes-content` and author each module's
`.ipynb`/`.slide`/`.tts` under review, wiring them in `manifest.json`.
