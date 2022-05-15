# Pilot Tier Random Assignment Generator

# Task

I have chosen to base this project around imaginary pilots who fly in the online game Star Wars: Squadrons.  The application will randomly create pilot names and then assign them random tiers.  Tiers range from S being the highest possible tier (a very loose grading of pilot skill - aces if you will) to D Tier (novices/cadets).  

The app will comprise four services.  Service 1 acts as a Front End for Service 2 and 3.  Service 2 and 3 relate to the Pilot and Tier assignment categories.  Essentially each application assigns a random choice from a list of possible choices (in string format) for both the "Pilot" and "Tier" categories and then provides these to the Front End which in turn displays them using render templates.  The Front End then provides Service 4 with a combination of the strings generated by Services 2 and 3 in the form of a JSON.  Some conditional logic is applied - certain tiers receive predetermined accompanying messages depending on the tier.  All this is then relayed back to the front end and displayed.

# Project specs

1. Trello Board or equivalent
2. Application with a feature-branch model VCS
3. Application built through a CI server and deployed to a cloud-based virtual machine. 
4. Webhooks such that Jenkins rebuilds and redeploys the newest version of the application whenever the main branch is updated (i.e. a change to the codebase)
5. Project uses Service-Oriented architecture: both containerisation and an orchestration tool.
6. An Ansible Playbook that provisions the environment needed for the application to run.
7. A reverse proxy to make the application accessible to the user.

**List of Required Technologies**

Trello Board <br />
Orchestration Tool: *Docker Swarm* <br />
Version Control: *Git* <br /> 
CI Server: *Jenkins* <br />
Configuration Management: *Ansible* <br />
Cloud server: *GCP virtual machines* <br />
Reverse Proxy: *NGINX* <br />
Containerisation: *Docker* <br />

# Trello Board

I used a trello board during this project for planning and prioritisation of tasks.  Each week was treated as a separate sprint with its own backlog.

