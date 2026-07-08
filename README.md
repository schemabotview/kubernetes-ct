# kubernetes-ct

Video-first content for the **Kubernetes** concept, consumed at runtime by the
[`graphl-movie`](../graphl-movie) app. Content only — notebooks, narration (`.tts` →
`.wav`), authored one-screen slides (`.slide`: a `# Title`, `## ` sub-labels, short prose,
fenced code, and `- `/numbered lists with **bold** key terms), and the wiring
`manifest.json`. Nothing to build or run here. For the authoring contract and folder
layout, see [`CLAUDE.md`](./CLAUDE.md).

This file is the **course outline** — the human-facing map of modules and sections. It is
the plan we author against; the machine source of truth for structure is `manifest.json`
(once authored).

**Status:** scaffolded + full section spine settled (10 modules × 10 = **100 sections**,
all mapped to a real `k8s-*` scene node). The `kubernetes` scene is **not yet ported** into
graphl-movie (next step: port `../graphl-ux/src/scenes/kubernetes.ts` →
`../graphl-movie/src/scenes/kubernetes.ts`, register + add the `kubernetes` concept to
`catalog.ts`). No sections authored yet (`notebooks/`, `tts/`, `slides/` empty); `audio/`
empty pending the owner's Colab run; nothing pushed. (Slides lead with a single `#` title;
`##` for sub-labels.)

## The scene — one dense map, framed per section

Every Kubernetes module rides a **single dense scene**, `kubernetes` (app-owned, ported into
graphl-movie from `../graphl-ux/src/scenes/kubernetes.ts`). It is the whole Kubernetes
platform on one 16:9 map — two bands:

- **TOP (spine):** **Client** (`kubectl` verbs) → **Cluster** (Control Plane
  `kube-apiserver · etcd · scheduler · controller-manager · cloud-controller-mgr` · Worker
  Node = Node runtime `kubelet · kube-proxy · CRI` + Pods) → **Registry**.
- **BOTTOM (detail):** **Workloads** (Pod spec · Workload kinds · Rollout) · **Resources**
  (Storage · Networking · Config) · **Operate** (Scheduling · RBAC · Security).

Geometry is the lesson: the `kube-apiserver` sits at the center of the control plane —
every kubectl verb points at it, the scheduler/controllers watch it, the kubelet executes
its decisions, and every workload/resource/policy resolves onto the Pods it governs. Each
module frames one band/subsystem of that map via per-section `focus` (camera) + `highlight`
(spotlight in-place, the rest dims), so the learner keeps one mental model the whole course.
**§1 of each module is the hook — the full map** (no focus), the picture the rest of the
module zooms into.

## Module spine (from `../kubernetes-content`)

The source curriculum is the **10-module beginner-to-CKA Kubernetes path** in
`../kubernetes-content` (the graphl-ux-era repo, source of truth for the notebook split).
The reader has finished the `docker` concept but has never touched Kubernetes. The video set
keeps all 10 modules, each normalized to **~10 tight teaching sections** (a section = one
narrated slide + scene focus, ≈ one page). The source notebooks run 10–15 `## ` headings
each; we consolidate fine-grained reference beats and drop the per-module "Cleaning up"
scaffolding to land near ~10.

