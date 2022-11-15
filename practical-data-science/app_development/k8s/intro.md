# Kubernetes

Kubernetes (k8s) is a container orchestration tool, typically used for 
managing Docker containers.

The rise of Kubernetes has been due to the trend of moving from Monolith to 
Microservice applications. The increased the use of containers requires 
software for managing them. 

The key features of kubernetes are {cite:p}``:
- High availability or no downtime
- Scalability or high performance
- Disaster recovery - backup and restore

The k8s architecture is always comprised of a master node (a virtual or 
physical machine) and worker nodes, each running a kubelet process. This is 
the process that makes it possible for nodes to communicate with one 
another. Each node can have different processes running on them (e.g. 
multiple containers).

The master node itself runs the most important functions of the cluster. It 
has an API server which has a UI, an API and a CLI.
It has a controller manager and a scheduler (based on workload can schedule 
using the worker nodes). Has an etcd key value storage, containing a 
backing store (this is where the disaster recovery works).

Between the master and worker nodes, there is a virtual network.

You should always have a backup of the master node, because if it fails 
then your whole processes will fail.

- pod
- service
- ingress
- ConfigMap
- Secret
- Deployment
- StatefulSet
- DaemonSet

- Pod: an abstraction over a container. This abstraction enables you to use 
  any containers that you wish, e.g. not necessarily Docker. Typically, a 
  pod will only contain 1 application. Each pod has an internal IP address. 
  When a pod crashes, then k8s master node restarts it, however this gets a 
  brand new IP address. You therefore can't guarantee access to a pod using 
  the IP Address.
- Service: a static IP address that can be attached to each pod. Therefore, 
  if a pod dies, then the internal IP address will be updated and will point 
  to the static IP address.
- Ingress: 


