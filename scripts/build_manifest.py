#!/usr/bin/env python3
"""Emit manifest.json from the section spine below.

The manifest wires each section → notebook / slide / audio / scene / focus /
highlight. The `kubernetes` scene is app-owned (graphl-movie/src/scenes); here we
only reference it by id and name the `k8s-*` nodes the camera frames.

Each section tuple is (slug, heading, focus, highlight):
  - focus     : node id the camera frames, or None for the whole-map hook
  - highlight : list of node ids brightened in-place (rest dim), or []
A hook section (focus is None) also gets role="hook". Every section is spine:true
(one continuous flow). Audio paths are wired now; the .wav files land later via
Colab (a missing clip 404s until then).

Run from repo root:  python3 scripts/build_manifest.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MODULES = [
    ("01-getting-started-with-kubernetes", "Getting Started with Kubernetes", [
        ("01-01-what-kubernetes-is", "What Kubernetes is — and the shape of the whole platform", None, []),
        ("01-02-orchestration-problem", "The orchestration problem — what Docker alone doesn't solve", "k8s-cluster", []),
        ("01-03-the-cluster", "The cluster at 30,000 feet", "k8s-cluster", ["k8s-control-plane", "k8s-worker"]),
        ("01-04-the-pod", "The pod — Kubernetes' smallest unit", "k8s-pods", []),
        ("01-05-local-cluster", "Getting a local cluster", "k8s-cluster", []),
        ("01-06-first-pod", "Your first pod — kubectl run", "k8s-kubectl", ["k8s-pods"]),
        ("01-07-how-kubectl-works", "How kubectl actually works", "k8s-client", ["k8s-apiserver"]),
        ("01-08-pod-lifecycle", "The core pod lifecycle", "k8s-pods", []),
        ("01-09-imperative-vs-declarative", "Imperative vs declarative", "k8s-kc-apply", ["k8s-apiserver"]),
        ("01-10-help-and-cleanup", "Getting help & cleaning up", "k8s-kubectl", []),
    ]),
    ("02-pods-labels-and-the-object-model", "Pods, Labels & the Object Model", [
        ("02-01-pods-and-object-model", "Pods, labels & the object model", None, []),
        ("02-02-object-model", "The Kubernetes object model", "k8s-apiserver", ["k8s-etcd"]),
        ("02-03-pod-manifest", "Anatomy of a Pod manifest", "k8s-pod-kind", ["k8s-pod-containers"]),
        ("02-04-pod-phases", "Pod phases, conditions & container states", "k8s-pods", []),
        ("02-05-restart-policy", "Restart policy", "k8s-pods", []),
        ("02-06-init-containers", "Init containers", "k8s-pod-kind", ["k8s-pod-init"]),
        ("02-07-sidecar", "Multi-container pods — the sidecar pattern", "k8s-pod-kind", ["k8s-pod-sidecar"]),
        ("02-08-probes", "Probes — liveness, readiness, startup", "k8s-pod-kind", ["k8s-pod-probes"]),
        ("02-09-labels-and-selectors", "Labels & selectors", "k8s-workloads", []),
        ("02-10-annotations-namespaces", "Annotations & namespaces", "k8s-cluster", []),
    ]),
    ("03-deployments-replicasets-and-rollouts", "Deployments, ReplicaSets & Rollouts", [
        ("03-01-deployments-overview", "Deployments, ReplicaSets & rollouts", None, []),
        ("03-02-why-not-bare-pods", "Why bare pods aren't enough", "k8s-pods", []),
        ("03-03-replicaset", "ReplicaSet — keeping N pods alive", "k8s-workload-kinds", ["k8s-replicaset"]),
        ("03-04-why-not-replicaset", "Why you almost never write a ReplicaSet directly", "k8s-workload-kinds", ["k8s-deployment", "k8s-replicaset"]),
        ("03-05-deployment-manifest", "Anatomy of a Deployment manifest", "k8s-workload-kinds", ["k8s-deployment"]),
        ("03-06-scaling", "Scaling — changing the desired count", "k8s-kc-scale", ["k8s-replicaset"]),
        ("03-07-rolling-updates", "Rolling updates — shipping a new version with no downtime", "k8s-rollout", ["k8s-ro-rolling"]),
        ("03-08-rollout-history", "Rollout history and rollback", "k8s-kc-rollout", ["k8s-deployment"]),
        ("03-09-update-strategies", "Update strategies — RollingUpdate vs Recreate", "k8s-rollout", ["k8s-ro-rolling", "k8s-ro-recreate"]),
        ("03-10-workload-family", "The rest of the workload family", "k8s-workload-kinds", ["k8s-statefulset", "k8s-daemonset", "k8s-job", "k8s-cronjob"]),
    ]),
    ("04-services-dns-and-service-discovery", "Services, DNS & Service Discovery", [
        ("04-01-services-overview", "Services, DNS & service discovery", None, []),
        ("04-02-why-services", "Why Services exist", "k8s-networking", ["k8s-service"]),
        ("04-03-service-abstraction", "The Service abstraction — stable identity by label selector", "k8s-service", ["k8s-pods"]),
        ("04-04-the-three-ports", "port, targetPort, nodePort — the three numbers", "k8s-service", []),
        ("04-05-endpoints", "Endpoints and EndpointSlices — what the Service actually points at", "k8s-service", ["k8s-pods"]),
        ("04-06-service-types", "Service types — ClusterIP, NodePort, LoadBalancer, ExternalName", "k8s-service", []),
        ("04-07-kube-proxy", "How kube-proxy actually routes traffic", "k8s-kube-proxy", ["k8s-service"]),
        ("04-08-dns-coredns", "DNS in Kubernetes — CoreDNS and the service name pattern", "k8s-networking", ["k8s-dns"]),
        ("04-09-headless-services", "Headless Services — DNS to pod IPs, no virtual IP", "k8s-service", ["k8s-pods"]),
        ("04-10-affinity-and-ingress", "Session affinity, multi-port & Service vs Ingress", "k8s-networking", ["k8s-service", "k8s-ingress"]),
    ]),
    ("05-configmaps-secrets-and-environment", "ConfigMaps, Secrets & Environment", [
        ("05-01-config-overview", "ConfigMaps, Secrets & environment", None, []),
        ("05-02-config-problem", "The configuration problem", "k8s-config", []),
        ("05-03-configmap", "ConfigMap — the object", "k8s-config", ["k8s-configmap"]),
        ("05-04-consuming-configmaps", "Three ways to consume a ConfigMap", "k8s-configmap", ["k8s-cfg-env"]),
        ("05-05-update-propagation", "Update propagation — env vars vs volume mounts", "k8s-config", ["k8s-cfg-env"]),
        ("05-06-immutable", "Immutable ConfigMaps & Secrets", "k8s-config", []),
        ("05-07-secrets", "Secrets — like ConfigMaps but for sensitive data", "k8s-config", ["k8s-secret"]),
        ("05-08-consuming-secrets", "Consuming Secrets & built-in types", "k8s-secret", ["k8s-cfg-env"]),
        ("05-09-image-pull-secrets", "Image pull secrets", "k8s-registry", ["k8s-pullsecret"]),
        ("05-10-downward-api", "The downward API — pod metadata as env vars or files", "k8s-config", ["k8s-cfg-env"]),
    ]),
    ("06-storage-volumes-pvs-and-pvcs", "Storage: Volumes, PVs & PVCs", [
        ("06-01-storage-overview", "Storage: volumes, PVs & PVCs", None, []),
        ("06-02-why-storage", "Why storage matters — the container filesystem is ephemeral", "k8s-storage", []),
        ("06-03-volumes-basics", "Volumes — the basics", "k8s-storage", []),
        ("06-04-ephemeral-volumes", "Ephemeral volume types — emptyDir, hostPath, projected", "k8s-storage", []),
        ("06-05-pv-pvc-sc", "The persistent storage abstraction — PV, PVC, StorageClass", "k8s-storage", ["k8s-pv", "k8s-pvc", "k8s-sc"]),
        ("06-06-access-modes", "Access modes and volume modes", "k8s-storage", ["k8s-pvc"]),
        ("06-07-storageclass", "StorageClass — dynamic provisioning", "k8s-storage", ["k8s-sc"]),
        ("06-08-reclaim-and-csi", "Reclaim policies & the CSI", "k8s-storage", ["k8s-csi"]),
        ("06-09-statefulset-storage", "StatefulSets & volumeClaimTemplates — per-pod PVCs", "k8s-statefulset", ["k8s-pvc"]),
        ("06-10-resizing-pvcs", "Resizing PVCs", "k8s-storage", ["k8s-pvc"]),
    ]),
    ("07-scheduling-resources-affinity-taints-tolerations", "Scheduling: Resources, Affinity, Taints & Tolerations", [
        ("07-01-scheduling-overview", "Scheduling — resources, affinity, taints", None, []),
        ("07-02-scheduling-problem", "The scheduling problem — what kube-scheduler does", "k8s-scheduler", []),
        ("07-03-requests-and-limits", "Resource requests and limits", "k8s-scheduling", ["k8s-requests", "k8s-limits"]),
        ("07-04-qos-classes", "QoS classes — Guaranteed, Burstable, BestEffort", "k8s-scheduling", ["k8s-requests", "k8s-limits"]),
        ("07-05-limitrange-quota", "LimitRange and ResourceQuota — namespace governance", "k8s-scheduling", []),
        ("07-06-nodeselector-affinity", "nodeSelector & node affinity", "k8s-scheduling", ["k8s-nodeselector", "k8s-affinity"]),
        ("07-07-pod-affinity", "Pod affinity and anti-affinity", "k8s-scheduling", ["k8s-affinity"]),
        ("07-08-taints-tolerations", "Taints and tolerations — the node-side go away", "k8s-scheduling", ["k8s-taints", "k8s-tolerations"]),
        ("07-09-eviction-topology", "Eviction & topology spread constraints", "k8s-scheduling", []),
        ("07-10-priority-and-scheduler", "PriorityClass, preemption & how the scheduler decides", "k8s-scheduler", []),
    ]),
    ("08-cluster-architecture-and-kubeadm", "Cluster Architecture & kubeadm", [
        ("08-01-architecture-overview", "Cluster architecture & kubeadm", None, []),
        ("08-02-etcd", "etcd — the cluster's source of truth", "k8s-control-plane", ["k8s-etcd"]),
        ("08-03-apiserver", "kube-apiserver — the front door", "k8s-control-plane", ["k8s-apiserver"]),
        ("08-04-scheduler-controllers", "kube-scheduler and kube-controller-manager", "k8s-control-plane", ["k8s-scheduler", "k8s-controllers"]),
        ("08-05-node-components", "Node components — kubelet, kube-proxy, the container runtime", "k8s-node-runtime", ["k8s-kubelet", "k8s-kube-proxy", "k8s-cri"]),
        ("08-06-plugin-interfaces", "The plug-in interfaces — CRI, CNI, CSI", "k8s-node-runtime", ["k8s-cri"]),
        ("08-07-static-pods-kubeadm", "Static pods & kubeadm — bootstrapping a cluster", "k8s-control-plane", []),
        ("08-08-cluster-pki", "The cluster PKI — who has what certificate", "k8s-apiserver", []),
        ("08-09-etcd-backup", "etcd backup & restore — the CKA's flag-bearer skill", "k8s-control-plane", ["k8s-etcd"]),
        ("08-10-cluster-upgrade", "Cluster upgrade with kubeadm", "k8s-control-plane", []),
    ]),
    ("09-networking-ingress-and-network-policies", "Networking, Ingress & Network Policies", [
        ("09-01-networking-overview", "Networking, Ingress & network policies", None, []),
        ("09-02-networking-model", "The Kubernetes networking model — four hard requirements", "k8s-networking", []),
        ("09-03-pod-ips-cidrs", "Pod IPs and pod CIDRs — where the addresses come from", "k8s-pods", []),
        ("09-04-cni-plugin", "What a CNI plugin actually does", "k8s-node-runtime", ["k8s-cri"]),
        ("09-05-communication-paths", "The three communication paths", "k8s-networking", ["k8s-service"]),
        ("09-06-ingress-controllers", "Why Ingress & Ingress controllers", "k8s-networking", ["k8s-ingress"]),
        ("09-07-ingress-resource", "Anatomy of an Ingress resource", "k8s-ingress", ["k8s-service"]),
        ("09-08-gateway-api", "The Gateway API — Ingress, but more", "k8s-networking", ["k8s-ingress"]),
        ("09-09-networkpolicy", "NetworkPolicy — Kubernetes' built-in firewall", "k8s-networking", ["k8s-netpol"]),
        ("09-10-coredns-revisit", "CoreDNS revisit — customising cluster DNS", "k8s-networking", ["k8s-dns"]),
    ]),
    ("10-rbac-security-troubleshooting-and-cka-prep", "RBAC, Security, Troubleshooting & CKA Prep", [
        ("10-01-rbac-security-overview", "RBAC, security, troubleshooting & CKA prep", None, []),
        ("10-02-serviceaccounts", "Identity — Users vs ServiceAccounts", "k8s-rbac", ["k8s-sa"]),
        ("10-03-rbac-roles", "RBAC — Roles & ClusterRoles", "k8s-rbac", ["k8s-role", "k8s-crole"]),
        ("10-04-rbac-bindings", "RBAC — bindings, subjects & auth can-i", "k8s-rbac", ["k8s-rb", "k8s-crb", "k8s-subject"]),
        ("10-05-security-context", "Pod security context — user, perms & capabilities", "k8s-security", ["k8s-sec-nonroot", "k8s-sec-readonly"]),
        ("10-06-psa-and-hardening", "Pod Security Admission, etcd encryption & image security", "k8s-security", ["k8s-sec-psa"]),
        ("10-07-troubleshoot-apps", "Troubleshooting — application failures", "k8s-pods", []),
        ("10-08-troubleshoot-cluster", "Troubleshooting — control plane & worker nodes", "k8s-control-plane", []),
        ("10-09-troubleshoot-networking", "Troubleshooting — networking failures", "k8s-networking", ["k8s-service"]),
        ("10-10-cka-prep", "CKA exam strategy & where to go next", None, []),
    ]),
]


def section(slug, heading, focus, highlight):
    s = {
        "heading": heading,
        "notebook": f"notebooks/{slug}.ipynb",
        "slide": f"slides/{slug}.slide",
        "audio": f"audio/{slug}.wav",
        "scene": "kubernetes",
    }
    if focus is None:
        s["role"] = "hook"
    else:
        s["focus"] = focus
        if highlight:
            s["highlight"] = highlight
    s["spine"] = True
    return s


def main():
    manifest = {
        "concept": "Kubernetes",
        "modules": [
            {"id": mid, "title": title, "sections": [section(*sec) for sec in secs]}
            for mid, title, secs in MODULES
        ],
    }
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    total = sum(len(secs) for _, _, secs in MODULES)
    print(f"wrote manifest.json — {len(MODULES)} module(s), {total} sections")


if __name__ == "__main__":
    main()
