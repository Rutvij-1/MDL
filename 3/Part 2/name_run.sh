name=zishan
rno=2019111031
mkdir $name
policy_file_name=$name/$rno.policy
model_file_name=$name/$rno.pomdp
statistics_file_name=$name/statistics.txt
policy_gen_output=$name/policy_gen_output.txt
python3 part2.py $rno 1 $model_file_name > $name/output.txt
cd sarsop/src/
./pomdpsol ../../$model_file_name -o ../../$policy_file_name > ../../$policy_gen_output
./pomdpeval ../../$model_file_name --policy-file ../../$policy_file_name --simLen 50 --simNum 500 > ../../temp.txt
./pomdpeval ../../$model_file_name --policy-file ../../$policy_file_name --simLen 50 --simNum 500 > ../../$statistics_file_name
cd ../../
file_extension=_b
policy_file_name=$name/$rno$file_extension.policy
model_file_name=$name/$rno$file_extension.pomdp
statistics_file_name=$name/statistics$file_extension.txt
policy_gen_output=$name/policy_gen_output$file_extension.txt
python3 part2.py $rno 2 $model_file_name > $name/output$file_extension.txt
cd sarsop/src/
./pomdpsol ../../$model_file_name -o ../../$policy_file_name > ../../$policy_gen_output
./pomdpeval ../../$model_file_name --policy-file ../../$policy_file_name --simLen 50 --simNum 500 > ../../temp.txt
./pomdpeval ../../$model_file_name --policy-file ../../$policy_file_name --simLen 50 --simNum 500 > ../../$statistics_file_name
cd ../../
file_extension=_d
policy_file_name=$name/$rno$file_extension.policy
model_file_name=$name/$rno$file_extension.pomdp
statistics_file_name=$name/statistics$file_extension.txt
policy_gen_output=$name/policy_gen_output$file_extension.txt
python3 part2.py $rno 4 $model_file_name > $name/output$file_extension.txt
cd sarsop/src/
./pomdpsol ../../$model_file_name -o ../../$policy_file_name > ../../$policy_gen_output
./pomdpeval ../../$model_file_name --policy-file ../../$policy_file_name --simLen 50 --simNum 500 > ../../temp.txt
./pomdpeval ../../$model_file_name --policy-file ../../$policy_file_name --simLen 50 --simNum 500 > ../../$statistics_file_name
cd ../../
rm temp.txt