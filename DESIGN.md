---
name: Palo Santo
description: Berlin-based band rooted in the music of Colombia's Caribbean coast.
colors:
  tambora-purple: "#a55ff5"
  tambora-purple-deep: "#8a40e0"
  palenque-red: "#EB3527"
  bone: "#f5f2f0"
  bone-warm: "#e8e4df"
  night: "#0a0809"
  night-raised: "#110e10"
  night-violet: "#16121a"
  panel: "#130f17"
typography:
  display:
    fontFamily: "SUSE, sans-serif"
    fontSize: "clamp(2.4rem, 6vw, 4rem)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0.08em"
  headline:
    fontFamily: "SUSE, sans-serif"
    fontSize: "clamp(1.3rem, 2.2vw, 1.9rem)"
    fontWeight: 700
    letterSpacing: "0.18em"
  title:
    fontFamily: "SUSE, sans-serif"
    fontSize: "1rem"
    fontWeight: 700
  body:
    fontFamily: "SUSE, sans-serif"
    fontSize: "clamp(1.05rem, 1.8vw, 1.35rem)"
    fontWeight: 300
    lineHeight: 2
  label:
    fontFamily: "SUSE, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    letterSpacing: "0.22em"
rounded:
  sm: "8px"
  md: "16px"
  pill: "999px"
spacing:
  gutter-mobile: "20px"
  gutter-desktop: "64px"
  section-mobile: "60px"
  section-desktop: "100px"
components:
  button-primary:
    backgroundColor: "{colors.tambora-purple-deep}"
    textColor: "{colors.bone}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "13px 36px"
  button-primary-hover:
    backgroundColor: "transparent"
    textColor: "{colors.tambora-purple}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.bone}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "13px 36px"
  button-outline-hover:
    textColor: "{colors.palenque-red}"
  chip:
    textColor: "{colors.tambora-purple}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "6px 16px"
  card:
    backgroundColor: "{colors.panel}"
    rounded: "{rounded.md}"
---

# Design System: Palo Santo

## Overview

**Creative North Star: "The Tambora at Night"**

Palo Santo's site feels like a show after dark in a Berlin club: a near-black room, a hand-drawn wallpaper of drums, maracas, gaitas and caimanes, and two loud colours cutting through it. The red and purple come straight from the band's lettering logo, and they do the shouting so the rest of the page can stay calm.

The pages are made for reading and listening. Text sits in one narrow, centred column, section titles are spaced-out capitals, and photos are shown big. Motion is gentle: things fade up as you scroll, and nothing should move just for show.

**Key Characteristics:**
- Dark, warm-black background with the illustrated pattern (`assets/asset-3cb5addc.svg`) showing through
- Two brand accents only: tambora purple and palenque red, taken from the logo
- One typeface (SUSE) across the whole system, light body text with heavy, tracked headings
- Pill-shaped controls and softly rounded cards
- Bilingual (EN/ES) on every page, switched in place with `data-i18n` keys

## Colors

A night palette: warm blacks, a bone white for text, and two saturated accents used sparingly.

