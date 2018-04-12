.. raw:: html

    <p align="center">
    <img alt="lala Logo" title="sequenticon Logo" src="https://raw.githubusercontent.com/Edinburgh-Genome-Foundry/sequenticon/master/docs/logo.png" width="550">
    <br /><br />
    </p>

.. image:: https://travis-ci.org/Edinburgh-Genome-Foundry/sequenticon.svg?branch=master
   :target: https://travis-ci.org/Edinburgh-Genome-Foundry/sequenticon
   :alt: Travis CI build status

.. image:: https://coveralls.io/repos/github/Edinburgh-Genome-Foundry/sequenticon/badge.svg?branch=master
   :target: https://coveralls.io/github/Edinburgh-Genome-Foundry/sequenticon?branch=master


Sequenticon is a Python library to generate `identicons <https://en.wikipedia.org/wiki/Identicon>`_ for DNA sequences. For instance the sequence ``ATGGTGCA`` gets converted to the following icon:

.. raw:: html

    <br />
    <p align="center">
    <img title="sequenticon example" src="https://raw.githubusercontent.com/Edinburgh-Genome-Foundry/sequenticon/master/docs/ATGGTGCA_sequenticon.png" width="80"/>
    <br /><br />
    </p>

When are sequenticons useful ?
-------------------------------

In biological engineering, DNA sequence files often get updated or re-named. This can cause critical confusions when the wrong files or wrong sequence versions get used in a process. Ideally, laboratory information systems would prevent such mistakes, but when they happen they are difficult to trace back to the faulty sequences.

Therefore, when using software to process large batches of sequences, one may want a way to quickly decide whether the sequence ``pLac3.gb`` used on March 15th is the same as ``plac3.gb`` which appears in the April 18th batch.

Identicons provide a simple visual way to know that two sequences are different (different identicons) or very probably the same (same identicon).

Also note that, theoretically, even two large sequences differing by one nucleotide only will have very different sequenticon looks.

Usage
-----

.. code:: python

    from sequenticon import sequenticon

    # Write a sequence to a PNG sequenticon file
    sequenticon("ATGGTGCA", size=120, output_path="icon.png")

    # Get a self-contained "<img/>" HTML string, to embed in a webpage
    img_tag = sequenticon("ATGGTGCA", size=60, output_format="html_image")

To process a batch:

.. code:: python

    from sequenticon import sequenticon_batch

    sequences = [("seq1", "ATTGTG"), ("seq2", "TAAATGCC"), ...] # OR
    sequences = ["record1.gb", "record2.fa", ...] # OR
    sequences = [biopython_record_1, biopython_record_2, ...]

    # Write a batch of sequences as PNG in a folder
    sequenticon_batch(sequences, size=120, output_path="my_emoticons/")

    # Get a list [(sequence_name, html_image_tag), (...)]
    data = sequenticon_batch(sequences, size=60, output_format="html_image")

    # Write a PDF report with every sequenticon
    sequenticon_batch_pdf(sequences, "my_report.pdf")

Here is an example PDF output from the last command (`full PDF <https://github.com/Edinburgh-Genome-Foundry/sequenticon/blob/master/docs/example_report.pdf">`_):

.. raw:: html

    <p align="center">
    <img alt="sequenticon Logo" title="sequenticon Logo" src="https://raw.githubusercontent.com/Edinburgh-Genome-Foundry/sequenticon/master/docs/pdf_screenshot.png" width="381">
    <br /><br />
    </p>

Installation
-------------

You can install Sequenticon through PIP

.. code::

    sudo pip install sequenticon

Alternatively, you can unzip the sources in a folder and type

.. code::

    sudo python setup.py install

License = MIT
--------------

This project is an open-source software originally written at the `Edinburgh Genome Foundry <http://genomefoundry.org>`_ by `Zulko <https://github.com/Zulko>`_ and `released on Github <https://github.com/Edinburgh-Genome-Foundry/sequenticon>`_ under the MIT licence (¢ Edinburg Genome Foundry).

Everyone is welcome to contribute !

More biology software
---------------------

.. image:: https://raw.githubusercontent.com/Edinburgh-Genome-Foundry/Edinburgh-Genome-Foundry.github.io/master/static/imgs/logos/egf-codon-horizontal.png
  :target: https://edinburgh-genome-foundry.github.io/

Sequenticon is part of the `EGF Codons <https://edinburgh-genome-foundry.github.io/>`_ synthetic biology software suite for DNA design, manufacturing and validation.

**Note: also check out Pydenticon.** Sequenticon is really just a few lines of Python around the more generic [pydenticon](https://github.com/azaghal/pydenticon) library. The upside of having an official *sequenticon* library is to make sure that the icons, colors, etc. remain consistent accross projects.
