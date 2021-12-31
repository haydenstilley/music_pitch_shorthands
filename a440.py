# Octaves 2-6:
C2 = 65.41
C_SHARP2 = 69.3
D_FLAT2 = C_SHARP2
D2 = 73.42
D_SHARP2 = 77.78
E_FLAT2 = D_SHARP2
E2 = 82.41
F2 = 87.31
F_SHARP2 = 92.5
G_FLAT2 = F_SHARP2
G2 = 98
G_SHARP2 = 103.83
A_FLAT2 = G_SHARP2
A2 = 110
A_SHARP2 = 116.54
B_FLAT2 = A_SHARP2
B2 = 61.74

C3 = 130.81
C_SHARP3 = 138.59
D_FLAT3 = C_SHARP3
D3 = 146.83
D_SHARP3 = 155.56
E_FLAT3 = D_SHARP3
E3 = 164.81
F3 = 174.61
F_SHARP3 = 185
G_FLAT3 = F_SHARP3
G3 = 196
G_SHARP3 = 207.65
A_FLAT3 = G_SHARP3
A3 = 220
A_SHARP3 = 233.08
B_FLAT3 = A_SHARP3
B3 = 246.94

C4 = 261.63
C_SHARP4 = 277.18
D_FLAT4 = C_SHARP4
D4 = 293.66
D_SHARP4 = 311.13
E_FLAT4 = D_SHARP4
E4 = 329.63
F4 = 349.23
F_SHARP4 = 369.99
G_FLAT4 = F_SHARP4
G4 = 392
G_SHARP4 = 415.3
A_FLAT4 = G_SHARP4
A4 = 440
A_SHARP4 = 466.16
B_FLAT4 = A_SHARP4
B4 = 493.88

C5 = 523.25
C_SHARP5 = 554.37
D_FLAT5 = C_SHARP5
D5 = 587.33
D_SHARP5 = 622.25
E_FLAT5 = D_SHARP5
E5 = 659.25
F5 = 698.46
F_SHARP5 = 739.99
G_FLAT5 = F_SHARP5
G5 = 783.99
G_SHARP5 = 830.61
A_FLAT5 = G_SHARP5
A5 = 880
A_SHARP5 = 932.33
B_FLAT5 = A_SHARP5
B5 = 987.77

C6 = 1046.5
C_SHARP6 = 1108.73
D_FLAT6 = C_SHARP6
D6 = 1174.66
D_SHARP6 = 1244.51
E_FLAT6 = D_SHARP6
E6 = 1318.51
F6 = 1396.91
F_SHARP6 = 1479.98
G_FLAT6 = F_SHARP6
G6 = 1567.98
G_SHARP6 = 1661.22
A_FLAT6 = G_SHARP6
A6 = 1760
A_SHARP6 = 1864.66
B_FLAT6 = A_SHARP6
B6 = 1975.53

# Basic chords in the 4th octave. To change octaves of any pitch, you can multiply/divide the Hz values.
# For example: A4 = 440hz, so (A4 * 2) = 880hz, which is equal to A5.
# Note that (A4 * 3) is not equal to A6, but (A5 * 2) is equal to A6.
# This is an easy way to make different chord inversions, too.
AMAJOR = [A4,C_SHARP4,E4]
AMINOR = [A4,C4,E4]
AS_MAJOR = [A_SHARP4,D4,F4]
BB_MAJOR = AS_MAJOR
AS_MINOR = [A_SHARP4,C_SHARP4,F4]
BB_MINOR = AS_MINOR
BMAJOR = [B4,D_SHARP4,F_SHARP4]
BMINOR = [B4,D4,F_SHARP4]
CMAJOR = [C4,E4,G4]
CMINOR = [C4,E_FLAT4,G4]
CS_MAJOR = [C_SHARP4,F4,G_SHARP4]
DB_MAJOR = CS_MAJOR
CS_MINOR = [C_SHARP4,E4,G_SHARP4]
DB_MINOR = CS_MINOR
DMAJOR = [D4,F_SHARP4,A4]
DMINOR = [D4,F4,A4]
DS_MAJOR = [D_SHARP4,G4,A_SHARP4]
EB_MAJOR = DS_MAJOR
DS_MINOR = [D_SHARP4,F_SHARP4,A_SHARP4]
EB_MINOR = DS_MINOR
EMAJOR = [E4,G_SHARP4,B4]
EMINOR = [E4,G4,B4]
FMAJOR = [F4,A4,C4]
FMINOR = [F4,A_FLAT4,C4]
FS_MAJOR = [F_SHARP4,A_SHARP4,C_SHARP4]
GB_MAJOR = FS_MAJOR
FS_MINOR = [F_SHARP4,A4,C_SHARP4]
GB_MINOR = FS_MINOR
GMAJOR = [G4,B4,D4]
GMINOR = [G4,B_FLAT4,D4]
GS_MAJOR = [G_SHARP4,C4,D_SHARP4]
AB_MAJOR = GS_MAJOR
GS_MINOR = [G_SHARP4,B4,D_SHARP4]
