# Takes an input science def file, with defs written in English, and splits it out into an English localization file
# and a localized science defs file. It only writes the content, so you'll have to copy and paste it into the
# actual mod files.
import re

defs_file_path = "ScienceDefs.cfg" # Input ScienceDefs.cfg file
scidef_file_path = "scidef_output.cfg" # Path to output localized ScienceDefs to.
locfile_path = "locfile_output.cfg" # Path to output English localization strings to

with open(defs_file_path, 'r') as defs_file:
    defs_content = defs_file.read()

line_list = defs_content.splitlines()

scidef_line_list = []
locfile_list = []

key_prefix = "#LOC_PW_sci_" # Prefix for each key
def_id = "" #active science def id
def_count = 0

# Don't change lines that are not defs (do not contain =)
for line in line_list:
    # If there's a science def ID, we will change the active def id
    if "#id" in line:
        def_id = re.sub(r"\]\]", "", re.sub(r"@EXPERIMENT_DEFINITION:HAS\[#id\[", "", line))
        print("def_id now: " + def_id)
        locfile_list.append("		// ******** " + def_id + " ********\n")
    if "=" in line:
        (key_name, en_string) = line.split("=", 1)
        loc_key = key_prefix + def_id + "_" + key_name.lstrip()
        scidef_line_list.append(key_name + "= " + loc_key + "\n")
        locfile_list.append("        " + loc_key + "= " + en_string + "\n")
        def_count = def_count + 1
    else:
        scidef_line_list.append(line + "\n")
        if not "@" in line and not "{" in line and not "}" in line:
            locfile_list.append(line + "\n")

# Write our new science def file with localization keys
with open(scidef_file_path, 'a') as scidef_file:
    for line in scidef_line_list:
        scidef_file.write(line)

print("Wrote new ScienceDefs file at " + scidef_file_path + ".")
# Write localizations and english strings
with open(locfile_path, 'a') as loc_file:
    for line in locfile_list:
        loc_file.write(line)

print("Wrote English localizations to file at " + locfile_path + ".")
print("Done! Converted " + str(def_count) + " science defs")
