# Part 1 source map and editorial boundaries

## Primary local sources
- `course-0800/bilingual-20261008-0800.md`, 2026-10-08 08:00 recording
- `course-0910/bilingual-20261008-0910.md`, 2026-10-08 09:10 recording
- `course-1008-1000/bilingual-20261008-1000.md`, 2026-10-08 10:00 recording
- `course-1008-1049/bilingual-20261008-1049.md`, 2026-10-08 10:49 recording
- `course-1009-0759-github-update/bilingual-20261009-0759.md`, 2026-10-09 07:59 recording
- `001-BasicConcepts.pdf`: 27 PDF sheets, each normally containing two slides. Below, “figure N” means ordered slide image N, not PDF sheet number or reset within-section footer numbering.
- `course-0800/01_Introduction_MSN_26-27.pdf`, contextual network introduction; transcript identifies embedded slide associations.

## Mapping
1. **From networks to one link**: Oct08 08:00 20:53–28:39 applications/requirements; 29:27–35:22 hosts/AP/BS/link/interfaces; 35:54–43:47 coverage/infrastructure/ad hoc; 45:36–52:47 nomadic mobility/handover; 52:47–01:03:28 hybrid/mesh/gateway. Administrative remarks and personal biographies omitted as nontechnical course framing.
2. **Bits, modulation and spectrum**: Oct08 09:10 03:39–18:09, BasicConcepts ordered figures 3–8 (PDF sheets 2–4), including duplicated figures 3/5 and 4/6. Carrier/baseband distinction follows 09:50–11:35. The distinction between frequency location and bandwidth is an explanatory bridge for later N0B/Wi-Fi material; 2.400–2.420 GHz is expressly a newly constructed arithmetic example, not an actual specified Wi-Fi channel.
3. **Symbols, constellation and QAM**: Oct08 09:10 19:00–22:41; Oct08 10:00 00:00–10:20; BasicConcepts figures 7–8. log2(M), symbol rate, illustrative 1 Msymbol/s examples expand the stated per-symbol bit relationship without introducing a new modulation family.
4. **Antenna/frequency/capacity**: Oct08 10:00 11:22–32:42; BasicConcepts figures 9–14 (PDF sheets 5–7). Capacity KLU is the lecture's base-station reuse reasoning written with explicit idealization, not a guarantee.
5. **Power, energy, dB/dBm, free space**: Oct08 10:00 32:42–40:28; BasicConcepts figures 16–21 (PDF sheets 8–11). Added explicit far-field, polarization, fixed-gain conditions so f² claim is not misapplied. Numerical wavelength and power examples are author-created illustrations.
6. **Atmosphere, horizon and obstacles**: Oct08 10:00 40:28–44:52; BasicConcepts figures 22–28. Radio-horizon formula visually verified in `course-1008-1000/slide-images/slide-025.png`: d_max=sqrt(2 K R_T h), R_T=6370 km. Simplified slide climate-specific K values not promoted into universal constants; explain K, units, small-height approximation and single-terminal horizon instead.
7. **Multipath/fading/SNR/SINR**: Oct08 10:49 01:10–23:58; BasicConcepts figures 27–41 (PDF sheets 14–21). Phase difference translated dimensionally correctly as 2pi Delta d/lambda, with possible reflection phase explicitly excluded from that path-only expression. N0B convention follows slide. SINR 100/(9+1) example is author-created.
8. **FEC/coding/parity**: Oct08 10:49 23:58–41:48; BasicConcepts figures 43–49 (PDF sheets 22–25). Repetition and matrix examples newly constructed. Single parity odd/even limitations reflect actual slide. The two-dimensional example explicitly assumes one information-bit error and correct check bits; no unsupported universal multiple-error correction claim. Convolutional codes confined to lecture register overview.
9. **Packets/CRC/stop-and-wait**: Oct08 10:49 41:48–46:34; Oct09 07:59 06:05–25:37; BasicConcepts figures 51–54 (PDF sheets 26–27). CRC in header and error-free header are explicitly classroom assumptions. “CRC equal ⇒ correct” refined to “check passed” because undetected errors exist. No CRC polynomial computations, ARQ efficiency derivation, Go-back-N or selective-repeat exposition. Sequence numbers are on figure 53; ACK-loss/duplicate motivation is a short explanatory clarification rather than an assertion that the lecturer fully developed it.
10. **Transition to MAC**: Oct09 07:59 26:28–44:46, introduction to IEEE 802.11, PHY/MAC split and application→stack→radio flow. Full Wi-Fi architecture/DCF details remain for part2.

## Original material and dependencies
- All six diagrams are newly drawn conceptual TikZ figures: network paths, radio processing chain, spectrum interval, 16QAM decisions, multipath, stop-and-wait (six figures total; network figure contains two panels). No slide screenshots embedded and no large verbatim passages copied.
- TikZ requires `decorations.pathreplacing` for the ARQ waiting brace; standard arrows/coordinates otherwise.
- Technical terms are bilingual on first relevant occurrence. All mathematical variables explained near their expressions. Examples are conceptual supplementary arithmetic; not labeled original examination questions.

## Examination emphasis
No specific physical-layer formula is claimed to be a promised examination question. The 07:59 lecture explicitly de-emphasizes memorizing all IEEE 802.11 letter designations; master exam introduction can summarize that verified statement. Complete taught coverage retained even where not explicitly prioritized for examination.

## Verification and remaining uncertainty
- Independent chapter audit reported no blocking technical issue; additions for reliability, coverage scale, nomadic mobility, atmosphere/horizon completed.
- Root confirmed successful compilation of part1 via project runtime. Full-page rendering and final cross-part terminology/pagination QA belong to the master build.
- The original lecture is introductory and sometimes colloquial. Explicit assumptions and limited technical clarifications are editorial explanations, not additional claimed lecture quotations.
