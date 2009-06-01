Name
----
trml2pdf - convert a Report Markup Language (RML) file to a PDF


Synopsis
--------

	rml2pdf --help
	rml2pdf input.rml output.pdf

Description
-----------

Tiny RML2PDF is a tool to easily create PDF document without programming. It
can be used as a Python library or as a standalone binary. It converts a RML,
an XML dialect that lets you define the precise appearance of a printed
document, to a PDF. You can use your existing tools to generate an input file
that exactly describes the layout of a printed document, and RML2PDF converts
it into PDF. RML is a much more powerful and flexible alternative to XSL:FO.

The executable read a RML file to the standard input and output a PDF file to
the standard output.


Command-line options
--------------------

	--help: command line options

Examples
--------

Create a PDF file:

	rml2pdf input.rml output.pdf

Use it as a python module:

	import trml2pdf
	
	input_file = file('input.rml','r').read()
	output_file = file('output.pdf', 'wb')
	output_file.write(trml2pdf.parse_string(input_file))

Original Author
------

Fabien Pinckaers (http://tiny.be)
