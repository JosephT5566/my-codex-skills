# Containers, Cloud Run, and Kubernetes

Use this reference when a reviewed role or interview asks about Docker, containers, Cloud Run, Kubernetes, orchestration, deployment platforms, autoscaling, probes, networking, or when to choose managed serverless over a cluster. The target is informed product-engineering judgment, not unsupported cluster-administration claims.

## Core Mental Model

- A **container image** packages application code, runtime, and dependencies into a versioned artifact.
- A **container runtime** starts that image with environment-specific configuration, identity, network, and resource limits.
- **Cloud Run** is a managed platform for request-driven containers with built-in revision management and autoscaling, reducing infrastructure ownership.
- **Kubernetes** is a declarative orchestration control plane that continuously reconciles actual cluster state toward desired state across workloads, networking, configuration, storage, and policy.

Containers improve packaging consistency. They do not by themselves provide security, observability, high availability, correct scaling, or recovery.

## Container Fundamentals

- Use a small trusted base image, deterministic dependency installation, and multi-stage builds where they reduce size or build/runtime coupling.
- Run as a non-root numeric user when possible and avoid unnecessary packages and privileges.
- Keep secrets and environment configuration outside the image.
- Handle termination signals, graceful shutdown, health behavior, temporary storage, and writable filesystem assumptions explicitly.
- Record image identity and scan dependencies according to the risk and remediation capacity.

## Cloud Run Decision Model

Cloud Run is a strong default when:

- the workload fits stateless request or supported job execution
- managed TLS, revisioning, autoscaling, and scale-to-zero are valuable
- the team wants low platform overhead
- provider-specific networking and execution limits are acceptable

Important design questions include:

- minimum and maximum instances, concurrency, startup time, and database connection pressure
- request timeout and whether long work belongs in a durable job
- service identity, secret access, ingress, and authenticated invocation
- health/startup behavior, revision promotion, rollback, logs, metrics, and cost

## Kubernetes Concept Map

| Concept | Responsibility |
| --- | --- |
| Pod | Smallest scheduled unit; one or more tightly coupled containers |
| Deployment | Desired replicas and rolling rollout for stateless workloads |
| ReplicaSet | Maintains the replica count behind a Deployment |
| Service | Stable discovery and virtual endpoint for a set of Pods |
| Ingress / Gateway | External HTTP routing and policy, depending on the platform |
| ConfigMap / Secret | Runtime configuration; a Secret still requires access and encryption controls |
| Readiness probe | Whether a Pod should receive traffic |
| Liveness probe | Whether a stuck container should be restarted |
| Startup probe | Protects slow startup from premature liveness failure |
| Requests / limits | Scheduling expectations and resource boundaries |
| HPA | Adjusts replica count from measured signals; does not remove downstream limits |
| Job / CronJob | Finite or scheduled work |
| StatefulSet / volume | Stable identity or persistent storage for stateful workloads |
| Namespace / RBAC | Administrative and authorization boundaries, not complete isolation alone |
| NetworkPolicy | Allowed network paths when supported and correctly enforced |

## Reconciliation and Rollout

- Users declare desired state; controllers observe and reconcile toward it.
- A Deployment rolling update creates new Pods while maintaining availability according to rollout settings.
- Readiness prevents unready Pods from receiving Service traffic; liveness should detect unrecoverable stuck behavior, not ordinary dependency failure.
- Rollback restores an earlier workload specification, but it cannot automatically reverse incompatible schema or external side effects.
- Pod replacement is normal. Applications must not depend on local process memory or ephemeral filesystem for durable truth.

## Cloud Run Versus Kubernetes

| Decision | Cloud Run tends to fit | Kubernetes tends to fit |
| --- | --- | --- |
| Operational ownership | Team wants provider-managed platform | Team can own or buy cluster/platform operations |
| Workload shape | Stateless HTTP/event workloads and managed jobs | Diverse services, workers, protocols, scheduling, or daemon workloads |
| Scaling | Request-driven managed autoscaling is sufficient | Custom metrics, placement, topology, or fine-grained capacity control is needed |
| Networking | Managed ingress and simpler service boundaries fit | Complex east-west networking, gateways, or policy control is required |
| Portability/control | Provider abstraction is acceptable | Kubernetes ecosystem or control is a justified requirement |
| Cost/complexity | Lower operational overhead matters most | Added platform cost produces measurable value |

