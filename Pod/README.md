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
