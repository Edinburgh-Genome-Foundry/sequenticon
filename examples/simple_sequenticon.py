import os
from sequenticon import sequenticon

# Sequence to PNG
sequenticon(sequence="ATGTGCCGAT", output_path="simple_sequenticon_1.png")

# Record file to PNG
sequenticon(sequence=os.path.join("example_sequences", "seq4.gb"),
            output_path="simple_sequenticon_2.png", size=120)