Do not choose Kubernetes merely for resume value, container count, or hypothetical future scale.

## Joseph Evidence Map

### Demonstrated professionally

- Collaborated in environments using Kubernetes and GitHub-based CI/CD/GitOps.
- Worked with platform engineers and production application tooling.
- This supports conceptual and collaborative familiarity, not cluster ownership.

### Implemented in projects

- Built and deployed a numeric non-root container for `english-learning`.
- Used Cloud Run revisions, managed TLS/ingress boundaries, workload identity, health checks, candidate verification, promotion, rollback, and Neon PostgreSQL.
- Considered startup, schema compatibility, authenticated smoke testing, secrets, and runtime identity.

### Current evidence boundary

- No demonstrated ownership of Kubernetes clusters, Helm-based release systems, controllers/operators, cluster networking, storage systems, upgrades, multi-cluster failover, or production autoscaling policy.
- Current strength is comparing managed container deployment with orchestration needs and collaborating across application/platform boundaries.

## Reusable Interview Answer

Use this structure:

1. Describe the workload, reliability, networking, and team-ownership requirements.
2. Explain the relevant container or orchestration concepts.
3. Compare the simplest managed option with Kubernetes.
4. Cover health, identity, configuration, resources, rollout, observability, and data compatibility.
5. Explain why added control is or is not worth the operational cost.
6. State the hands-on evidence boundary.

Example outline:

> Kubernetes is a declarative orchestration platform: controllers continuously reconcile workloads such as Deployments toward desired state, Services provide stable discovery, and probes and resource settings influence traffic, restart, scheduling, and scaling behavior. I would choose it when the workload needs diverse execution models, detailed networking or placement control, or a shared platform that justifies cluster operations. For my `english-learning` service, Cloud Run is the better tradeoff because it provides managed revisions, TLS, request-driven autoscaling, and lower operational overhead. I have hands-on container and Cloud Run release experience plus professional Kubernetes collaboration, but I would not claim production cluster administration.

## Learning and Proof Backlog

### High priority

- Be able to draw the request path through external routing, Service, Pod, application, and database, including identity, health, logs, and failure points.
- Practice distinguishing readiness, liveness, and startup probes with concrete failure scenarios.
- Explain requests, limits, horizontal scaling, database connection pressure, and why autoscaling can amplify downstream failure.
- Compare Cloud Run and Kubernetes for the actual `english-learning` workload and state the threshold that would justify migration.

### Medium priority

- Deploy a small disposable version of an existing service to a local or managed Kubernetes learning environment only if a recurring target role requires it.
- Exercise Deployment rollout, failed readiness, rollback, ConfigMap/Secret handling, a Job, resource settings, and log/metric inspection.
- Learn basic RBAC, namespace boundaries, NetworkPolicy, Pod disruption, and graceful termination conceptually and through one bounded lab.
- Learn Helm or Kustomize only after understanding the underlying Kubernetes objects they render.

### Lower priority unless targeting platform roles

- Cluster provisioning and upgrades, CNI/CSI internals, service mesh, custom controllers/operators, multi-cluster topology, advanced scheduling, and etcd recovery.

### Evidence to capture

- Container build and security decisions.
- Platform comparison with workload assumptions and cost/complexity tradeoffs.
- A small deployment manifest or lab showing probes, resources, rollout, and failure recovery.
- Clear separation between local lab evidence, deployed project evidence, and professional collaboration.

## Readiness Standard

Use `Good` for product/full-stack roles when Joseph can explain orchestration and choose appropriately between Cloud Run and Kubernetes. Use `Needs Improvement` for platform roles until hands-on cluster operations and networking/observability ownership are demonstrated. Do not upgrade readiness because a local tutorial was completed once.
