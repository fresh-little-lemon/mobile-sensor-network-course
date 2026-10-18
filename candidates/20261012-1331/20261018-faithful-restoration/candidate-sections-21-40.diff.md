# 21–40段忠实恢复候选差异审计

状态：candidate_not_audio_certified；仅本地候选，不代表已回写飞书或已人工听辨。

每段完整 before/after 均保存在 JSON 的 changes 中；下列为逐段具体来源理由及词级可读差异。

## 21 · 00:22:43

Restore the repeated questions Out of what? and So what it will do?, repeated channel-is-idle statement, future forms, right/oh/again, and underived pronoun uncertainty. Qwen 1320–1440 and medium chunk-008 preserve wording compressed in the current paragraph.

来源：Feishu historical snapshot mapped source_index_zero_based=24,25; source block(s) 53,55; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=12, absolute 1320.00–1440.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-008,chunk-009

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -4,10 +4,20 @@
 to
 do
 is
+to
 apply
 backoff.
-It
-waits
+So
+what
+[it
+will
+/
+you
+will,
+unclear]
+do
+is
+wait
 for
 the
 channel
@@ -15,39 +25,52 @@
 become
 idle
 again,
-senses
-it
-as
+sense
+the
+channel
 idle
 for
 DIFS,
 and
+then,
 if
 the
 channel
-stays
+is
 idle
 for
 DIFS,
 it
-can
+will
+be
+able
+to
 draw
 an
-integer
-out
+integer,
+right?
+Out
+of
+what?
+Out
 of
 the
 range
-zero
-to
+zero,
 CW_min.
-The
+And
+the
 same
-applies
-to
-C.
+C,
+right?
 C
-says:
+at
+this
+point
+in
+time
+says,
+oh,
 I
 got
 a
@@ -59,26 +82,40 @@
 channel
 is
 busy.
-It
+So
+again,
+it
 knows
+that
 it
 has
 to
 perform
+a
 backoff.
+So
+what
+it
+will
+do?
 It
-waits
+will
+wait
 for
 the
 channel
 to
 become
-idle
-and
-verifies
+idle.
+Then
+it
+needs
+to
+verify
 that
-it
-remains
+the
+channel
+is
 idle
 for
 DIFS.
@@ -92,4 +129,9 @@
 else
 is
 doing
-anything.
+anything,
+so
+the
+channel
+is
+idle.
```

- [it will / you will, unclear]: Qwen says it will; historical Feishu says you will; Whisper says you do. Pronoun and auxiliary remain unresolved.

## 22 · 00:24:00

Restore both lets-assume clauses, the apposition the value drawn by B, the integer, and okay. Mark the unstable it too / it will do restart instead of smoothing it to It too draws.

来源：Feishu historical snapshot mapped source_index_zero_based=26; source block(s) 57; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-008,chunk-009

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,28 +1,56 @@
-It
+[And
+it
 too
-draws
+will
+draw
+/
+And
+it
+will
+do,
+will
+draw,
+unclear]
 an
 integer
 with
 equal
 probability
-from
-the
+out
+of
+this
 same
 range
 of
-values.
-Let's
+values,
+okay?
+So
+let's
 assume
 that
-B
-draws
+the
+value
+drawn
+by
+B,
+the
+integer,
+is
+equal
+to
+two.
+And
+let's
+assume
+that
 the
 integer
-two
-and
+drawn
+by
 C
-draws
+is
+equal
+to
 five.
 This
 is
```

- [And it too will draw / And it will do, will draw, unclear]: Feishu has And if we two will draw; Qwen has And you will do will draw; Whisper has and it will do, will draw. The short restart or too is not resolved.

## 23 · 00:24:36

Restore will compute, will start sensing, and successive conjunctions; keep the it by, its own counter restart. The C-will-do-the-same / B-reaches-zero ending is supported by Qwen 1540–1660 and medium although missing from Feishu.

来源：Feishu historical snapshot mapped source_index_zero_based=27; source block(s) 59; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=13, absolute 1430.00–1550.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-009

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,44 +1,72 @@
-In
+Okay,
+so
+if
+this
+is
+the
+case,
+then
+we
+know
 that
-case,
 B
-computes
-a
+will
+compute
+its
 backoff
-time
+time,
+that
+will
+be
 equal
 to
-twice
+two
+times
 the
 time-slot
-duration.
-Similarly,
+duration,
+right?
+And
+similarly
 C
-computes
-a
+will
+compute
+its
 backoff
-time
-of
+time,
+that
+will
+be
 five
 time
 slots.
