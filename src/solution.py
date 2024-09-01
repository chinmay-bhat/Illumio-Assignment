from functions import process_input_file, process_lookup_file, compute_matches, export_to_output
INPUT_FILE = "../input/input.txt"
LOOKUP_FILE = "../input/lookup.txt"
OUTPUT_FILE = "../output.txt"


flow_log_data = process_input_file(INPUT_FILE)
lookup_data = process_lookup_file(LOOKUP_FILE)
tag_counter, match_counter = compute_matches(flow_log_data, lookup_data)
export_to_output(OUTPUT_FILE, tag_counter, match_counter)
