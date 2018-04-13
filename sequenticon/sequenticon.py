import base64
import os
from datetime import datetime

from Bio import SeqIO
import pydenticon
import flametree
from pdf_reports import pug_to_html, write_report

from .tools import load_records
from .version import __version__


SETTINGS = dict(
    color_palette=[
        '#1f77b4',
        '#ff7f0e',
        '#2ca02c',
        '#d62728',
        '#9467bd',
        '#8c564b',
        '#e377c2',
        '#7f7f7f',
        '#dada85',
        '#17becf'
    ],
    rows=6,
    columns=6,
)


def sequenticon(sequence, output_format='png', size=60, output_path=None):
    """Return sequenticon image data for the provided sequence.

    Note: to change the number of rows and columns, or the colors of the
    sequenticon, change the values in ``sequenticons.SETTINGS``

    Parameters
    ----------

    sequence
      A string, for instance "ATTGTGCGTGTGC". Sequenticon is case-insensitive
      and will upper-case the full sequence.

    output_format
      One of "png", "base64", "html_image". If "png", raw PNG image data is
      returned (as bytes). If base64, the png data is base64-encoded (string),
      and if html_image, the returned string is ``<img src='data:X'/>`` where
      X is base64 image data (this string is ready to be used in a webpage).

    size
      The sequenticon image will be of dimensions (size x size), in pixels.

    output_path
      Optional path to a PNG file to which to write the sequenticon


    """
    if hasattr(sequence, 'seq'):
        sequence = str(sequence.seq)
    sequence = sequence.upper()
    generator = pydenticon.Generator(SETTINGS["rows"], SETTINGS["columns"],
                                     foreground=SETTINGS["color_palette"])
    img = generator.generate(sequence, size, size)
    base_64 = base64.b64encode(img).decode()
    html_image = "<img src='data:image/png;base64,%s'/>" % base_64
    data = {
        'png': img,
        'base64': base_64,
        'html_image': html_image
    }[output_format]
    if output_path is not None:
        with open(output_path, "wb") as f:
            f.write(data)
    return data




def sequenticon_batch(sequences, output_format='png', size=60,
                      output_path=None):
    """Utility to generate sequenticons for a batch of sequences.

    Parameters
    ----------

    sequences
      A list of either ``name, sequence`` tuples, or Biopython records (with
      different IDs), or paths to genbank or fasta files containing one or
      more record each.

     output_format
      One of "png", "base64", "html_image". If "png", raw PNG image data is
      returned (as bytes). If base64, the png data is base64-encoded (string),
      and if html_image, the returned string is ``<img src='data:X'/>`` where
      X is base64 image data (this string is ready to be used in a webpage).

    size
      The sequenticon image will be of dimensions (size x size), in pixels.

    target
      An optional folder or zip path in which to write the PNG files.

    Returns
    -------

    sequenticons
      A list of the form [(sequence_name, sequenticon_image_data), ...]

    """

    if "." in sequences[0]:
        sequences = load_records(sequences)
    if hasattr(sequences[0], 'seq'):
        sequences = [(record.id, str(record.seq)) for record in sequences]

    result = [
        (name, sequenticon(sequence, output_format=output_format, size=size))
        for name, sequence in sequences
    ]
    if output_path is not None:
        root = flametree.file_tree(output_path)
        for name, data in result:
            root._file(name + ".png").write(data)

    return result


THIS_PATH = os.path.dirname(os.path.realpath(__file__))
ASSETS_PATH = os.path.join(THIS_PATH, "report_assets")
PUG_TEMPLATE = os.path.join(ASSETS_PATH, "report_template.pug")
STYLESHEET = os.path.join(ASSETS_PATH, "report_style.css")

def sequenticon_batch_pdf(sequences, target, title="Sequenticons batch"):
    """Generate a PDF report with sequenticons for a batch of sequences.

    Parameters
    ----------

    sequences
      A list of either ``name, sequence`` tuples, or Biopython records (with
      different IDs), or paths to genbank or fasta files containing one or
      more record each.

    target
      path to a PDF file

    title
      Title that will appear in the document
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    sequenticons = sequenticon_batch(sequences, output_format='html_image')
    html = pug_to_html(
        PUG_TEMPLATE,
        sidebar_text="Generated on %s by Sequenticon version %s" %
                      (now, __version__),
        sequenticon_logo_url=os.path.join(ASSETS_PATH, 'logo.png'),
        sequenticons=sequenticons,
        title=title
    )
    write_report(html, target, extra_stylesheets=(STYLESHEET,))