-Each
+And
+then
+each
 of
 them
-decreases
+will
+have
+to
+decrease
 its
 own
 backoff
-counter
+counter,
+time
 slot
 by
+time
 slot.
+So
 B
-senses
+will
+start
+sensing
 the
 channel
 for
-one
+a
 time
 slot.
 The
@@ -48,48 +76,64 @@
 idle,
 so
 it
-decreases
+will
+decrease
 its
+backoff
 counter
 by
 one.
-C
-does
+And
 the
-same,
-decreasing
+same
+will
+do
+C,
+right?
+So
+it
+will
+decrease
+it
+by,
 its
 own
 counter
 by
 one.
-In
-the
+Then,
 next
 time
 slot,
+again
 B
-again
 senses
 the
 channel
-as
-idle
-and
+[is
+/
+as,
+unclear]
+idle,
 decreases
 its
+backoff
 counter
 by
 one.
+And
 C
-does
+will
+do
 the
-same,
-but
+same.
+But
 now
-B's
+the
 backoff
 counter
+of
+B
 has
 reached
 zero.
```

- [is / as, unclear]: Historical Feishu and Qwen say is idle; Whisper says as idle.

## 24 · 00:26:12

Restore clearly, as we said, the network topology, network architecture restart, and will send back. Mark the extra and transmit that appears only in new medium rather than deciding silently.

来源：Feishu historical snapshot mapped source_index_zero_based=28; source block(s) 61; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-009,chunk-010

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,60 +1,79 @@
+So
 B
 is
 entitled
 to
 access
 the
-channel,
-so
+channel
+[and
+transmit,
+unclear].
+So
 it
-transmits
+will
+transmit
 its
 data
 packet.
 The
+data
 packet
+clearly
 is
 intended
 for
 the
 access
 point
-because
+because,
+as
+we
+said,
 we
 are
 considering
 unicast
-packets,
-and
+packets.
+And
 in
 this
 network
-architecture
+topology,
+network
+architecture,
 all
 Wi-Fi
 user
 nodes
 communicate
-only
 with
 the
 access
-point.
-Again,
-let's
+point
+only.
+Let's
+again
 be
-optimistic:
-the
+optimistic.
+So
+this
+means
+that
+this
 packet
 is
+received
 successfully
-received,
-and
+by
 the
 access
-point
-sends
+point,
+which
+will
+send
+back
 an
-acknowledgment
+acknowledgement
 after
 SIFS.
```

- [and transmit, unclear]: Whisper adds and transmit; historical Feishu and Qwen end this sentence at channel. Do not silently choose the longer or shorter version.

## 25 · 00:27:02

Restore Upon the data transmission by B, both A and also C, repeated So, will, right, and a source conflict around so thats not okay/okay. NAV is an explicit acronym spelling normalization, not a semantic paraphrase.

来源：Feishu historical snapshot mapped source_index_zero_based=29,30; source block(s) 63,65; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=14, absolute 1540.00–1660.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-009,chunk-010

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,10 +1,13 @@
 Upon
-B's
+the
 data
-transmission,
+transmission
+by
+B,
 the
 other
-nodes
+nodes,
+right,
 can
 set
 their
@@ -17,48 +20,71 @@
 field
 in
 the
+header
+of
+the
 data
-packet's
-header.
-We
+packet.
+So
+we
+need
 also
-need
 to
 highlight
+this,
 that
 both
 A
 and
+also
 C
+will
 set
 their
-NAV.
-What
+NAV,
+right?
+So
+what
 does
-this
+it
 mean
 for
 A?
-It's
-fine;
+This
+is
+okay,
+fine,
 it
 doesn't
 have
 anything
 to
-do.
+do,
+so
+that's
+[not
+okay
+/
+okay,
+unclear].
 But
 for
 C,
-it
+this
 means
 that
-it
-must
+[it
+/
+you,
+unclear]
+will
+have
+to
 freeze
 its
 backoff
 counter
 for
 this
