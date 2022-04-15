# Adapter Container Pattern
The adapter container is no different from the sidecar when it comes to the concept where both terms refer to another container running in the same Pod as the application container. The essence of both pattern is making changes to how the application container operates without changing its logic or modifying its code. **Using the Adapter Pattern, we establish a unified interface for our application container that can be used by a third-party service.**

![Adapter Container Pattarn](https://github.com/ishubhoshaha/k8-pattarn/blob/main/adapter/adapter_container_pattarn.png)

## When should we use this pattern? 
- Whenever you want to enhance the functionality of the existing single container pod without touching the existing one.
- When you need a unified/generic interface of your main container to interface with other system/app.
- When you want to standardize and normalize application output or monitoring data for aggregation.

## TL;DR
- Sidecar containers run in parallel with the main container. So that you need to consider resource limits of sidecar containers while defining request/resource limits for the pod.
- You should configure health checks for sidecar containers as main containers to make sure they are healthy.