| # | Module | Source notebook (`../kubernetes-content`) | `## ` in source | Scene | Frames (`k8s-*` anchors) |
|---|---|---|---|---|---|
| 01 | Getting Started with Kubernetes | `01-getting-started-with-kubernetes.ipynb` | 13 | `kubernetes` | whole map (hook) → `k8s-client` · `k8s-cluster` · `k8s-pods` |
| 02 | Pods, Labels & the Object Model | `02-pods-labels-and-the-object-model.ipynb` | 12 | `kubernetes` | `k8s-workloads` → `k8s-pod-kind` (`k8s-pod-init`/`k8s-pod-sidecar`/`k8s-pod-probes`) |
| 03 | Deployments, ReplicaSets & Rollouts | `03-deployments-replicasets-and-rollouts.ipynb` | 10 | `kubernetes` | `k8s-workload-kinds` (`k8s-deployment`/`k8s-replicaset`/…) + `k8s-rollout` |
| 04 | Services, DNS & Service Discovery | `04-services-dns-and-service-discovery.ipynb` | 11 | `kubernetes` | `k8s-networking` → `k8s-service` · `k8s-dns` · `k8s-kube-proxy` |
| 05 | ConfigMaps, Secrets & Environment | `05-configmaps-secrets-and-environment.ipynb` | 12 | `kubernetes` | `k8s-config` → `k8s-configmap` · `k8s-secret` · `k8s-cfg-env` |
| 06 | Storage: Volumes, PVs & PVCs | `06-storage-volumes-pvs-and-pvcs.ipynb` | 11 | `kubernetes` | `k8s-storage` → `k8s-pv`/`k8s-pvc`/`k8s-sc`/`k8s-csi` |
| 07 | Scheduling: Resources, Affinity, Taints | `07-scheduling-resources-affinity-taints-tolerations.ipynb` | 13 | `kubernetes` | `k8s-scheduling` (`k8s-nodeselector`/`k8s-affinity`/`k8s-taints`/…) + `k8s-scheduler` |
| 08 | Cluster Architecture & kubeadm | `08-cluster-architecture-and-kubeadm.ipynb` | 12 | `kubernetes` | `k8s-control-plane` (`k8s-apiserver`/`k8s-etcd`/…) + `k8s-node-runtime` |
| 09 | Networking, Ingress & Network Policies | `09-networking-ingress-and-network-policies.ipynb` | 13 | `kubernetes` | `k8s-networking` → `k8s-service`/`k8s-ingress`/`k8s-netpol`/`k8s-dns` |
| 10 | RBAC, Security, Troubleshooting & CKA Prep | `10-rbac-security-troubleshooting-and-cka-prep.ipynb` | 15 | `kubernetes` | `k8s-rbac` + `k8s-security`, then whole-map troubleshooting synthesis |

The "Frames" column is the **intended** wiring (which subsystem of the one `kubernetes` map
each module zooms into) — recorded here to guide section authoring; the authoritative
per-section `focus`/`highlight` lands in `manifest.json`.

## Sections

Each module is normalized to **~10 tight teaching sections**. **§1 is the hook** — it rides
the whole `kubernetes` map (no camera `focus`); §2–N each `focus` one `k8s-*` box and
`highlight` the relevant nodes. Merges/drops consolidate the fine-grained source beats (and
drop the per-module "Cleaning up").

The full per-module spine is settled below (all 10 modules, 100 sections). Each source
notebook's `## ` headings were consolidated to ~10 tight video sections; the "focus →
highlight" column names the `k8s-*` node(s) each section frames. These are the agreed plan;
content is then **authored one reviewed slice at a time** (see the working agreement in
`CLAUDE.md`), and `manifest.json` becomes the machine source of truth once authored.

### 01 — Getting Started with Kubernetes  ⬜ planned (10)
Establishes "you are here" on the whole map — what Kubernetes is, the kubectl → api-server →
control-loop → pod flow, and the first commands. Source: 13 `## ` headings → 10.

| # | Section | slug | focus → highlight |
|---|---|---|---|
| 1 | What Kubernetes is — and the shape of the whole platform | `01-01-what-kubernetes-is` | **hook** — whole map |
| 2 | The orchestration problem — what Docker alone doesn't solve | `01-02-orchestration-problem` | `k8s-cluster` |
| 3 | The cluster at 30,000 feet | `01-03-the-cluster` | `k8s-cluster` → `k8s-control-plane`,`k8s-worker` |
| 4 | The pod — Kubernetes' smallest unit | `01-04-the-pod` | `k8s-pods` |
| 5 | Getting a local cluster | `01-05-local-cluster` | `k8s-cluster` |
| 6 | Your first pod — `kubectl run` | `01-06-first-pod` | `k8s-kubectl` → `k8s-pods` |
| 7 | How `kubectl` actually works *(+ anatomy of a command)* | `01-07-how-kubectl-works` | `k8s-client` → `k8s-apiserver` |
| 8 | The core pod lifecycle | `01-08-pod-lifecycle` | `k8s-pods` |
| 9 | Imperative vs declarative | `01-09-imperative-vs-declarative` | `k8s-kc-apply` → `k8s-apiserver` |
| 10 | Getting help & cleaning up | `01-10-help-and-cleanup` | `k8s-kubectl` |