-duration.
+duration,
+right?
```

- [not okay / okay, unclear]: Feishu and Whisper say not okay; Qwen says okay. The contradictory wording is not repaired for logic.
- [it / you, unclear]: Qwen says it will; Whisper says you will. Feishu truncates before the predicate. The following right is near the 28:03 boundary.

## 26 · 00:28:03

Restore Because now, Okay so, will be essentially blocked, what it does, It has still, and the repeated per-slot description. Leave the possibly unfinished for a... and pronoun/counter-count choices unresolved.

来源：Feishu historical snapshot mapped source_index_zero_based=31; source block(s) 67; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-010

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,30 +1,39 @@
-The
+Because
+now
+the
 channel
 is
-now
 busy,
 so
 C
 cannot
 decrease
 its
-counter;
+counter,
 it
 has
 to
 suspend
 the
 countdown.
-During
+Okay,
+so
+during
 all
 this
 time
 C
+will
+be
+essentially
+blocked,
+and
+what
+it
+does
 is
-essentially
-blocked
-and
-waits
+to
+wait
 for
 the
 channel
@@ -32,39 +41,61 @@
 become
 idle
 again.
-It
+[It
+/
+he,
+unclear]
 makes
 sure
+that
 the
 channel
 is
 idle
 for
 DIFS,
+and
 then
-resumes
+[it
+/
+he,
+unclear]
+can
+resume
 decreasing
 its
 backoff
-counter.
+[counter
+/
+count,
+unclear],
+[right,
+unclear]?
 It
+has
 still
-has
 three
 time
 slots
 to
-go.
-It
-senses
+go,
+so
+[it
+/
+he,
+unclear]
+will
+sense
 the
 channel
 for
 a
-time
-slot:
-yes,
-it
+[time
+slot,
+possibly
+incomplete].
+Yes,
+this
 is
 idle,
 so
@@ -72,30 +103,33 @@
 can
 decrease
 the
+backoff
 counter
 by
 one.
-It
+Then
+it
 senses
 the
 channel
 again
 for
-another
+a
 time
-slot;
-it
+slot.
+The
+channel
 is
 idle,
-so
 it
 can
 decrease
 the
 counter
 by
-one.
-Then
+one,
+and
+then
 again,
 the
 channel
@@ -106,10 +140,10 @@
 more
 time
 slot,
-so
 it
-decreases
-the
+can
+decrease
+its
 counter
 by
 one.
```

- [It / he, unclear]: Feishu and Qwen use it; Whisper uses he. Feishu has right; both ASR runs omit that filler. Counter/count is left unresolved rather than silently substituted.
- [it / he, unclear]: Feishu and Qwen use it; Whisper uses he. Feishu has right; both ASR runs omit that filler. Counter/count is left unresolved rather than silently substituted.
- [counter / count, unclear]: Feishu and Qwen use it; Whisper uses he. Feishu has right; both ASR runs omit that filler. Counter/count is left unresolved rather than silently substituted.
- [right, unclear]: Feishu and Qwen use it; Whisper uses he. Feishu has right; both ASR runs omit that filler. Counter/count is left unresolved rather than silently substituted.
- [it / he, unclear]: Qwen has it will sense the channel for a yes; Whisper has he will change the channel followed by yes. Do not silently supply a complete time-slot phrase.
- [time slot, possibly incomplete]: Qwen has it will sense the channel for a yes; Whisper has he will change the channel followed by yes. Do not silently supply a complete time-slot phrase.

## 27 · 00:29:23

Restore And again, future receive, okay/right, But, and final goal / ultimate goal restart. Mark corrupted all-nodes-success clause and disfluent apply-in-the words; do not certify the existing smooth wording.

来源：Feishu historical snapshot mapped source_index_zero_based=32; source block(s) 69; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=15, absolute 1650.00–1770.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-010,chunk-011

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -7,7 +7,10 @@
 to
 zero,
 so
-it
+[it
+/
+you,
+unclear]
 can
 access
 the
@@ -17,7 +20,8 @@
 its
 data
 packet.
-Again,
+And
+again,
 being
 optimistic,
 we
@@ -27,13 +31,18 @@
 is
 successful,
 so
-it
-receives
+[it
+/
+we,
+unclear]
+will
+receive
 the
-acknowledgment
+acknowledgement
 after
 SIFS.
-We
+And
+we
 are
 all
 happy
@@ -42,38 +51,55 @@
 nodes
 could
 transmit
-their
+[their
 data
-packets
-successfully.
-This
+packet
+successfully,
+unclear].
+Okay,
+so
+this
 is
 an
 example
 of
-applying
-the
+how
+we
+apply
+[in
+the,
+unclear]
 backoff
-procedure
+procedure,
+in
+particular
 under
 this
-condition.
-It
+condition,
+right?
+But
+it
+allows
+[us,
+unclear]
 also
-allows
-us
 to
 understand
 the
 importance
 of
 backoff.
-That
-is
+That's
+the
+final
+goal
+[that
+I,
+unclear],
 the
 ultimate
 goal
+that
 I
 was
