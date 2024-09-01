from collections import defaultdict

# downloaded csv from https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml which was linked
# in the Amazon VPC flow log reference webpage provided in the question.
# I've pre-processed csv to remove all lines starting with words
PROTOCOL_NUMBERS_FILE = "../input/protocol-numbers-1.csv"
UNTAGGED = "Untagged"


def _process_protocol_csv(protocol_filename):
    mapping = {}
    print("Processing protocols csv file...")
    with open(protocol_filename) as protocol_file:
        for line in protocol_file:
            line = line.rstrip('\n').split(',')
            protocol_num, protocol_string = line[0], line[1]
            mapping[protocol_num] = protocol_string
    print("Completed processing possible protocols!")
    return mapping


_protocol_mapping = _process_protocol_csv(PROTOCOL_NUMBERS_FILE)


def get_protocol_mapping(protocol):
    if 146 <= int(protocol) <= 254:
        return ""
    return _protocol_mapping[protocol]


def process_input_file(input_filename):
    print("Processing input file...")
    result = []
    with open(input_filename, "r") as input_file:
        for line in input_file:
            line = line.rstrip('\n').split(' ')
            dstport, protocol = line[6], line[7]
            result.append((dstport, get_protocol_mapping(protocol)))
    print("Completed processing input file!")
    return result


def process_lookup_file(lookup_filename):
    data = defaultdict()
    print("Processing lookup file...")
    with open(lookup_filename, "r") as lookup_file:
        # remove csv header string before this step
        for line in lookup_file:
            dstport, protocol, tag = line.rstrip('\n').split(',')
            data[(dstport, str.lower(protocol))] = tag
    print("Completed processing lookup file!")
    return data


def compute_matches(flow_log_data, lookup_data):
    print("Counting matches and tags...")
    tag_count, match_count = defaultdict(int), defaultdict(int)
    for (dstport, protocol) in flow_log_data:
        protocol = str.lower(protocol)
        if (dstport, protocol) in lookup_data:
            tag = lookup_data[(dstport, protocol)]
            tag_count[tag] += 1
            match_count[(dstport, protocol)] += 1
        else:
            tag_count[UNTAGGED] += 1
    print("Completed counting!")
    return tag_count, match_count


def export_to_output(filename, tag_counter, match_counter):
    with open(filename, "w") as output_file:
        output_file.write("Count of matches for each tag\n")
        output_file.write("Tag,Counts\n")
        for tag, count in tag_counter.items():
            output_file.write(f"{tag},{count}\n")
        output_file.write("\n\n")
        output_file.write("Count of matches for each port/protocol combination\n")
        output_file.write("Port,Protocol,Count\n")
        for (port, protocol), count in match_counter.items():
            output_file.write(f"{port},{protocol},{count}\n")
    print("Counts exported to output.txt file!")