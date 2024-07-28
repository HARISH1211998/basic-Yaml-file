Kubernetes Commands Cheat Sheet Pod
Get Logs for a Pod:

**kubectl logs <pod-name>**

Describe a Pod:
**kubectl describe pod <pod-name>**

View History of Changes for a Pod:
**kubectl rollout history pod <pod-name>**

Monitor Pod Metrics:
**kubectl top pod <pod-name>**

ReplicaSet
Get Logs for ReplicaSet Pods:
**kubectl logs -l app=<app-label>**

Describe a ReplicaSet:
**kubectl describe replicaset <replicaset-name>**

View History of Changes for a ReplicaSet:
**kubectl rollout history replicaset <replicaset-name>**

Monitor ReplicaSet Metrics:
**kubectl top replicaset <replicaset-name>**

Deployment
Get Logs for Deployment Pods:
**kubectl logs -l app=<app-label>**

Describe a Deployment:
**kubectl describe deployment <deployment-name>**

View History of Changes for a Deployment:
**kubectl rollout history deployment <deployment-name>**

Monitor Deployment Metrics:
**kubectl top deployment <deployment-name>**

DaemonSet
Get Logs for DaemonSet Pods:
**kubectl logs -l app=<app-label>**

Describe a DaemonSet:
**kubectl describe daemonset <daemonset-name>**

View History of Changes for a DaemonSet:
**kubectl rollout history daemonset <daemonset-name>**

Monitor DaemonSet Metrics:
**kubectl top daemonset <daemonset-name>**

Revision Process 
we can easliy rollback all the template

Order By -> config Map, secret, Deployment, Service

NodePort Range -> 30000 into 32767

Port -> Service Port
Target Port -> Container Port
NodePort -> Worker Node

kubectl expose pod <pod name> --type=NodePort --port=80 --name=my-first-service

kubectl get pod -o wide

Logs:
   1. kubectl logs -l name=mylabels --all-containers
   2. kubectl logs my-pods --previous
   3. kubectl logs my-pods -c my-container

To check the env:
kubectl exec -it my-first-pod env

yaml output:
kubectl get pods <pod name> -o yaml

Deployment:
kubectl set image deployment/<daployment name> imagename=imageversion --record=true
kubectl rollout status deployment/mydeploymentname
kubectl rollout history deployment/deployment name --revision=1

Pasues and Resume:
kubectl rollout pause deployment/deployment-name
kubectl rollout resume deployment/deploymentname

kubernetes service:
    1. ClusterIP
    2. nodeport
    3. load balancer
    4. ingress
    5. external name

PV and PVC
PVC -> namespace object
pv -> cluster based object
If your deleting the pod volume can't be deleted
kubectl get pods -w # w for watch mode

probes type:
liveness -> kubelet will check the pod alive state, liveness props could catch the deadlock
readness -> kubelet will see the container is ready to accept the traffics
startup -> it will be disable the liveness and readness probes, it will major use for slow startup container to avoid to restart the container again and again

Request and Limit:
Request -> minimum cpu and memory (500m, 128Mi)
limit -> maximum cpu and memory (1000m, 256mi)

LimitRange
It will be implemented by namespace level
default: max
defaultRequest: min

ResourceQuote
if we set something in resourcequote we can able to run into, for example pod =5 you can't run more than 5 pods in that namespace


Namespace -> isolated boundary for our kubernetes cluster
we use request and limit as per resource quote allocation in kubernetes.

update replicaset
kubectl scale --replica=30 deployment/<deploymentname>

OSI layer 7 -> alb
OSI layer 4 -> nlb
OSI layer 7 and 4 -> clb