-aiming
-for.
+aiming.
```

- [it / you, unclear]: Feishu and Qwen say it; Whisper says you.
- [it / we, unclear]: Qwen says it will receive; Feishu and Whisper say we will receive.
- [their data packet successfully, unclear]: The final words are corrupted across all three sources: Feishu data packet.Success; Qwen all nice good transmit that part, success; Whisper all knots go towards making that part successful. The displayed wording is an explicit provisional reading, not a certified restoration.
- [in the, unclear]: All three sources retain a disfluent word sequence before backoff; do not silently smooth it into applying the backoff procedure.
- [us, unclear]: Whisper includes us; Qwen omits it; this continuation is absent in the mapped Feishu paragraph but present in both raw ASR windows.
- [that I, unclear]: Qwen retains that I before the restart; Whisper omits it. Preserve final goal and ultimate goal rather than merging them.

## 28 · 00:30:26

Restore Well, that is...is, okay, repeated or, or and lets make this small game. Mark um and this a conflicts rather than deleting fillers or grammatically repairing the doubled is.

来源：Feishu historical snapshot mapped source_index_zero_based=33,34; source block(s) 71,73; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=16, absolute 1760.00–1880.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-011

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -6,19 +6,21 @@
 importance
 of
 backoff?
-Let's
+Well,
+let's
 make
 a
 little
 game
-that,
+that
+is,
 scientifically
 speaking,
 is
 called
-an
 ablation
-study.
+study,
+okay?
 An
 ablation
 study
@@ -30,8 +32,9 @@
 feature
 of
 a
-system
+system,
 and
+you
 study
 the
 behavior
@@ -41,7 +44,8 @@
 without
 that
 feature.
-Our
+So
+our
 small
 game
 is
@@ -51,18 +55,30 @@
 of
 this
 particular
+[um,
+unclear]
 backoff
 procedure,
+or,
 or
 Wi-Fi
 channel
 access.
-Let's
-think:
+So
+let's
+make
+this
+[a,
+unclear]
+small
+game
+and
+think,
 what
 would
 happen
 if
+the
 backoff
 were
 not
```

- [um, unclear]: Qwen records um; Feishu and Whisper omit it. The repeated or, or is present in Feishu and Qwen and is retained.
- [a, unclear]: Qwen and Whisper say this a small game; Feishu says this small game. No grammatical cleanup is applied.

## 29 · 00:31:22

Restore Okay, so, lets start, lets assume and the final okay. Preserve the spoken two lets clauses instead of connecting them with and.

来源：Feishu historical snapshot mapped source_index_zero_based=35; source block(s) 75; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-011

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,9 +1,11 @@
-Let's
+Okay,
+so
+let's
 roll
 back
 the
-story
-and
+story,
+let's
 start
 from
 the
@@ -11,12 +13,16 @@
 but
 this
 time
+let's
 assume
+that
 there
 is
 no
-backoff.
-What
+backoff,
+okay?
+So
+what
 would
 be
 the
```


## 30 · 00:31:43

Restore Well, the only node that has got, right, So, and both will clauses. Do not substitute simple-present actions for the spoken future forms.

来源：Feishu historical snapshot mapped source_index_zero_based=36; source block(s) 77; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-011

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,4 +1,5 @@
-At
+Well,
+at
 the
 beginning
 everything
@@ -9,15 +10,20 @@
 the
 only
 node
-with
+that
+has
+got
 a
 packet
 to
 transmit
 is
-A.
-It
-listens
+A,
+right?
+So
+it
+will
+listen
 to
 the
 channel,
@@ -26,13 +32,13 @@
 is
 idle
 for
-DIFS,
-and
-it
-accesses
+DIFS.
+It
+will
+access
 the
 channel
 and
-transmits
+transmit
 the
 packet.
```


## 31 · 00:32:02

Restore repeated questions, Okay/So/Well/right, Till...I cannot, no backoff restart, and because they overlap, their transmissions overlap. Preserve the grammatically awkward either this packet. Article and get/got remain flagged.

来源：Feishu historical snapshot mapped source_index_zero_based=37,38; source block(s) 79,81; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=17, absolute 1870.00–1990.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-011,chunk-012

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,57 +1,74 @@
-Again,
+And
+again,
 let's
 be
-optimistic:
-the
+optimistic.
+The
 access
 point
 sends
 back
+[the
+/
 an
-acknowledgment,
+/
+no
+article,
+unclear]
+acknowledgement,
 and
 the
 other
-nodes
-B
-and
-C
+nodes,
+B
+and
+C,
 both
 set
 their
-NAV.
+NAV,
+right?
 This
 is
 exactly
 as
 before.
