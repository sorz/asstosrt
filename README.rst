asstosrt
===========


asstosrt is a tool which can convert Advanced SubStation Alpha (ASS/SSA) 
subtitle files to SubRip (SRT) files. Many old devices only support SubRip.


Usage
-----

Install asstosrt.

::

    # pip install asstosrt

``chardet`` is suggested, which provide auto charset detection.

::

    # pip install charset


Then ``cd`` into the directory of ASS/SSA files. Run asstosrt.
	
::

    $ asstosrt
	
Done. All converted SRT files will be wrote to current directory.

Run with ``--help`` see more.

::

    $ asstosrt --help


More Examples
-------------

Specify input and output encoding, output directory:

::

    $ asstosrt -e utf-8 -s utf-18be -o /to/some/path/


Convert to Simplified Chinese (Using ``langconv``
`download <https://code.google.com/p/pyswim/downloads/detail?name=langconv-0.0.1dev.tgz>`__):

::

    $ asstosrt -t zh-hans -s gb18030 /path/to/some.big5.ass


Convert to Traditional Chinese (Using OpenCC):

::

	# pip install pyopencc
	$ asstosrt -c zhs2zht.ini 


Only keep first line for each dialogue and delete all effects:

::

	$ asstosrt --only-first-line --no-effact


Used as a Library
-----------------

You can use asstosrt on your program easily.

::

    import asstosrt
	
    ass_file = open('example.ass')
    srt_str = asstosrt.convert(ass_file)
	

License
-------

MIT License

Bugs and Issues
---------------

Please visit `GitHub <https://github.com/sorz/asstosrt>`__.