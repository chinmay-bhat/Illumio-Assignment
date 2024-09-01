from src.functions import process_input_file, process_lookup_file, compute_matches, export_to_output
import time
INPUT_FILE = "../input/input.txt"
LOOKUP_FILE = "../input/lookup.txt"
INPUT10MB = "../input/input10mb.txt"
LOOKUP10k = "../input/lookup10klines.txt"
TEST_OUTPUT_FILE1 = "./output/process10MB.txt"
TEST_OUTPUT_FILE2 = "./output/process10klookup.txt"
TEST_OUTPUT_FILE3 = "./output/process10MBand10klookup.txt"


# test if 10mb input file can be processed
start = time.time()
flow_log_data = process_input_file(INPUT10MB)
lookup_data = process_lookup_file(LOOKUP_FILE)
tag_counter, match_counter = compute_matches(flow_log_data, lookup_data)
export_to_output(TEST_OUTPUT_FILE1, tag_counter, match_counter)
end = time.time()
print(f"Time elapsed: {end - start}")

# test if 10k lines in lookup file can be processed
start = time.time()
flow_log_data = process_input_file(INPUT_FILE)
lookup_data = process_lookup_file(LOOKUP10k)
tag_counter, match_counter = compute_matches(flow_log_data, lookup_data)
export_to_output(TEST_OUTPUT_FILE2, tag_counter, match_counter)
end = time.time()
print(f"Time elapsed: {end - start}")

# test if both 10mb input and 10k lookup can be processed
start = time.time()
flow_log_data = process_input_file(INPUT10MB)
lookup_data = process_lookup_file(LOOKUP10k)
tag_counter, match_counter = compute_matches(flow_log_data, lookup_data)
export_to_output(TEST_OUTPUT_FILE3, tag_counter, match_counter)
end = time.time()
print(f"Time elapsed: {end - start}")