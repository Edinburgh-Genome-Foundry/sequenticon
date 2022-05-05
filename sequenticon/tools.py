import os

from Bio import SeqIO

from snapgene_reader import snapgene_file_to_seqrecord


def load_records(path):
    if isinstance(path, (list, tuple)):
        return [record for p in path for record in load_records(p)]
    no_extension, extension = os.path.splitext(path)
    fmt = {".fa": "fasta", ".gb": "genbank", ".gbk": "genbank", ".dna": "snapgene"}[
        extension
    ]
    if fmt == "snapgene":
        records = [snapgene_file_to_seqrecord(path)]
    else:
        records = list(SeqIO.parse(path, fmt))
    for i, record in enumerate(records):
        if str(record.id) in ["None", "", "<unknown id>", ".", " "]:
            record.id = path.replace("/", "_").replace("\\", "_")
            if len(records) > 1:
                record.id += "_%04d" % i
    return records
