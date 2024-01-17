Kubernetes Commands Cheat Sheet
Pod
Get Logs for a Pod:

bash
Copy code
kubectl logs <pod-name>
Describe a Pod:

bash
Copy code
kubectl describe pod <pod-name>
View History of Changes for a Pod:

bash
Copy code
kubectl rollout history pod <pod-name>
Monitor Pod Metrics:

bash
Copy code
kubectl top pod <pod-name>
ReplicaSet
Get Logs for ReplicaSet Pods:

bash
Copy code
kubectl logs -l app=<app-label>
Describe a ReplicaSet:

bash
Copy code
kubectl describe replicaset <replicaset-name>
View History of Changes for a ReplicaSet:

bash
Copy code
kubectl rollout history replicaset <replicaset-name>
Monitor ReplicaSet Metrics:

bash
Copy code
kubectl top replicaset <replicaset-name>
Deployment
Get Logs for Deployment Pods:

bash
Copy code
kubectl logs -l app=<app-label>
Describe a Deployment:

bash
Copy code
kubectl describe deployment <deployment-name>
View History of Changes for a Deployment:

bash
Copy code
kubectl rollout history deployment <deployment-name>
Monitor Deployment Metrics:

bash
Copy code
kubectl top deployment <deployment-name>
DaemonSet
Get Logs for DaemonSet Pods:

bash
Copy code
kubectl logs -l app=<app-label>
Describe a DaemonSet:

bash
Copy code
kubectl describe daemonset <daemonset-name>
View History of Changes for a DaemonSet:

bash
Copy code
kubectl rollout history daemonset <daemonset-name>
Monitor DaemonSet Metrics:

bash
Copy code
kubectl top daemonset <daemonset-name>