-Assume
-that
-B
-and
-C
-also
-get
-a
-packet
-to
-transmit
+And
+again,
+B
+and
+C
 at
 different
 points
 in
-time.
+time,
+assume
+that
+they
+[get
+/
+got,
+unclear]
+also
+a
+packet
+to
+transmit.
 But
+again,
 now
 we
 do
 not
 have
-backoff.
-We
-have
-to
-think
+backoff,
+okay?
+So
+we
+have
+to
+think,
 what
 would
 happen
@@ -59,58 +76,80 @@
 backoff
 were
 not
-there.
-What
+there?
+So
+what
 would
 B
 and
 C
 do?
-We
+Well,
+we
 still
 have
-carrier-sense
+carrier
+sensing,
+right,
 multiple
 access.
-Since
-B
-and
-C
-both
+So
+since
+both
+B
+and
+C
 sense
 the
 channel
 as
 busy
 because
+they
+have
 their
 NAV
-is
 set,
 they
 cannot
 access
 the
-channel
-while
-it
-is
-busy.
-They
-will
+channel,
+right?
+Till
+the
+channel
+is
+busy,
+I
+cannot
+access
+the
+channel.
+So
+for
+sure
+B
+and
+C
+will
+again
 wait
 for
-it
-to
-become
-idle
-and
+the
+channel
+to
+be
+idle,
 make
 sure
-it
+that
+the
+channel
 is
 idle.
 But
+then
 if
 there
 is
@@ -118,49 +157,72 @@
 backoff,
 they
 can
-then
-access
-the
-channel.
-They
-say:
-the
-channel
-is
+just
+access
+the
+channel,
+right?
+Because
+now
+the
+channel
+is
+idle,
+so
+they
+say,
+oh,
+channel
 idle,
 I
 can
 access
-it
+the
+channel
 and
 transmit.
 Remember,
-in
+we
+are
+playing
 this
+small
 game
-we
-assume
+assuming
+that
 there
 is
 no
 backoff.
-Both
-transmit
+So
+what
+we
+have
+is
+that,
+no
+backoff,
+we
+have
+both
+transmitting
 their
 data
-packets
+packet
 after
-sensing
+having
+sensed
 the
 channel
 idle.
-What
+So
+what
 do
 we
 have
 here?
-A
-collision.
+Collision,
+right?
 They
 both
 access
@@ -175,19 +237,26 @@
 one.
 It
 is
-certain
+sure
+that
 they
 will
 do
 that,
 and
-they
+of
+course
+they
+will
 fail
 because
+they
+overlap,
 their
 transmissions
 overlap.
-The
+And
+the
 access
 point
 will
@@ -196,6 +265,7 @@
 able
 to
 demodulate
+correctly
 either
-packet
-correctly.
+this
+packet.
```

- [the / an / no article, unclear]: Acknowledgement article differs across sources. NAV is explicit technical normalization of NAF/knobs/now variants; historical Feishu incorrectly has send their packets.
- [get / got, unclear]: Feishu and Whisper say get; Qwen says got. The loose sentence structure is retained.

## 32 · 00:34:43

Restore the question-and-answer opening, our contending nodes in these examples, They are contending..., and So again remember that we said. The Wi-Fi/CSMA continuation is corroborated by both raw ASR windows.

来源：Feishu historical snapshot mapped source_index_zero_based=39; source block(s) 83; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=18, absolute 1980.00–2100.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-012

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,39 +1,61 @@
-The
+Okay,
+so
+what
+is
+the
 first
 conclusion
-is
-that
+here?
+That
+the
 backoff
-was
+procedure
+has
+been
 introduced
 in
 our
 system
+in
+order
 to
 avoid
 collisions
 between
 contending
 nodes.
-In
-this
-example
+Our
+contending
+nodes
+in
+these
+examples
+are
 B
 and
-C
-contend
+C,
+right?
+They
+are
+contending
 for
 the
-channel,
-and
+channel.
+And
+the
 backoff
+procedure
 is
 there
 to
 avoid
-their
-collision.
-Remember
+the
+collision
+between
+them.
+So
+again,
+remember
 that
 we
 said
@@ -44,4 +66,6 @@
 scheme
 with
 collision
-avoidance.
+avoidance,
+[right,
+unclear]?
```

- [right, unclear]: Qwen includes right; Whisper does not. This continuation is supported by both ASR windows though absent from the mapped Feishu block.

## 33 · 00:35:39

Restore the basic principle, the basic idea restart and right. Keep route/road and as all/as for conflicts visible. Desynchronize is supported by both independent model families against Feishu synchronize.

