---
name: "{{Brand or project name}}"
category: "{{Appropriate project category}}"
surface: "{{Confirmed surface or medium; do not assume web}}"
colors:
  background: null
  surface: null
  foreground: null
  muted: null
  border: null
  accent: null
  accent-secondary: null
---

# {{Brand or project name}}

> Category: {{Category matching the frontmatter}}

> Surface: {{Surface matching the frontmatter}}

*{{Confirmed guiding message or identified proposal; omit if absent.}}*

{{Brief contextual description. Document status: draft/proposal or approved.
Link BRAND_IDENTITY.md if present. Null tokens indicate pending decisions; replace
with approved values and reflect them in the table as well.}}

## Color Palette

| Role | Name | Hex | Usage |
| --- | --- | --- | --- |
| background | {{Name}} | {{Approved hex or To be decided}} | {{Usage or Not applicable}} |
| surface | {{Name}} | {{Approved hex or To be decided}} | {{Usage or Not applicable}} |
| foreground | {{Name}} | {{Approved hex or To be decided}} | {{Usage or Not applicable}} |
| muted | {{Name}} | {{Approved hex or To be decided}} | {{Usage or Not applicable}} |
| border | {{Name}} | {{Approved hex or To be decided}} | {{Usage or Not applicable}} |
| accent | {{Name}} | {{Approved hex or To be decided}} | {{Usage or Not applicable}} |
| accent-secondary | {{Name}} | {{Approved hex or To be decided}} | {{Usage or Not applicable}} |
| success | {{Name}} | {{Approved hex or To be decided}} | {{Usage or Not applicable}} |
| warning | {{Name}} | {{Approved hex or To be decided}} | {{Usage or Not applicable}} |

{{Adapt roles to the surfaces. If success/warning are used as tokens, add them to
the colors map. Do not claim measured contrast results without evidence; follow
the WCAG AA section below.}}

### Accessibility: WCAG AA contrast

**Mandatory requirement for CTA buttons:** every call-to-action button (primary,
secondary or any other CTA variant) must meet WCAG 2.x level AA in all of its
interactive states (default, hover, focus, active/pressed):

- **Label text vs. CTA background:** at least 4.5:1 (SC 1.4.3); 3:1 only if the
  label is large text (≥ 24 px regular or ≥ 18.66 px bold, or the surface
  equivalent).
- **CTA boundary vs. adjacent background:** at least 3:1 when the button's shape
  is conveyed by its fill or border (SC 1.4.11).
- **Focus indicator:** visible and at least 3:1 against adjacent colors (SC 1.4.11).
- A CTA color combination that fails AA must not be approved or used; it stays
  marked as a pending decision until a compliant alternative is approved.

**Proactive palette evaluation (instruction for the AI agent):** as soon as the
palette is defined or any color changes, and before marking it as approved, the
agent must, without waiting to be asked:

1. Calculate the WCAG contrast ratio of every relevant pair: `foreground` and
   `muted` on `background` and `surface`; CTA label on `accent` and
   `accent-secondary` (and on each state color); `accent`/`accent-secondary`
   against `background`/`surface` for non-text UI; `border` when it is the only
   indicator of a component; `success`/`warning` with the text they carry.
2. Record the results in the table below with the measured ratio, the required
   threshold and the outcome (passes AA / fails AA). Report only computed values;
   never estimate.
3. Present a general WCAG AA compliance summary to the user, highlighting every
   failure (CTA failures first) and proposing concrete remediation options for
   each one (e.g. darken/lighten a tone with its new hex and ratio, change the
   label color, restrict the pair to large text or decorative use, add a border).
4. Ask the user explicitly which actions to approve or take for each finding
   (apply the proposed fix, choose another alternative, accept a documented
   exception for non-CTA usage, or keep it pending). Do not change approved colors
   or mark the palette as approved without that confirmation. CTA failures cannot
   be accepted as exceptions.
5. Update the palette, the `colors` frontmatter and this table with the approved
   decisions, and repeat the evaluation if any color changes.

| Pair (foreground / background) | Usage | Ratio | Required AA | Result | Approved action |
| --- | --- | --- | --- | --- | --- |
| {{e.g. CTA label / accent}} | {{Primary CTA}} | {{Computed ratio or Pending}} | {{4.5:1 / 3:1}} | {{Passes AA / Fails AA / Pending}} | {{Decision confirmed by the user or Pending}} |
| {{e.g. foreground / background}} | {{Body text}} | {{Computed ratio or Pending}} | {{4.5:1}} | {{Passes AA / Fails AA / Pending}} | {{Decision confirmed by the user or Pending}} |

## Typography

- **Display:** {{Approved family, weights/fallbacks or pending decisions.}}
- **Body:** {{Approved family, weights/fallbacks or pending decisions.}}

## Voice & Tone

- **Adjectives:** {{Confirmed brand traits.}}
- **Tone:** {{Operational rule and contextual adaptation.}}

### Messaging pillars

{{Key messages consistent with BRAND_IDENTITY.md if present; mark proposals.}}

### Vocabulary

- **Use:** {{Recommended vocabulary.}}
- **Avoid:** {{Expressions to avoid.}}

## Imagery

- **Style:** {{Visual style/criteria; do not impose an aesthetic.}}
- **Subjects:** {{Relevant subjects without invented people or existing assets.}}
- **Treatment:** {{Art direction and treatment.}}
- **Avoid:** {{Agreed exclusions.}}

## Layout

- **Radius:** {{Value/unit or To be decided/Not applicable.}}
- **Border weight:** {{Value/unit or To be decided/Not applicable.}}
- **Spacing:** {{System/units for the surface or To be decided.}}

### Posture rules

{{Density, hierarchy, composition and behavior for the chosen surfaces. Do not
assume cards, glassmorphism, dark mode or animations. State pending decisions and
how to validate them.}}
