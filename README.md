Question is in question.txt

### Requirements
All the requirements provided in the question have been satisfied:
- [x] Input file as well as the file containing tag mappings are plain text (ascii) files
- [x] The flow log file size can be up to 10 MB
- [x] The lookup file can have up to 10000 mappings
- [x] The tags can map to more than one port, protocol combinations.  for e.g. sv_P1 and sv_P2 in the sample above.
- [x] The matches should be case insensitive
Also, no non-default libraries have been used.

### Assumptions
- This program only supports default log format, version 2.
- In the example, protocols include a few - tcp, udp, icmp. To allow for every possible protocol, I have downloaded & pre-processed the list of protocol numbers and string values from [here](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml), which was linked in the reference provided in the question.
- Each unique (port, protocol) combo can map to one tag. 
  - for example, (25,tcp) can only map to "email" tag, not multiple tags. But "email" tag can map to multiple (port, protocol) combo.
- Only 1 output file is expected with both tag and matches count.

### Program logic
1. Create a protocol mapping using protocol-numbers-1.csv file. The key is the protocol number and value is the protocol string.
For example: {"6":"TCP", "17":"UDP"}
2. Create tags mapping using lookup.txt file. The key is a combination of dstport and protocol name, the value is the tag.
For example: {("25","tcp"): sv_P1}
3. Process the flow log file where each line is split on space (delimiter), and the 6th and 7th positions give us the destination port and protocol.
4. Use the protocol mapping to find corresponding protocol string.
5. Combine destination port and protocol string. If the combo exists in tags mapping, update the tag_counter and match counter. Otherwise, update Untagged count.
6. Export the tag and match counts to output.txt file.

### Run the solution
Use Python3. Add the project path to $PYTHONPATH.

```commandline
export PYTHONPATH="${PYTHONPATH}:<absolute-path-to-cloned-directory>"
cd src
python solution.py
```
Output is in output.txt

### Run tests

```commandline
cd tests
python test.py
```
Test output is in tests/output/

To minimise external libraries used, I've not used a test framework like pytest.

I've focused the tests on the limits of the file size and input size.

With pytest, I would have added more unit tests.

  Tests are:
- test if 10mb input file can be processed
- test if 10k lines in lookup file can be processed
- test if both 10mb input and 10k lookup can be processed at the same time
