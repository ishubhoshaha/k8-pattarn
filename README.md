# Multi-Container Pod Design Patterns in Kubernetes

### Multi-container pods are extremely useful for specific purposes in Kubernetes. While it’s not always necessary to combine multiple containers into a single pod, knowing the right patterns to adopt creates more robust Kubernetes deployments.

- Sidecar pattern: An extra container in your pod to enhance or extend the functionality of the main container.
- Ambassador pattern: A container that proxy the network connection to the main container.
- Adapter pattern: A container that transform output of the main container.

