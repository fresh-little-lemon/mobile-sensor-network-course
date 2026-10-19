# Part 4 source map and editorial decisions

## Scope and deliverables

- Text: `part4.tex`, 3 article-level sections, course progression from 2026-10-14 through 2026-10-16
- Original TikZ diagrams: hidden-node topology, D2D spatial reuse, alternative routes, sensor architecture, LEACH slots, superframe, outer MAC flow, slotted variable evolution, supplemental asynchronous worked-example timeline
- Local readonly sources only; no remote document writes, repository operations, or changes to original bilingual/audit data
- Body is textbook Chinese prose. First substantive English technical term given beside Chinese. Equations added to unpack taught relationships; illustrative derivations are distinguished from classroom numerical problems

## Canonical source locations

Each recording is backed by its corresponding local directory:

1. `/workspace/shared/course-1014-0801/bilingual-20261014-0801.md`
2. `/workspace/shared/course-1014-1000/bilingual-20261014-1000.md`
3. `/workspace/shared/course-1015-0803/bilingual-20261015-0803.md`
4. `/workspace/shared/course-1015-1000/bilingual-20261015-1000.md`
5. `/workspace/shared/course-1016-0805/bilingual-20261016-0805.md`

For each, inspected `titles.txt`, bilingual passages and `audit-readonly/slide-alignment-audit.md`; figures are anchored by that audit and the accompanying `slide-alignment-manifest.json`. Used actual local slide images for critical flow-chart branch conventions: Oct 16 `slide-040.png`, `slide-041.png`, `slide-048.png`, `slide-051.png`.

Fixed source deck revision recorded by existing audits:
`b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8`

- https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/02-WiFi_1-7.pdf
- https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/03-D2D-Networks.pdf
- https://huggingface.co/datasets/freshlittlelemon/mobile-sensor-network-course/blob/b89315ff4995ed67ca2fd6f5e6b682ff53afa5a8/04-Sensors-MAC.pdf

These links are source provenance from the supplied archives, not a claim of new live web verification.

## Section-to-source mapping

### From hidden nodes to D2D

- Different packet lengths, A hears B tail, EIFS, C competes first: Oct14-0801 P06–14; revisited Oct16 P74–83
- Exercise 3 hidden A/B, AP and C can hear all, two queued B packets, post-backoff and ordering constraint: Oct14-0801 P15–22, P24–33, P37–50
- Exercise 3 normalized solution b=13+r, r in 1..4, hence 14..17; C residual5 from original7 and already counted2: Oct14-0801 P39–50, especially P44/P46–48
- Exercise 4 setup: Oct14-0801 P52–59; resolution: Oct15-0803 P01–13. Normalized b=16+r, exclude b16 and b21, allow 17..20 and 22..31 under stated example cap
- D2D transition: Oct14-0801 P60–62; Oct14-1000 P17–24; D2D figures3–6
- Cellular assistance, content dissemination, short-range low-power spatial reuse, channel/user capacity analogy: Oct14-1000 P25–46; source audit explicitly identifies classroom drawing not available as fixed deck slide; book drawing is new conceptual artwork
- Heterogeneous capability and responsibility: Oct14-1000 P47–49; D2D fig7
- Unicast/broadcast/multicast/geocast/anycast, rate/delay/reliability: Oct14-1000 P50–53; D2D fig8
- Mobility patterns: Oct14-1000 P57–59; D2D fig9
- Neighbor/radio range/interference range/half-duplex: Oct14-1000 P60–64; D2D fig10–11
- Time-varying graph, obstacles/failure, flat/mesh/tree/cluster, edge counts/reliability/bridges: Oct14-1000 P65–78; D2D fig12–17
- Channel access, hidden nodes, multihop, relay, paths, network-layer routing: Oct14-1000 P79–92; D2D fig18–19 and repeated fig15
- Multihop tradeoffs source energy/interference/reuse versus load/delay/global energy: Oct14-1000 P93–99; D2D fig20
- Cooperation/incentives and willing-relay assumption: Oct15-0803 P15–21; D2D fig21
- Layering and A–C / A–B–C / A–D–E–C alternatives, fallback route: Oct15-0803 P22–31; D2D fig22
- Battery, size, longevity, sustainability: Oct15-0803 P34–41; D2D fig23
- Sleeping/power control/path-loss alpha/connectivity/deep sleep: Oct15-0803 P42–58; D2D fig24–28 and fig30
- Distributed versus centralized/autonomous networks: Oct15-0803 P59–60; D2D fig29
- Technology/BAN/sensor bridge: Oct15-0803 P61–64; D2D fig31,34,32 (actual teaching order), Sensors fig1