来源：Feishu historical snapshot mapped source_index_zero_based=40; source block(s) 85; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-012,chunk-013

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,23 +1,30 @@
-Backoff
+This
+backoff
 is
 a
 mechanism
 that
 helps
+to
 avoid
 collisions.
-The
+So
+the
+basic
+principle,
+the
 basic
 idea
 is
 very
-simple:
-whenever
+simple.
+Whenever
 there
 is
 a
 crowded
 situation,
+right,
 you
 try
 to
@@ -31,16 +38,21 @@
 find
 a
 free
-road
-ahead.
-It
+[route
+/
+road,
+unclear]
+ahead,
+and
+this
 is
 exactly
 the
 same
 thing.
-If
-it
+So
+if
+there
 is
 peak
 hour,
@@ -51,7 +63,13 @@
 jump
 into
 the
-traffic
-like
-everyone
-else.
+traffic,
+right,
+[as
+all
+/
+as
+for,
+unclear]
+the
+others.
```

- [route / road, unclear]: Qwen and Whisper support desynchronize against the Feishu synchronize error. Route is in Qwen and one Whisper overlap, road in Feishu; keep the lexical conflict.
- [as all / as for, unclear]: Feishu has as all the others; Qwen has as for the others; Whisper has or the others. Do not recast this as like everyone else.

## 34 · 00:36:25

Restore You try to pick, you wait, you try to pick, with respect to the others, and in a, in a. Leave corrupted linking words before colliding and possible Hmm unresolved rather than inventing a smooth sentence.

来源：Feishu historical snapshot mapped source_index_zero_based=41; source block(s) 87; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=19, absolute 2090.00–2210.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-013

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,12 +1,17 @@
 You
-wait
-and
+try
+to
+pick,
+you
+wait,
+you
 try
 to
 pick
 a
 time
-when
+at
+which
 not
 many
 other
@@ -14,34 +19,54 @@
 will
 be
 there.
-It
+And
+this
 is
+exactly
 the
 same
 principle.
 You
+try
+to
 pick
 a
 time
+in
+order
 to
 desynchronize
 your
 action
-from
+with
+respect
+to
 the
 others,
-avoiding
-collisions
+and
+this
+way
+you
+avoid
+meeting,
+[unclear
+words],
+colliding
 with
-them
+the
+others,
 or
 finding
 yourself
 in
+a,
+in
 a
 traffic
 jam.
-That's
+[Hmm,
+unclear],
+that's
 exactly
 the
 same
```

- [unclear words]: Feishu/Qwen have meeting like they colliding; Whisper has meeting and fake aligning. The connecting words remain unclear. The repeated in a, in a is supported by Feishu and Qwen, not removed for fluency.
- [Hmm, unclear]: Hmm occurs in the historical snapshot only.

## 35 · 00:37:02

Restore Now what I would like to underline, so we observe, our first observation; restore because/okay/future clauses. Do not silently turn synchronized into technically expected desynchronized; retain both as pending listening.

来源：Feishu historical snapshot mapped source_index_zero_based=42; source block(s) 89; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=20, absolute 2200.00–2320.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-013,chunk-014

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,10 +1,15 @@
-What
+Now
+what
 I
-want
+would
+like
 to
 underline
 is
-that
+that,
+so
+we
+observe,
 our
 first
 observation
@@ -13,81 +18,122 @@
 backoff
 is
 a
-collision-avoidance
-mechanism,
+mechanism
+for
+avoiding
+collisions,
 but
 it
 is
 still
-probabilistic.
+probabilistic,
+okay?
 Why?
-If
+Because
+if,
+like
+in
+our
+example,
+both
 B
 and
 C
 draw
 the
 same
-backoff
-value,
+value
+of
+backoff,
 they
 are
 going
 to
 collide.
-If
+Okay,
+so
+if,
+for
+example,
 C
 too
 drew
 two
 as
-its
+an
 integer,
 then
 they
-would
+will
 not
 be
-desynchronized
+[synchronized
+/
+desynchronized,
+unclear]
 from
 each
-other.
-Both
+other,
+okay?
+Because
+they
+will
+both
 decrease
-their
-counters
+the
+[the,
+unclear]
+backoff
+counter
 during
 the
 first
 time
-slot
+slot,
 and
+then
 again
 during
 the
-second.
-Under
+second
+time
+slot.
+But
+under
 the
 assumption
 that
+they
+now
 both
 drew
