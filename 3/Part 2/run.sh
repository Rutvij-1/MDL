policy_file_name=2019111032_2019111013d.policy
model_file_name=2019111032_2019111013d.pomdp
statistics_file_name=statistics_d.txt
python3 part2.py 2019111013 4 $model_file_name > output_d.txt
cd sarsop/src/
./pomdpsol ../../$model_file_name -o ../../$policy_file_name
./pomdpeval ../../$model_file_name --policy-file ../../$policy_file_name --simLen 50 --simNum 500 > ../../temp.txt
./pomdpeval ../../$model_file_name --policy-file ../../$policy_file_name --simLen 50 --simNum 500 > ../../$statistics_file_name
cd ../../
rm temp.txt