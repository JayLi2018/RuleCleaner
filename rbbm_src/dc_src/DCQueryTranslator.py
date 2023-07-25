from string import Template
from rbbm_src.dc_src.src.classes import parse_rule_to_where_clause
from rbbm_src.dc_src.DCRepair import dc_tuple_violation_template_targeted_t1,dc_tuple_violation_template_targeted_t2,non_symetric_op

import re

# dc_query_template=Template("SELECT DISTINCT t2.* FROM $table t1, $table t2 WHERE $dc_desc AND $tuple_desc;")

dc_tuple_violation_template_t1=Template("SELECT t1.* FROM $table AS t1, $table AS t2 WHERE $dc_desc;")
dc_tuple_violation_template_t2=Template("SELECT t2.* FROM $table AS t1, $table AS t2 WHERE $dc_desc;")


def convert_dc_to_muse_rule(dc_text, target_table, role):
    predicates = dc_text.split('&')
#     clause = parse_rule_to_where_clause(dc_text)
    constants=[]

    for pred in predicates[2:]:
        attr = re.search(r't[1|2]\.([-\w]+)', pred).group(1)

    # constants_clause = ' AND '.join(constants)
    # print(f"dc_text:{dc_text}")
    if(non_symetric_op.search(dc_text)):
    	res = [dc_tuple_violation_template_t1.substitute(table=target_table, dc_desc=parse_rule_to_where_clause(dc_text)),\
    	dc_tuple_violation_template_t2.substitute(table=target_table, dc_desc=parse_rule_to_where_clause(dc_text))]
    else:
    	res = [dc_tuple_violation_template_t1.substitute(table=target_table, dc_desc=parse_rule_to_where_clause(dc_text))]
    return res



if __name__ == '__main__':

	# dc_file='/home/opc/chenjie/RBBM/experiments/dc/dc_sample_10'
	# table_name='adult'
	# res=[]
	# try:
	#     with open(dc_file, "r") as file:
	#     	for line in file:
	# 	    	rules_from_line = [(table_name, x) for x in convert_dc_to_muse_rule(line, 'adult', 't1')]
	# 	    	res.extend(rules_from_line)
	# except FileNotFoundError:
	#     print("File not found.")
	# except IOError:
	#     print("Error reading the file.")

	dc_file='/home/opc/chenjie/RBBM/experiments/dc/hospital_golden_rules.txt'
	table_name='hospital'
	res=[]
	try:
	    with open(dc_file, "r") as file:
	    	for line in file:
		    	rules_from_line = [(table_name, x) for x in convert_dc_to_muse_rule(line, 'hospital', 't1')]
		    	res.extend(rules_from_line)
	except FileNotFoundError:
	    print("File not found.")
	except IOError:
	    print("Error reading the file.")

	# test_rule='t1&t2&EQ(t1.occupation,t2.occupation)&EQ(t1.hours-per-week,t2.hours-per-week)&IQ(t1.race,t2.race)&IQ(t1.sex,t2.sex)'

	# print(res)
	print(res)