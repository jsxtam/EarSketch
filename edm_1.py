from earsketch import *

init()
setTempo(120)

## add small intro beat to beginning
############################################################
#clips

lead = EIGHT_BIT_ATARI_SINEDOT_001


rd_lead = RD_TRAP_PLUCKLEAD_2
strings = RD_CINEMATIC_SCORE_STRINGS_15
#bass in ascending pitch order
ea_bass = [ELECTRO_ANALOGUE_BASS_009, ELECTRO_ANALOGUE_BASS_012,
           ELECTRO_ANALOGUE_BASS_010, ELECTRO_ANALOGUE_BASS_011]

elec_p = YG_ELECTRO_RHODES_1
rev_edm = YG_EDM_REVERSE_FX_1

d_intro = RD_EDM_DRUMROLL_BREAK_7
drum1 = EIGHT_BIT_ANALOG_DRUM_LOOP_003
drum2 = TECHNO_KICKROLL_002
h_drum = YG_HOUSE_DRUMS_1
cbell = YG_FUNK_COWBELL_3

##############################################################
#tracks

### Drum Line - Track 1
d_start = 1
track = 1
length = dur(h_drum)

insertMedia(d_intro, track, d_start)
d_start += dur(d_intro)

d=1
while d < 3:
  insertMedia(h_drum, track, d_start)
  d_start += length
  d += 1
  length = dur(drum2)
d_start += 3 * length
makeBeat(drum2, track, d_start, "0+------0+------0+------0+------")
d_start += length
insertMedia(drum2, track, d_start)
d_start += length
fitMedia(RD_TRAP_BASSDROPS_1, track, d_start, 17.5 + dur(d_intro))
d_start += .5
while 2 < d < 7:
  length = dur(drum1)
  insertMedia(drum1, track, d_start)
  d += 1
  d_start += length
fitMedia(RD_TRAP_BASSDROPS_1, track, d_start, 26 + dur(d_intro))
d_start += .5
while 6 < d < 11:
  length = dur(drum1)
  insertMedia(drum1, track, d_start)
  d += 1
  d_start += length
insertMedia(rev_edm, track, d_start)

#makeBeat(drums, 1, d_start, drumPattern)

### Bass Line - Tracks 2, 3, 4, 5
b_start = 3
track += 1
numBassClips = len(ea_bass)
pan = [-100, -33, 33, 100]
 
b = 1
while b < 3:
  for c in range(0, numBassClips):
    insertMedia(ea_bass[c], track, b_start)
    b_start += dur(ea_bass[c])
    setEffect(track, PAN, LEFT_RIGHT, pan[c])
    track += 1
  track -= 4
  b += 1
track +=4

### Lead - Track 6
l_start = 9 + dur(d_intro)
l = 1
while l < 5:
  insertMedia(lead, track, l_start)
  l += 1
  l_start += dur(lead)
  track += 1
  if 1 < l < 5:
    ### Cowbell - Track 7
    cb_beat = "--0+----0+0+--0+--0+0+0+--0+--0+"
    #track = 7
    makeBeat(cbell, track, l_start, cb_beat)
    setEffect(track, VOLUME, GAIN, 4)
    track += 1
  if 3 < l < 5:
    fitMedia(strings, track, l_start, 18)
  track = 6
track +=3

### Part B Lead - Track 9
lb_start = 21 + dur(d_intro)
insertMedia(rd_lead, track, lb_start)
lb_start += 5
lb = 1
while lb < 3:
  insertMedia(rd_lead, track, lb_start)
  lb_start += dur(rd_lead)
  lb += 1
track += 1
  
### Piano - Track 8
p_start = 27 + dur(d_intro)
for num in "11":
  if num == "1":
    insertMedia(elec_p, track, p_start)
    setEffect(track, VOLUME, GAIN, 6)
    p_start += dur(elec_p)
track += 1
### Strings - Track 9
s = 1
s_start = 29 + dur(d_intro)
while s < 4:
  fitMedia(strings, track, s_start, s_start + 1)
  s += 1
  s_start += 2
setEffect(track, VOLUME, GAIN, 8)

finish()
