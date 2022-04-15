# Sidecar Container Pattarn
Sidecar container pattern **extends and enhances** the functionality of app/main containers without changing it. Imagine that you have the pod with a single container working very well and you want to add some functionality to the current container without touching or changing, how can you add the additional functionality or extending the current functionality? This sidecar container pattern really helps exactly in that situation.

## When should we use this pattern? 
- Whenever you want to enhance the functionality of the existing single container pod without touching the existing one.
- You can use this pattern to synchronize the main container code with the git server pull.
- You can use this pattern for sending log events to the external server.
- You can use this pattern for network-related tasks.

## TL;DR
- Sidecar containers run in parallel with the main container. So that you need to consider resource limits of sidecar containers while defining request/resource limits for the pod.
- You should configure health checks for sidecar containers as main containers to make sure they are healthy.