### Sensor networks and MAC

- Remote sensing, forest alarms, sink, low power/rate: Oct15-0803 P65–69; Sensors fig2
- Sensing board, processing, space/time sampling: Oct15-0803 P70–71; Oct15-1000 P02–03; Sensors fig3
- Wireless media RF/IR/optical, LOS, Smart Dust, approximate RF range/rate/power: Oct15-1000 P04–10; Sensors fig4–5
- Data preprocessing, sink uplink, addressing overhead, sync/localization: Oct15-1000 P11–15; Sensors fig6
- Environmental, structural, animal, grid, water/soil uses: Oct15-1000 P16–23; Sensors fig7–9
- Commercial modular sensors / Waspmote / sleep modes and boards: Oct15-1000 P24–27; Sensors fig10. No current product specification asserted
- Reference multihop sink scenario, asymmetric upstream/downstream: Oct15-1000 P28–31; Sensors fig11
- PHY/MAC/network/high layers, topology changes from sleep, cache/query/aggregation: Oct15-1000 P32–36; Sensors fig12
- MAC priorities, distributed decisions/collisions, utilization/delay/throughput/fairness: Oct15-1000 P40–48; Sensors fig13–15
- Radio state energy, idle listening/collision/overhead/overhearing: Oct15-1000 P48–52; Sensors fig16–17
- Schedule/contend classification: Oct15-1000 P52–53; Sensors fig18–19
- LEACH cluster TDMA, intercluster CDMA conceptual treatment, CH rotation, new-node schedule and code scarcity: Oct15-1000 P54–71; Sensors fig20. Source audit notes two classroom visuals missing; our slot drawing is explicitly new, not restored footage
- 802.15.4/Zigbee separation: Oct15-1000 P72–74; Sensors fig21–23
- FFD/RFD, coordinator, star/peer-to-peer/cluster-tree: Oct15-1000 P75–82; Sensors fig24–28

### 802.15.4 beacon and access procedures

- Bandwidth/rates and packet size, no demand to memorize modulation: Oct16-0805 P01–04; Sensors fig31–33
- Coordinator beacon, sync, superframe CAP/CFP, global/individual sleep, buffering: Oct16 P05–12; Sensors fig34–38
- Outer first, ACK and retry/drop: Oct16 P13–19; Sensors fig40 before fig39 (actual teaching order)
- NB/CW/BE, boundaries, random draw, continuous countdown, two clear assessments, busy reset and limits: Oct16 P20–28; Sensors fig39,41,42
- Distinct retries, NB reset on re-entry: Oct16 P29–30; Sensors fig44
- Half-duplex DATA/SIFS/ACK/SIFS: Oct16 P33–39; Sensors fig43. Exact 192us classroom example P38 at 00:38:58
- Nonbeacon mode, unchanged outer, distinct discard causes: Oct16 P40–41; Sensors fig45,47,52
- Unslotted variables and inner, no boundary alignment, continuous backoff, CCA, busy retry and double turnaround: Oct16 P42–45; Sensors fig46,48–51
- General CSMA/CA versus DCF implementation: Oct16 P50–61
- NAV vs freeze vs defer, PHY/NAV OR condition, cases triggering contention: Oct16 P62–73; Wi-Fi recovered fig36 and45
- EIFS two collision cases, new valid frame restores normal handling, DIFS and EIFS relationship: Oct16 P74–86
- RTS length threshold, not a hidden-node detection switch: Oct16 P87

## Explicit numerical/editorial boundaries