### 02 — Pods, Labels & the Object Model  ⬜ planned (10)
Frames the `k8s-workloads` band → `k8s-pod-kind` (the pod spec: init/sidecar/probes) and the
object-model plumbing at the api-server. Source: 12 `## ` headings → 10 (drop "Cleaning up").

| # | Section | slug | focus → highlight |
|---|---|---|---|
| 1 | Pods, labels & the object model | `02-01-pods-and-object-model` | **hook** — whole map |
| 2 | The Kubernetes object model | `02-02-object-model` | `k8s-apiserver` → `k8s-etcd` |
| 3 | Anatomy of a Pod manifest | `02-03-pod-manifest` | `k8s-pod-kind` → `k8s-pod-containers` |
| 4 | Pod phases, conditions & container states | `02-04-pod-phases` | `k8s-pods` |
| 5 | Restart policy | `02-05-restart-policy` | `k8s-pods` |
| 6 | Init containers | `02-06-init-containers` | `k8s-pod-kind` → `k8s-pod-init` |
| 7 | Multi-container pods — the sidecar pattern | `02-07-sidecar` | `k8s-pod-kind` → `k8s-pod-sidecar` |
| 8 | Probes — liveness, readiness, startup | `02-08-probes` | `k8s-pod-kind` → `k8s-pod-probes` |
| 9 | Labels & selectors | `02-09-labels-and-selectors` | `k8s-workloads` |
| 10 | Annotations & namespaces | `02-10-annotations-namespaces` | `k8s-cluster` |

### 03 — Deployments, ReplicaSets & Rollouts  ⬜ planned (10)
Frames the `k8s-workload-kinds` region + `k8s-rollout` — the controllers that keep N pods
alive and ship new versions. Source: 10 `## ` headings → 10 (drop "Cleaning up", add hook).

| # | Section | slug | focus → highlight |
|---|---|---|---|
| 1 | Deployments, ReplicaSets & rollouts | `03-01-deployments-overview` | **hook** — whole map |
| 2 | Why bare pods aren't enough | `03-02-why-not-bare-pods` | `k8s-pods` |
| 3 | ReplicaSet — keeping N pods alive | `03-03-replicaset` | `k8s-workload-kinds` → `k8s-replicaset` |
| 4 | Why you almost never write a ReplicaSet directly | `03-04-why-not-replicaset` | `k8s-workload-kinds` → `k8s-deployment`,`k8s-replicaset` |
| 5 | Anatomy of a Deployment manifest | `03-05-deployment-manifest` | `k8s-workload-kinds` → `k8s-deployment` |
| 6 | Scaling — changing the desired count | `03-06-scaling` | `k8s-kc-scale` → `k8s-replicaset` |
| 7 | Rolling updates — a new version, no downtime | `03-07-rolling-updates` | `k8s-rollout` → `k8s-ro-rolling` |
| 8 | Rollout history & rollback | `03-08-rollout-history` | `k8s-kc-rollout` → `k8s-deployment` |
| 9 | Update strategies — `RollingUpdate` vs `Recreate` | `03-09-update-strategies` | `k8s-rollout` → `k8s-ro-rolling`,`k8s-ro-recreate` |
| 10 | The rest of the workload family | `03-10-workload-family` | `k8s-workload-kinds` → `k8s-statefulset`,`k8s-daemonset`,`k8s-job`,`k8s-cronjob` |

### 04 — Services, DNS & Service Discovery  ⬜ planned (10)
Frames the `k8s-networking` band → `k8s-service` · `k8s-dns` · `k8s-kube-proxy`. Source: 11
`## ` headings → 10 (drop "Cleaning up").

