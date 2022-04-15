# Ambassador Pattarn
Ambassador container pattern is a special form of sidecar containers, where sidecar containers used as a proxy between the application container and one or more outside services. The Ambassador container forms an abstraction layer so that the application developer can focus on the application itself without worrying about the infrastructure connectivity details.

![Ambassador Container Pattarn](https://github.com/ishubhoshaha/k8-pattarn/blob/main/ambassador/ambassador_container_pattarn.png)

## When should we use this pattern? 
- Whenever your containerized services want to talk to external serivces you can use this pattarn to handle request and response for these services.
- Whenever there is a need to convert or standardize the format of external services responses.

## TL;DR
- Ambassador containers run in parallel with the main container. So that you need to consider resource limits of ambassador containers while defining request/resource limits for the pod.
- You should configure health checks for Ambassador containers as main containers to make sure they are healthy.
