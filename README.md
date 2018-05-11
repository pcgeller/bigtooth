### bigtooth

bigtooth sniffs out out Bluetooth Low-Energy and BT Classic signals.  It collects
this data, along with the GPS location of the bigtooth device and stores it in a
database.  

On top of this data there's an analytical and data management layer for removing
data from a remote bigtooth device and storing it in a local database. Once the
data is loaded into the local database it's ready for analysis.  In the analysis
layer you can create visualizations of recorded observations and show the
observations on map.

To prep for deeper analysis a subset of the data can be loaded into device objects
that represent each unique device found.  Each device contains the meta data about
discovered device in addition to the time and location of each observation.

Future plans include LTE capabilties... but SDRs aren't cheap.

Because who the hell cares if you're being tracking **another** way.

Apologies if my git shenanigans messed up anyone - I started a new version of
this (Bigtooth2) before when I was a mere git-boy.... now I am a git-man.
Bigtooth2 is now the master branch of this project.  The master will be a
version of that actually works - breaking changes will only be made on develop.