[Trello Board](https://trello.com/b/ufgHK3VC/pilot-tiers)

<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Practical-Project/blob/ansible/images/Project%202%20trello.JPG" width="1000"/>
</p>

# Risk Assessment

[Risk Assessment](https://docs.google.com/spreadsheets/d/1SNXdg196MBaFU69MoC1mMkt9sLWLh0RzoJxBbpi-0C8/edit#gid=0)

<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Practical-Project/blob/ansible/images/Project%202%20Risk%20Assessment.JPG" width="2000"/>
</p>

# Description of services

Service 1 aka front_end_api is what is displayed using render_template to my index.html.  pilot_api assigns a pilot name chosen at random from a list.  tier_api does the same but this time for the tier.  The front end uses a get request to access these strings and then sends them to service_4 (which itself receives HTTP POST requests from the front end) where the additional logic is applied regarding which message to assign a given pilot and tier.  The message, tier and pilot are then returned as a json which in turn the front end uses when displaying a final statement including all the randomly generated information via render_template.  A reverse proxy using an NGINX service directs traffic from port 80 on the host to port 5000 on the front-end_api container.  Please see my presentation video linked below for further clarification.

# Diagram of services and how they interact

<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Practical-Project/blob/ansible/images/Services%20Diagram.jpg" width="800"/>
</p>

# CDP (Continuous Deployment Pipeline)

A key required facet of the project is one of continous deployment, such that the end user may access the app and not experience any downtime or loss of service in the event changes to the codebase are being made through successive builds - essentially simulating how an app would function in the wild, albeit an extremely paired down version of one.  In order to meet this objective we use a combination of tools, namely Docker, Docker-Swarm, Jenkins and Ansible.  Once the app is functional and can be run using a docker-compose file, Dockerfiles for the respective services and an Nginx reverse-proxy, we can go about deploying it in a pipeline environment.  Firstly, the repo is uploaded to Github.  Secondly, we set up a Jenkins VM and configure a Jenkins Pipeline Job using our new repo.  Using a Jenkinsfile in our repo, we can lay out the various stages we require to test, build and deploy our app.

# Testing Stage

We include a tests folder in each of the respective services containing a test_ unit test relating to its parent service.  Is the service reachable (do we get a 200 response) and are we getting back the data we put in in the way we expect?  The testing process is the first stage in the Jenkinsfile.  We need to make sure all the individual components are working in the way we want them to before we instruct Jenkins to build our app.  The testing process is therefore a necessary first stage in continuous deployment.  The below image shows the testing coverage attained in the project:

<p align="center">
<img src="https://github.com/Harry84/DevOps-Core-Practical-Project/blob/ansible/images/testing%20project%202.JPG" width="700"/>
</p>

# Build Stage

This is where we instruct Jenkins via the Jenkinsfile (which it knows to look for in the repo we have provided a link to on our Github) to build the images for our services and then to push them to Dockerhub.  To do so we need to set our Dockerhub username and password as environment variables.  Prior to this we will need to have stored them via secret text files in Jenkins Credentials.  These named secret text files are then called when setting the environment variables we need to login to Dockerhub.  Once we are successfully logged in we can give the command to push our newly built images up to our Dockerhub account.

# Deploy Stage

This is where Ansible is used to simplify the process of deployment.  Now we have our images ready to go, we have to decide how we want to deploy our app.  If we'd like to deploy using Docker-Swarm, Ansible provides a useful framework for specifying how.  If we'd like to use an Nginx load-balancer, Ansible lets us specify how.  This is achieved using Ansible through the use of a playbook, an inventory and various roles.  Therefore we install Ansible onto our Jenkins VM.

In our use case, the playbook describes the steps to follow to deploy the swarm.  The inventory describes the configuration of the swarm.  Which VMs are to be used - which will act as manager and which will act as worker - what are the exact host names for these?  In terms of the playbook, there is a logical order to be followed.  Firstly we must provision all machines (managers and workers) with Docker.  Therefore we define a dockerinstall role, the task within which sets out all the commands required to install docker including any dependencies.  This new role necessarily goes in a "roles" folder next to the playbook.yaml and inventory.yaml files in the folder heirachy.  The next logical step is to initialise the swarm on the manager node.  So we specify this in the playbook using a manger type role with its own respective task.  Next we instruct any worker nodes to join the swarm (again by way of a task in an accompanying worker type role, named swarm-join or similar), by providing the necessary swarm info and join tokens in the same order of events as if we were setting up a swarm manually.

The Jenkins user needs a way of accessing the manager node and worker node in order to place the necessary docker-compose.yaml file there and to configure Nginx.  We do this via an SSH key pair we generate on the Jenkins VM (where Ansible is installed).  This allows the jenkins user to SSH in before finally running the Ansible playbook.  In terms of replicas, these are defined in the docker-compose.yaml file.

# Rolling Update

Having multiple replicas for each service running across a Manager and Worker node enables a rolling update.  Firstly we configure a webhook for our Jenkins job/pipeline.  This is done under settings on our Github repo, where we supply the ip for our Jenkins VM.  We want a new build to trigger every time a push event occurs on whatever branch we have specified in our Jenkins job/pipeline configuration.  This means if ever a new version of the app is rolled out (by pushing it from the dev branch to main), a new build is triggered in the Jenkins Pipeline.  The replicas then receive the new changes one by one meaning that there are always a number of replicas with a version of the codebase running, thereby keeping the app in continuous delivery whilst allowing it to be updated at the same time.  Please find a quick demo of this in action in my presentation video below.

# Future Developments

A enxt step would be the inclusion of a database to persist data.  I would also like to add external data sources to populate it such as excel files using actual squadrons league data.  This would allow the creation of tier lists based on real data which could then be compared to more subjective tier lists to identify a difference in percieved ability and more objective measures of actual performance.  This as well as providing a source of entertainment could provide the Squadrons community valuable insight and act as a prototype for other games to drive community engagement.  Eventually it could be a basis for a tier list creation app that might include random elements for entertainment value or in turn act as a basis for a kind of top trumps or fantasy league type game.

# Acknowledgements

Thanks to all the QA tutors along the way who provided much needed guidance!

# Video Demo

[Video Demo](https://youtu.be/StPZ4MkuYBw)