-two,
-their
-counters
-reach
+two
+as
+an
+integer,
+they
+will
+decrease
+the
+backoff
+counter
+to
 zero
+exactly
 at
-exactly
 the
 same
 time.
-They
+That
+means
+that
+they
+will
 access
 the
 channel
+exactly
 at
-exactly
 the
 same
 time
```

- [synchronized / desynchronized, unclear]: Historical Feishu and Qwen say synchronized; Whisper skips the relevant phrase. The expected technical meaning would suggest desynchronized, but that is not authority to replace the spoken word.
- [the, unclear]: Qwen has the the; historical Feishu has the once; Whisper drops part of this clause. The potential repetition is not silently either added or removed.

## 36 · 00:38:58

Restore So, repeated collisions instead of them, and the nodes, the contending nodes restart. Keep the right/okay filler conflict visible.

来源：Feishu historical snapshot mapped source_index_zero_based=43; source block(s) 91; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-013,chunk-014

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,4 +1,5 @@
-Backoff
+So
+backoff
 is
 a
 way
@@ -10,7 +11,7 @@
 does
 not
 avoid
-them
+collisions
 with
 probability
 one.
@@ -20,13 +21,21 @@
 a
 certain
 probability
-that
+with
+which
+the
+nodes,
+the
 contending
-nodes
+nodes,
 may
-collide.
-It
-is
+collide,
+[right
+/
+okay,
+unclear]?
+So
+it's
 a
 probabilistic
 collision-avoidance
```

- [right / okay, unclear]: Feishu has right; Qwen has okay; Whisper omits the filler. The nodes, the contending nodes restart is supported by all three.

## 37 · 00:39:28

Restore Okay, now if this is clear, let me make a second and the repeated second observation. Mark the aside found in Feishu but corrupted/omitted in both models instead of declaring it verified.

来源：Feishu historical snapshot mapped source_index_zero_based=44; source block(s) 93; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-014

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,4 +1,5 @@
-This
+Okay,
+this
 is
 our
 first
@@ -8,17 +9,18 @@
 clear
 so
 far?
-If
-so,
+Okay,
+now
+if
+this
+is
+clear,
 let
 me
 make
 a
-second
-one.
-Sorry,
-let
-me
+second,
+[sorry,
 check
 this,
 because
@@ -26,8 +28,10 @@
 is
 a
 bit
-different.
-We
+different,
+unclear].
+Okay,
+we
 have
 a
 second
@@ -46,11 +50,15 @@
 start
 introducing
 it,
+and
 then
 we
 will
 finish
 after
-the
+[the
+/
+a,
+unclear]
 short
 break.
```

- [sorry, check this, because today is a bit different, unclear]: The historical snapshot contains this aside; Qwen corrupts it into Say, check this time. This was the possibility; Whisper drops it. Do not present the fluent existing aside as independently verified.
- [the / a, unclear]: Feishu and Whisper have the short break; Qwen has a short break.

## 38 · 00:40:13

Restore parameter, given, Okay/So, A talk, both of them, the corrupted phrase following draw, out of...out of, as a possible range, as a range. Keep in/in in unresolved. Split the CW_min sentence at the existing 41:48 anchor according to new word times; do not duplicate the continuation.

来源：Feishu historical snapshot mapped source_index_zero_based=45,46; source block(s) 95,97; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=21, absolute 2310.00–2430.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-014,chunk-015

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,7 +1,14 @@
-The
+So
+the
 second
 observation
-concerns
+that
+I
+want
+to
+make
+is
+about
 the
 benefit
 of
@@ -9,33 +16,44 @@
 the
 contention
 window
+parameter
 every
 time
 we
 need
 to
 perform
+a
 backoff
+procedure
 for
 a
 given
 data
-packet.
-Consider
+packet,
+okay?
+So
+let's
+consider
+still
 the
 same
 example
 as
-before:
+before.
+So
+we
+still
+have
 the
 access
 point,
 A,
-B,
+B
 and
 C.
 A
-talks
+talk
 with
 the
 access
@@ -44,67 +62,100 @@
 B
 and
 C
+get
+the
+packet,
 both
-get
-a
-packet
+of
+them,
 while
 the
 channel
 is
 busy.
-They
+So
+they
 need
 to
 apply
-backoff
-and,
+the
+backoff,
+and
+they
+need
+to
+draw
+[unclear
+words],
 after
-sensing
+having
+sensed
 the
 channel
+as
 idle
 for
 DIFS,
-draw
 an
 integer
-from
+out
+of,
+as
+we
+know,
+out
+of
 this
 range
 of
-values.
-Since
+values,
+because
 this
 is
 the
 first
 time
+that
 they
 run
+the
 backoff
 for
-this
-packet,
+the
+packet.
+So
+they
 both
 use
-zero
-to
-CW_min
+zero,
+contention
+window
+minimum,
 as
-the
+a
+possible
+range,
+as
+a
 range
 of
 possible
-integers.
-How
+integers
+to
+be
+selected.
+So
+how
 many
 values
 are
-there?
+[in
+/
+in
+in,
+unclear]
+this
+range?
 There
 are
-CW_min
-plus
-one
-integers.
+CW_min...
```

