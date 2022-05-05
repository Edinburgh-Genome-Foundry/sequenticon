import os
import sequenticon

from sequenticon import (
    sequenticon,
    sequenticon_batch,
    sequenticon_batch_pdf,
    load_records,
)


RECORDS_PATHS = [
    os.path.join("tests", "data", r) for r in ["records.fa", "seq4.gb", "seq5.dna"]
]


def test_load_records():
    records = load_records(RECORDS_PATHS)
    assert len(records) == 5


def test_sequenticon(tmpdir):
    output_path = os.path.join(str(tmpdir), "icon.png")

    sequenticon("ATGGTGCA", size=120, output_path=output_path)
    base64 = sequenticon("ATGGTGCA", size=60, output_format="base64")
    assert len(base64) == 292
    assert base64.startswith("iVBORw0KGgoAAAA")


def test_sequenticon_batch(tmpdir):

    sequences = [("seq1", "ATTGTG"), ("seq2", "TAAATGCC")]

    # Write a batch of sequences as PNG in a folder
    output_dir = os.path.join(str(tmpdir), "pngs")
    sequenticon_batch(sequences, size=120, output_path=output_dir)
    assert os.path.exists(os.path.join(output_dir, "seq1.png"))

    # Get a list [(sequence_name, html_image_tag), (...)]
    sequenticon_batch(sequences, size=60, output_format="html_image")
    sequenticon_batch(RECORDS_PATHS, size=60, output_format="html_image")

    # Write a PDF report with every sequenticon
    output_path = os.path.join(str(tmpdir), "my_report.pdf")
    sequenticon_batch_pdf(sequences, output_path)
    assert os.path.exists(output_path)
