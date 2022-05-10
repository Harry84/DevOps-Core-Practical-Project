!/bin/bash

rsync docker-compose.yaml nginx.conf swarm-manager:

ssh swarm-manager << EOF
docker stack deploy --compose-file docker-compose.yaml pilot-tier-generator
EOF

'''
sh "scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml swarm-manager:/home/jenkins/docker-compose.yaml"
sh "scp -i ~/.ssh/ansible_id_rsa nginx.conf swarm-manager:/home/jenkins/nginx.conf"
sh "ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"
'''



            