| # | Section | slug | focus → highlight |
|---|---|---|---|
| 1 | Services, DNS & service discovery | `04-01-services-overview` | **hook** — whole map |
| 2 | Why Services exist | `04-02-why-services` | `k8s-networking` → `k8s-service` |
| 3 | The Service abstraction — stable identity by selector | `04-03-service-abstraction` | `k8s-service` → `k8s-pods` |
| 4 | `port`, `targetPort`, `nodePort` — the three numbers | `04-04-the-three-ports` | `k8s-service` |
| 5 | Endpoints & EndpointSlices | `04-05-endpoints` | `k8s-service` → `k8s-pods` |
| 6 | Service types — ClusterIP, NodePort, LoadBalancer, ExternalName | `04-06-service-types` | `k8s-service` |
| 7 | How `kube-proxy` actually routes traffic | `04-07-kube-proxy` | `k8s-kube-proxy` → `k8s-service` |
| 8 | DNS in Kubernetes — CoreDNS | `04-08-dns-coredns` | `k8s-networking` → `k8s-dns` |
| 9 | Headless Services — DNS to pod IPs | `04-09-headless-services` | `k8s-service` → `k8s-pods` |
| 10 | Session affinity, multi-port & Service vs Ingress | `04-10-affinity-and-ingress` | `k8s-networking` → `k8s-service`,`k8s-ingress` |

### 05 — ConfigMaps, Secrets & Environment  ⬜ planned (10)
Frames the `k8s-config` box → `k8s-configmap` · `k8s-secret` · `k8s-cfg-env`. Source: 12
`## ` headings → 10 (drop "Cleaning up").

| # | Section | slug | focus → highlight |
|---|---|---|---|
| 1 | ConfigMaps, Secrets & environment | `05-01-config-overview` | **hook** — whole map |
| 2 | The configuration problem | `05-02-config-problem` | `k8s-config` |
| 3 | ConfigMap — the object | `05-03-configmap` | `k8s-config` → `k8s-configmap` |
| 4 | Three ways to consume a ConfigMap | `05-04-consuming-configmaps` | `k8s-configmap` → `k8s-cfg-env` |
| 5 | Update propagation — env vars vs volume mounts | `05-05-update-propagation` | `k8s-config` → `k8s-cfg-env` |
| 6 | Immutable ConfigMaps & Secrets | `05-06-immutable` | `k8s-config` |
| 7 | Secrets — like ConfigMaps but sensitive *(+ creating)* | `05-07-secrets` | `k8s-config` → `k8s-secret` |
| 8 | Consuming Secrets & built-in types | `05-08-consuming-secrets` | `k8s-secret` → `k8s-cfg-env` |
| 9 | Image pull secrets | `05-09-image-pull-secrets` | `k8s-registry` → `k8s-pullsecret` |
| 10 | The downward API — pod metadata as env/files | `05-10-downward-api` | `k8s-config` → `k8s-cfg-env` |

### 06 — Storage: Volumes, PVs & PVCs  ⬜ planned (10)
Frames the `k8s-storage` box → `k8s-pv`/`k8s-pvc`/`k8s-sc`/`k8s-csi`. Source: 11 `## `
headings → 10 (drop "Cleaning up").

| # | Section | slug | focus → highlight |
|---|---|---|---|
| 1 | Storage: volumes, PVs & PVCs | `06-01-storage-overview` | **hook** — whole map |
| 2 | Why storage matters — the container fs is ephemeral | `06-02-why-storage` | `k8s-storage` |
| 3 | Volumes — the basics | `06-03-volumes-basics` | `k8s-storage` |
| 4 | Ephemeral volume types — `emptyDir`, `hostPath`, `projected` | `06-04-ephemeral-volumes` | `k8s-storage` |
| 5 | The persistent storage abstraction — PV, PVC, StorageClass | `06-05-pv-pvc-sc` | `k8s-storage` → `k8s-pv`,`k8s-pvc`,`k8s-sc` |
| 6 | Access modes & volume modes | `06-06-access-modes` | `k8s-storage` → `k8s-pvc` |
| 7 | `StorageClass` — dynamic provisioning | `06-07-storageclass` | `k8s-storage` → `k8s-sc` |
| 8 | Reclaim policies & the CSI | `06-08-reclaim-and-csi` | `k8s-storage` → `k8s-csi` |
| 9 | StatefulSets & `volumeClaimTemplates` — per-pod PVCs | `06-09-statefulset-storage` | `k8s-statefulset` → `k8s-pvc` |
| 10 | Resizing PVCs | `06-10-resizing-pvcs` | `k8s-storage` → `k8s-pvc` |