### Primary
- **Tambora Purple** (#a55ff5): links, section accents, dates, chips, active nav item, focus states. It is also the purple in the logo.
- **Tambora Purple Deep** (#8a40e0): fill colour for solid buttons (Listen Now, Pre-Save, Get in Touch). It is darker than Tambora Purple so white text on it reaches 4.8:1 contrast.

### Secondary
- **Palenque Red** (#EB3527): small labels (contact labels, EP status) and the hover colour of outline buttons. It is the red of the logo.

### Neutral
- **Bone** (#f5f2f0): main text and headings.
- **Bone Warm** (#e8e4df): secondary light tone.
- **Night** (#0a0809): page background.
- **Night Raised** (#110e10): alternating section background (About, Concerts).
- **Night Violet** (#16121a): violet-tinted surface on the Our Rhythms page.
- **Panel** (#130f17): cards and photo placeholders.

### Named Rules
**The Logo Owns the Colour Rule.** Purple and red come from the logo and stay the only accents. Don't add new hues: no blue, no green, no gradients between the two.

**The Readable Fade Rule.** Secondary text is Bone at reduced alpha, never below `rgba(245,242,240,.6)` on Night. Faint text that falls under 4.5:1 is a bug, not a mood.

## Typography

**Display Font:** SUSE (with sans-serif), weights 200–700 from Google Fonts
**Body Font:** SUSE
**Label Font:** SUSE

**Character:** One family carries everything. Light 300 body text reads soft and open; 700 headings in wide-tracked capitals give the stage-sign feel.

### Hierarchy
- **Display** (700, clamp(2.4rem, 6vw, 4rem), 1.1): page titles such as "Our Rhythms". On the home page the logo takes this role and a visually hidden `<h1>` carries the text.
- **Headline** (700, clamp(1.3rem, 2.2vw, 1.9rem), uppercase, 0.18em tracking): section titles (About, Music, Recent Concerts, Contact).
- **Title** (700, 1rem): concert names, card titles.
- **Body** (300, clamp(1.05rem, 1.8vw, 1.35rem), line-height 2): long-form copy, max about 760px wide, justified.
- **Label** (600, 0.75rem, 0.18–0.22em tracking, uppercase): buttons, nav, chips, dates.

### Named Rules
**The 11px Floor Rule.** No text that people need to read goes below 0.75rem (12px). Small labels earn their legibility through weight and tracking, not by shrinking.

## Layout

A single centred column. Content sections use `.sw` (max-width 860px, padding 100px 64px on desktop, 60px 20px on mobile). The hero is full-viewport (`100svh`) with the logo and two CTAs centred over a muted video loop. The breakpoint is 768px. Below it, the CTAs stack, the concert grid collapses to date and info, and the navigation moves into the menu button.

## Elevation & Depth

Mostly flat. Depth comes from tone (Night → Night Raised → Panel) and from the pattern showing behind sections. Shadows are only for things that really float: the lightbox, the concert flyer preview, and lifted photo/EP cards.

### Shadow Vocabulary
- **Lift** (`box-shadow: 0 24px 60px -12px rgba(0,0,0,.7)`): the featured EP card, gallery photos on hover.
- **Overlay** (`box-shadow: 0 16px 48px rgba(0,0,0,.7)`): floating previews (concert flyer thumbnail).

### Named Rules
**The No-Glow Rule.** No coloured glows or neon halos. Lift with dark, neutral shadows.

## Shapes

Pills for anything you press or tag (buttons, chips, language toggle, social icons). Cards and photos use 16px radius, thumbnails 8px. Borders are 1px in low-alpha purple (`rgba(165,95,245,.2)`). The hero frame uses thin corner brackets, purple top-left and red bottom-right.

## Components

- **Buttons:** pill, uppercase label type. Primary is solid Tambora Purple Deep and turns transparent with purple text on hover. Outline has a bone border at 30% and turns red on hover. Hover effects only apply on devices that can hover (`@media (hover:hover)`).
- **Navigation:** fixed top bar, always visible. On desktop the links sit in a row next to the ES/EN toggle. On mobile a menu button opens a full-width list with 44px+ tap targets. Escape or tapping a link closes it.
- **Concert list:** grid of big purple day number, month and year label, name and venue, type chip, and flyer thumbnail.
- **Chips:** purple text, purple 20% border, pill.
- **Gallery marquee:** an endless horizontal strip of photos that opens a lightbox. It stops when reduced motion is requested.

## Do's and Don'ts

**Do**
- Keep the two logo colours as the only accents.
- Write every visible string in both EN and ES (`data-i18n` key plus both dictionaries).
- Give every `<img>` its `width`/`height` and `alt`; compress photos to 2000px max, WebP.
- Put any "hidden until revealed" state behind motion that `prefers-reduced-motion` turns off.
- Use punctuation (full stop, comma, colon) instead of em dashes in copy.

**Don't**
- Don't add coloured glows, gradients between brand colours, or new accent hues.
- Don't set readable text below 0.75rem or below 4.5:1 contrast.
- Don't hide navigation until scroll.
- Don't put white text on the light Tambora Purple (#a55ff5); use the Deep variant for fills.
