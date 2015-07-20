Pandoc Report
=============


Pandoc Container with Mustache template for MGMIC metegenomic workflow.

docker build -t mgmic/report .


Example

docker -d -v /data:/data -f << forward read file >> -r << reverse read file >> -t << task_id >>


The report will be placed in the mgmic_tasks folder under the task_id.