### 07 — Scheduling: Resources, Affinity, Taints  ⬜ planned (10)
Frames the `k8s-scheduling` box (nodeSelector/affinity/taints/tolerations/requests/limits)
with `k8s-scheduler`. Source: 13 `## ` headings → 10 (drop "Cleaning up").

| # | Section | slug | focus → highlight |
|---|---|---|---|
| 1 | Scheduling — resources, affinity, taints | `07-01-scheduling-overview` | **hook** — whole map |
| 2 | The scheduling problem — what `kube-scheduler` does | `07-02-scheduling-problem` | `k8s-scheduler` |
| 3 | Resource requests & limits | `07-03-requests-and-limits` | `k8s-scheduling` → `k8s-requests`,`k8s-limits` |
| 4 | QoS classes — Guaranteed, Burstable, BestEffort | `07-04-qos-classes` | `k8s-scheduling` → `k8s-requests`,`k8s-limits` |
| 5 | `LimitRange` & `ResourceQuota` — namespace governance | `07-05-limitrange-quota` | `k8s-scheduling` |
| 6 | `nodeSelector` & node affinity | `07-06-nodeselector-affinity` | `k8s-scheduling` → `k8s-nodeselector`,`k8s-affinity` |
| 7 | Pod affinity & anti-affinity | `07-07-pod-affinity` | `k8s-scheduling` → `k8s-affinity` |
| 8 | Taints & tolerations — the node-side "go away" | `07-08-taints-tolerations` | `k8s-scheduling` → `k8s-taints`,`k8s-tolerations` |
| 9 | Eviction & topology spread constraints | `07-09-eviction-topology` | `k8s-scheduling` |
| 10 | `PriorityClass`, preemption & how the scheduler decides | `07-10-priority-and-scheduler` | `k8s-scheduler` |

### 08 — Cluster Architecture & kubeadm  ⬜ planned (10)
Frames the `k8s-control-plane` (apiserver/etcd/scheduler/controllers) + `k8s-node-runtime`
(kubelet/kube-proxy/CRI) — the machinery behind everything so far. Source: 12 `## `
headings → 10.

| # | Section | slug | focus → highlight |
|---|---|---|---|
| 1 | Cluster architecture & kubeadm | `08-01-architecture-overview` | **hook** — whole map |
| 2 | `etcd` — the cluster's source of truth | `08-02-etcd` | `k8s-control-plane` → `k8s-etcd` |
| 3 | `kube-apiserver` — the front door | `08-03-apiserver` | `k8s-control-plane` → `k8s-apiserver` |
| 4 | `kube-scheduler` & `kube-controller-manager` | `08-04-scheduler-controllers` | `k8s-control-plane` → `k8s-scheduler`,`k8s-controllers` |
| 5 | Node components — `kubelet`, `kube-proxy`, the runtime | `08-05-node-components` | `k8s-node-runtime` → `k8s-kubelet`,`k8s-kube-proxy`,`k8s-cri` |
| 6 | The plug-in interfaces — CRI, CNI, CSI | `08-06-plugin-interfaces` | `k8s-node-runtime` → `k8s-cri` |
| 7 | Static pods & `kubeadm` — bootstrapping a cluster | `08-07-static-pods-kubeadm` | `k8s-control-plane` |
| 8 | The cluster PKI — who has what certificate | `08-08-cluster-pki` | `k8s-apiserver` |
| 9 | etcd backup & restore — the CKA's flag-bearer skill | `08-09-etcd-backup` | `k8s-control-plane` → `k8s-etcd` |
| 10 | Cluster upgrade with `kubeadm` | `08-10-cluster-upgrade` | `k8s-control-plane` |