1. Exercise 3 original time of C arrival conflicts (0.35 vs0.55ms), and one spoken count says15 instead of repeated13. Do not silently reconstruct a unique absolute timeline. Text uses the repeatedly supported normalized relation b=13+r and final14–17, with concise endnote. It preserves actual logic instead of printing uncertain arrivals.
2. Exercise 4 ACK unit is ambiguous in transcript; introductory A offset is clearer in Oct14 setup. Text does not manufacture a complete microsecond problem statement from this. Uses established normalized16+residual and answers, identifies31 as problem cap.
3. Lecture says hearing ACK sets NAV in some places. Text relies on physical sensing to freeze, without claiming ordinary ACK necessarily sets a positive NAV. Original can remain as provenance, not propagated as a universal rule.
4. 127 bytes is correctly identified as PHY PSDU / MAC-frame size, not application payload; source's broad 'payload127' terminology is tightened by explicitly naming layers. Six bytes refers to preamble+SFD+PHR of discussed classic format.
5. FFD does not mean IEEE MAC itself implements complete network routing; clarify higher-layer routing when describing capability and Zigbee.
6. Source states (and diagrams) DATA-SIFS-ACK-SIFS with192us example. Body explicitly calls this classroom simplified half-duplex model, not universal normative IFS rules. Supplemental numerical use retains192us while all other chosen timing values are explicitly pedagogical.
7. Flowcharts use NB<macMaxCSMABackoff and NF<macMaxFrameRetry. To avoid off-by-one confusion or silently substituting another standard convention, body explains budget convention; supplemental example defines NB<3 and NF<2 exactly and does not call these default standard parameters.
8. Spain blackout discussion not used to assert historical causation; only the taught sensing/control motivation retained. Source audit itself says it does not certify cause.
9. Flat topology maximumN(N−1)/2 applies to complete simple undirected graph, not every flat topology. TreeN−1 requires connected and acyclic.
10. Schedule/TDMA, layered energy and spatial reuse equations are pedagogical unpacking of directly taught relationships, not a newly claimed lecture formula. Added relations: rho delivered/generated; lifetimeE/P; address efficiencyL/(L+H); state-energy sumPt; sample field notation; TDMA report1/(NTs); simple exchange-time sum.
11. Supplemental unslotted worked example is newly authored and labelled so. Parameters: BP100us, CCA20us, DATA200us, ACK40us, BEmin2/max3, classroom SIFS192us, ACK timeout500us after DATA end. Busy CCA200–220; next idle CCA520–540; failed DATA540–740; timeout1240; NB+BE reset; next idle CCA1340–1360; successful DATA1360–1560; ACK1752–1792; receive-ready1984. Distinct branches show all-busy access failure and NF-budget exhaustion.
12. Added original drawings do not claim to restore missing classroom drawings. Captioned as conceptual, not scale-accurate, where appropriate.

## Omissions deliberately outside substantive teaching

Removed break chatter, unrelated meals/travel/personal invitations, equipment troubleshooting, pauses, and repeated acknowledgments. Exam procedure content is delegated to the parent handbook's front matter and exam-priority material rather than duplicated here. No invented sensor routing algorithms added: the available later lectures introduce routing roles but do not teach AODV, DSR, Dijkstra, or a dedicated sensor routing algorithm in this segment. LEACH not expanded into unprovided election-probability derivations.

## Exam emphasis provenance for parent

Independent auditor reports fixed `Exam_Information.pdf`: sensor ASYNCHRONOUS channel-access numerical30points, Wi-Fi30points, two open questions20each. Parent owns source verification and exam frontmatter. This evidence motivated expanding asynchronous treatment beyond the proportion of its short lecture recap. Oct16 P02 at00:00:48 directly says not to memorize modulation slide; packet sizing is interesting/important. All major actually taught D2D/WSN topics remain in body despite numerical priorities.

## Validation

Standalone XeLaTeX build completed: 14 pages with parent-recommended fontspec preamble and TikZ. Cross-references resolved on second pass. One long bilingual paragraph overflow was fixed by separating schedule-based and contention-based definitions. Parent performs final integrated rendering. Auditor verified asynchronous arithmetic/state resets; hidden examples explicitly identify13/16 as supplied intermediate counts rather than pretending to recover complete ambiguous absolute-time problem statements.