- [unclear words]: The phrase after draw is corrupted as the forum / the pour / the quorum across sources. It is explicitly left unresolved, not replaced with a connective that makes the sentence smoother.
- [in / in in, unclear]: Qwen has in in; Whisper has in once; the question is absent in the mapped Feishu source block.

## 39 · 00:41:48

Restore Plus one integers, right? at the 41:48 anchor as the continuation of paragraph 38. Mark unclear words before including the zero rather than reducing the whole utterance to Including zero makes it plus one. Boundary adjustment is explicit.

来源：Feishu historical snapshot mapped source_index_zero_based=47; source block(s) 99; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-014,chunk-015

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,10 +1,18 @@
-Including
+Plus
+one
+integers,
+right?
+Because
+[unclear
+words],
+including
+the
 zero
-makes
-it
+is
 plus
 one.
-This
+Okay,
+this
 is
 the
 number
```

- [unclear words]: Whisper has Because the subunit; Qwen has We call this minimum; the Feishu source is corrupted. Only including the zero is plus one has stable support.

## 40 · 00:41:59

Restore repeated Okay, now, we know already, And remember, same probability fragment, equal probability, uniform probability, and an integer, a generic integer. Keep spoken formula words and standard Chinese denominator grouping; do not replace them with a cleaner derivation.

来源：Feishu historical snapshot mapped source_index_zero_based=48,49,50; source block(s) 101,103,105; may contain earlier edits and ASR errors；Qwen recovery rerun raw: window_index=22, absolute 2420.00–2540.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=23, absolute 2530.00–2650.00s; broad context window, not a word-aligned paragraph；Qwen recovery rerun raw: window_index=24, absolute 2640.00–2760.00s; broad context window, not a word-aligned paragraph；Whisper medium.en unprompted core/context chunks: chunk-014,chunk-015

```diff
--- current_word_sequence
+++ candidate_word_sequence
@@ -1,4 +1,6 @@
-What
+Okay,
+so
+what
 we
 want
 to
@@ -21,16 +23,20 @@
 and
 C
 collide.
-That's
-the
-probability
+Okay,
+that's
+the
+probability
+that
 we
 want
 to
 compute.
-We
+Okay,
+now
+we
+know
 already
-know
 that
 they
 will
@@ -41,46 +47,72 @@
 the
 same
 integer
-from
+out
+of
 this
 range.
-Remember
-that
+And
+remember
+that
+the
+way
 a
 node
 draws
 an
 integer
+out
+of
+this
+range
+is
 with
 uniform
-probability:
-the
+probability,
+right?
+So
 same
 probability
 for
 every
-value.
-If
+value
+to
+be
+selected
+by
+the
+node.
+So
+if
 we
 consider
 the
 probability
-that
+for
 a
 node
-draws
+to
+draw
 a
 generic
 integer
-n,
-it
-is
+n
+out
+of
+this
+range,
+this
+probability
+is
+given
+by
 one
 over
-(CW_min
-+
-1),
-because
+CW_min
+plus
+one,
+right?
+Because
 this
 is
 the
@@ -91,13 +123,16 @@
 the
 range.
 Since
+we
+draw
 each
 value
-has
+with
 equal
 probability,
-it
-is
+uniform
+probability,
+it's
 easy
 to
 see
@@ -112,33 +147,49 @@
 integer,
 is
 drawn
-from
+out
+of
 this
 range
 by
 a
 node
 is
+given
+by
 one
 over
-(CW_min
-+
-1).
+CW_min
+plus
+one.
 This
 is
 basic
 probability
-theory.
-Each
-integer
-is
+theory,
+okay?
+So
+in
+this
+way
+you
+can
+see
+that
+they
+are
 selected
+exactly,
+each
+of
+them
 with
-exactly
 the
 same
 probability.
-This
+[Okay,
+unclear],
+this
 probability
 is
 the
```

- [Okay, unclear]: The final Okay occurs in Qwen but not Feishu or Whisper.