### 09 — Networking, Ingress & Network Policies  ⬜ planned (10)
Frames the `k8s-networking` band → `k8s-service`/`k8s-ingress`/`k8s-netpol`/`k8s-dns` (the
deeper networking layer after module 04). Source: 13 `## ` headings → 10 (drop "Cleaning up").

| # | Section | slug | focus → highlight |
|---|---|---|---|
| 1 | Networking, Ingress & network policies | `09-01-networking-overview` | **hook** — whole map |
| 2 | The Kubernetes networking model — four requirements | `09-02-networking-model` | `k8s-networking` |
| 3 | Pod IPs & pod CIDRs — where addresses come from | `09-03-pod-ips-cidrs` | `k8s-pods` |
| 4 | What a CNI plugin actually does | `09-04-cni-plugin` | `k8s-node-runtime` → `k8s-cri` |
| 5 | The three communication paths | `09-05-communication-paths` | `k8s-networking` → `k8s-service` |
| 6 | Why Ingress & Ingress controllers | `09-06-ingress-controllers` | `k8s-networking` → `k8s-ingress` |
| 7 | Anatomy of an Ingress resource | `09-07-ingress-resource` | `k8s-ingress` → `k8s-service` |
| 8 | The Gateway API — Ingress, but more | `09-08-gateway-api` | `k8s-networking` → `k8s-ingress` |
| 9 | NetworkPolicy — the built-in firewall *(+ semantics + patterns)* | `09-09-networkpolicy` | `k8s-networking` → `k8s-netpol` |
| 10 | CoreDNS revisit — customising cluster DNS | `09-10-coredns-revisit` | `k8s-networking` → `k8s-dns` |

### 10 — RBAC, Security, Troubleshooting & CKA Prep  ⬜ planned (10)
Frames the `k8s-rbac` + `k8s-security` boxes, then tours the whole map as troubleshooting
playbooks + exam prep (§10 = whole-map synthesis, no focus). Source: 15 `## ` headings → 10.

| # | Section | slug | focus → highlight |
|---|---|---|---|
| 1 | RBAC, security, troubleshooting & CKA prep | `10-01-rbac-security-overview` | **hook** — whole map |
| 2 | Identity — Users vs ServiceAccounts | `10-02-serviceaccounts` | `k8s-rbac` → `k8s-sa` |
| 3 | RBAC — Roles & ClusterRoles | `10-03-rbac-roles` | `k8s-rbac` → `k8s-role`,`k8s-crole` |
| 4 | RBAC — bindings, subjects & `auth can-i` *(+ aggregated/default roles)* | `10-04-rbac-bindings` | `k8s-rbac` → `k8s-rb`,`k8s-crb`,`k8s-subject` |
| 5 | Pod security context — user, perms & capabilities | `10-05-security-context` | `k8s-security` → `k8s-sec-nonroot`,`k8s-sec-readonly` |
| 6 | Pod Security Admission, etcd encryption & image security | `10-06-psa-and-hardening` | `k8s-security` → `k8s-sec-psa` |
| 7 | Troubleshooting — application failures | `10-07-troubleshoot-apps` | `k8s-pods` |
| 8 | Troubleshooting — control plane & worker nodes | `10-08-troubleshoot-cluster` | `k8s-control-plane` |
| 9 | Troubleshooting — networking failures | `10-09-troubleshoot-networking` | `k8s-networking` → `k8s-service` |
| 10 | CKA exam strategy & where to go next | `10-10-cka-prep` | whole-map synthesis (no focus) |

**Total:** 100 sections (10 modules × 10). Every `focus`/`highlight` targets a node that
exists in the ported `kubernetes` scene (`k8s-*` ids in
`../graphl-movie/src/scenes/kubernetes.ts`, once ported).
