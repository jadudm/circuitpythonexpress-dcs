# circuitpythonexpress-dcs

A functional abstraction over the CPx library for the Circuit Python Express.

The goal is to provide a functional pathway from Makecode to Python. The CPx object wrapper is excellent, but I'd rather not have to introduce objects as soon as I move from Makecode to Python; instead, I want to be able to have functions that mirror those experiences that students had in the visual environment, so as to have (as close as possible) to a 1:1 correspondence between their visual and textual experience.

Currently, Javascript and Python for learning platforms like the MicroBit and Circuit Playground Express fail this simple pedagogic need. Until events are well supported on the CPx, it will be difficult to write (for example) event handlers like "on shake". But, in the meantime, this starts to build a bridge.

