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


update replicaset
kubectl scale --replica=30 deployment/<deploymentname>

OSI layer 7 -> alb
OSI layer 4 -> nlb
OSI layer 7 and 4 -> clb


