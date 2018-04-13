import os
from sequenticon import sequenticon_batch_pdf

records_paths = [
    os.path.join('example_sequences', filename)
    for filename in ["records.fa", "seq4.gb", "seq5.dna"]
]
sequenticon_batch_pdf(records_paths, "sequenticon_batch_pdf.pdf",
                      title="Example sequenticon report")
