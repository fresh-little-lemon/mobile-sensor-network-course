# Part 3 source map

Scope: PCF, 802.11e QoS/EDCA/HCCA, 802.11n PHY motivation and aggregation, Oct13 DCF exercises. Original narrative and TikZ diagrams; no screenshots copied as if originals. Local bilingual records and their audit-readonly slide evidence read. User later supplied/parent located actual Exercise 1 screenshot, which supersedes oral numeric conflict.

## Source coverage
- 20261012-1530 bilingual §§18–44, 00:15:23–00:44:31: PCF/DCF coexistence, polling, piggyback ACK, null response, TBTT/PIFS, static list and beacon delay. Fixed `02-WiFi_1-7.pdf` actual PDF pp29–30, original slide IDs57–60; IFS pp17 and EIFS pp27–28 used as connective background only.
- 20261012-1620 §§2–8, 00:01:12–00:06:44: unknown transmission duration completes PCF limitations. PDF p30 lower and p31 upper, slides60–61.
- Same record §§9–17, 00:07:04–00:14:15: QoS/HCF and TXOP. PDF pp31–33, slides62–65; burst slide74 p37 lower shown early but details taught next day.
- Same §§18–50, 00:14:59–00:43:51: four queues, applications, AIFS/CW, TXOP limit, QoS Control. PDF pp33–37, slides66–74. Internal collision is a supporting slide detail (72), not claimed as a separately spoken lecture passage.
- 20261013-0803 §§1–3, 00:00:02–00:01:54: BAR/Block ACK bitmap and overhead. PDF p38–39 upper, slides75–77.
- Same §§4–22 and 34–46, 00:03:39–00:25:42 and 00:49:23–01:02:16: per-packet vs temporal fairness. Actual PDF pp39 lower/40 upper, slides78–79, lectured in reverse visual order. Explicit exam possibility at §44 01:01:14 included prominently, without guaranteeing exam content.
- Same §§23–32 and47–50, 00:28:37–00:41:45 and01:03:51–01:10:16: HCCA, queue state, controlled time, CP/CAP, traffic signaling and admission. PDF pp40–43 upper, original slides80–85 (printed labels offset after82; use actual physical PDF page).
- Same §§51–69, 01:11:16–01:31:40: PHY background beamforming, channel bonding, MCS/MIMO, rate meaning. PDF pp43–46, slides86–91. Extra PHY details described as awareness rather than memorization at01:11:16 and01:26:25.
- 20261013-1000 §§1–20, 00:00:20–00:24:57: rates, headers, time vs throughput, overhead. PDF p26 lower slide52 and p45 upper original slide89 (printed90). Worked11Mb/s numbers follow slide, not inconsistent verbal ACK-rate shortcuts.
- Same §§21–23, 00:25:49–00:30:58: two-level aggregation. PDF pp46 lower/47 lower/48 both halves, original slides92,94–96.
- Same §§24–37 and40–46, 00:33:14–00:48:20 /00:55:41–01:02:49: Exercise1 scenario and solution. Primary numeric source additionally inspected with view_image: `/workspace/scratch/0959da8a7ffd/390f79c514c4c477537fb8efd8be3e18.png`. Explicit values ACK140us, DIFS50us,SIFS10us,EIFS200us,slot20us,Tf150us,A10/B11,C arrival1.25ms; dataA/B1ms,C1.5ms. Full solution3.10ms A start and5.47ms completion derived in text. Parent also identifies solution screenshot6b0bfa57513f605ebc359ed8b6e14b52.png and existing network-exercise PDF; not needed to assert unseen image.
- Same §§48–64, 01:05:29–01:35:24: Exercise2 A/C1ms,B1.4ms,Tf150us,A19,C5; B13/30 conflict handled once in caption and explained using order consistency. C andA useEIFS;B starts ordinary retreat afterF+D;B has decremented11vsA5; chooseB30 yieldsremaining19vs14 andAthenB. Missing interval table retained symbolic, not invented.

## Editorial precision and limitations
- No verbatim transcript dumps, Q&A, private reasoning, or classroom breaks/personal administrative dialogue included.
- Correct naming: 802.11e is QoS amendment,802.11n isWi-Fi4; source's “Wi-Fi4 bundles e+n” not repeated as fact.
- HC architecture presented as AP-resident classroom/common case; no repeat of broad slide statement it can reside at arbitraryQSTA.
- QoS Control field interpretations qualified by frame context; avoids source assertion all subfields simultaneously encode same contents.
- Same-AC equality is statistical and assumes comparable contention, saturation, sufficient time; TXOP equality needs full use and neglect/effective accounting of overhead. Formula limits explained.
- PHY lowest rate6.5Mb/s not called a universal basic control or preamble rate. No claim2x2mandatory. No regional universal channel counts.
- A-MPDU conventional same receiver/traffic flow scope; does not repeat questionable multi-TID aggregation generalization in slide. No version-independent64MPDU/65535byte cap claim. Burst vs aggregation clearly separated.
- EIFS criterion is error reception, not every arbitrary instance of energy withzeroNAV; exercise assumes corrupt/no decodableheader as recorded. Successful reception resets normal behavior only under stated recovery logic.
- Exercise1 screenshots resolveTf=150us; caption notes primary image use, no lingering claim unavailable. Exercise2 remains uncertainty-limited.
- Added teaching derivations: mean uniform backoff, CW upper-bound convention, burst overhead difference, simplified admission necessary condition, PHY factorization, asymptotic throughput/efficiency, aggregation amortization and independent-bit error illustration. Clearly conditional mathematical models, not quoted standard mandates or claimed explicit lecture derivations.
