# LRG XML file parser (Python)

A simple parser which reads in LRG XML files (schema version 1.9) and returns XML output of the intronic sequences in the source file.

## Usage

#### Command line / terminal

```bash
python LRG_parser.py
```

#### Specifiy file
Users must enter the XML file they intend to parse including the .xml extension
Users can specify the relative/absolute path to the input file.
```bash
Please enter file name: LRG_5.xml
```

## Output
The output file is exported with the naming convention **introns _lrg id_.mxl**
The output of the script is an XML file containing:
- Schema details
- Source/contact details
- Intron details
-- Intron number
-- Start position
-- End position
-- Intron sequence
