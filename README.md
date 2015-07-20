Pandoc Report
=============


Pandoc Container with Mustache template for MGMIC metegenomic workflow.

docker build -t mgmic/report .


Example

docker run -d -v /data:/data  mgmic/report make_report -f VIGDIS3_forward_paired.50K.fq  -r VIGDIS3_reverse_paired.50K.fq -t c5553b13-2493-4c53-ab27-f58227eee417

Example Output : http://mgmic.oscer.ou.edu/mgmic_tasks/c5553b13-2493-4c53-ab27-f58227eee417/report.html

The report will be placed in the mgmic_tasks folder under the task_id.
