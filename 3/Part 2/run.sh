rno=2019111013
policy_file_name=2019111032_2019111013.policy
model_file_name=2019111032_2019111013.pomdp
statistics_file_name=statistics.txt
policy_gen_output=policy_gen_output.txt
python3 part2.py $rno 1 $model_file_name > output.txt
cd sarsop/src/
./pomdpsol ../../$model_file_name -o ../../$policy_file_name > ../../$policy_gen_output
./pomdpeval ../../$model_file_name --policy-file ../../$policy_file_name --simLen 50 --simNum 500 > ../../temp.txt
./pomdpeval ../../$model_file_name --policy-file ../../$policy_file_name --simLen 50 --simNum 500 > ../../$statistics_file_name
cd ../../
policy_file_name=2019111032_2019111013_b.policy
model_file_name=2019111032_2019111013_b.pomdp
statistics_file_name=statistics_b.txt
policy_gen_output=policy_gen_output_b.txt
python3 part2.py $rno 2 $model_file_name > output_b.txt
cd sarsop/src/
./pomdpsol ../../$model_file_name -o ../../$policy_file_name > ../../$policy_gen_output
./pomdpeval ../../$model_file_name --policy-file ../../$policy_file_name --simLen 50 --simNum 500 > ../../temp.txt
./pomdpeval ../../$model_file_name --policy-file ../../$policy_file_name --simLen 50 --simNum 500 > ../../$statistics_file_name
cd ../../
policy_file_name=2019111032_2019111013_d.policy
model_file_name=2019111032_2019111013_d.pomdp
statistics_file_name=statistics_d.txt
policy_gen_output=policy_gen_output_d.txt
python3 part2.py $rno 4 $model_file_name > output_d.txt
cd sarsop/src/
./pomdpsol ../../$model_file_name -o ../../$policy_file_name > ../../$policy_gen_output
./pomdpeval ../../$model_file_name --policy-file ../../$policy_file_name --simLen 50 --simNum 500 > ../../temp.txt
./pomdpeval ../../$model_file_name --policy-file ../../$policy_file_name --simLen 50 --simNum 500 > ../../$statistics_file_name
cd ../../
rm temp.txt