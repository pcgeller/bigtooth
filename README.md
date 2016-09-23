##BigTooth

We are surrounded by a world that we can't see: wifi, radio, cellular, BlueTooth, and many 
other signals are carrying data right through us. BigTooth seeks to tap into the unseen 
world of BlueTooth.  

This project scans for BlueTooth signals on a Raspberry Pi.  After collecting the signals from 
several different locations (commute, commerical stores, public transit) tests will be run to 
determine whether or not the types of BlueTooth devices seen nearby can be used to identify 
the location.  

Right now the code consists of getting Blue Hydra set-up.  After this is accomplished the same 
environment will be set-up on a Raspberry Pi to enable mobile signal collection.  Then, some signals
from various locations mentioned before will be collected.  After a large enough data set is collected
machine learning algorithms from Python's sci-kit will be used for the location classification.


